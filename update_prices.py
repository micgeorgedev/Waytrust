import os
import re

directory = '/root/Waytrust'

patterns = [
    (re.compile(r"AED\s*[0-9,]+"), "Price on Request"),
    (re.compile(r"[0-9,]+\s*AED"), "Price on Request"),
    (re.compile(r"\$\s*[0-9,]+"), "Price on Request"),
    (re.compile(r"USD\s*[0-9,]+"), "Price on Request"),
    (re.compile(r"[0-9,]+\s*<br>\s*AED"), "Price on Request")
]

modified_files_count = 0

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
            for pattern, replacement in patterns:
                new_content = pattern.sub(replacement, new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified_files_count += 1

print(f"Done. Modified {modified_files_count} files for price replacement.")
