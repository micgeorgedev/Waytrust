import os

directory = '/root/Waytrust'

replacements = [
    ("Gulf Oasis Travel & Tourism LLC", "WAYTRANSIT TRAVEL AND TOURISM LLC"),
    ("Gulf Oasis Travel & Tourism", "WAYTRANSIT TRAVEL AND TOURISM LLC"),
    ("Gulf Oasis Tours LLC", "WAYTRANSIT TRAVEL AND TOURISM LLC"),
    ("Gulf Oasis Tours", "WAYTRANSIT TRAVEL AND TOURISM LLC"),
    ("Gulf Oasis", "Waytransit"),
    ("National Cinema - Baniyas Najda Street - Al Danah - Zone 1 - Abu Dhabi - United Arab Emirates", "5th Floor, Liwa Tower, Al Khaleej Al Arabi Street, Abu Dhabi United Arab Emirates. P.O. Box 0822. HEAD OF SERVICE CONTACT: Mr.Mohamed Hassan"),
    ("971565207328", "971562232593"),
    ("565207328", "562232593")
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

print(f"Done. Modified {modified_files_count} files.")
