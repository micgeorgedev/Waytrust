import os
import shutil

directory = '/root/Waytrust'

# 1. Rename directories and files bottom-up
for root, dirs, files in os.walk(directory, topdown=False):
    if '.git' in root:
        continue
    # Rename files
    for file in files:
        if 'dubai' in file.lower():
            new_file = file.replace('dubai', 'abu-dhabi').replace('Dubai', 'Abu-Dhabi').replace('DUBAI', 'ABU-DHABI')
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_file)
            if os.path.exists(new_path):
                os.remove(old_path) # if target file exists, just delete old
            else:
                os.rename(old_path, new_path)
    
    # Rename dirs
    for d in dirs:
        if 'dubai' in d.lower():
            old_dir = os.path.join(root, d)
            new_dir_name = d.replace('dubai', 'abu-dhabi').replace('Dubai', 'Abu-Dhabi').replace('DUBAI', 'ABU-DHABI')
            new_dir = os.path.join(root, new_dir_name)
            if os.path.exists(new_dir):
                shutil.rmtree(old_dir)
            else:
                os.rename(old_dir, new_dir)

modified_files_count = 0

# 2. Replace text in files
for root, dirs, files in os.walk(directory):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.htm', '.json', '.js', '.css', '.txt')):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                continue

            new_content = content
            # Replacing strings
            new_content = new_content.replace('dubai', 'abu-dhabi')
            new_content = new_content.replace('Dubai', 'Abu Dhabi')
            new_content = new_content.replace('DUBAI', 'ABU DHABI')
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified_files_count += 1

print(f"Done renaming folders/files and modified {modified_files_count} files.")
