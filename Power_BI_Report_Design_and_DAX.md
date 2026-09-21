# RSK Madhya Pradesh — Shikshak Samvad & District Orientation Power BI Report Architecture & Analytics

This document provides the complete end-to-end Power BI report specification, data dictionary, DAX formula library, Star-Schema data model, and detailed analytical findings extracted from all 7 Excel files.

---

## 1. Executive Summary & Data Catalog

The analyzed dataset represents the **Madhya Pradesh Rajya Shiksha Kendra (RSK) Academic Dialogue (शैक्षिक संवाद)** program for **Grades 6-8 (August Cycle)**. It encompasses two tiers of interventions across 52 districts of MP:

1. **District Orientation (DO / जिला स्तरीय उन्मुखीकरण)**: Preparatory training and readiness orientation for facilitators and observers.
2. **Cluster Level Shikshak Samvad (CLSS / संकुल स्तरीय शैक्षिक संवाद)**: Decentralized peer-learning dialogues held at 2,851 cluster resource centers for teachers.

### High-Level Reach & Participation Summary:
- **Districts Covered**: 50 active districts (96.2% coverage)
- **Blocks Active**: 314 blocks (98.1% coverage)
- **Clusters Active**: 2,851 clusters (92.0% coverage)
- **State Total Participation**: **29,285 participants**
  - **Teacher Attendees**: **23,926** (81.7%)
  - **Facilitators (सहजकर्ता)**: **4,841** (16.5%)
  - **Monitors / Observers (अवलोकनकर्ता)**: **518** (1.8%)
- **Gender Split (CLSS Attendees)**:
  - Female Teachers: **5,372** (22.5%)
  - Male Teachers: **18,554** (77.5%)
- **Teacher Trust & Satisfaction**:
  - Trust in Shikshak Samvad: **94.2%** high trust
  - Satisfaction with Academic Focus: **99.4%**
  - Ability of Samwad to Resolve Classroom Issues: **98.9%**
  - 2-Year Longitudinal Role Clarity Growth: **99.2%**

---

## 2. Power BI Relational Star-Schema Model

All raw Excel workbooks have been processed and transformed into normalized, clean, relational CSV tables stored in `PowerBI_Model_Data/`:

```
                    +-----------------------------+
                    |        Dim_District         |
                    | (District, Region, Blocks)  |
                    +--------------+--------------+
                                   | 1
                                   |
         +-------------------------+-------------------------+
         | *                                                 | *
+--------+----------------------+                  +---------+--------------------+
| Fact_CLSS_District_Summary    |                  | Fact_Survey_Responses_Enriched|
| (District, Clusters, Monitors,|                  | (District, Program, Role,    |
|  Facilitators, Attendees)     |                  |  Sheet, MetricCode, Values)  |
+-------------------------------+                  +---------+--------------------+
                                                             | *
                                                             | 
                                                             | 1
                                                   +---------+--------------------+
                                                   |     Dim_Metric_Dictionary    |
                                                   | (Program, Role, MetricCode,  |
                                                   |  MetricNameEnglish/Hindi)    |
                                                   +------------------------------+
```

### Table Inventory:
1. `Fact_CLSS_District_Summary.csv`: District targets, blocks, clusters, and stakeholder turnout.
2. `Fact_CLSS_Block_Summary.csv`: Granular block-level counts (314 blocks).
3. `Fact_Survey_Responses_Enriched.csv`: 8,783 unpivoted survey responses mapped to standardized English/Hindi descriptions.
4. `Fact_Pedagogy_Assessment.csv`: Teacher assessment accuracy data on student belongingness, engagement, and safety.
5. `Fact_Operations_Attendance.csv`: Expected attendance, female/male actual breakdown, and core committee metrics.
6. `Dim_Question_Master.csv`: Master repository of all survey questions.
7. `Dim_Metric_Dictionary.csv`: Metric labels, options, and categories.
8. `Dim_Field_Issues.csv`: Field operational issues and RSK portal governance items.

---

## 3. Ready-to-Use DAX Measures Library

Add these DAX measures into a dedicated `_Measures` table in Power BI:

### Core Turnout & Coverage DAX:
```dax
Total Districts Active = 
DISTINCTCOUNT(Fact_CLSS_District_Summary[District])

Total Blocks = 
SUM(Fact_CLSS_District_Summary[TotalBlocks])

Total Clusters = 
SUM(Fact_CLSS_District_Summary[TotalClusters])

Total Teacher Attendees = 
SUM(Fact_CLSS_District_Summary[Attendees])

Total Facilitators = 
SUM(Fact_CLSS_District_Summary[Facilitators])

Total Monitors = 
SUM(Fact_CLSS_District_Summary[Monitors])

Total Participation = 
SUM(Fact_CLSS_District_Summary[TotalParticipation])

Avg Attendees Per Cluster = 
DIVIDE(
    [Total Teacher Attendees], 
    [Total Clusters], 
    0
)
```

### Gender Breakdown DAX:
```dax
Female Attendance = 
SUM(Fact_Operations_Attendance[FemaleAttendance])

Male Attendance = 
SUM(Fact_Operations_Attendance[MaleAttendance])

Total Actual Attendance = 
[Female Attendance] + [Male Attendance]

Female Attendance Pct = 
DIVIDE([Female Attendance], [Total Actual Attendance], 0)

Male Attendance Pct = 
DIVIDE([Male Attendance], [Total Actual Attendance], 0)
```

### Pedagogy & Assessment DAX:
```dax
Pedagogy Correct Count = 
SUM(Fact_Pedagogy_Assessment[CorrectCount])

Pedagogy Total Respondents = 
SUM(Fact_Pedagogy_Assessment[TotalRespondents])

Pedagogy Accuracy Pct = 
DIVIDE([Pedagogy Correct Count], [Pedagogy Total Respondents], 0)

Belongingness Accuracy = 
CALCULATE(
    [Pedagogy Accuracy Pct], 
    Fact_Pedagogy_Assessment[QuestionId] IN {"97", "45"}
)

Student Engagement Accuracy = 
CALCULATE(
    [Pedagogy Accuracy Pct], 
    Fact_Pedagogy_Assessment[QuestionId] IN {"95", "43"}
)

Psychological Safety Accuracy = 
CALCULATE(
    [Pedagogy Accuracy Pct], 
    Fact_Pedagogy_Assessment[QuestionId] IN {"96", "44"}
)
```

### Quality & Design Principles DAX:
```dax
Design Principle Adoption Rate = 
DIVIDE(
    CALCULATE(SUM(Fact_Survey_Responses_Enriched[ResponseCount]), Fact_Survey_Responses_Enriched[Category] = "Design Principle"),
    CALCULATE(SUM(Fact_Survey_Responses_Enriched[TotalDistrictRespondents]), Fact_Survey_Responses_Enriched[Category] = "Design Principle"),
    0
)

High Trust Rate = 
DIVIDE(
    CALCULATE(SUM(Fact_Survey_Responses_Enriched[ResponseCount]), Fact_Survey_Responses_Enriched[MetricCode] = "91.1"),
    CALCULATE(SUM(Fact_Survey_Responses_Enriched[TotalDistrictRespondents]), Fact_Survey_Responses_Enriched[MetricCode] = "91.1"),
    0
)
```

---

## 4. Power BI Report Page Wireframes (5 Pages)

### Page 1: Executive Overview & State Scale
- **Top Ribbon Cards**: Active Districts (50), Total Blocks (314), Active Clusters (2,851), Participating Teachers (23,926), Overall Turnout (29,285).
- **Visual 1 (Donut Chart)**: Turnout by Stakeholder (81.7% Teachers, 16.5% Facilitators, 1.8% Monitors).
- **Visual 2 (Clustered Bar Chart)**: Top 15 Districts by Teacher Attendees (Alirajpur, Dhar, Chhindwara, Barwani, Khargone lead).
- **Visual 3 (Gauge Chart)**: CLSS Cluster Coverage Rate vs State Target (92.0%).
- **Visual 4 (Card / Donut)**: Gender Attendance Split (22.5% Female, 77.5% Male).

### Page 2: District & Block Performance Matrix
- **Slicers**: District multi-select, Block search, Region.
- **Visual 1 (Matrix / Table)**: District | Total Blocks | Total Clusters | Monitors | Facilitators | Attendees | Turnout | Avg Attendees / Cluster.
- **Visual 2 (Scatter Plot)**: Total Clusters (X-Axis) vs Teacher Attendees (Y-Axis) to identify high/low turnout density.
- **Visual 3 (Decomposition Tree)**: State Turnout -> District -> Block -> Role.

### Page 3: Teacher Pedagogy & Assessment Analytics
- **Visual 1 (Radar / Column Chart)**: 4 Key Concept Accuracy Comparison:
  1. Dialogue Topic Recall (93.8% - Excellent)
  2. Psychological Safety / Timid Student Support (68.7% - Moderate)
  3. Student Active Engagement (41.5% - Low)
  4. Deep Belongingness Concept (38.2% - Critical Area)
- **Visual 2 (Heatmap Matrix)**: District vs Pedagogy Concepts to spot districts needing targeted refresher modules.
- **Visual 3 (Comparison Bar)**: DO Facilitators vs CLSS Teachers comprehension baseline.

### Page 4: Samwad Fidelity & Design Principles
- **Visual 1 (Side-by-side Clustered Bar)**: Facilitator Implementation Rate vs Observer & Participant Observation Rate for 7 Core Design Principles:
  - 30:70 Talk-time ratio
  - Academic topic adherence
  - Equal participation opportunities
  - Classroom & school context grounding
  - Post-work assignment & reflection
  - Time discipline
  - Quality feedback collection
- **Visual 2 (100% Stacked Bar)**: Facilitator Behavior Index (Respectful language 96%, Openness 94%, Positive reinforcement 92%, Non-academic drift prevention 85%).
- **Visual 3 (Doughnut)**: Print Guide Delivery Status (89.5% Printout provided, 8.2% Soft copy, 2.3% No access).

### Page 5: Field Bottlenecks & RSK Governance
- **Visual 1 (Card Grid / Issue List)**: Structured field challenge log:
  1. Teacher Attendance & VSK double-punch issue.
  2. Education Portal 3.0 CPD hour credit mapping.
  3. Vidisha DIET (TI) / APC RSKMP role visibility.
  4. Sehore & Dewas CAC vacancies requiring urgent administrative appointment.
  5. Anuppur & Khandwa Google Form data synchronization.
- **Visual 2 (Bar Chart)**: Facilitator-reported challenges (Time shortage 24%, Teacher late arrival 18%, Venue constraints 9%).

---

## 5. Standalone Interactive Visual Dashboard

A complete, live interactive dashboard replicating Power BI Desktop has been built and saved at:
`c:\My Files Work\CLSS RF BI\Power_BI_Interactive_Dashboard.html`

To open and explore the report:
1. Double-click `Power_BI_Interactive_Dashboard.html` in your file explorer.
2. It runs directly in any modern browser with zero dependencies.
3. It features interactive navigation, dynamic Chart.js visualizations, district search, and bilingual (Hindi/English) metadata.
