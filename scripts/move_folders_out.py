import os
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

src_base = os.path.join('Nada_Portfolio', 'Nada_Portfolio')
dest_base = '.'

folders = []

# Collect from 01_Content_Plans
cp = os.path.join(src_base, '01_Content_Plans')
if os.path.exists(cp):
    for item in os.listdir(cp):
        p = os.path.join(cp, item)
        if os.path.isdir(p):
            folders.append(p)

# Collect from 02_Campaigns
camp = os.path.join(src_base, '02_Campaigns')
if os.path.exists(camp):
    for item in os.listdir(camp):
        p = os.path.join(camp, item)
        if os.path.isdir(p):
            folders.append(p)

# Collect from designs
des = os.path.join(src_base, 'designs')
if os.path.exists(des):
    for item in os.listdir(des):
        p = os.path.join(des, item)
        if os.path.isdir(p):
            folders.append(p)

# Collect scripts
scr = os.path.join(src_base, 'اسكريبتات لفيديوهات واخراج')
if os.path.exists(scr) and os.path.isdir(scr):
    folders.append(scr)

print(f"Found {len(folders)} internal folders to move.")
sys.stdout.flush()

for src in folders:
    folder_name = os.path.basename(src)
    dst = os.path.join(dest_base, folder_name)
    print(f"Moving: {folder_name} -> {dst}")
    sys.stdout.flush()
    try:
        shutil.move(src, dst)
        print(f"Done: {folder_name}")
    except Exception as e:
        print(f"Error moving {folder_name}: {e}")
    sys.stdout.flush()

print("All folders moved successfully!")
