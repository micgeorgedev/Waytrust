import os

directory = '/root/Waytrust'

replacements = [
    ("gulfoasistravelsandtourism.com", "waytransittourism.com")
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
            for old, new in replacements:
                new_content = new_content.replace(old, new)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified_files_count += 1

print(f"Done. Modified {modified_files_count} files for domain update.")
