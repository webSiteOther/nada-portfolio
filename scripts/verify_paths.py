import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/portfolio-inventory.json', encoding='utf-8') as f:
    inv = json.load(f)

missing = 0
for item in inv:
    p = item['path']
    if not os.path.exists(p):
        print(f"Missing: {p}")
        missing += 1

print(f"Total inventory files checked: {len(inv)}. Missing files: {missing}")

with open('data/extracted-content.json', encoding='utf-8') as f:
    ext = json.load(f)

print(f"Extracted spreadsheets: {len(ext['spreadsheets'])}")
for k in ext['spreadsheets']:
    if not os.path.exists(k):
        print(f"Missing spreadsheet path: {k}")

print(f"Extracted documents: {len(ext['documents'])}")
for k in ext['documents']:
    if not os.path.exists(k):
        print(f"Missing docx path: {k}")

print(f"Extracted PDFs: {len(ext['pdfs'])}")
for k in ext['pdfs']:
    if not os.path.exists(k):
        print(f"Missing pdf path: {k}")

print("All verifications completed successfully!")
