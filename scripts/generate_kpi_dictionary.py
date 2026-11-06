"""
generate_kpi_dictionary.py

Generates the exhaustive CLSS Master Dashboard KPI and Visuals Dictionary.
Outputs: CLSS_Dashboard_KPI_Dictionary.xlsx

Key specifications:
1. Covers every visualization, chart, table, card, map, and model across all 11 dashboard tabs.
2. Formats all unique teacher deduplication using official "Unique Teacher ID / Employee Code (कर्मचारी कोड)".
3. Uses human-crafted executive formatting:
   - Deep Navy (#1E3A8A) header styling with white bold text
   - Subtle (#F8FAFC) alternate row striping
   - Hairline (#E2E8F0) gridlines
   - Auto-adjusted column widths with safety margin (+4)
   - Text wrap enabled on long descriptions and formulas
   - Sticky header panes (freeze_panes) on all sheets
   - Clean, plain language with no AI boilerplate or raw dashes
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
    sheet.cell(row=1, column=1, value=title_text)
    sheet.cell(row=1, column=1).font = Font(name="Calibri", size=14, bold=True, color=NAVY_HEADER)
    sheet.cell(row=2, column=1, value=subtitle_text)
    sheet.cell(row=2, column=1).font = Font(name="Calibri", size=10, italic=True, color=TEXT_MUTED)
    
    h_style = get_header_style()
    sheet.row_dimensions[start_row].height = 28
    for col_idx, h in enumerate(headers, start=1):
        cell = sheet.cell(row=start_row, column=col_idx, value=h)
        cell.font = h_style["font"]
        cell.fill = h_style["fill"]
        cell.alignment = h_style["alignment"]
        cell.border = h_style["border"]

def auto_fit_columns(sheet, min_width=12, max_width=65, padding=4):
    for col in sheet.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = 0
        for cell in col:
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
        ("Primary Teacher Identifier", "Unique Teacher ID / Employee Code (कर्मचारी कोड)", "Shiksha Portal / Treasury Employee Code used for all unique teacher tracking", "Certified State Roster Standard"),
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
        ("S3", "August CLSS Response", "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx", "Participants, Facilitator, Monitor", "29,825 Total Forms", "Unique Teacher ID (कर्मचारी कोड)", "23,785 Attendees, 5,463 Facilitators, 577 Monitors"),
        ("S4", "September CLSS Response", "SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx", "Participants, Facilitator, Monitor", "29,399 Total Forms", "Unique Teacher ID (कर्मचारी कोड)", "23,169 Attendees, 5,618 Facilitators, 612 Monitors"),
        ("S5", "District Orientation Form", "SS_ResponseDetail_District Level_Grades 6-8_August.xlsx", "Participants", "4,454 Participants", "Participant Employee Code / Mobile", "District, Role/Designation, DO Attendance, Post-DO Clarity Responses"),
        ("S6", "State TPD Master Mapping", "TPD reach_User mapping_till 20260926.xlsx", "UserMaster", "Unified State Roster", "Employee Code (Unique ID)", "Cross-cycle teacher verification, DIKSHA ID, and school affiliation"),
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
# Sheet 2: KPIs & Visuals Dictionary (All Tabs)
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
        title_text="CLSS Master Dashboard: Complete Visualizations & KPI Dictionary (All Tabs)",
        subtitle_text="Exhaustive explanation of where every indicator comes from and how it is mathematically derived across all 11 tabs",
        headers=headers,
        start_row=4
    )
    
    components = [
        # TAB 1: Overview & Summary
        (
            "1. Overview & Summary", "KPI-01", "Coverage Rate", "KPI Ribbon Card", "Ratio / %",
            "Measures administrative footprint: how many of the state's 52 districts actively conducted and reported workshops.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheet: Participants]", "Distinct District column count",
            "(Count of unique reporting districts) / 52 * 100",
            "Fixed state denominator of 52 total districts",
            "August = 50 districts (96.2%) because Dewas and Sehore stalled; September = 52 districts (100.0%)",
            "Live on Dashboard"
        ),
        (
            "1. Overview & Summary", "KPI-02", "Training Centers / Venues", "KPI Ribbon Card", "Integer Count",
            "Shows total active physical workshop locations conducting CLSS across the state.",
            "Madhya_Pradesh_All_Clusters_Master_List.xlsx [Sheet: Clusters]", "Cluster Name & DIET Master List",
            "Count of unique operational CRC clusters (2,822) + active DIET venues (50)",
            "Fixed physical infrastructure footprint of 2,872 venues",
            "Dewas and Sehore DIET venues remained vacant during August cycle",
            "Live on Dashboard"
        ),
        (
            "1. Overview & Summary", "KPI-03", "Attending Teachers", "KPI Ribbon Card", "Count & %",
            "Primary participation metric: total middle school teachers who attended CLSS, compared against expected target.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheet: Participants]", "Participant records where Role in ('Teacher', 'Primary Teacher', 'HM')",
            "August: 23,785 / 68,427 = 34.8% turnout. September: 23,169 / 68,427 = 33.9% turnout",
            "Single-cycle denominator = 68,427 Varg-2 base (or facilitator ground target ~68.3k)",
            "Excludes facilitators and monitors to prevent double counting attendee numbers",
            "Live on Dashboard"
        ),
        (
            "1. Overview & Summary", "KPI-04", "District Orientation (DO) Participants & Cascade", "KPI Ribbon Card", "Count & Ratio",
            "Measures capacity building cascade: how many district leaders attended DO, and what share actually deployed to facilitate CLSS.",
            "SS_ResponseDetail_District Level_Grades 6-8_August.xlsx [Sheet: Participants] & Cluster Facilitator Sheet",
            "Participant Unique ID / Employee Code matched across DO and CLSS Facilitator forms",
            "DO Attendees = 4,454. Deployed to CLSS = 3,387 (76.0% cascade). Standby / Non-facilitating = 1,067 (24.0%)",
            "Total DO attendee pool = 4,454 participants across 50 active districts",
            "Identifies district orientation cascade leakages where trained officials did not facilitate cluster sessions",
            "Live on Dashboard"
        ),
        (
            "1. Overview & Summary", "KPI-05", "Trainers & Observers", "KPI Ribbon Card", "Count & Ratio",
            "Tracks ground facilitation cadre and monitoring coverage during CLSS sessions.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheets: Facilitator & Monitor]",
            "Facilitator Sheet records (5,463) + Monitor Sheet records (577)",
            "Facilitators: 3,387 DO-trained (70.4%) + 1,427 local facilitators (29.6%). Monitors: 577 total",
            "Total active facilitators deployed = 5,463",
            "Captures instances where local arrangements filled gaps left by non-attending DO leaders",
            "Live on Dashboard"
        ),
        (
            "1. Overview & Summary", "KPI-06", "Total Teacher Universe", "KPI Ribbon Card", "Integer Universe",
            "The baseline denominator: total middle school (Varg-2) teacher pool in Madhya Pradesh registered on Shiksha Portal.",
            "Varg Wise Teacher Count.xlsx [Sheet: Sheet1]", "Col D: Madhymik (Varg-2) Total Teachers",
            "68,427 Total Varg-2 Teachers across all 52 districts (Department baseline)",
            "Fixed departmental headcount baseline",
            "Used to prevent false claims of 100% saturation by anchoring to real payroll teacher numbers",
            "Live on Dashboard"
        ),
        (
            "1. Overview & Summary", "VIS-01", "District Participation Leaderboard", "Horizontal Bar Chart", "Ranked %",
            "Ranks all 50/52 districts by teacher turnout rate against expected targets, identifying top and bottom performers.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Participants]", "District column aggregated count / District Varg-2 baseline",
            "For each district: (District Attendees / District Target) * 100. Sorted descending",
            "District-level Varg-2 teacher baseline",
            "Slicers allow viewing All 50, Top 15 frontrunners, or Bottom 15 intervention districts",
            "Live on Dashboard"
        ),
        (
            "1. Overview & Summary", "VIS-02", "Participant Cadre Breakdown", "Donut Chart", "Category %",
            "Shows who actually attended CLSS workshops: Middle School teachers vs Primary teachers, HMs, and Guest teachers.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheet: Participants]", "Question: आपका पद नाम (Designation / Role)",
            "Count(Role == 'Madhymik Shikshak') / Total Attendees * 100. Repeat for Primary, HM, Guest",
            "Total verified attendees (23,785 in Aug)",
            "Reveals cross-cadre participation where primary teachers attend middle school workshops",
            "Live on Dashboard"
        ),
        (
            "1. Overview & Summary", "VIS-03", "Interactive 52-District SVG Map", "Choropleth SVG Map", "Spatial",
            "Geographic map of Madhya Pradesh coloring every district by its 4-quadrant standing with low-pedagogy red alert.",
            "Derived from 4-Quadrant Matrix and District Pedagogy Score", "District boundaries mapped to TopoJSON coordinates",
            "Color assigned per district quadrant: Green (Q1), Blue (Q2), Amber (Q3), Gray (Q4). Red pulse border if Pedagogy < 56%",
            "State map of 52 districts",
            "Hover displays exact turnout %, pedagogy score, attendee count, and quadrant label",
            "Live on Dashboard"
        ),
        (
            "1. Overview & Summary", "VIS-04", "Pedagogy Benchmark Bar", "Horizontal Bar Chart", "Positive %",
            "Displays state-level positive adoption rate across core pedagogy focus areas (TLM, questioning, wrap-up).",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheet: Participants]", "Survey Questions Q1 to Q15",
            "Sum of positive constructivist answers / Total question responses * 100",
            "Total participant survey responses",
            "Highlights pedagogical areas lagging behind state standard (56%)",
            "Live on Dashboard"
        ),
        (
            "1. Overview & Summary", "VIS-05", "Teacher Trust Index (NTS)", "Bar & Gauge", "Score (-100 to +100)",
            "Calculates Net Trust Score: percentage of enthusiastic promoters minus passive/detractor participants.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheet: Participants]", "Feedback Question: क्या यह सत्र आपके शिक्षण में उपयोगी रहा?",
            "Net Trust Score (NTS) = (% Strongly Agree) - (% Disagree / Strongly Disagree) = +93.8%",
            "Total survey respondents",
            "Validates field teacher satisfaction with cluster training quality",
            "Live on Dashboard"
        ),
        (
            "1. Overview & Summary", "VIS-06", "Teacher Trust & Sentiment Heatmap Table", "Data Heatmap Table", "Tabular %",
            "District-by-district heatmap ranking sentiment, usefulness, and logistical comfort ratings.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Sheet: Participants]", "Feedback columns (Training utility, venue adequacy, facilitator support)",
            "Average positive sentiment score per district mapped to color gradient",
            "All reporting districts",
            "Pinpoints districts where teacher sentiment is low despite high attendance",
            "Live on Dashboard"
        ),
        (
            "1. Overview & Summary", "VIS-07", "4-Quadrant Priority Matrix Table", "Bento Grid Table", "Categorical Roster",
            "Lists all districts grouped into their respective 4 quadrants with headcount and pedagogy scores.",
            "Derived from Turnout Rate (VIS-01) and Pedagogy Score (VIS-04)", "District Turnout % vs District Pedagogy %",
            "Q1 (Frontrunners), Q2 (Pedagogy Focus), Q3 (Turnout Focus), Q4 (Priority Support - 27 dist. Consolidated)",
            "52 reporting districts",
            "Enables instant executive filtering to see priority intervention districts",
            "Live on Dashboard"
        ),
        (
            "1. Overview & Summary", "VIS-08", "Turnout vs Pedagogy Scatter Plot Modal", "2D Coordinate Scatter", "Bivariate Plot",
            "Continuous 2D plane showing all districts with crosshair benchmarks at 35% Turnout and 56% Pedagogy.",
            "Derived from District Turnout % and District Pedagogy Score", "X: Turnout Rate (0-100%), Y: Pedagogy Score (0-100%)",
            "Plotted point (x, y) per district with bubble radius scaled to district teacher population",
            "All active reporting districts",
            "Provides an unrounded visual distribution of district performance without category binning artifacts",
            "Live on Dashboard"
        ),

        # TAB 2: Key Goals & Results Framework
        (
            "Key Goals & Results Framework", "VIS-09", "Results Framework Sub-Indicator Breakdown", "Horizontal Stacked Bar", "Indicator %",
            "Visualizes progress across the 4 Results Framework pillars: Institutional Participation, Training Delivery, Pedagogy Mastery, and Governance.",
            "SS_ResponseDetail_Cluster Level & District Level workbooks", "RF Indicator codes RF-1.1 through RF-4.3",
            "Achieved benchmark percentage per sub-indicator against milestone target",
            "Pillar milestone targets",
            "Identifies specific institutional bottlenecks in the training delivery chain",
            "Live on Dashboard"
        ),
        (
            "Key Goals & Results Framework", "VIS-10", "Sub-Indicators & Data Source Verification Table", "Tabular Registry", "Verification Matrix",
            "Detailed registry proving the data source, calculation method, and verified baseline for all RF indicators.",
            "All response workbooks and admin registers", "Indicator ID and corresponding survey question ID",
            "Formula, verified numerator, denominator, and certified zero-delta reconciliation",
            "All RF indicators",
            "Provides audit trail for third-party evaluation and state review committee",
            "Live on Dashboard"
        ),
        (
            "Key Goals & Results Framework", "VIS-11", "Statewide 52-District RF Compliance Matrix", "Grid Heatmap Table", "District Compliance",
            "Matrix showing compliance status (Green/Amber/Red) across all 52 districts for every core RF indicator.",
            "District aggregated survey responses", "District compliance across 8 core operational milestones",
            "Threshold checks: Green = Achieved, Amber = In Progress, Red = Off Track",
            "52 Districts x 8 Indicators",
            "Allows state directors to spot systemic district non-compliance at a glance",
            "Live on Dashboard"
        ),

        # TAB 3: District Profile (360°)
        (
            "2. District Profile (360°)", "VIS-12", "District 360 Executive KPI Cards", "Stat Cards", "District Metrics",
            "Displays headline numbers for the selected district: Turnout %, Total Attendees, Active Clusters, DO Cascade %, State Rank.",
            "Response workbooks filtered by selected district", "District aggregated totals",
            "District specific metrics calculated dynamically upon dropdown selection",
            "Selected district teacher universe",
            "Gives district collector and DPC an immediate executive briefing on their district",
            "Live on Dashboard"
        ),
        (
            "2. District Profile (360°)", "VIS-13", "Block-Level Turnout Comparison Chart", "Horizontal Bar Chart", "Block Turnout %",
            "Compares teacher turnout percentages across all blocks within the selected district.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Participants]", "Block column aggregated counts / Block target",
            "(Block Attendees / Block Expected Target) * 100",
            "Block teacher target",
            "Pinpoints intra-district disparity where 1 lagging block drags down the entire district",
            "Live on Dashboard"
        ),
        (
            "2. District Profile (360°)", "VIS-14", "Block Breakdown Interactive Table", "Sortable Table", "Block Roster",
            "Scrollable table of blocks in the district showing target, actual attendees, cluster count, and percentage.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx", "Block name, clusters conducting, attendee counts",
            "Granular block statistics with row click-to-filter capability",
            "Blocks within chosen district",
            "Enables district officials to review specific block targets during review meetings",
            "Live on Dashboard"
        ),
        (
            "2. District Profile (360°)", "VIS-15", "District Pedagogy Assessment Radar/Bar", "Bar / Radar", "Domain Score",
            "Compares the chosen district's pedagogical performance against the statewide benchmark across 5 core domains.",
            "Cluster Level Participants Sheet", "Pedagogy questions grouped by domain",
            "District average positive score vs State average positive score",
            "District survey respondents",
            "Helps DIET academic faculty identify where teacher training content needs strengthening",
            "Live on Dashboard"
        ),
        (
            "2. District Profile (360°)", "VIS-16", "Attendance Gender Split", "Donut Chart", "Gender %",
            "Shows male vs female teacher attendance proportions in the selected district.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Participants]", "Demographic question: लिंग (Gender)",
            "Count(Female) / Total Attendees * 100 vs Count(Male) / Total Attendees * 100",
            "Total district attendees",
            "Monitors gender equity and participation dynamics across rural and urban clusters",
            "Live on Dashboard"
        ),
        (
            "2. District Profile (360°)", "VIS-17", "Side-by-Side District Comparator", "Dual-Bar Chart", "Peer Benchmark",
            "Allows direct head-to-head comparison between any two chosen districts on Turnout, Pedagogy, and Cascade.",
            "All response datasets", "Two user-selected district dropdowns",
            "Side-by-side metric comparison with delta indicators",
            "Both selected districts",
            "Enables peer learning by pairing a lower-performing district with a high-performing neighbor",
            "Live on Dashboard"
        ),

        # TAB 4: District Rankings & League Table
        (
            "3. District Rankings", "VIS-18", "State League Performance Matrix", "Interactive Table", "State League Table",
            "Comprehensive ranking table of all 52 districts sortable by Turnout %, Pedagogy %, DO Attendance, Rank, and Quadrant.",
            "All response datasets aggregated at district level", "District summary metrics",
            "Multi-column sorting and filtering across attendance, pedagogy, and cascade metrics",
            "All 52 districts in Madhya Pradesh",
            "Serves as the official state league table for state-level monthly review video conferences",
            "Live on Dashboard"
        ),

        # TAB 5: Block Directory & Scale Matrix
        (
            "4. Block Directory", "VIS-19", "Madhya Pradesh Block Directory Table", "Searchable Grid Table", "Block Registry",
            "Searchable directory of all 313 blocks in MP, showing turnout %, cluster venues, and attendance density.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Participants]", "Block name, District, Cluster count, Attendees",
            "Block Attendees, Target, Turnout %, Venues conducting, Avg attendees per venue",
            "All 313 blocks across Madhya Pradesh",
            "Equips state and divisional officers to inspect block-level operational density",
            "Live on Dashboard"
        ),

        # TAB 6: Survey Questions Master
        (
            "5. Survey Questions", "VIS-20", "Statewide Response Distribution Chart", "Bar Chart", "Option %",
            "Dynamic bar chart displaying the percentage breakdown of choices selected for any of the 74 survey questions.",
            "Cluster Level Participants, Facilitator, and Monitor workbooks", "Selected Question ID dropdown",
            "Count(Selected Option) / Total Question Responses * 100",
            "Total responses for chosen question",
            "Reveals the exact spread of teacher responses on pedagogy, logistics, and training materials",
            "Live on Dashboard"
        ),
        (
            "5. Survey Questions", "VIS-21", "District & Block Breakdown Heatmap Table", "Data Heatmap Table", "Intra-District %",
            "Shows how each district and block answered the selected survey question, highlighting high and low adoption areas.",
            "Cluster Level response workbooks", "District, Block, and Question choice",
            "Positive response rate per district/block for the chosen question",
            "All reporting districts and blocks",
            "Allows subject specialists to see which specific districts have misunderstood key pedagogical concepts",
            "Live on Dashboard"
        ),

        # TAB 7: Teaching Quality & Pedagogy Radar
        (
            "6. Teaching Quality", "VIS-22", "Teacher Pedagogy Competency Radar", "Polar Radar Chart", "Domain Competencies",
            "Multi-axis radar comparing teacher competency across Hook Activities, Checks for Understanding, Cold Calling, TLM, and Wrap-up.",
            "Cluster Level Participants Sheet", "Questions grouped into 5 constructivist domains",
            "Calculated domain mastery scores plotted across 5 radial axes",
            "Statewide participant pool",
            "Identifies cold calling and independent student practice as the lowest-scoring competencies statewide",
            "Live on Dashboard"
        ),
        (
            "6. Teaching Quality", "VIS-23", "Classroom Reality Triangulation Table (CRO)", "Triangulation Matrix", "Observation Data",
            "Triangulates self-reported teacher survey responses against independent Classroom Observation (CRO) field notes.",
            "Analysis_CRO Dataset & Master Survey Telemetry", "Triangulated indicator codes",
            "Compares teacher-reported adoption % against external monitor-observed classroom reality",
            "Sampled classroom observation venues",
            "Highlights reporting biases where teachers report high TLM usage but monitors observe low physical handling",
            "Live on Dashboard"
        ),

        # TAB 8: Recommended Measures & Governance
        (
            "7. Recommended Measures", "VIS-24", "Recommended Measures & Action Matrix for RSK", "Governance Matrix", "Policy Directives",
            "Actionable policy suggestions categorized into Immediate Directives, Capacity Building, and Resource Allocation.",
            "Synthesized from field monitor reports and teacher suggestions", "Qualitative recommendations tagged by operational urgency",
            "Prioritized matrix with designated responsible nodal officers and completion timelines",
            "Statewide program governance",
            "Translates dashboard analytics into concrete executive actions for upcoming monthly cycles",
            "Live on Dashboard"
        ),

        # TAB 9: AI Insights & Strategic Briefing
        (
            "8. AI Insights", "VIS-25", "Breakthrough Turnarounds & Gainers Matrix", "Ranked Gainer Cards", "Delta Trajectory",
            "Highlights districts that demonstrated the largest positive growth in teacher turnout between August and September.",
            "Comparative multi-cycle dataset", "September Turnout % minus August Turnout %",
            "Sorted descending by turnout percentage point increase",
            "Districts with positive multi-cycle deltas",
            "Celebrates district leadership efforts and provides case studies of successful mobilization",
            "Live on Dashboard"
        ),
        (
            "8. AI Insights", "VIS-26", "Districts Requiring Rapid Intervention Table", "Priority Alert Table", "Intervention Matrix",
            "Flags districts experiencing significant drops in attendance or persisting in the low-pedagogy red alert zone.",
            "Comparative multi-cycle dataset", "Negative delta in turnout or pedagogy score < 50%",
            "Ranked by severity of drop, specifying exact failure modes (cascade leak, low cluster density)",
            "Lagging districts",
            "Triggers targeted field visits and support calls from the RSK state monitoring team",
            "Live on Dashboard"
        ),
        (
            "8. AI Insights", "VIS-27", "NITI Aspirational Districts Trajectory Matrix", "8-District Matrix Table", "Aspirational Tracking",
            "Dedicated performance tracking matrix for the 8 NITI Aayog aspirational districts in Madhya Pradesh.",
            "Multi-cycle response datasets", "Filtered for 8 Aspirational Districts (Barwani, Chhatarpur, Damoh, Guna, Khandwa, Rajgarh, Sheopur, Vidisha)",
            "Tracks Turnout, Pedagogy, and Cascade growth across cycles for aspirational districts",
            "8 NITI Aspirational Districts",
            "Supports high-level government reporting for state and central aspirational district programs",
            "Live on Dashboard"
        ),

        # TAB 10: Qualitative Research & Teacher Voice
        (
            "9. Qualitative Research", "VIS-28", "Thematic Topology of Field Voices", "Semantic Cluster Bar", "Theme Share %",
            "Visual cluster breakdown of 30,000+ teacher open-ended feedback comments into 5 primary themes.",
            "SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx [Participants]", "Open-ended Hindi text comment field",
            "Academic Utility (39.5%), Joyful Pedagogies (14.0%), Tech Constraints (4.3%), Motivation (1.3%), Logistics (40.9%)",
            "30,000+ open-ended text submissions",
            "Validates that teachers value hands-on activity kits far more than theoretical lectures",
            "Live on Dashboard"
        ),
        (
            "9. Qualitative Research", "VIS-29", "DO Leaders vs Classroom Teachers Alignment Comparator", "Divergence Bar Chart", "Psychometric Gap",
            "Measures perceptual gap between what District Orientation leaders believe was trained vs what teachers experienced.",
            "Matched responses from DO Attendee and CLSS Attendee workbooks", "Comparative understanding questions on themes and TLM",
            "Difference between DO participant confidence % and CLSS teacher comprehension %",
            "District Orientation and Cluster participant cohorts",
            "Identifies training transmission loss occurring between district level and cluster level",
            "Live on Dashboard"
        ),
        (
            "9. Qualitative Research", "VIS-30", "Diagnostic Distractor Deconstruction Matrix", "Root-Cause Error Matrix", "Cognitive Traps",
            "Breaks down why teachers chose incorrect distractor options on pedagogy survey questions.",
            "Cluster Level Participants Sheet", "Incorrect choices on conceptual pedagogy questions",
            "Categorization of wrong options into Rote Thinking, Time Scarcity, or Lack of Material",
            "Incorrect participant responses",
            "Guides curriculum designers to rewrite facilitator guidebooks to address specific teacher misconceptions",
            "Live on Dashboard"
        ),

        # TAB 11: Teacher Attendance & Cohorts
        (
            "10. Attendance & Cohorts", "COH-01", "Total Unique Teachers Reached", "Cohort Ribbon Card", "Net Headcount",
            "Cumulative net unique middle school teachers reached across both workshop cycles, deduplicated by Unique Teacher ID (कर्मचारी कोड).",
            "Combined August & September Participants Sheets", "Unique Teacher ID / Employee Code (कर्मचारी कोड)",
            "Count of distinct Employee Codes participating in August or September = 33,866 net unique teachers",
            "State Varg-2 baseline of 68,427 teachers (49.5% state coverage reached)",
            "Deduplicates teachers who attended both months so each educator is counted exactly once",
            "Live on Dashboard"
        ),
        (
            "10. Attendance & Cohorts", "COH-02", "Retained Teachers Coming Back", "Cohort Ribbon Card", "Repeat Count & %",
            "Shows teachers who attended both August and September workshops, measuring sustained program engagement.",
            "Combined August & September Participants Sheets", "Unique Teacher ID (कर्मचारी कोड) present in both datasets",
            "Count of Employee Codes present in BOTH months = 13,088 repeat teachers (55.0% retention of August cohort)",
            "August attendee cohort (23,785)",
            "Demonstrates that over half of initial attendees returned for the second consecutive month",
            "Live on Dashboard"
        ),
        (
            "10. Attendance & Cohorts", "COH-03", "New Teachers Joining (Fresh Faces)", "Cohort Ribbon Card", "Acquisition Count",
            "Measures program expansion: teachers who attended September workshop for the first time.",
            "Combined August & September Participants Sheets", "Unique Teacher ID (कर्मचारी कोड) in September but not August",
            "Count of Employee Codes present in September only = 10,081 fresh teachers (44.3% of September attendance)",
            "September attendee cohort (23,169)",
            "Proves the program expanded reach to new teachers rather than circulating among the same cohort",
            "Live on Dashboard"
        ),
        (
            "10. Attendance & Cohorts", "COH-04", "Missed Last Month (Follow-up List)", "Cohort Ribbon Card", "Churn Count",
            "Identifies teachers who attended August but did not return in September, creating an actionable re-engagement list.",
            "Combined August & September Participants Sheets", "Unique Teacher ID (कर्मचारी कोड) in August but absent in September",
            "Count of Employee Codes present in August only = 10,697 single-cycle teachers",
            "August attendee cohort (23,785)",
            "Generates targeted calling rosters for CACs to invite these teachers back for upcoming workshops",
            "Live on Dashboard"
        ),
        (
            "10. Attendance & Cohorts", "COH-05", "Unreached Teacher Universe", "Cohort Ribbon Card", "Gap Count",
            "Shows the remaining middle school teacher population yet to attend a single Shaikshik Samwaad workshop.",
            "Varg Wise Teacher Count.xlsx & Combined Attendance Roster", "Statewide Varg-2 Universe minus Net Unique Reached",
            "68,427 Total Teachers minus 33,866 Net Unique Reached = 34,561 unreached teachers (50.5% gap)",
            "Total state teacher universe (68,427)",
            "Maintains administrative transparency on remaining work needed to achieve 100% saturation",
            "Live on Dashboard"
        ),
        (
            "10. Attendance & Cohorts", "VIS-31", "District-by-District Cohort Retention Matrix", "Interactive Table", "District Cohort Table",
            "Complete 52-district roster displaying August attendees, September attendees, Retained repeats, Fresh joiners, and Net reach.",
            "Combined attendance datasets aggregated by district", "District and Unique Teacher ID (कर्मचारी कोड)",
            "District Gross Attendance, Net Unique Teachers, Retention Rate %, Fresh Joiner Count",
            "All 52 districts in Madhya Pradesh",
            "Allows each district to see its exact retention rate and unreached teacher gap",
            "Live on Dashboard"
        ),
        (
            "10. Attendance & Cohorts", "VIS-32", "Mathematical Saturation Trajectory Model", "Projection Curve", "Trajectory Curve",
            "Mathematical model simulating cumulative unique teacher reach over upcoming monthly cycles (Target: 80%+ by Dec 2026).",
            "Historical new acquisition rate across cycles (44.3% fresh joiner rate)", "Logarithmic reach projection formula based on fresh joiner retention",
            "Projected unique reach = Previous Unique + (Target * Fresh Rate * Unreached Pool Factor)",
            "Statewide teacher universe",
            "Assists state planning leadership in scheduling follow-up cycles to reach universal teacher coverage",
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
        subtitle_text="Technical definitions, benchmark thresholds, and deduplication logic based on Unique Teacher ID (कर्मचारी कोड)",
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

        # Cohort Deduplication (Mapped via Unique Teacher ID / Employee Code)
        ("Teacher Cohorts", "Primary Teacher Identifier", "Official Employee Code", "Official Unique Teacher ID / Employee Code (कर्मचारी कोड) from Shiksha Portal", "Standardized ID Key", "Ensures precise individual teacher tracking and eliminates duplicate records"),
        ("Teacher Cohorts", "Gross Attendees (August)", "Cycle 1 Participation", "Count of verified teacher records in August form", "23,785 Attendees", "Total middle school teachers who participated in August Shaikshik Samwaad workshops"),
        ("Teacher Cohorts", "Gross Attendees (September)", "Cycle 2 Participation", "Count of verified teacher records in September form", "23,169 Attendees", "Total middle school teachers who participated in September Shaikshik Samwaad workshops"),
        ("Teacher Cohorts", "Gross Cumulative Footprint", "Gross Turnout (Cycles 1 + 2)", "Sum of August attendees (23,785) + September attendees (23,169)", "46,954 Gross Attendances", "Combined seat occupancy across both monthly workshops"),
        ("Teacher Cohorts", "Net Unique Teachers Reached", "Deduplicated Teacher Reach", "Distinct Employee Codes (कर्मचारी कोड) matched across both monthly forms", "33,866 Net Unique Teachers", "True individual teacher reach (49.5% of total 68,427 state teacher universe)"),
        ("Teacher Cohorts", "Retained Teachers (Both Cycles)", "Repeat Attendance", "Teachers whose Employee Code is present in both August and September response forms", "13,088 Repeat Attendees", "55.0% of August cohort returned in September, reflecting strong sustained engagement"),
        ("Teacher Cohorts", "Fresh Joiners (September Only)", "New Teacher Acquisition", "Teachers whose Employee Code is present in September but absent in August", "10,081 Fresh Joiners", "Expands cumulative program footprint by engaging previously unreached teachers"),
        ("Teacher Cohorts", "August Only Attendees", "Single-Cycle Churn", "Teachers whose Employee Code is present in August but absent in September", "10,697 Single-Cycle", "Requires district CAC follow-up to understand why they did not return for the second cycle"),
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
    default_sheet = wb.active
    wb.remove(default_sheet)
    
    build_overview_sheet(wb)
    build_kpi_dictionary_sheet(wb)
    build_pedagogy_sheet(wb)
    build_cohorts_quadrants_sheet(wb)
    
    return wb

def main():
    wb = build_workbook()
    primary_filename = "CLSS_Dashboard_KPI_Dictionary.xlsx"
    fallback_filename = "CLSS_Dashboard_KPI_Dictionary_Updated.xlsx"
    
    try:
        wb.save(primary_filename)
        print(f"Successfully generated {primary_filename}")
        return primary_filename
    except PermissionError:
        wb.save(fallback_filename)
        print(f"Primary file was open in Excel. Successfully saved updated version to {fallback_filename}")
        return fallback_filename

if __name__ == "__main__":
    main()
