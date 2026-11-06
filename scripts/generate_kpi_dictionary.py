"""
generate_kpi_dictionary.py

Generates the CLSS Master Dashboard KPI and Indicator Reference Workbook.
Outputs: CLSS_Dashboard_KPI_Dictionary.xlsx
Follows human-crafted executive formatting standards:
- Deep Navy (#1E3A8A) header styling with white bold text
- Subtle (#F8FAFC) alternate row striping
- Hairline (#E2E8F0) gridlines
- Auto-adjusted column widths with safety margin (+4)
- Text wrap enabled on long descriptions and formulas
- Sticky header panes (freeze_panes) on all sheets
- Clean, plain language with no AI boilerplate
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Palette Constants
NAVY_HEADER = "1E3A8A"
WHITE = "FFFFFF"
ROW_STRIPE = "F8FAFC"
BORDER_GRAY = "E2E8F0"
TEXT_MAIN = "0F172A"
TEXT_MUTED = "475569"
ACCENT_BLUE = "E0F2FE"
ACCENT_GREEN = "DCFCE7"
ACCENT_AMBER = "FEF3C7"
ACCENT_RED = "FEE2E2"

def get_header_style():
    return {
        "font": Font(name="Calibri", size=11, bold=True, color=WHITE),
        "fill": PatternFill(start_color=NAVY_HEADER, end_color=NAVY_HEADER, fill_type="solid"),
        "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
        "border": Border(
            left=Side(style="thin", color=BORDER_GRAY),
            right=Side(style="thin", color=BORDER_GRAY),
            top=Side(style="thin", color=BORDER_GRAY),
            bottom=Side(style="medium", color=NAVY_HEADER),
        )
    }

def get_data_style(is_even=False, align="left", bold=False, num_format=None):
    fill_color = ROW_STRIPE if is_even else WHITE
    border = Border(
        left=Side(style="thin", color=BORDER_GRAY),
        right=Side(style="thin", color=BORDER_GRAY),
        top=Side(style="thin", color=BORDER_GRAY),
        bottom=Side(style="thin", color=BORDER_GRAY),
    )
    return {
        "font": Font(name="Calibri", size=10, bold=bold, color=TEXT_MAIN),
        "fill": PatternFill(start_color=fill_color, end_color=fill_color, fill_type="solid"),
        "alignment": Alignment(horizontal=align, vertical="center", wrap_text=True),
        "border": border,
        "number_format": num_format
    }

def apply_row_style(sheet, row_idx, values, is_even=False, aligns=None, bolds=None, num_formats=None):
    for col_idx, val in enumerate(values, start=1):
        cell = sheet.cell(row=row_idx, column=col_idx, value=val)
        align = aligns[col_idx - 1] if aligns and col_idx - 1 < len(aligns) else "left"
        bold = bolds[col_idx - 1] if bolds and col_idx - 1 < len(bolds) else False
        num_fmt = num_formats[col_idx - 1] if num_formats and col_idx - 1 < len(num_formats) else None
        
        style = get_data_style(is_even, align=align, bold=bold, num_format=num_fmt)
        cell.font = style["font"]
        cell.fill = style["fill"]
        cell.alignment = style["alignment"]
        cell.border = style["border"]
        if num_fmt:
            cell.number_format = num_fmt

def setup_sheet_header(sheet, title_text, subtitle_text, headers, start_row=4):
    # Title Block
    sheet.cell(row=1, column=1, value=title_text)
    sheet.cell(row=1, column=1).font = Font(name="Calibri", size=14, bold=True, color=NAVY_HEADER)
    sheet.cell(row=2, column=1, value=subtitle_text)
    sheet.cell(row=2, column=1).font = Font(name="Calibri", size=10, italic=True, color=TEXT_MUTED)
    
    # Headers
    h_style = get_header_style()
    sheet.row_dimensions[start_row].height = 28
    for col_idx, h in enumerate(headers, start=1):
        cell = sheet.cell(row=start_row, column=col_idx, value=h)
        cell.font = h_style["font"]
        cell.fill = h_style["fill"]
        cell.alignment = h_style["alignment"]
        cell.border = h_style["border"]

def auto_fit_columns(sheet, min_width=12, max_width=60, padding=4):
    for col in sheet.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = 0
        for cell in col:
            # Skip title row in width calculation
            if cell.row in [1, 2]:
                continue
            val_str = str(cell.value or "")
            lines = val_str.split("\n")
            for line in lines:
                if len(line) > max_len:
                    max_len = len(line)
        width = max(min_width, min(max_len + padding, max_width))
        sheet.column_dimensions[col_letter].width = width


# ==========================================
# Sheet 1: Overview & Summary
# ==========================================
def build_overview_sheet(wb):
    sheet = wb.create_sheet(title="Overview & Summary")
    
    setup_sheet_header(
        sheet,
        title_text="RSK Madhya Pradesh: CLSS Master Dashboard Architecture & Data Register",
        subtitle_text="Reference register of dashboard scope, user roles, cycle filters, and raw data lineage",
        headers=["Field / Dimension", "System Specification", "Operational Description & User Group", "Coverage Standard"],
        start_row=4
    )
    
    meta_rows = [
        ("Dashboard Title", "Shaikshik Samwaad (CLSS) Master Dashboard", "Executive BI reporting on cluster level teacher professional development", "Grades 6-8 Math & Science"),
        ("Primary Ownership", "Rajya Shiksha Kendra (RSK) & Peepul", "Teacher Education & Assessment (TEA) wing with Peepul technical team", "Statewide (All 52 Districts)"),
        ("Target User: State Apex", "RSK Leadership & State Observers", "Monitors overall state turnout, district rankings, and pedagogy benchmarks", "State Overview & League Table"),
        ("Target User: District Core", "DPC, APC, DIET Principals, Program In-charge", "Tracks district standing, DO-to-CLSS cascade, and block variations", "District 360 & Block Directory"),
        ("Target User: Cluster Level", "CACs, Master Facilitators, Monitors", "Tracks local venue conduct, attendance counts, and training delivery", "Cluster Attendance Lists"),
        ("Reporting Cadence", "Monthly Workshop Cycles", "Data captured within 48 hours of each month's Shaikshik Samwaad", "August, September, Consolidated"),
        ("August Scope", "50 Operational Reporting Districts", "Dewas and Sehore recorded 0 workshops (stalled districts in August)", "96.2% District Coverage"),
        ("September Scope", "52 Active Reporting Districts", "All 52 districts conducted workshops and submitted monitoring responses", "100.0% District Coverage"),
        ("Consolidated Scope", "Multi-Cycle Cumulative Footprint", "Combines gross attendance across cycles using a 2-cycle universe standard", "136,854 Gross Universe Base"),
    ]
    
    current_row = 5
    for idx, r in enumerate(meta_rows):
        is_even = (idx % 2 == 1)
        apply_row_style(sheet, current_row, r, is_even=is_even, 
                        bolds=[True, False, False, False],
                        aligns=["left", "left", "left", "center"])
        current_row += 1
        
    current_row += 2
    # Section 2: Raw Data Lineage Table
    sheet.cell(row=current_row, column=1, value="Master Raw Data Lineage Register (Source Files S1 to S6)")
    sheet.cell(row=current_row, column=1).font = Font(name="Calibri", size=12, bold=True, color=NAVY_HEADER)
    current_row += 1
    
    lineage_headers = ["Source ID", "Dataset Name", "Source File Name", "Worksheet Name", "Verified Records (N)", "Primary Key", "Critical Data Fields Used"]
    h_style = get_header_style()
    sheet.row_dimensions[current_row].height = 26
    for col_idx, h in enumerate(lineage_headers, start=1):
        cell = sheet.cell(row=current_row, column=col_idx, value=h)
        cell.font = h_style["font"]
        cell.fill = h_style["fill"]
        cell.alignment = h_style["alignment"]
        cell.border = h_style["border"]
    current_row += 1
    
    lineage_data = [
        ("S1", "Teacher Universe Master", "Varg Wise Teacher Count.xlsx", "Sheet1", "68,427 Teachers", "District + Block", "District, Block, Madhymik (Varg-2) Teacher Count (Col D)"),
        ("S2", "Training Venues Master", "Madhya_Pradesh_All_Clusters_Master_List.xlsx", "Clusters", "2,872 Venues", "Cluster UDISE Code", "2,822 CRC Clusters + 50 DIET Venues (Sehore & Dewas vacant in Aug)"),
        ("S3", "August CLSS Response", "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx", "Participants, Facilitator, Monitor", "29,825 Total Forms", "Phone Number / Timestamp", "23,785 Attendees, 5,463 Facilitators, 577 Monitors"),
        ("S4", "September CLSS Response", "SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx", "Participants, Facilitator, Monitor", "29,399 Total Forms", "Phone Number / Timestamp", "23,169 Attendees, 5,618 Facilitators, 612 Monitors"),
        ("S5", "District Orientation Form", "SS_ResponseDetail_District Level_Grades 6-8_August.xlsx", "Participants", "4,454 Participants", "Participant Phone Number", "District, Role/Designation, DO Attendance, Post-DO Clarity Responses"),
        ("S6", "State TPD Master Mapping", "TPD reach_User mapping_till 20260926.xlsx", "UserMaster", "Unified State Roster", "Employee ID / Mobile", "Cross-cycle teacher verification, DIKSHA ID, and school affiliation"),
    ]
    
    for idx, r in enumerate(lineage_data):
        is_even = (idx % 2 == 1)
        apply_row_style(sheet, current_row, r, is_even=is_even,
                        bolds=[True, True, False, False, False, False, False],
                        aligns=["center", "left", "left", "left", "center", "left", "left"])
        current_row += 1

    sheet.freeze_panes = "B5"
    auto_fit_columns(sheet)


# ==========================================
# Sheet 2: KPIs & Visuals Dictionary
# ==========================================
def build_kpi_dictionary_sheet(wb):
    sheet = wb.create_sheet(title="KPIs & Visuals Dictionary")
    
    headers = [
        "Tab / Location",
        "Item #",
        "Component Name",
        "Component Type",
        "Data Type",
        "What It Tells Leadership",
        "Raw Source File & Sheet",
        "Raw Field / Question ID",
        "Derivation & Calculation Formula",
        "Denominator & Universe Standard",
        "Edge Cases & Exclusions",
        "Status on Dashboard"
    ]
    
    setup_sheet_header(
        sheet,
        title_text="CLSS Master Dashboard: KPI, Metric & Visual Component Dictionary",
        subtitle_text="Exhaustive explanation of where every indicator comes from and how it is mathematically derived",
        headers=headers,
        start_row=4
    )
    
    components = [
        # Top 6 KPI Cards
        (
            "Overview Ribbon", "KPI-01", "Coverage Rate", "KPI Ribbon Card", "Ratio / %",
            "Measures administrative footprint: how many of the state's 52 districts actively conducted and reported workshops.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheet: Participants]", "Distinct District column count",
            "(Count of unique reporting districts) / 52 * 100",
            "Fixed state denominator of 52 total districts",
            "August = 50 districts (96.2%) because Dewas and Sehore stalled; September = 52 districts (100.0%)",
            "Live on Dashboard"
        ),
        (
            "Overview Ribbon", "KPI-02", "Training Centers / Venues", "KPI Ribbon Card", "Integer Count",
            "Shows total active physical workshop locations conducting CLSS across the state.",
            "Madhya_Pradesh_All_Clusters_Master_List.xlsx [Sheet: Clusters]", "Cluster Name & DIET Master List",
            "Count of unique operational CRC clusters (2,822) + active DIET venues (50)",
            "Fixed physical infrastructure footprint of 2,872 venues",
            "Dewas and Sehore DIET venues remained vacant during August cycle",
            "Live on Dashboard"
        ),
        (
            "Overview Ribbon", "KPI-03", "Attending Teachers", "KPI Ribbon Card", "Count & %",
            "Primary participation metric: total middle school teachers who attended CLSS, compared against expected target.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheet: Participants]", "Participant records where Role in ('Teacher', 'Primary Teacher', 'HM')",
            "August: 23,785 / 68,427 = 34.8% turnout. September: 23,169 / 68,427 = 33.9% turnout",
            "Single-cycle denominator = 68,427 Varg-2 base (or facilitator ground target ~68.3k)",
            "Excludes facilitators and monitors to prevent double counting attendee numbers",
            "Live on Dashboard"
        ),
        (
            "Overview Ribbon", "KPI-04", "District Orientation (DO) Participants & Cascade", "KPI Ribbon Card", "Count & Ratio",
            "Measures capacity building cascade: how many district leaders attended DO, and what share actually deployed to facilitate CLSS.",
            "SS_ResponseDetail_District Level_Grades 6-8_August.xlsx [Sheet: Participants] & Cluster Facilitator Sheet",
            "Participant mobile numbers matched across DO and CLSS Facilitator forms",
            "DO Attendees = 4,454. Deployed to CLSS = 3,387 (76.0% cascade). Standby / Non-facilitating = 1,067 (24.0%)",
            "Total DO attendee pool = 4,454 participants across 50 active districts",
            "Identifies district orientation cascade leakages where trained officials did not facilitate cluster sessions",
            "Live on Dashboard"
        ),
        (
            "Overview Ribbon", "KPI-05", "Trainers & Observers", "KPI Ribbon Card", "Count & Ratio",
            "Tracks ground facilitation cadre and monitoring coverage during CLSS sessions.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheets: Facilitator & Monitor]",
            "Facilitator Sheet records (5,463) + Monitor Sheet records (577)",
            "Facilitators: 3,387 DO-trained (70.4%) + 1,427 local facilitators (29.6%). Monitors: 577 total",
            "Total active facilitators deployed = 5,463",
            "Captures instances where local arrangements filled gaps left by non-attending DO leaders",
            "Live on Dashboard"
        ),
        (
            "Overview Ribbon", "KPI-06", "Total Teacher Universe", "KPI Ribbon Card", "Integer Universe",
            "The baseline denominator: total middle school (Varg-2) teacher pool in Madhya Pradesh registered on Shiksha Portal.",
            "Varg Wise Teacher Count.xlsx [Sheet: Sheet1]", "Col D: Madhymik (Varg-2) Total Teachers",
            "68,427 Total Varg-2 Teachers across all 52 districts (Department baseline)",
            "Fixed departmental headcount baseline",
            "Used to prevent false claims of 100% saturation by anchoring to real payroll teacher numbers",
            "Live on Dashboard"
        ),
        # Visuals & Charts
        (
            "State Participation", "VIS-01", "District Participation Leaderboard", "Horizontal Bar Chart", "Ranked %",
            "Ranks all 50/52 districts by teacher turnout rate against expected targets, identifying top and bottom performers.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Participants]", "District column aggregated count / District Varg-2 baseline",
            "For each district: (District Attendees / District Target) * 100. Sorted descending",
            "District-level Varg-2 teacher baseline",
            "Slicers allow viewing All 50, Top 15 frontrunners, or Bottom 15 intervention districts",
            "Live on Dashboard"
        ),
        (
            "State Participation", "VIS-02", "Participant Cadre Breakdown", "Donut / Breakdown", "Category %",
            "Shows who actually attended CLSS workshops: Middle School teachers vs Primary teachers, HMs, and Guest teachers.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheet: Participants]", "Question: आपका पद नाम (Designation / Role)",
            "Count(Role == 'Madhymik Shikshak') / Total Attendees * 100. Repeat for Primary, HM, Guest",
            "Total verified attendees (23,785 in Aug)",
            "Reveals cross-cadre participation where primary teachers attend middle school workshops",
            "Live on Dashboard"
        ),
        (
            "Strategic Matrix", "VIS-03", "4-Quadrant Strategic Distribution", "Bento Grid & Matrix", "Matrix Grouping",
            "Segments districts into 4 actionable operational categories based on Turnout and Pedagogy benchmarks.",
            "Derived from Turnout Rate (VIS-01) and Composite Pedagogy Score (Sheet 3)", "District Turnout % vs District Pedagogy %",
            "Q1 Frontrunners (Turnout >=35%, Pedagogy >=56%); Q2 High Pedagogy, Low Turnout; Q3 High Turnout, Low Pedagogy; Q4 Priority Support (<35%, <56%)",
            "All active districts (50 in Aug, 52 in Sept, 52 Consolidated)",
            "Consolidated view places exactly 27 districts into Priority Support Zone across both cycles",
            "Live on Dashboard"
        ),
        (
            "State Overview Map", "VIS-04", "Interactive 52-District SVG Map", "Choropleth SVG Map", "Spatial",
            "Geographic map of Madhya Pradesh coloring every district by its 4-quadrant standing with low-pedagogy red alert.",
            "Derived from 4-Quadrant Matrix and District Pedagogy Score", "District boundaries mapped to TopoJSON coordinates",
            "Color assigned per district quadrant: Green (Q1), Blue (Q2), Amber (Q3), Gray (Q4). Red pulse border if Pedagogy < 56%",
            "State map of 52 districts",
            "Hover displays exact turnout %, pedagogy score, attendee count, and quadrant label",
            "Live on Dashboard"
        ),
        (
            "Scatter Modal", "VIS-05", "Turnout vs Pedagogy Scatter Plot", "2D Coordinate Scatter", "Bivariate Plot",
            "Plots all districts on a continuous 2D plane with crosshairs at 35% Turnout and 56% Pedagogy to show cluster patterns.",
            "Derived from District Turnout % and District Pedagogy Score", "X: Turnout Rate (0-100%), Y: Pedagogy Score (0-100%)",
            "Plotted point (x, y) per district with bubble radius scaled to district teacher population",
            "All active reporting districts",
            "Provides an unrounded visual distribution of district performance without category binning artifacts",
            "Live on Dashboard"
        ),
        (
            "District 360", "VIS-06", "District Profile & Scorecard", "District Scorecard", "Composite",
            "Provides district leadership with a single deep-dive view into attendance, DO cascade, and cluster-level performance.",
            "All August & September response workbooks", "Filtered by selected District dropdown",
            "District Turnout, Active Venues, DO Cascade %%, Pedagogy Score, Cluster breakdown list",
            "District total universe and clusters",
            "Allows DPCs and APCs to identify which specific clusters within their district brought down the average",
            "Live on Dashboard"
        ),
        (
            "Block Directory", "VIS-07", "Block Directory & Density Scale", "Matrix Table", "Tabular",
            "Granular performance breakdown across all 313 blocks in Madhya Pradesh, grouped by block scale.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Participants]", "Block column aggregated counts",
            "Block Attendees, CRC clusters conducting, average attendance per cluster venue",
            "Block-level cluster lists",
            "Helps pinpoint whether low district turnout is concentrated in 1 or 2 remote blocks",
            "Live on Dashboard"
        ),
        (
            "Teacher Voice", "VIS-08", "Qualitative Feedback Themes", "Horizontal Bar / Cards", "Semantic Categorization",
            "Classifies open-ended Hindi feedback from teachers into actionable qualitative insight categories.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Participants]", "Open-text comment column: आपके सुझाव / अनुभव",
            "Categorized into Academic Utility (39.5%), Joyful Pedagogies (14.0%), Infra/Tech constraints (4.3%), Motivation (1.3%)",
            "Total teachers submitting written feedback (30,000+ comments)",
            "Extracts direct teacher sentiment on classroom readiness and training material quality",
            "Live on Dashboard"
        ),
    ]
    
    current_row = 5
    for idx, c in enumerate(components):
        is_even = (idx % 2 == 1)
        apply_row_style(
            sheet, current_row, c, is_even=is_even,
            bolds=[True, True, True, False, False, False, False, False, False, False, False, True],
            aligns=["left", "center", "left", "left", "center", "left", "left", "left", "left", "left", "left", "center"]
        )
        current_row += 1

    sheet.freeze_panes = "C5"
    sheet.auto_filter.ref = f"A4:L{current_row - 1}"
    auto_fit_columns(sheet)


# ==========================================
# Sheet 3: Pedagogy & Survey Questions
# ==========================================
def build_pedagogy_sheet(wb):
    sheet = wb.create_sheet(title="Pedagogy & Survey Questions")
    
    headers = [
        "Cycle",
        "Question Code",
        "Question Text (Hindi)",
        "Question Text (English Translation)",
        "Academic Domain",
        "Scoring Rubric & Benchmark Key",
        "State Average Baseline %",
        "Weightage (%)",
        "District Aggregation Formula"
    ]
    
    setup_sheet_header(
        sheet,
        title_text="CLSS Pedagogy Index: Question-by-Question Scoring Rubric & Survey Mapping",
        subtitle_text="Item-level breakdown of all pedagogical questions in August and September survey forms",
        headers=headers,
        start_row=4
    )
    
    questions = [
        # August Questions (15 Core)
        ("August 2026", "AUG-PED-01", "क्या सत्र के दौरान शिक्षण सामग्री (TLM) का उपयोग किया गया?", "Was teaching-learning material (TLM) utilized during the session?", "TLM & Teaching Aids", "1 = Yes, actively used; 0 = No or theoretical only", 0.642, 0.08, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-02", "क्या बच्चों के पूर्व ज्ञान को जोड़ने का प्रयास किया गया?", "Did the teacher connect new concepts to students' prior knowledge?", "Lesson Planning & Hook", "1 = Systematic prior knowledge hook; 0 = Direct lecture", 0.584, 0.07, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-03", "क्या कक्षा में सभी बच्चों को बोलने का अवसर मिला?", "Were all students provided equal opportunity to participate and speak?", "Student Engagement", "1 = Inclusive participation across all rows; 0 = Few vocal students", 0.531, 0.07, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-04", "क्या अवधारणा को स्पष्ट करने के लिए दैनिक जीवन के उदाहरण दिए गए?", "Were real-world contextual examples used to explain concepts?", "Contextual Learning", "1 = Contextual local examples used; 0 = Textbook only", 0.612, 0.06, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-05", "क्या शिक्षक ने बच्चों की समझ की जांच के लिए प्रश्न पूछे?", "Did the facilitator ask formative questions to check understanding?", "Formative Assessment", "1 = Regular checks for understanding during flow; 0 = None", 0.558, 0.08, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-06", "क्या बच्चों की गलतियों को सीखने के अवसर के रूप में देखा गया?", "Were student errors treated positively as learning opportunities?", "Constructivist Culture", "1 = Constructive error analysis; 0 = Dismissed or unaddressed", 0.495, 0.06, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-07", "क्या जोड़ी या समूह कार्य (Pair/Group Work) कराया गया?", "Was structured pair or group collaboration conducted?", "Collaborative Learning", "1 = Structured group activity observed; 0 = Individual only", 0.468, 0.07, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-08", "क्या गतिविधि के बाद मुख्य बिंदुओं का समेकन (Wrap-up) किया गया?", "Was there structured summarization and wrap-up after activities?", "Wrap-up & Consolidation", "1 = Dedicated wrap-up and synthesis; 0 = Rushed ending", 0.512, 0.07, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-09", "क्या बच्चों को स्वयं अभ्यास करने का पर्याप्त समय दिया गया?", "Was adequate time allotted for independent student practice?", "Independent Practice", "1 = Minimum 15 mins independent practice; 0 = <5 mins", 0.573, 0.07, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-10", "क्या सत्र की गति बच्चों की सीखने की गति के अनुरूप थी?", "Was the pacing of the session aligned with student learning pace?", "Instructional Pacing", "1 = Paced to student grasp; 0 = Too fast or purely covering syllabus", 0.589, 0.06, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-11", "क्या विज्ञान/गणित किट की सामग्री का प्रत्यक्ष उपयोग हुआ?", "Were Science and Math kit manipulatives physically handled?", "Math & Science Kits", "1 = Hands-on manipulative usage; 0 = Kept locked/unused", 0.524, 0.08, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-12", "क्या शंका समाधान के लिए बच्चों को प्रश्न पूछने के लिए प्रेरित किया गया?", "Were students encouraged to ask clarifying questions?", "Inquiry & Curiosity", "1 = Open questioning encouraged; 0 = One-way instruction", 0.601, 0.06, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-13", "क्या श्यामपट्ट (Blackboard) का कार्य व्यवस्थित और स्पष्ट था?", "Was blackboard work organized, readable, and structured?", "Blackboard Work", "1 = Structured board division and clear notes; 0 = Disorganized", 0.638, 0.05, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-14", "क्या गृहकार्य या आगामी कार्य की स्पष्ट दिशा दी गई?", "Were explicit directions given for homework or follow-up tasks?", "Follow-up & Homework", "1 = Clear practice task assigned; 0 = No closing direction", 0.625, 0.05, "Avg of participant responses in district * 100"),
        ("August 2026", "AUG-PED-15", "क्या शिक्षक ने सत्र के उद्देश्यों को प्राप्त किया?", "Were the core stated session objectives successfully achieved?", "Objective Attainment", "1 = Full objective alignment; 0 = Incomplete coverage", 0.665, 0.07, "Avg of participant responses in district * 100"),

        # September Questions (13 Core Streamlined)
        ("September 2026", "SEPT-PED-01", "क्या अवधारणा को स्पष्ट करने हेतु उपयुक्त TLM/किट का उपयोग हुआ?", "Were appropriate TLMs or kit tools used to clarify concepts?", "TLM & Teaching Aids", "1 = Direct manipulative usage; 0 = Absent", 0.658, 0.09, "Avg of participant responses in district * 100"),
        ("September 2026", "SEPT-PED-02", "क्या बच्चों के दैनिक जीवन और स्थानीय परिवेश से उदाहरण लिए गए?", "Were examples drawn from students' daily life and local context?", "Contextual Learning", "1 = Relevant local references; 0 = Abstract only", 0.627, 0.08, "Avg of participant responses in district * 100"),
        ("September 2026", "SEPT-PED-03", "क्या कक्षा में प्रश्नोत्तर के माध्यम से बच्चों की समझ परखी गई?", "Was understanding checked through structured questioning?", "Formative Assessment", "1 = Frequent checks throughout session; 0 = None", 0.579, 0.09, "Avg of participant responses in district * 100"),
        ("September 2026", "SEPT-PED-04", "क्या बच्चों को समूह या जोड़ी में कार्य करने का अवसर मिला?", "Did students have opportunity to work in pairs or small groups?", "Collaborative Learning", "1 = Group/pair discussion conducted; 0 = Whole-class only", 0.492, 0.08, "Avg of participant responses in district * 100"),
        ("September 2026", "SEPT-PED-05", "क्या गलत उत्तर देने पर बच्चों को सही उत्तर तक पहुंचने में मदद की गई?", "Were students guided toward correct answers upon making mistakes?", "Constructivist Culture", "1 = Prompting and scaffolding; 0 = Corrected directly/scolded", 0.518, 0.08, "Avg of participant responses in district * 100"),
        ("September 2026", "SEPT-PED-06", "क्या बच्चों ने स्वयं करके सीखने (Hands-on Practice) का अनुभव प्राप्त किया?", "Did students experience direct hands-on practice?", "Independent Practice", "1 = Direct student manipulation; 0 = Teacher demonstration only", 0.541, 0.09, "Avg of participant responses in district * 100"),
        ("September 2026", "SEPT-PED-07", "क्या सीखने में पीछे छूट रहे बच्चों पर विशेष ध्यान दिया गया?", "Was targeted attention given to struggling learners?", "Differentiated Support", "1 = Support to slow-paced learners; 0 = Ignored", 0.485, 0.08, "Avg of participant responses in district * 100"),
        ("September 2026", "SEPT-PED-08", "क्या सत्र के अंत में मुख्य बिंदुओं का समेकन हुआ?", "Was there proper consolidation and summary at session end?", "Wrap-up & Consolidation", "1 = Structured wrap-up present; 0 = Abrupt end", 0.534, 0.08, "Avg of participant responses in district * 100"),
        ("September 2026", "SEPT-PED-09", "क्या बच्चों को अपनी बात रखने और प्रश्न पूछने की स्वतंत्रता थी?", "Were students free to express ideas and raise doubts?", "Student Agency", "1 = Open student agency; 0 = Strict one-way lecture", 0.621, 0.07, "Avg of participant responses in district * 100"),
        ("September 2026", "SEPT-PED-10", "क्या श्यामपट्ट का उपयोग अवधारणा को सुव्यवस्थित दर्शाने में हुआ?", "Was blackboard used systematically to map concept flow?", "Blackboard Work", "1 = Clear step-by-step board work; 0 = Minimal or messy", 0.645, 0.06, "Avg of participant responses in district * 100"),
        ("September 2026", "SEPT-PED-11", "क्या गणित/विज्ञान अभ्यास कार्यपुस्तिका का उपयोग हुआ?", "Were Math/Science student practice workbooks actively used?", "Workbook Usage", "1 = Workbook exercises integrated; 0 = Not opened", 0.569, 0.08, "Avg of participant responses in district * 100"),
        ("September 2026", "SEPT-PED-12", "क्या शिक्षक ने पाठ्यपुस्तकीय सिद्धांतों को व्यावहारिक रूप दिया?", "Did the teacher make textbook theory practical and applicable?", "Practical Application", "1 = Demonstrations and models; 0 = Pure reading", 0.598, 0.06, "Avg of participant responses in district * 100"),
        ("September 2026", "SEPT-PED-13", "क्या सत्र समग्र रूप से आनंददायी और प्रेरक था?", "Was the session overall joyful, active, and motivating?", "Joyful Learning", "1 = High student enthusiasm and joy; 0 = Passive/bored", 0.672, 0.06, "Avg of participant responses in district * 100"),
    ]
    
    current_row = 5
    for idx, q in enumerate(questions):
        is_even = (idx % 2 == 1)
        apply_row_style(
            sheet, current_row, q, is_even=is_even,
            bolds=[True, True, False, False, True, False, False, False, False],
            aligns=["center", "center", "left", "left", "left", "left", "center", "center", "left"],
            num_formats=[None, None, None, None, None, None, "0.0%", "0.0%", None]
        )
        current_row += 1

    sheet.freeze_panes = "C5"
    sheet.auto_filter.ref = f"A4:I{current_row - 1}"
    auto_fit_columns(sheet)


# ==========================================
# Sheet 4: Cohorts & Quadrants Logic
# ==========================================
def build_cohorts_quadrants_sheet(wb):
    sheet = wb.create_sheet(title="Cohorts & Quadrants Logic")
    
    setup_sheet_header(
        sheet,
        title_text="CLSS Analytical Models: 4-Quadrant Strategic Matrix & Multi-Cycle Teacher Cohort Deduplication",
        subtitle_text="Technical definitions, benchmark thresholds, and deduplication logic across August and September",
        headers=["Model / Dimension", "Parameter / Classification", "Benchmark Threshold", "Formula / Derivation", "State Total / Footprint", "Operational Meaning & Strategic Action"],
        start_row=4
    )
    
    models_data = [
        # 4 Quadrants
        ("4-Quadrant Matrix", "X-Axis: Participation Benchmark", ">= 35.0% Turnout", "Total Attending Teachers / Baseline Expected Target", "State Avg ~34.8%", "Districts with >=35% are classified as high participation; below 35% require mobilization support"),
        ("4-Quadrant Matrix", "Y-Axis: Pedagogy Benchmark", ">= 56.0% Constructivist Score", "Composite positive response rate across core pedagogy survey items", "State Benchmark 56.0%", "Districts with >=56% reflect active constructivist classroom practices; below 56% trigger low-pedagogy red alert"),
        ("4-Quadrant Matrix", "Quadrant 1: Frontrunners (High Turnout, High Pedagogy)", "Turnout >= 35% AND Pedagogy >= 56%", "Both benchmarks satisfied simultaneously", "August: 12 Districts | Consolidated: 15 Districts", "Role model districts; document and scale their cluster planning and facilitator preparation practices"),
        ("4-Quadrant Matrix", "Quadrant 2: Pedagogical Focus (Low Turnout, High Pedagogy)", "Turnout < 35% AND Pedagogy >= 56%", "High classroom rigor but low overall teacher attendance", "August: 7 Districts | Consolidated: 6 Districts", "Strong academic quality in venues, but administrative follow-up needed to mobilize missing teachers"),
        ("4-Quadrant Matrix", "Quadrant 3: Mobilization Drive (High Turnout, Low Pedagogy)", "Turnout >= 35% AND Pedagogy < 56%", "High attendance but classroom instruction remains traditional/lecture", "August: 14 Districts | Consolidated: 4 Districts", "Successful mobilization; intervention needed to train facilitators on TLM and formative assessment"),
        ("4-Quadrant Matrix", "Quadrant 4: Priority Support Zone (Low Turnout, Low Pedagogy)", "Turnout < 35% AND Pedagogy < 56%", "Both participation and pedagogical indicators lag state benchmarks", "August: 17 Districts | Consolidated: Exactly 27 Districts", "Highest state priority; requires joint administrative and academic review by RSK, DPC, and DIET teams"),
        ("4-Quadrant Matrix", "Low Pedagogy Red Alert", "Pedagogy < 56.0%", "Independent visual flag across maps and tables", "Statewide Trigger", "Highlights districts where classroom delivery falls below acceptable standards regardless of attendance"),

        # Cohort Deduplication
        ("Teacher Cohorts", "Gross Attendees (August)", "Cycle 1 Participation", "Raw count of verified attendee submissions in August form", "23,785 Attendees", "Total middle school teachers who participated in August Shaikshik Samwaad workshops"),
        ("Teacher Cohorts", "Gross Attendees (September)", "Cycle 2 Participation", "Raw count of verified attendee submissions in September form", "23,169 Attendees", "Total middle school teachers who participated in September Shaikshik Samwaad workshops"),
        ("Teacher Cohorts", "Gross Cumulative Footprint", "Gross Turnout (Cycles 1 + 2)", "Sum of August attendees (23,785) + September attendees (23,169)", "46,954 Gross Attendances", "Combined seat occupancy across both monthly workshops"),
        ("Teacher Cohorts", "Net Unique Teachers Reached", "Deduplicated Teacher Reach", "Distinct phone numbers matched across both monthly forms", "33,866 Net Unique Teachers", "True individual teacher reach (49.5% of total 68,427 state teacher universe)"),
        ("Teacher Cohorts", "Retained Teachers (Both Cycles)", "Repeat Attendance", "Teachers present in both August and September response forms", "13,088 Repeat Attendees", "55.0% of August cohort returned in September, reflecting strong sustained engagement"),
        ("Teacher Cohorts", "Fresh Joiners (September Only)", "New Teacher Acquisition", "Teachers present in September who did not attend in August", "10,081 Fresh Joiners", "Expands cumulative program footprint by engaging previously unreached teachers"),
        ("Teacher Cohorts", "August Only Attendees", "Single-Cycle Churn", "Teachers present in August who missed the September workshop", "10,697 Single-Cycle", "Requires district CAC follow-up to understand why they did not return for the second cycle"),
        ("Teacher Cohorts", "Consolidated Universe Standard", "2-Cycle Multiplier Standard", "Gross Attendance / (2 * 68,427 Varg-2 Baseline) * 100", "136,854 Gross Denominator", "Statistically rigorous standard ensuring gross turnout percentages correctly reflect two months of potential attendance"),
    ]
    
    current_row = 5
    for idx, m in enumerate(models_data):
        is_even = (idx % 2 == 1)
        apply_row_style(
            sheet, current_row, m, is_even=is_even,
            bolds=[True, True, False, False, True, False],
            aligns=["left", "left", "center", "left", "center", "left"]
        )
        current_row += 1

    sheet.freeze_panes = "C5"
    sheet.auto_filter.ref = f"A4:F{current_row - 1}"
    auto_fit_columns(sheet)


# ==========================================
# Main Builder
# ==========================================
def build_workbook():
    wb = openpyxl.Workbook()
    # Remove default sheet
    default_sheet = wb.active
    wb.remove(default_sheet)
    
    build_overview_sheet(wb)
    build_kpi_dictionary_sheet(wb)
    build_pedagogy_sheet(wb)
    build_cohorts_quadrants_sheet(wb)
    
    return wb

def main():
    wb = build_workbook()
    output_filename = "CLSS_Dashboard_KPI_Dictionary.xlsx"
    wb.save(output_filename)
    print(f"Successfully generated {output_filename}")

if __name__ == "__main__":
    main()
