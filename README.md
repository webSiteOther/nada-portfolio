# Nada Nasser Mohamed — Premium Animated Bilingual Portfolio

> **Content Creator | Social Media Specialist | Marketing Coordinator**  
> Beni Suef, Egypt • 24 Pages Managed • 114K+ Video Views • 263 Original Portfolio Assets

An ultra-premium, responsive, animated, and interactive digital portfolio engineered directly from the project repository of **Nada Nasser Mohamed**.

All project folders are organized directly at the top level of the workspace, making each project a clean, standalone directory ready for immediate GitHub upload or local execution.

---

## 📁 Updated Project Folder Structure (Ready for GitHub)

All internal project folders have been moved directly to the root directory for easy folder-by-folder GitHub uploading:

```
d:\projects\nada\
│
├── السيف/                               # Al-Saif Real Estate (26 files: XLSX, DOCX, PNG)
├── اللؤلؤه/                             # Al-Lo'loa Brand (13 files: XLSX, PNG, JPG)
├── المركز العلمي/                       # Scientific Center (55 files: Course artboards & branding)
├── المركز المصري السعودي/               # Egyptian Saudi Center (18 files: XLSX, PNG, JPG)
├── اور/                                 # OUR Retail Brand (6 files: XLSX, JPG)
├── بلاتنيوم/                            # Platinum Plus Developments (15 files: XLSX, PDF, PNG)
├── تهنئات اكتوبر/                       # 6th of October National Campaigns (8 files: DOCX, PDF, PNG, JPG)
├── توب لاند/                            # Top Land Towers (19 files: XLSX, DOCX, PNG)
├── د.الملا/                             # Dr. Al-Mulla Clinic (9 files: XLSX, PNG)
├── د.هادي/                              # Dr. Hady Clinic (6 files: XLSX, PNG)
├── رحال/                                # Rahhal Strategy (7 files: XLSX, PNG, JPG)
├── مستشفي الزهراء/                      # Al-Zahraa Hospital (21 files: DOCX, PNG, ZIP)
│
├── campaign El Mansour 6/               # Al-Mansour 6th Anniversary (8 files: ODS, PNG)
├── campaign med guide/                  # Med Guide Mystery Teaser (6 files: XLSX, PNG)
├── campaign rashed/                     # Koshary Rashed (4 files: XLSX, PNG)
├── campaign tameem/                     # Tameem District League (8 files: PDF, ODS, PNG)
├── اسكريبتات لفيديوهات واخراج/          # Video Scripts & HD MP4 Productions (8 files: DOCX, MP4)
│
├── assets/                              # Audio soundtrack and AI WebP previews
├── css/                                 # Stylesheet & responsive layout
├── js/                                  # Portfolio logic, audio player, interactive viewers
├── data/                                # Generated portfolio databases (inventory & extracted data)
├── scripts/                             # Automation & data build scripts
│
├── index.html                           # Portfolio application entry point
├── NADA NASSER MOHAMED con.pdf          # Official 4-page Curriculum Vitae
├── WhatsApp Image 2026-10-23...jpeg     # Official portrait photograph
├── package.json                         # Node scripts
└── README.md                            # Documentation & GitHub guide
```

---

## 🐙 How to Upload to GitHub (طريقة الرفع على جيت هاب)

### الطريقة الأولى: الرفع فولدر فولدر عبر موقع GitHub (Web Drag & Drop)
كل الفولدرات الآن موجودة خارجياً ومباشرة أمامك في المسار الرئيسي:
1. ادخلي على حسابك في **GitHub** وافتحي المستودع (Repository) الخاص بك.
2. اضغطي على زر **`Add file`** ثم اختاري **`Upload files`**.
3. اسحبي أي فولدر من الفولدرات الخارجية (مثلاً: `السيف` أو `المركز العلمي` أو `campaign El Mansour 6`) وأفلتيه في الصفحة مباشرة.
4. اكتبي اسم الـ Commit واضغطي **`Commit changes`**.
5. كرري العملية لكل فولدر ترغبين في رفعه بكل سهولة، حيث أصبح كل فولدر خفيفاً ومنفصلاً دون أي تداخل أو تكرار مسارات!

---

### الطريقة الثانية: الرفع بضغطة واحدة عبر Git (الأسرع والأسهل خلال ثوانٍ)
بدلاً من رفع كل فولدر بشكل يدوي، يمكنك رفع البورتفوليو كاملاً بكل فولدراته بضغطة واحدة من خلال الـ Terminal في نفس المجلد:

```bash
# 1. تهيئة المستودع
git init

# 2. إضافة جميع الملفات والفولدرات الخارجية
git add .

# 3. حفظ التغييرات
git commit -m "Initial commit: Nada Nasser Portfolio with all project folders"

# 4. الربط مع مستودع GitHub الخاص بك (استبدلي الرابط برابط مستودعك)
git remote add origin https://github.com/USERNAME/nada-portfolio.git

# 5. الرفع الفوري
git branch -M main
git push -u origin main
```

---

## 🚀 تشغيل البورتفوليو محلياً (Run Locally)

```bash
# باستخدام بايثون (لا يتطلب أي تثبيت):
python -m http.server 3000
```
ثم افتحي المتصفح على: `http://localhost:3000`
أو اضغطي مرتين مباشرة على ملف `index.html`.
