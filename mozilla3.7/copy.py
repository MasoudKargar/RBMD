import os
import shutil

target_folder = 'target'

folders_to_create = ['accessible', 'browser', 'build', 'content', 'db', 'dom', 'extensions', 'gfx', 'intl', 'ipc']

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

for folder in folders_to_create:
    folder_path = os.path.join(target_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# source_folder = download firefox v3.7

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
    copy_files(source_subfolder, target_subfolder, ('.cpp', '.h'))

print("All files were copied successfully.")