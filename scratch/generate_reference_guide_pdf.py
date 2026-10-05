import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas
import pypdf

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(36, 810, "RSK Shaikshik Samwaad — Data Provenance & Reference Guide")
            self.drawRightString(559, 810, "Rajya Shiksha Kendra (RSK) MP")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(36, 804, 559, 804)

        # Footer
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawString(36, 25, "Confidential — Prepared for RSK Leadership by Peepul India")
        self.drawRightString(559, 25, page_text)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 35, 559, 35)
        self.restoreState()

def build_pdf(filename="RSK_Shaikshik_Samwaad_Executive_Visual_Briefing_Exact_Data_Origin_and_Reference_Guide.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()
    
    primary_color = colors.HexColor("#0f172a") # Slate 900
    teal_color = colors.HexColor("#008080")    # Peepul Teal

    title_style = ParagraphStyle(
        'DocTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=16, leading=20,
        textColor=primary_color, spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10, leading=14,
        textColor=teal_color, spaceAfter=6
    )

    meta_style = ParagraphStyle(
        'MetaStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=11,
        textColor=colors.HexColor("#475569")
    )

    h2_style = ParagraphStyle(
        'H2Style', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=11, leading=15,
        textColor=primary_color, spaceBefore=10, spaceAfter=4
    )

    body_style = ParagraphStyle(
        'BodyDark', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=11.5,
        textColor=colors.HexColor("#334155")
    )

    table_header_style = ParagraphStyle(
        'TableHeader', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=7.5, leading=10,
        textColor=colors.white, alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCell', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.5, leading=10,
        textColor=colors.HexColor("#1e293b")
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=7.5, leading=10,
        textColor=colors.HexColor("#0f172a")
    )

    table_cell_center = ParagraphStyle(
        'TableCellCenter', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.5, leading=10,
        textColor=colors.HexColor("#1e293b"), alignment=1
    )

    story = []

    # Title Banner
    story.append(Paragraph("RSK Shaikshik Samwaad: Data Origin & Reference Guide", title_style))
    story.append(Paragraph("Granular Provenance, Formula Derivations & Strategic Reference Manual", subtitle_style))
    
    meta_text = (
        "<b>State Apex:</b> Rajya Shiksha Kendra (RSK), MP | "
        "<b>Evaluation Partner:</b> Peepul India | "
        "<b>Cadre Universe:</b> 68,427 Varg-2 Teachers<br/>"
        "<b>Scope:</b> Classes 6–8 Shikshak Samvad (52 Districts, 322 Blocks, 4,804 Mapped Clusters) | "
        "<b>Cycles:</b> August & September 2026"
    )
    story.append(Paragraph(meta_text, meta_style))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=teal_color, spaceAfter=8))

    # 1. Purpose of Metrics Table
    story.append(Paragraph("1. Executive Summary: Why We Track Each Metric", h2_style))
    
    why_data = [
        [
            Paragraph("Metric Name", table_header_style),
            Paragraph("Reported Value", table_header_style),
            Paragraph("Strategic Leadership Purpose for RSK", table_header_style)
        ],
        [
            Paragraph("<b>Total Cadre Universe</b>", table_cell_bold),
            Paragraph("<b>68,427</b> Varg-2 Teachers", table_cell_center),
            Paragraph("Official sanctioned EMIS headcount defining 100% saturation potential.", table_cell_style)
        ],
        [
            Paragraph("<b>Field Expected Target</b>", table_cell_bold),
            Paragraph("<b>68,369</b> (Aug) | <b>67,222</b> (Sep)", table_cell_center),
            Paragraph("Ground-level facilitator rosters entered at cluster session start.", table_cell_style)
        ],
        [
            Paragraph("<b>Actual Attending Teachers</b>", table_cell_bold),
            Paragraph("<b>23,785</b> (Aug) | <b>23,169</b> (Sep)", table_cell_center),
            Paragraph("Physical classroom teacher reach verified by individual survey submissions.", table_cell_style)
        ],
        [
            Paragraph("<b>District Saturation</b>", table_cell_bold),
            Paragraph("<b>50/52</b> (Aug) → <b>52/52</b> (Sep)", table_cell_center),
            Paragraph("Administrative operationalization across all 52 districts (Dewas/Sehore in Sep).", table_cell_style)
        ],
        [
            Paragraph("<b>Active Centres / Venues</b>", table_cell_bold),
            Paragraph("<b>2,874</b> (Aug) → <b>2,861</b> (Sep)", table_cell_center),
            Paragraph("Infrastructure delivery footprint across CRC cluster centres and DIETs.", table_cell_style)
        ],
        [
            Paragraph("<b>District Officials (DO)</b>", table_cell_bold),
            Paragraph("<b>4,454</b> (Aug) → <b>4,520</b> (Sep)", table_cell_center),
            Paragraph("Leadership orientation and governance cascading through district headquarters.", table_cell_style)
        ],
        [
            Paragraph("<b>Master Facilitators</b>", table_cell_bold),
            Paragraph("<b>4,891</b> (Aug) → <b>4,850</b> (Sep)", table_cell_center),
            Paragraph("Academic delivery capacity driving peer-learning dialogue.", table_cell_style)
        ],
        [
            Paragraph("<b>Field Observers / Monitors</b>", table_cell_bold),
            Paragraph("<b>572</b> (Aug) → <b>560</b> (Sep)", table_cell_center),
            Paragraph("Independent quality assurance on session fidelity, TLM usage, and dialogue ratio.", table_cell_style)
        ]
    ]

    t_why = Table(why_data, colWidths=[130, 120, 273])
    t_why.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), teal_color),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_why)
    story.append(Spacer(1, 8))

    # 2. Granular Data Lineage Table
    story.append(Paragraph("2. Granular Data Origin & Source Lineage Table", h2_style))
    
    lineage_data = [
        [
            Paragraph("Metric Name", table_header_style),
            Paragraph("Value", table_header_style),
            Paragraph("Raw Source File", table_header_style),
            Paragraph("Sheet Name", table_header_style),
            Paragraph("Column / Location", table_header_style),
            Paragraph("Mathematical Operation", table_header_style)
        ],
        [
            Paragraph("<b>Sanctioned Universe</b>", table_cell_bold),
            Paragraph("68,427", table_cell_center),
            Paragraph("Varg Wise Teacher Count.xlsx", table_cell_style),
            Paragraph("Sheet1", table_cell_center),
            Paragraph("Col E (Madhymik Shikshak Total)", table_cell_style),
            Paragraph("Sum of all 322 blocks across 52 dists", table_cell_style)
        ],
        [
            Paragraph("<b>August Expected Target</b>", table_cell_bold),
            Paragraph("68,369", table_cell_center),
            Paragraph("SS_ResponseDetail_Cluster_Aug.xlsx", table_cell_style),
            Paragraph("Facilitator", table_cell_center),
            Paragraph("Col O (Q72: अपेक्षित प्रतिभागी)", table_cell_style),
            Paragraph("Sum of all facilitator target entries", table_cell_style)
        ],
        [
            Paragraph("<b>September Expected Target</b>", table_cell_bold),
            Paragraph("67,222", table_cell_center),
            Paragraph("SS_ResponseDetail_Cluster_Sep.xlsx", table_cell_style),
            Paragraph("Facilitator", table_cell_center),
            Paragraph("Col O (Q72: अपेक्षित प्रतिभागी)", table_cell_style),
            Paragraph("Sum of all facilitator target entries", table_cell_style)
        ],
        [
            Paragraph("<b>August Actual Teachers</b>", table_cell_bold),
            Paragraph("23,785", table_cell_center),
            Paragraph("SS_ResponseDetail_Cluster_Aug.xlsx", table_cell_style),
            Paragraph("Participants", table_cell_center),
            Paragraph("All rows (Role=Participant)", table_cell_style),
            Paragraph("Exact count of teacher survey rows", table_cell_style)
        ],
        [
            Paragraph("<b>September Actual Teachers</b>", table_cell_bold),
            Paragraph("23,169", table_cell_center),
            Paragraph("SS_ResponseDetail_Cluster_Sep.xlsx", table_cell_style),
            Paragraph("Participants", table_cell_center),
            Paragraph("All rows (Role=Participant)", table_cell_style),
            Paragraph("Exact count of teacher survey rows", table_cell_style)
        ],
        [
            Paragraph("<b>August Active Dists</b>", table_cell_bold),
            Paragraph("50 / 52", table_cell_center),
            Paragraph("SS_ResponseDetail_Cluster_Aug.xlsx", table_cell_style),
            Paragraph("Participants", table_cell_center),
            Paragraph("Col E (DistrictName)", table_cell_style),
            Paragraph("Distinct count (Dewas & Sehore = 0)", table_cell_style)
        ],
        [
            Paragraph("<b>September Active Dists</b>", table_cell_bold),
            Paragraph("52 / 52", table_cell_center),
            Paragraph("SS_ResponseDetail_Cluster_Sep.xlsx", table_cell_style),
            Paragraph("Participants", table_cell_center),
            Paragraph("Col E (DistrictName)", table_cell_style),
            Paragraph("Distinct count (100% saturation)", table_cell_style)
        ],
        [
            Paragraph("<b>August Active Venues</b>", table_cell_bold),
            Paragraph("2,874", table_cell_center),
            Paragraph("Both August Workbooks", table_cell_style),
            Paragraph("Participants", table_cell_center),
            Paragraph("ClusterCode & DistrictCode", table_cell_style),
            Paragraph("2,822 Cluster + 52 DIET HQ Venues", table_cell_style)
        ],
        [
            Paragraph("<b>September Active Venues</b>", table_cell_bold),
            Paragraph("2,861", table_cell_center),
            Paragraph("Both September Workbooks", table_cell_style),
            Paragraph("Participants", table_cell_center),
            Paragraph("ClusterCode & DistrictCode", table_cell_style),
            Paragraph("2,809 Cluster + 52 DIET HQ Venues", table_cell_style)
        ],
        [
            Paragraph("<b>August DO Officials</b>", table_cell_bold),
            Paragraph("4,454", table_cell_center),
            Paragraph("SS_ResponseDetail_District_Aug.xlsx", table_cell_style),
            Paragraph("Participants", table_cell_center),
            Paragraph("All rows in Participants", table_cell_style),
            Paragraph("Count of oriented DO officials", table_cell_style)
        ],
        [
            Paragraph("<b>September DO Officials</b>", table_cell_bold),
            Paragraph("4,520", table_cell_center),
            Paragraph("SS_ResponseDetail_District_Sep.xlsx", table_cell_style),
            Paragraph("Participants", table_cell_center),
            Paragraph("All rows in Participants", table_cell_style),
            Paragraph("Count of oriented DO officials", table_cell_style)
        ],
        [
            Paragraph("<b>Q95: Hands-on TLM</b>", table_cell_bold),
            Paragraph("51.9%", table_cell_center),
            Paragraph("SS_ResponseDetail_Cluster_Aug.xlsx", table_cell_style),
            Paragraph("Participants", table_cell_center),
            Paragraph("Col 95", table_cell_style),
            Paragraph("Choice 1 (51.9%) vs Choice 2 (48.1%)", table_cell_style)
        ],
        [
            Paragraph("<b>Q97: Struggle & Errors</b>", table_cell_bold),
            Paragraph("33.9%", table_cell_center),
            Paragraph("SS_ResponseDetail_Cluster_Aug.xlsx", table_cell_style),
            Paragraph("Participants", table_cell_center),
            Paragraph("Col 97", table_cell_style),
            Paragraph("Choice 1 (33.9%) vs Choice 2 (66.1%)", table_cell_style)
        ],
        [
            Paragraph("<b>Q96: Misconceptions</b>", table_cell_bold),
            Paragraph("62.0%", table_cell_center),
            Paragraph("SS_ResponseDetail_Cluster_Aug.xlsx", table_cell_style),
            Paragraph("Participants", table_cell_center),
            Paragraph("Col 96", table_cell_style),
            Paragraph("Choice 1 (62.0%) vs Choice 2 (38.0%)", table_cell_style)
        ],
        [
            Paragraph("<b>Q98: Peer Dialogue</b>", table_cell_bold),
            Paragraph("54.2%", table_cell_center),
            Paragraph("SS_ResponseDetail_Cluster_Aug.xlsx", table_cell_style),
            Paragraph("Participants", table_cell_center),
            Paragraph("Col 98", table_cell_style),
            Paragraph("Choice 1 (54.2%) vs Choice 2 (45.8%)", table_cell_style)
        ]
    ]

    col_widths_lineage = [90, 48, 110, 60, 105, 110]
    t_lin = Table(lineage_data, colWidths=col_widths_lineage)
    t_lin.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e293b")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(t_lin)
    story.append(Spacer(1, 8))

    # 3. Strategic Recommendations
    story.append(Paragraph("3. Strategic Recommendations & Suggested Additions for RSK", h2_style))
    
    recs = [
        "<b>1. Teacher Repeat Attendance & Retention Tracking:</b> Track individual teacher participation across consecutive cycles (August vs. September) to measure consistent core attendance vs. transient participation.",
        "<b>2. Cluster-Level Saturation Depth:</b> Implement a micro-drilldown showing what percentage of CRC clusters in each block reach $\ge 15$ attending teachers.",
        "<b>3. Longitudinal Misconception Shift Analysis:</b> Measure month-on-month changes in distractor trap selection to track the direct impact of pedagogical micro-modules.",
        "<b>4. Special Equity Cohorts:</b> Provide dedicated automated tracking for NITI Aayog Aspirational Blocks (8 districts) and Special Tribal Focus Blocks (15 districts)."
    ]

    for r in recs:
        story.append(Paragraph(f"• {r}", body_style))
        story.append(Spacer(1, 2))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename}")

if __name__ == '__main__':
    build_pdf()
