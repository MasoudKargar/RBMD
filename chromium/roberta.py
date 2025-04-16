import os
import re
import torch
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, f1_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset

target_folder = "target"

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def traverse_folder(folder):
    data = []
    for subdir, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".cc") or file.endswith(".h"):
                file_path = os.path.join(subdir, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                except Exception as e:
                    print(f"Readinf file error {file_path}: {e}")
                    content = ""
                processed_content = preprocess_text(content)
                folder_name = os.path.basename(subdir)
                data.append({"text": processed_content, "label": folder_name})
    return data

raw_data = traverse_folder(target_folder)

labels = list(set([item["label"] for item in raw_data]))
label_to_id = {label: i for i, label in enumerate(labels)}
id_to_label = {i: label for label, i in label_to_id.items()}

for item in raw_data:
    item["label"] = label_to_id[item["label"]]

df = pd.DataFrame(raw_data)

counts = df["label"].value_counts()
plt.figure(figsize=(10, 5))
plt.bar(counts.index.map(id_to_label), counts.values, color="skyblue")
plt.title("Class count")
plt.xlabel("Class")
plt.ylabel("Sample count")
plt.xticks(rotation=45)
plt.show()

train_data_list = []
test_data_list = []

for label in df["label"].unique():
    class_data = df[df["label"] == label]
    train_class_data, test_class_data = train_test_split(
        class_data, test_size=0.2, random_state=42
    )
    train_data_list.append(train_class_data)
    test_data_list.append(test_class_data)

train_data = pd.concat(train_data_list).reset_index(drop=True)
test_data = pd.concat(test_data_list).reset_index(drop=True)

train_counts = train_data["label"].value_counts()
test_counts = test_data["label"].value_counts()

print("Number of training samples for each class:")
for label, count in train_counts.items():
    print(f"{id_to_label[label]}: {count} Sample")

print("\nNumber of testing samples for each class:")
for label, count in test_counts.items():
    print(f"{id_to_label[label]}: {count} Sample")

train_dataset = Dataset.from_pandas(train_data)
test_dataset = Dataset.from_pandas(test_data)

model_name = "roberta-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=len(labels))

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)

train_dataset = train_dataset.map(tokenize_function, batched=True)
test_dataset = test_dataset.map(tokenize_function, batched=True)

train_dataset = train_dataset.remove_columns(["text"])
test_dataset = test_dataset.remove_columns(["text"])

train_dataset.set_format("torch")
test_dataset.set_format("torch")

training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=4,
    weight_decay=0.01,
    logging_dir="./logs",
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    logging_steps=50,
    logging_first_step=True
)

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = torch.argmax(torch.tensor(logits), dim=1)
    accuracy = accuracy_score(labels, predictions)
    f1 = f1_score(labels, predictions, average="weighted")
    return {"accuracy": accuracy, "f1": f1}

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)

trainer.train()

predictions = trainer.predict(test_dataset)
preds = torch.argmax(torch.tensor(predictions.predictions), dim=1)

accuracy = accuracy_score(test_dataset["label"], preds)
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nReport classification:")
print(classification_report(test_dataset["label"], preds, target_names=labels))

from sklearn.metrics import confusion_matrix
import seaborn as sns

cm = confusion_matrix(test_dataset["label"], preds)

# Plot the confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")

plt.savefig("confusion_matrix.png", dpi=300)

plt.show()