import os
import sys
import pypdf
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

workspace = os.path.abspath('.')
pdf_reports = os.path.join(workspace, "PDF_Reports")
new_folder = os.path.join(pdf_reports, "New folder")

# Source components
img_poster = os.path.join(workspace, "RSK_Shaikshik_Samwaad_One_Page_Visual_Summary.png")
pdf_ref_guide = os.path.join(new_folder, "RSK_Shaikshik_Samwaad_Executive_Visual_Briefing_Exact_Data_Origin_and_Reference_Guide.pdf")
pdf_lineage = os.path.join(new_folder, "RSK_Shaikshik_Samwaad_Master_Data_Provenance_and_Lineage_Matrix.pdf")
pdf_qwen = os.path.join(workspace, "RSK_Qwen_2026_Pedagogical_Strategic_Intelligence_Dossier.pdf")

# Step 1: Render poster image as page 1 PDF
temp_poster_pdf = os.path.join(workspace, "temp_compendium_poster_p1.pdf")
im = Image.open(img_poster)
im_rgb = im.convert('RGB')
im_rgb.save(temp_poster_pdf, 'PDF', resolution=100.0)
print("Generated Cover Poster PDF:", temp_poster_pdf)

# Step 2: Assemble all sections in systematic order
writer = pypdf.PdfWriter()

# 1. Page 1: Poster (Contains explicit 52 vs 55 district baseline note with 3 parent districts)
r_poster = pypdf.PdfReader(temp_poster_pdf)
for p in r_poster.pages:
    writer.add_page(p)

# 2. Pages 2-3: Exact Data Origin & Reference Guide
r_ref = pypdf.PdfReader(pdf_ref_guide)
for p in r_ref.pages:
    writer.add_page(p)

# 3. Pages 4-6: Master Provenance Map & Lineage Matrix
r_lin = pypdf.PdfReader(pdf_lineage)
for p in r_lin.pages:
    writer.add_page(p)

# 4. Pages 7-8: Qwen Strategic AI & Pedagogical Intelligence Dossier
r_qwen = pypdf.PdfReader(pdf_qwen)
for p in r_qwen.pages:
    writer.add_page(p)

total_pages = len(writer.pages)
print(f"Total Combined Pages: {total_pages}")

targets = [
    os.path.join(workspace, "RSK_Shaikshik_Samwaad_Master_Executive_Compendium_Complete_2026.pdf"),
    os.path.join(workspace, "RSK_Shaikshik_Samwaad_Complete_Executive_Master_Compendium_2026.pdf"),
    os.path.join(pdf_reports, "RSK_Shaikshik_Samwaad_Master_Executive_Compendium_Complete_2026.pdf"),
    os.path.join(pdf_reports, "RSK_Shaikshik_Samwaad_Complete_Executive_Master_Compendium_2026.pdf"),
    os.path.join(new_folder, "RSK_Shaikshik_Samwaad_Master_Executive_Compendium_Complete_2026.pdf"),
    os.path.join(new_folder, "RSK_Shaikshik_Samwaad_Complete_Executive_Master_Compendium_2026.pdf"),
]

for out_path in targets:
    try:
        with open(out_path, "wb") as f_out:
            writer.write(f_out)
        print(f"Successfully created: {out_path} ({total_pages} Pages)")
    except Exception as e:
        print(f"Could not write {out_path}: {e}")

# Clean up temp
if os.path.exists(temp_poster_pdf):
    os.remove(temp_poster_pdf)
