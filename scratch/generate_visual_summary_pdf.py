import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.pdfgen import canvas
import pypdf

def generate_compact_one_page_pdf(filename="RSK_Shaikshik_Samwaad_One_Page_Visual_Summary.pdf"):
    # Target exact 1-page layout on A4 (595.27 x 841.89 pt)
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=28,
        rightMargin=28,
        topMargin=20,
        bottomMargin=20
    )

    styles = getSampleStyleSheet()
    
    primary_color = colors.HexColor("#0f172a") # Slate 900
    teal_color = colors.HexColor("#008080")    # Peepul Teal
    emerald_color = colors.HexColor("#047857") # Accent Green
    amber_color = colors.HexColor("#b45309")   # Accent Amber
    dark_red = colors.HexColor("#b91c1c")      # Red

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=15,
        textColor=primary_color,
        spaceAfter=1
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10,
        textColor=teal_color,
        spaceAfter=3
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor("#475569")
    )

    h2_style = ParagraphStyle(
        'H2Style',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=primary_color,
        spaceBefore=4,
        spaceAfter=2
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.8,
        leading=8.5,
        textColor=colors.HexColor("#334155")
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=8.5,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.8,
        leading=8.2,
        textColor=colors.HexColor("#1e293b")
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.8,
        leading=8.2,
        textColor=colors.HexColor("#0f172a")
    )

    table_cell_center = ParagraphStyle(
        'TableCellCenter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.8,
        leading=8.2,
        textColor=colors.HexColor("#1e293b"),
        alignment=1
    )

    story = []

    # Title & Metadata Block
    story.append(Paragraph("RSK Shaikshik Samwaad: Executive Visual Summary (One-Page Briefing)", title_style))
    story.append(Paragraph("Statewide Implementation, Cadre Mobilization & Pedagogical Diagnostic Briefing", subtitle_style))
    
    meta_text = (
        "<b>State Apex:</b> Rajya Shiksha Kendra (RSK), MP | "
        "<b>Evaluation Partner:</b> Peepul India | "
        "<b>Cadre Universe:</b> 68,427 Varg-2 Teachers | "
        "<b>Target Scope:</b> Classes 6–8 Shikshak Samvad (52 Districts, 322 Blocks, 4,804 Mapped Clusters) | "
        "<b>Cycles:</b> Aug & Sep 2026"
    )
    story.append(Paragraph(meta_text, meta_style))
    story.append(Spacer(1, 2))
    story.append(HRFlowable(width="100%", thickness=1, color=teal_color, spaceAfter=3))

    # 1. Executive Master KPIs
    story.append(Paragraph("1. Executive Master KPIs (Live Dashboard Reconciled)", h2_style))
    
    kpi_data = [
        [
            Paragraph("KPI Metric", table_header_style),
            Paragraph("August 2026", table_header_style),
            Paragraph("September 2026", table_header_style),
            Paragraph("Consolidated Total", table_header_style),
            Paragraph("Operational Lineage & Scope", table_header_style)
        ],
        [
            Paragraph("<b>District Saturation</b>", table_cell_bold),
            Paragraph("<b>50 / 52</b> (96.2%)", table_cell_center),
            Paragraph("<b>52 / 52</b> (100%)", table_cell_center),
            Paragraph("<b>52 / 52</b> (100%)", table_cell_center),
            Paragraph("<b>Aug:</b> 50 active (Dewas & Sehore vacant). <b>Sep:</b> 52 active (100% full coverage)", table_cell_style)
        ],
        [
            Paragraph("<b>Active Venues</b>", table_cell_bold),
            Paragraph("<b>2,874</b> Venues", table_cell_center),
            Paragraph("<b>2,861</b> Venues", table_cell_center),
            Paragraph("<b>5,735</b> Sessions", table_cell_center),
            Paragraph("2,822 Cluster + 52 DIETs (Aug) | 2,809 Cluster + 52 DIETs (Sep)", table_cell_style)
        ],
        [
            Paragraph("<b>Classroom Teachers</b>", table_cell_bold),
            Paragraph("<b>23,785</b> / 68,369 (<b>34.8%</b>)", table_cell_center),
            Paragraph("<b>23,169</b> / 67,222 (<b>34.5%</b>)", table_cell_center),
            Paragraph("<b>46,954</b> / 135,591 (<b>34.6%</b>)", table_cell_center),
            Paragraph("Actual attending Varg-2 teachers vs. Facilitator expected target", table_cell_style)
        ],
        [
            Paragraph("<b>District Officials (DO)</b>", table_cell_bold),
            Paragraph("<b>4,454</b> Officers", table_cell_center),
            Paragraph("<b>4,520</b> Officers", table_cell_center),
            Paragraph("<b>8,974</b> Attendees", table_cell_center),
            Paragraph("DIET faculty, APCs, BACs, and CACs oriented at District HQ", table_cell_style)
        ],
        [
            Paragraph("<b>Master Facilitators</b>", table_cell_bold),
            Paragraph("<b>4,891</b> Leads", table_cell_center),
            Paragraph("<b>4,850</b> Leads", table_cell_center),
            Paragraph("<b>9,741</b> Leads", table_cell_center),
            Paragraph("4,814 Cluster Facilitators + 77 District Master Trainers (Aug)", table_cell_style)
        ],
        [
            Paragraph("<b>Field Observers / Monitors</b>", table_cell_bold),
            Paragraph("<b>572</b> Monitors", table_cell_center),
            Paragraph("<b>560</b> Monitors", table_cell_center),
            Paragraph("<b>1,132</b> Audits", table_cell_center),
            Paragraph("516 Cluster Observers + 56 District Observers (Aug)", table_cell_style)
        ]
    ]

    col_widths_kpi = [105, 80, 80, 85, 189]
    t_kpi = Table(kpi_data, colWidths=col_widths_kpi)
    t_kpi.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), teal_color),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(t_kpi)

    # 2. Statewide Varg-2 Participation Funnel
    story.append(Paragraph("2. Statewide Varg-2 Participation Funnel (Total Universe: 68,427)", h2_style))
    
    funnel_data = [
        [
            Paragraph("<b>Funnel Stage</b>", table_cell_bold),
            Paragraph("<b>August 2026 Cycle</b>", table_cell_bold),
            Paragraph("<b>September 2026 Cycle</b>", table_cell_bold),
            Paragraph("<b>Strategic Operational Takeaway</b>", table_cell_bold)
        ],
        [
            Paragraph("<b>1. District Coverage Status</b>", table_cell_style),
            Paragraph("<b>50 / 52</b> (Dewas & Sehore Vacant)", table_cell_center),
            Paragraph("<b>52 / 52</b> (100% Full Saturation)", table_cell_center),
            Paragraph("Full coverage restored in Sep after initial August cluster delay", table_cell_style)
        ],
        [
            Paragraph("<b>2. Facilitator Expected Target</b>", table_cell_style),
            Paragraph("<b>68,369</b> (99.9% of Universe)", table_cell_center),
            Paragraph("<b>67,222</b> (98.2% of Universe)", table_cell_center),
            Paragraph("Ground facilitators accurately reflect full ~68k Varg-2 teacher baseline", table_cell_style)
        ],
        [
            Paragraph("<b>3. Actual Attending Teachers</b>", table_cell_bold),
            Paragraph("<font color='#047857'><b>23,785 (34.8% Turnout)</b></font>", table_cell_center),
            Paragraph("<font color='#047857'><b>23,169 (34.5% Turnout)</b></font>", table_cell_center),
            Paragraph("High month-on-month core participation stability across both cycles", table_cell_style)
        ],
        [
            Paragraph("<b>4. Non-Attendance Mobilization Gap</b>", table_cell_style),
            Paragraph("<font color='#b91c1c'><b>44,584 (65.2% Gap)</b></font>", table_cell_center),
            Paragraph("<font color='#b91c1c'><b>44,053 (65.5% Gap)</b></font>", table_cell_center),
            Paragraph("Primary growth lever for RSK: Enforcing block-level attendance follow-up", table_cell_style)
        ]
    ]

    t_funnel = Table(funnel_data, colWidths=[130, 110, 110, 189])
    t_funnel.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#e2e8f0")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0, 0), (-1, -1), 1.8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.8),
    ]))
    story.append(t_funnel)

    # 3. Classroom Pedagogy & Misconception Matrix
    story.append(Paragraph("3. Classroom Pedagogy & Misconception Matrix", h2_style))

    ped_data = [
        [
            Paragraph("Pedagogical Domain", table_header_style),
            Paragraph("Diagnostic Question & Construct", table_header_style),
            Paragraph("Constructive Mastery Option", table_header_style),
            Paragraph("Dominant Misconception Trap", table_header_style),
            Paragraph("Mastery", table_header_style),
            Paragraph("Trap %", table_header_style)
        ],
        [
            Paragraph("<b>Hands-on TLM Purpose</b>", table_cell_bold),
            Paragraph("<b>Q95</b>: Role of concrete materials", table_cell_style),
            Paragraph("Structured reflection & inquiry on concept", table_cell_style),
            Paragraph("<i>'Activities ensure learning automatically'</i>", table_cell_style),
            Paragraph("<font color='#047857'><b>51.9%</b></font>", table_cell_center),
            Paragraph("<font color='#b91c1c'><b>48.1%</b></font>", table_cell_center)
        ],
        [
            Paragraph("<b>Classroom Belonging</b>", table_cell_bold),
            Paragraph("<b>Q97</b>: Response to student struggle", table_cell_style),
            Paragraph("Normalize mistakes as natural steps", table_cell_style),
            Paragraph("<i>'Praise only students with correct answers'</i>", table_cell_style),
            Paragraph("<font color='#b91c1c'><b>33.9%</b></font>", table_cell_center),
            Paragraph("<font color='#b91c1c'><b>66.1%</b></font>", table_cell_center)
        ],
        [
            Paragraph("<b>Intellectual Safety</b>", table_cell_bold),
            Paragraph("<b>Q96</b>: Handling misconceptions", table_cell_style),
            Paragraph("Use errors as diagnostic entry points", table_cell_style),
            Paragraph("<i>'Correct student immediately before failing'</i>", table_cell_style),
            Paragraph("<font color='#047857'><b>62.0%</b></font>", table_cell_center),
            Paragraph("<font color='#b45309'><b>38.0%</b></font>", table_cell_center)
        ],
        [
            Paragraph("<b>Peer Dialogue</b>", table_cell_bold),
            Paragraph("<b>Q98</b>: Structuring group discussions", table_cell_style),
            Paragraph("Students argue and debate in peer groups", table_cell_style),
            Paragraph("<i>'Teacher summarizes topic after question'</i>", table_cell_style),
            Paragraph("<font color='#047857'><b>54.2%</b></font>", table_cell_center),
            Paragraph("<font color='#b45309'><b>45.8%</b></font>", table_cell_center)
        ]
    ]

    col_widths_ped = [95, 95, 115, 145, 42, 47]
    t_ped = Table(ped_data, colWidths=col_widths_ped)
    t_ped.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e293b")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0, 0), (-1, -1), 1.8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.8),
    ]))
    story.append(t_ped)

    # 4. 52-District Strategic Quadrants
    story.append(Paragraph("4. 52-District Strategic Quadrants (Group Breakdown)", h2_style))

    quad_data = [
        [
            Paragraph("<b>Quadrant Group</b>", table_cell_bold),
            Paragraph("<b>Core Criteria</b>", table_cell_bold),
            Paragraph("<b>Representative Districts (52 Total)</b>", table_cell_bold),
            Paragraph("<b>Strategic RSK Focus</b>", table_cell_bold)
        ],
        [
            Paragraph("<font color='#047857'><b>Q1: Champions</b></font>", table_cell_bold),
            Paragraph("Turnout ≥34.8%<br/>Pedagogy ≥50.5%", table_cell_style),
            Paragraph("Harda, Narsinghpur, Raisen, Shajapur, Neemuch, Mandsaur, Jabalpur, Dewas (Sep), Sehore (Sep)", table_cell_style),
            Paragraph("Scale best practices; deploy master facilitators as peer mentors.", table_cell_style)
        ],
        [
            Paragraph("<font color='#b45309'><b>Q2: Scale Gap</b></font>", table_cell_bold),
            Paragraph("Turnout ≥34.8%<br/>Pedagogy <50.5%", table_cell_style),
            Paragraph("Chhatarpur, Damoh, Panna, Rewa, Satna, Tikamgarh, Bhind, Morena, Shahdol", table_cell_style),
            Paragraph("High turnout; prioritize conceptual reflection over rote activity.", table_cell_style)
        ],
        [
            Paragraph("<font color='#1d4ed8'><b>Q3: Reach Gap</b></font>", table_cell_bold),
            Paragraph("Turnout <34.8%<br/>Pedagogy ≥50.5%", table_cell_style),
            Paragraph("Bhopal, Indore, Ujjain, Gwalior, Sagar, Hoshangabad, Ratlam, Khargone", table_cell_style),
            Paragraph("High quality; enforce block/CRC attendance follow-up drives.", table_cell_style)
        ],
        [
            Paragraph("<font color='#b91c1c'><b>Q4: Priority Support</b></font>", table_cell_bold),
            Paragraph("Turnout <34.8%<br/>Pedagogy <50.5%", table_cell_style),
            Paragraph("Alirajpur, Barwani, Jhabua, Singrauli, Sheopur, Dindori, Mandla, Sidhi, Umaria", table_cell_style),
            Paragraph("Intensive dual-track intervention: attendance drive + academic support.", table_cell_style)
        ]
    ]

    t_quad = Table(quad_data, colWidths=[85, 85, 175, 194])
    t_quad.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#e2e8f0")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0, 0), (-1, -1), 1.8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.8),
    ]))
    story.append(t_quad)

    # 5. Executive Action Directives
    story.append(Paragraph("5. Executive Action Directives for RSK Leadership", h2_style))
    
    directives = [
        "<b>1. Targeted Block Attendance Mandate:</b> Direct DPCs and BEOs in Quadrant 3 & 4 districts to track CRC rosters against the ~44k non-attending Varg-2 teachers.",
        "<b>2. Pedagogical Refocus on Normalizing Struggle (Q97):</b> Deploy 15-minute micro-modules targeting the 66.1% misconception that equates praise only with correct answers.",
        "<b>3. Cross-District Mentorship:</b> Pair Champion districts (Harda, Narsinghpur, Dewas) with Priority Support districts (Alirajpur, Barwani) for facilitator co-planning.",
        "<b>4. Real-time Telemetry Feedback:</b> Utilize live monitoring telemetry from the 572 field observers to execute mid-cycle course corrections."
    ]

    for d in directives:
        story.append(Paragraph(f"• {d}", body_style))
        story.append(Spacer(1, 1))

    # Build Document
    doc.build(story)
    
    # Check page count
    reader = pypdf.PdfReader(filename)
    page_count = len(reader.pages)
    print(f"Generated {filename} — Total Pages: {page_count}")
    return page_count

if __name__ == '__main__':
    generate_compact_one_page_pdf()
