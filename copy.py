import os
import shutil

target_folder = 'target'

source_folder = 'chromium-main'

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

folders_to_create = [folder for folder in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, folder))]

for folder in folders_to_create:
    folder_path = os.path.join(target_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def copy_files(src_folder, dst_folder, extensions):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.endswith(extensions):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_folder, file)
                shutil.copy(src_file, dst_file)

for folder in folders_to_create:
    source_subfolder = os.path.join(source_folder, folder)
    target_subfolder = os.path.join(target_folder, folder)
    copy_files(source_subfolder, target_subfolder, ('.cc', '.h'))

print("OK")

import os

source_folder = 'target'

folders = [folder for folder in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, folder))]

folder_file_count = {}

for folder in folders:
    folder_path = os.path.join(source_folder, folder)
    file_count = 0

    for root, dirs, files in os.walk(folder_path):
        file_count += len(files)

    folder_file_count[folder] = file_count

sorted_folders = sorted(folder_file_count.items(), key=lambda x: x[1], reverse=True)

print("Folders sorted by the number of files:")
for folder, count in sorted_folders:
    print(f"{folder}: {count} files")