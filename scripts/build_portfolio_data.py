import os
import sys
import json
import zipfile
import xml.etree.ElementTree as ET
import openpyxl
import docx
import pypdf
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = '.'

def read_ods(filepath):
    try:
        with zipfile.ZipFile(filepath, 'r') as z:
            content = z.read('content.xml')
            root = ET.fromstring(content)
            sheets = {}
            for table in root.iter('{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table'):
                tname = table.attrib.get('{urn:oasis:names:tc:opendocument:xmlns:table:1.0}name', 'Sheet1')
                rows = []
                for tr in table.iter('{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-row'):
                    row_cells = []
                    for tc in tr.iter('{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-cell'):
                        txt = ''.join(tc.itertext()).strip()
                        rep = int(tc.attrib.get('{urn:oasis:names:tc:opendocument:xmlns:table:1.0}number-columns-repeated', 1))
                        if rep > 25:
                            continue
                        for _ in range(rep):
                            row_cells.append(txt)
                    if any(c != '' for c in row_cells):
                        rows.append(row_cells)
                if rows:
                    sheets[tname] = rows
            return sheets
    except Exception as e:
        print(f"Error reading ODS {filepath}: {e}")
        return {}

def read_xlsx(filepath):
    try:
        wb = openpyxl.load_workbook(filepath, data_only=True)
        sheets = {}
        for sname in wb.sheetnames:
            ws = wb[sname]
            rows = []
            for r in range(1, min(ws.max_row + 1, 200)):
                row_vals = []
                for c in range(1, min(ws.max_column + 1, 30)):
                    val = ws.cell(r, c).value
                    row_vals.append('' if val is None else str(val).strip())
                if any(v != '' for v in row_vals):
                    rows.append(row_vals)
            if rows:
                sheets[sname] = rows
        return sheets
    except Exception as e:
        print(f"Error reading XLSX {filepath}: {e}")
        return {}

def read_docx(filepath):
    try:
        doc = docx.Document(filepath)
        paragraphs = []
        for p in doc.paragraphs:
            txt = p.text.strip()
            if txt:
                paragraphs.append({
                    "text": txt,
                    "style": p.style.name if p.style else "Normal"
                })
        return paragraphs
    except Exception as e:
        print(f"Error reading DOCX {filepath}: {e}")
        return []

def read_pdf(filepath):
    try:
        reader = pypdf.PdfReader(filepath)
        pages = []
        for i, page in enumerate(reader.pages):
            pages.append({
                "page": i + 1,
                "text": (page.extract_text() or '').strip()
            })
        return pages
    except Exception as e:
        print(f"Error reading PDF {filepath}: {e}")
        return []

def get_file_info(full_path):
    rel_path = os.path.relpath(full_path, ROOT_DIR).replace('\\', '/')
    filename = os.path.basename(full_path)
    ext = os.path.splitext(filename)[1].lower()
    size = os.path.getsize(full_path)
    
    if size < 1024:
        fsize = f"{size} B"
    elif size < 1024 * 1024:
        fsize = f"{size / 1024:.1f} KB"
    else:
        fsize = f"{size / (1024*1024):.2f} MB"
        
    return {
        "filename": filename,
        "path": rel_path,
        "ext": ext,
        "size_bytes": size,
        "size_formatted": fsize
    }

def main():
    all_files = []
    
    # Ignore folders that belong to portfolio app infrastructure
    ignore_dirs = {
        'node_modules', '.git', 'assets/audio', 'assets\\audio',
        'css', 'js', 'scripts', 'data', '.gemini'
    }
    
    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        skip = False
        for ign in ignore_dirs:
            if ign in dirpath.replace('/', '\\'):
                skip = True
                break
        if skip:
            continue
            
        for f in filenames:
            # Skip root dev files
            if dirpath == '.' and f in ['package.json', 'package-lock.json', 'README.md', 'index.html']:
                continue
            full = os.path.join(dirpath, f)
            all_files.append(full)
            
    print(f"Discovered {len(all_files)} portfolio asset files.")
    
    # Process PSD previews map
    psd_previews = {}
    psd_preview_dir = os.path.join('assets', 'previews', 'psd')
    if os.path.exists(psd_preview_dir):
        for f in os.listdir(psd_preview_dir):
            if f.endswith('.webp'):
                psd_previews[f] = f"assets/previews/psd/{f}"

    spreadsheets_data = {}
    documents_data = {}
    pdf_data = {}
    
    file_inventory = []
    
    for fpath in all_files:
        info = get_file_info(fpath)
        ext = info["ext"]
        rel = info["path"]
        
        # Categorize projects according to new top-level directories
        cat = "Other"
        proj_id = "general"
        
        if rel.startswith("السيف/") or rel == "السيف":
            cat = "Content Plans"
            proj_id = "al_saif"
        elif rel.startswith("اللؤلؤه/") or rel == "اللؤلؤه":
            cat = "Content Plans"
            proj_id = "al_loloa"
        elif rel.startswith("المركز المصري السعودي/") or rel == "المركز المصري السعودي":
            cat = "Content Plans"
            proj_id = "egyptian_saudi_center"
        elif rel.startswith("اور/") or rel == "اور":
            cat = "Content Plans"
            proj_id = "our_retail"
        elif rel.startswith("بلاتنيوم/") or rel == "بلاتنيوم":
            cat = "Content Plans"
            proj_id = "platinum"
        elif rel.startswith("تهنئات اكتوبر/") or rel == "تهنئات اكتوبر":
            cat = "Content Plans"
            proj_id = "october_greetings"
        elif rel.startswith("توب لاند/") or rel == "توب لاند":
            cat = "Content Plans"
            proj_id = "top_land"
        elif rel.startswith("د.الملا/") or rel == "د.الملا":
            cat = "Content Plans"
            proj_id = "dr_mulla"
        elif rel.startswith("د.هادي/") or rel == "د.هادي":
            cat = "Content Plans"
            proj_id = "dr_hady"
        elif rel.startswith("رحال/") or rel == "رحال":
            cat = "Content Plans"
            proj_id = "rahhal"
        elif rel.startswith("مستشفي الزهراء/") or rel == "مستشفي الزهراء":
            cat = "Content Plans"
            proj_id = "al_zahraa_hospital"
        elif rel.startswith("campaign El Mansour 6/") or rel == "campaign El Mansour 6":
            cat = "Campaigns"
            proj_id = "al_mansour_6"
        elif rel.startswith("campaign med guide/") or rel == "campaign med guide":
            cat = "Campaigns"
            proj_id = "med_guide"
        elif rel.startswith("campaign rashed/") or rel == "campaign rashed":
            cat = "Campaigns"
            proj_id = "koshary_rashed"
        elif rel.startswith("campaign tameem/") or rel == "campaign tameem":
            cat = "Campaigns"
            proj_id = "tameem"
        elif rel.startswith("المركز العلمي/") or rel == "المركز العلمي":
            cat = "Creative Design"
            proj_id = "scientific_center_designs"
        elif rel.startswith("اسكريبتات لفيديوهات واخراج/") or rel == "اسكريبتات لفيديوهات واخراج":
            cat = "Video Production & Direction"
            proj_id = "video_production"
        elif rel.startswith("assets/previews/psd/"):
            cat = "Creative Design"
            proj_id = "alpha_care"
        elif info["filename"].startswith("NADA NASSER MOHAMED") or info["filename"].startswith("WhatsApp Image"):
            cat = "Professional Profile"
            proj_id = "nada_profile"
            
        info["category"] = cat
        info["project_id"] = proj_id
        
        # Parse content
        if ext == '.xlsx':
            info["preview_type"] = "interactive_spreadsheet"
            sheets = read_xlsx(fpath)
            spreadsheets_data[rel] = {
                "filename": info["filename"],
                "path": rel,
                "sheets": sheets
            }
        elif ext == '.ods':
            info["preview_type"] = "interactive_spreadsheet"
            sheets = read_ods(fpath)
            spreadsheets_data[rel] = {
                "filename": info["filename"],
                "path": rel,
                "sheets": sheets
            }
        elif ext == '.docx':
            info["preview_type"] = "formatted_document"
            paragraphs = read_docx(fpath)
            documents_data[rel] = {
                "filename": info["filename"],
                "path": rel,
                "paragraphs": paragraphs
            }
        elif ext == '.pdf':
            info["preview_type"] = "pdf_reader"
            pages = read_pdf(fpath)
            pdf_data[rel] = {
                "filename": info["filename"],
                "path": rel,
                "num_pages": len(pages),
                "pages": pages
            }
        elif ext in ['.png', '.jpg', '.jpeg']:
            info["preview_type"] = "image_gallery"
        elif ext == '.mp4':
            info["preview_type"] = "video_player"
        elif ext == '.psd':
            info["preview_type"] = "psd_preview"
            base = os.path.splitext(info["filename"])[0]
            clean_name = base.replace(' ', '_').replace(',', '').replace('(', '').replace(')', '') + '.webp'
            if clean_name in psd_previews:
                info["preview_image"] = psd_previews[clean_name]
        elif ext == '.webp' and 'assets/previews/psd/' in rel:
            info["preview_type"] = "psd_preview"
            info["preview_image"] = rel
        elif ext == '.zip':
            info["preview_type"] = "zip_archive"
            
        file_inventory.append(info)
        
    print(f"Total inventory items processed: {len(file_inventory)}")
    print(f"Spreadsheets with live data: {len(spreadsheets_data)}")
    print(f"DOCX documents with live text: {len(documents_data)}")
    print(f"PDFs with extracted text: {len(pdf_data)}")
    
    inv_path = os.path.join('data', 'portfolio-inventory.json')
    with open(inv_path, 'w', encoding='utf-8') as f:
        json.dump(file_inventory, f, ensure_ascii=False, indent=2)
    print(f"Saved {inv_path}")
    
    extracted_path = os.path.join('data', 'extracted-content.json')
    with open(extracted_path, 'w', encoding='utf-8') as f:
        json.dump({
            "spreadsheets": spreadsheets_data,
            "documents": documents_data,
            "pdfs": pdf_data
        }, f, ensure_ascii=False, indent=2)
    print(f"Saved {extracted_path}")

if __name__ == '__main__':
    main()
