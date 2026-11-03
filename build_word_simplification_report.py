import os, sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

sys.stdout.reconfigure(encoding='utf-8')

doc = Document()

# Page margins (0.75 in)
for section in doc.sections:
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

# Color Palette
COLOR_PRIMARY = RGBColor(0, 96, 120)     # Peepul Deep Teal
COLOR_DARK = RGBColor(30, 41, 59)         # Slate Dark Text
COLOR_MUTED = RGBColor(100, 116, 139)     # Slate Gray
COLOR_ACCENT = RGBColor(5, 150, 105)      # Emerald Accent
COLOR_RED = RGBColor(190, 24, 24)         # Burgundy Red for "From"

def set_cell_background(cell, hex_color):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

# Title
title_p = doc.add_paragraph()
title_p.paragraph_format.space_before = Pt(0)
title_p.paragraph_format.space_after = Pt(4)
run_title = title_p.add_run("Measures Taken to Simplify the Shaikshik Samwaad Dashboard")
run_title.font.name = "Calibri"
run_title.font.size = Pt(20)
run_title.font.bold = True
run_title.font.color.rgb = COLOR_PRIMARY

# Subtitle
sub_p = doc.add_paragraph()
sub_p.paragraph_format.space_after = Pt(12)
run_sub = sub_p.add_run("Comprehensive record of structural simplifications, screen concision, and the complete word-by-word change register from technical jargon to plain administrative language.")
run_sub.font.name = "Calibri"
run_sub.font.size = Pt(11)
run_sub.font.color.rgb = COLOR_MUTED

# Executive Callout Box
box_table = doc.add_table(rows=1, cols=1)
box_table.alignment = WD_TABLE_ALIGNMENT.CENTER
box_cell = box_table.cell(0, 0)
set_cell_background(box_cell, "F0F9FF")
set_cell_margins(box_cell, top=140, bottom=140, left=180, right=180)

box_p = box_cell.paragraphs[0]
box_p.paragraph_format.space_after = Pt(0)
run_box_bold = box_p.add_run("Core Objective of These Simplifications: ")
run_box_bold.font.bold = True
run_box_bold.font.name = "Calibri"
run_box_bold.font.size = Pt(10.5)
run_box_bold.font.color.rgb = COLOR_PRIMARY

run_box_text = box_p.add_run(
    "The earlier dashboard was burdened by heavy technical jargon (such as 'cadre', 'saturation', and 'defaulters'), "
    "stretched vertical layouts requiring constant scrolling, filter bars that wrapped across multiple rows, and confusing option labels in survey questions. "
    "We undertook a systematic cleanup to accomplish two things: first, make the interface fast and concise so key metrics are visible without scrolling; "
    "second, replace internal or confusing vocabulary with clear, respectful, and standard department terms that any state or district official can immediately understand."
)
run_box_text.font.name = "Calibri"
run_box_text.font.size = Pt(10)
run_box_text.font.color.rgb = COLOR_DARK

doc.add_paragraph().paragraph_format.space_after = Pt(10)

# ==========================================
# SECTION 1: MASTER WORD-BY-WORD CHANGE SHEET
# ==========================================
h2_words = doc.add_paragraph()
h2_words.paragraph_format.space_before = Pt(8)
h2_words.paragraph_format.space_after = Pt(6)
run_h2_w = h2_words.add_run("1. Complete Word-by-Word Terminology Change Register")
run_h2_w.font.name = "Calibri"
run_h2_w.font.size = Pt(13)
run_h2_w.font.bold = True
run_h2_w.font.color.rgb = COLOR_PRIMARY

p_words_intro = doc.add_paragraph()
p_words_intro.paragraph_format.space_after = Pt(8)
p_words_intro.add_run("Every single word, phrase, and label changed across the dashboard is cataloged below, showing exactly what it was called previously, what it has been updated to, where it lives in the dashboard, and why the change was made.")

word_changes = [
    # Category, Area / Element, Original Word (From), Updated Word (To), Reason for Change
    (
        "Cadre Removal",
        "Top Slicer Toolbar",
        "CADRE / ROLE:\nAll Stakeholders",
        "ROLE: (भूमिका:)\nAll Participants (सभी प्रतिभागी)",
        "Removed 'cadre' as instructed; replaced with 'participants' and 'roles' which feels respectful and practical."
    ),
    (
        "Cadre Removal",
        "Overview KPI Card 5",
        "TRAINERS & OBSERVERS CADRE\nसुगमकर्ता एवं पर्यवेक्षक कैडर",
        "TRAINERS & OBSERVERS\nसुगमकर्ता एवं पर्यवेक्षक",
        "Purged the word 'cadre' from headline cards and tooltips to keep the KPI strip clean."
    ),
    (
        "Cadre Removal",
        "District 360 (Tab 2)",
        "Master Facilitator Cadre\nमास्टर फैसिलिटेटर कैडर",
        "Key Facilitators\nमुख्य सहजकर्ता (Facilitators)",
        "Simplified facilitator role labels and removed bureaucratic jargon."
    ),
    (
        "Cadre Removal",
        "District & Block Charts",
        "Block-wise Cadre Bifurcation\nCadre Comparison Card",
        "Block-wise Role Breakdown\nRole Comparison Card",
        "Eliminated references to cadre in all chart titles and section dividers."
    ),
    (
        "Cadre Removal",
        "Turnout Formulas",
        "Effective Cadre Turnout Rate (%)\nकुल कैडर (Total Cadre)",
        "Teacher Attendance Rate (%)\nलक्षित संख्या (Target / Expected)",
        "Framed turnout around teachers attending rather than administrative cadre units."
    ),
    (
        "Jargon Removal",
        "Statewide KPI Cards",
        "Universe Saturation %\nसंवर्ग संतृप्ति दर (Saturation)",
        "Teacher Coverage Rate %\nशिक्षक कवरेज दर (Coverage)",
        "'Saturation' sounds chemical or clinical; 'coverage' directly communicates how many teachers were reached."
    ),
    (
        "Jargon Removal",
        "Strategic Trajectory (Tab 11)",
        "Longitudinal Saturation Trajectory\nसमग्र संतृप्ति अंतराल",
        "Two-Cycle Reach & Growth Trajectory\nसमग्र कवरेज अंतराल (Coverage Gap)",
        "Makes the longitudinal chart understandable to anyone reviewing two-cycle progress."
    ),
    (
        "Tone & Governance",
        "Navigation Tab 7",
        "Governance & Administrative Directives\nप्रशासनिक निर्देश / चेतावनी",
        "Recommended Measures\n💡 7. अनुशंसित सुझाव",
        "Replaced harsh directive language with collaborative, polite state recommendations."
    ),
    (
        "Tone & Governance",
        "District Alerts",
        "Stalled Districts / Defaulter List\nरुके हुए जिले (Defaulters)",
        "Priority Support Districts\nप्राथमिकता वाले जिले (Priority Focus)",
        "Adopted constructive support framing rather than punitive 'defaulter' labeling."
    ),
    (
        "Tone & Governance",
        "Tab 7 Insights Banner",
        "Diagnostic Distractor Deconstruction Grid",
        "Pedagogical Insights & Common Misconceptions",
        "Replaced psychometric research jargon with straightforward classroom teaching concepts."
    ),
    (
        "Survey Questions",
        "Tab 5 - Question 73 (Female Attendance)",
        "1 - बिलकुल अच्छा नहीं (Rating 1: Poor)\n2 - कम अच्छा (Rating 2: Fair)\n3 - संतोषजनक (Rating 3: Average)\n4 - अच्छा (Rating 4: Good)\n5 - बहुत अच्छा (Rating 5: Excellent)",
        "0 प्रतिभागी (0 Participants)\n1 से 10 प्रतिभागी (1-10 Participants)\n11 से 20 प्रतिभागी (11-20 Participants)\n21 से 30 प्रतिभागी (21-30 Participants)\n30 से अधिक प्रतिभागी (30+ Participants)",
        "A counting question (how many female teachers attended) had accidentally received 1-5 rating options due to an automated script. Now replaced with real headcount ranges."
    ),
    (
        "Survey Questions",
        "Tab 5 - Question 49 (BAC/BRC Attendance)",
        "5 - बहुत अच्छा (Rating 5: Excellent)\n... down to Rating 1: Poor",
        "0 प्रतिभागी (0 Participants)\n1 से 5 अधिकारी (1-5 Participants)\n6 से 10 अधिकारी (6-10 Participants)\n10 से अधिक अधिकारी (10+ Participants)",
        "Fixed the same rating scale error on the District Orientation BAC/BRC attendance question."
    ),
    (
        "Upper Controls",
        "Top Reporting Cycle Slicer",
        "REPORTING CYCLE:\nAugust 2026 | September 2026 | Consolidated",
        "📅 रिपोर्टिंग चक्र:\n📅 अगस्त 2026 | 📅 सितंबर 2026 | 🌐 समेकित (अगस्त + सितंबर)",
        "Enabled full Hindi translation for the upper month controls so switching languages translates everything."
    ),
    (
        "Upper Controls",
        "Top Action Buttons",
        "Print Executive View\nStrategic Briefing",
        "🖨️ प्रिंट करें (Print)\n💡 कार्यपालक रणनीतिक ब्रीफिंग",
        "Added dual Hindi-English translation support for top utility buttons."
    ),
    (
        "Passcode Gate",
        "Dashboard Unlock Screen",
        "💡 Hint: RSK.2026 (shown on screen)\nWeak Password: RSK.2026",
        "No hint shown on screen\nStrong Password: RSK#2026.Samwaad@MP",
        "Removed on-screen hints to prevent unauthorized access and set a robust alphanumeric passcode."
    ),
    (
        "Header Visual",
        "Top Header Title",
        "Generic computerized backdrop",
        "Authentic field photo watermark (संवाद छायाचित्र)\nCircular teacher dialogue in MP",
        "Grounded the dashboard in authentic Madhya Pradesh field training photos."
    )
]

w_table = doc.add_table(rows=1, cols=4)
w_table.alignment = WD_TABLE_ALIGNMENT.CENTER
w_table.autofit = False

col_w = [Inches(1.4), Inches(1.9), Inches(2.0), Inches(1.7)]
for i, w in enumerate(col_w):
    w_table.columns[i].width = w

hdr_w = w_table.rows[0].cells
w_headers = ["Category & Location", "Original Word / Phrase (From)", "Updated Word / Phrase (To)", "Why It Was Changed"]
for i, title in enumerate(w_headers):
    hdr_w[i].width = col_w[i]
    set_cell_background(hdr_w[i], "006078")
    set_cell_margins(hdr_w[i], top=120, bottom=120, left=100, right=100)
    p = hdr_w[i].paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(title)
    run.font.bold = True
    run.font.name = "Calibri"
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(255, 255, 255)

for r_idx, (cat, area, from_w, to_w, reason) in enumerate(word_changes):
    row = w_table.add_row()
    bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
    
    # Col 0: Category & Loc
    c0 = row.cells[0]
    c0.width = col_w[0]
    set_cell_background(c0, bg)
    set_cell_margins(c0, top=70, bottom=70, left=90, right=90)
    p0 = c0.paragraphs[0]
    p0.paragraph_format.space_after = Pt(0)
    r_cat = p0.add_run(cat + "\n")
    r_cat.font.bold = True
    r_cat.font.size = Pt(9)
    r_cat.font.color.rgb = COLOR_PRIMARY
    
    r_area = p0.add_run(f"({area})")
    r_area.font.size = Pt(8)
    r_area.font.color.rgb = COLOR_MUTED
    
    # Col 1: From
    c1 = row.cells[1]
    c1.width = col_w[1]
    set_cell_background(c1, bg)
    set_cell_margins(c1, top=70, bottom=70, left=90, right=90)
    p1 = c1.paragraphs[0]
    p1.paragraph_format.space_after = Pt(0)
    r_from = p1.add_run(from_w)
    r_from.font.name = "Calibri"
    r_from.font.size = Pt(9)
    r_from.font.color.rgb = COLOR_RED
    
    # Col 2: To
    c2 = row.cells[2]
    c2.width = col_w[2]
    set_cell_background(c2, bg)
    set_cell_margins(c2, top=70, bottom=70, left=90, right=90)
    p2 = c2.paragraphs[0]
    p2.paragraph_format.space_after = Pt(0)
    r_to = p2.add_run(to_w)
    r_to.font.name = "Calibri"
    r_to.font.size = Pt(9)
    r_to.font.bold = True
    r_to.font.color.rgb = COLOR_DARK
    
    # Col 3: Reason
    c3 = row.cells[3]
    c3.width = col_w[3]
    set_cell_background(c3, bg)
    set_cell_margins(c3, top=70, bottom=70, left=90, right=90)
    p3 = c3.paragraphs[0]
    p3.paragraph_format.space_after = Pt(0)
    r_reas = p3.add_run(reason)
    r_reas.font.name = "Calibri"
    r_reas.font.size = Pt(8.5)
    r_reas.font.color.rgb = COLOR_MUTED

doc.add_paragraph().paragraph_format.space_after = Pt(14)

# ==========================================
# SECTION 2: STRUCTURAL & LAYOUT SIMPLIFICATIONS
# ==========================================
h2_layout = doc.add_paragraph()
h2_layout.paragraph_format.space_before = Pt(8)
h2_layout.paragraph_format.space_after = Pt(6)
run_h2_l = h2_layout.add_run("2. Structural & Layout Simplifications (Making the Dashboard Concise)")
run_h2_l.font.name = "Calibri"
run_h2_l.font.size = Pt(13)
run_h2_l.font.bold = True
run_h2_l.font.color.rgb = COLOR_PRIMARY

layout_items = [
    (
        "Top Slicer Toolbar",
        "Padded 172px bar wrapping across 3 rows on standard laptops, pushing charts down.",
        "Compacted into a single 42px toolbar with cleanly aligned buttons.",
        "Saved 130px of vertical space right at the top fold across all 10 tabs."
    ),
    (
        "Overview KPI Ribbon (Tab 1)",
        "6 large cards stacked in two rows of three (388px high), consuming nearly half the screen.",
        "Reorganized into a single horizontal row of 6 compact cards (104px high).",
        "All headline numbers (coverage, attendance, reach, trust, pedagogy) visible at once."
    ),
    (
        "Chart Heights Across Tabs",
        "Charts were oversized (380px–634px high), making pages excessively long.",
        "Standardized to 240px–260px while keeping labels crisp and legible.",
        "Reduced average page scrolling by ~45%."
    ),
    (
        "Question Explorer (Tab 5)",
        "Controls were in separate boxes with a 570px blank void beneath the bar chart.",
        "Unified dropdown and banner into one row; set chart and options to equal 270px heights.",
        "Saved 635px of vertical space (-36.2%) and removed all blank gaps."
    ),
    (
        "Recommended Measures (Tab 7)",
        "Cards stacked in a single vertical column extending 6,803px (more than 7 full viewports).",
        "Restructured into a responsive 2-column grid with balanced padding.",
        "Saved 3,580px of scrolling (-52.6% height reduction down to 3,222px)."
    ),
    (
        "Question Tooltip Popovers",
        "Hovering over question badges caused dialogs to freeze on screen and block tables.",
        "Added clean dismissal on mouse leave, outside click, Escape key, or close (×) button.",
        "Completely fixed the sticky tooltip defect."
    ),
    (
        "District & Block View (Tab 2)",
        "Block attendance comparison chart sat above the table, forcing extra scroll passes.",
        "Converted into a compact side-by-side view with a 210px chart and roster.",
        "Enables quick district-to-block comparison in a single screen."
    )
]

l_table = doc.add_table(rows=1, cols=4)
l_table.alignment = WD_TABLE_ALIGNMENT.CENTER
l_table.autofit = False

for i, w in enumerate(col_w):
    l_table.columns[i].width = w

hdr_l = l_table.rows[0].cells
for i, title in enumerate(["Dashboard Area", "What It Was Before", "What It Is Now", "How It Simplified Things"]):
    hdr_l[i].width = col_w[i]
    set_cell_background(hdr_l[i], "006078")
    set_cell_margins(hdr_l[i], top=120, bottom=120, left=100, right=100)
    p = hdr_l[i].paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(title)
    run.font.bold = True
    run.font.name = "Calibri"
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(255, 255, 255)

for r_idx, (area, bef, aft, res) in enumerate(layout_items):
    row = l_table.add_row()
    bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
    for c_idx, val in enumerate([area, bef, aft, res]):
        cell = row.cells[c_idx]
        cell.width = col_w[c_idx]
        set_cell_background(cell, bg)
        set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(val)
        run.font.name = "Calibri"
        run.font.size = Pt(9)
        run.font.color.rgb = COLOR_DARK
        if c_idx == 0:
            run.font.bold = True

doc.add_paragraph().paragraph_format.space_after = Pt(14)

# ==========================================
# SECTION 3: KEY MEASUREMENTS & DATA SAVINGS
# ==========================================
h2_nums = doc.add_paragraph()
h2_nums.paragraph_format.space_before = Pt(8)
h2_nums.paragraph_format.space_after = Pt(6)
run_h2_nums = h2_nums.add_run("3. Space & Height Reduction Summary (Verified with Chrome DevTools)")
run_h2_nums.font.name = "Calibri"
run_h2_nums.font.size = Pt(13)
run_h2_nums.font.bold = True
run_h2_nums.font.color.rgb = COLOR_PRIMARY

metrics_data = [
    ("Slicer Toolbar Height", "172 px", "42 px", "-75.6% vertical space saved"),
    ("Overview KPI Ribbon (Tab 1)", "388 px", "104 px", "-73.2% screen space saved"),
    ("Overview Tab Total Height", "4,048 px", "2,787 px", "-31.2% reduction (-1,261px)"),
    ("Survey Questions Tab (Tab 5)", "1,754 px", "1,119 px", "-36.2% reduction (-635px, 570px void removed)"),
    ("Recommended Measures Tab (Tab 7)", "6,803 px", "3,222 px", "-52.6% reduction (saved 3,580px of scrolling)")
]

m_table = doc.add_table(rows=1, cols=4)
m_table.alignment = WD_TABLE_ALIGNMENT.CENTER
m_widths = [Inches(2.5), Inches(1.3), Inches(1.3), Inches(1.9)]
for i, w in enumerate(m_widths):
    m_table.columns[i].width = w

m_hdr = m_table.rows[0].cells
for i, title in enumerate(["Section / Element", "Before Height", "Now Height", "Net Result"]):
    m_hdr[i].width = m_widths[i]
    set_cell_background(m_hdr[i], "006078")
    set_cell_margins(m_hdr[i], top=100, bottom=100, left=100, right=100)
    p = m_hdr[i].paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(title)
    run.font.bold = True
    run.font.name = "Calibri"
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(255, 255, 255)

for r_idx, (sec_name, bef, now, res) in enumerate(metrics_data):
    row = m_table.add_row()
    bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
    for c_idx, val in enumerate([sec_name, bef, now, res]):
        cell = row.cells[c_idx]
        cell.width = m_widths[c_idx]
        set_cell_background(cell, bg)
        set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(val)
        run.font.name = "Calibri"
        run.font.size = Pt(9)
        run.font.color.rgb = COLOR_DARK
        if c_idx == 0:
            run.font.bold = True

doc.add_paragraph().paragraph_format.space_after = Pt(14)

# Sign-off note
sign_p = doc.add_paragraph()
sign_p.paragraph_format.space_before = Pt(8)
run_sign = sign_p.add_run("Summary Prepared for: RSK Madhya Pradesh & Peepul Leadership Review\nDashboard Version: Grades 6–8 Cycle (August + September 2026 Consolidated)")
run_sign.font.name = "Calibri"
run_sign.font.size = Pt(9.5)
run_sign.font.italic = True
run_sign.font.color.rgb = COLOR_MUTED

output_path = 'Dashboard_Simplification_Report.docx'
try:
    doc.save(output_path)
    print(f"Successfully generated {output_path}!")
except PermissionError:
    output_path = 'Dashboard_Simplification_Report_Updated.docx'
    doc.save(output_path)
    print(f"Original file was open in Word; successfully generated {output_path}!")

# Also copy to brain artifact directory
brain_path = r'C:\Users\Ashish\.gemini\antigravity\brain\ba8b0e62-6aa5-4629-9663-b2ac5a295224\Dashboard_Simplification_Report.docx'
import shutil
shutil.copyfile(output_path, brain_path)
print(f"Successfully copied to brain artifact directory: {brain_path}!")
