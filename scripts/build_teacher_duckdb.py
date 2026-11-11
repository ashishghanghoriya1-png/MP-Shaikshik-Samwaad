import openpyxl
import duckdb
import json
import os
import time

print("Starting DuckDB Teacher Pedagogy Pipeline...")
start_time = time.time()

# 1. Connect to DuckDB database
db_path = "data/teacher_pedagogy.duckdb"
os.makedirs("data", exist_ok=True)
if os.path.exists(db_path):
    try:
        os.remove(db_path)
    except Exception:
        pass

con = duckdb.connect(db_path)

# 2. Ingest August Participants
print("Reading August Participants workbook...")
wb_aug = openpyxl.load_workbook('SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx', read_only=True)
ws_aug = wb_aug['Participants']

aug_rows = []
aug_headers = None
for i, r in enumerate(ws_aug.iter_rows(values_only=True)):
    if i == 0:
        aug_headers = [str(c).strip() for c in r]
    else:
        # map key columns
        d = dict(zip(aug_headers, r))
        code = str(d.get('EmployeeCode') or '').strip()
        if not code or code == 'None' or code == 'NULL':
            continue
        aug_rows.append((
            code,
            str(d.get('EmployeeName') or 'Teacher').strip(),
            str(d.get('ClusterCode') or '').strip(),
            str(d.get('ClusterName') or '').strip(),
            str(d.get('DistrictName') or '').strip(),
            str(d.get('BlockName') or '').strip(),
            str(d.get('RoleName') or 'प्रतिभागी').strip(),
            str(d.get('82') or '').strip(),
            str(d.get('86') or '').strip(),
            str(d.get('95') or '').strip(),
            str(d.get('96') or '').strip(),
            str(d.get('97') or '').strip(),
            str(d.get('90') or '').strip(),
            str(d.get('89') or '').strip(),
            str(d.get('88') or '').strip(),
            str(d.get('91') or '').strip()
        ))

print(f"Loaded {len(aug_rows)} August teachers into memory. Ingesting into DuckDB...")
con.execute("""
CREATE TABLE raw_participants_aug (
    emp_code VARCHAR,
    emp_name VARCHAR,
    cluster_code VARCHAR,
    cluster_name VARCHAR,
    district VARCHAR,
    block VARCHAR,
    role VARCHAR,
    q82 VARCHAR,
    q86 VARCHAR,
    q95 VARCHAR,
    q96 VARCHAR,
    q97 VARCHAR,
    q90 VARCHAR,
    q89 VARCHAR,
    q88 VARCHAR,
    q91 VARCHAR
);
""")
con.executemany("INSERT INTO raw_participants_aug VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", aug_rows)
print("August table created in DuckDB.")

# 3. Ingest September Participants
print("Reading September Participants workbook...")
wb_sep = openpyxl.load_workbook('September_2026_Raw_Data/SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx', read_only=True)
ws_sep = wb_sep['Participants']

sep_rows = []
sep_headers = None
for i, r in enumerate(ws_sep.iter_rows(values_only=True)):
    if i == 0:
        sep_headers = [str(c).strip() for c in r]
    else:
        d = dict(zip(sep_headers, r))
        code = str(d.get('EmployeeCode') or '').strip()
        if not code or code == 'None' or code == 'NULL':
            continue
        sep_rows.append((
            code,
            str(d.get('EmployeeName') or 'Teacher').strip(),
            str(d.get('ClusterCode') or '').strip(),
            str(d.get('ClusterName') or '').strip(),
            str(d.get('DistrictName') or '').strip(),
            str(d.get('BlockName') or '').strip(),
            str(d.get('RoleName') or 'प्रतिभागी').strip(),
            str(d.get('82') or '').strip(),
            str(d.get('86') or '').strip(),
            str(d.get('177') or '').strip(),
            str(d.get('178') or '').strip(),
            str(d.get('179') or '').strip(),
            str(d.get('90') or '').strip(),
            str(d.get('89') or '').strip(),
            str(d.get('88') or '').strip(),
            str(d.get('91') or '').strip()
        ))

print(f"Loaded {len(sep_rows)} September teachers into memory. Ingesting into DuckDB...")
con.execute("""
CREATE TABLE raw_participants_sep (
    emp_code VARCHAR,
    emp_name VARCHAR,
    cluster_code VARCHAR,
    cluster_name VARCHAR,
    district VARCHAR,
    block VARCHAR,
    role VARCHAR,
    q82 VARCHAR,
    q86 VARCHAR,
    q177 VARCHAR,
    q178 VARCHAR,
    q179 VARCHAR,
    q90 VARCHAR,
    q89 VARCHAR,
    q88 VARCHAR,
    q91 VARCHAR
);
""")
con.executemany("INSERT INTO raw_participants_sep VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", sep_rows)
print("September table created in DuckDB.")

# 4. DuckDB SQL Analytical Views
print("Executing DuckDB analytical transformations...")

# Scored August View (5 pedagogy questions + 4 application/trust questions)
con.execute("""
CREATE VIEW v_scored_aug AS
SELECT 
    emp_code,
    emp_name,
    cluster_code,
    cluster_name,
    district,
    block,
    -- Core Pedagogy Correctness (1 or 0)
    CASE WHEN q82 LIKE '%सांस्कृतिक कार्यक्रम%' THEN 1 ELSE 0 END AS corr_q82,
    CASE WHEN q86 LIKE '%30:70%' OR q86 LIKE '%पूर्व निर्धारित%' OR q86 LIKE '%परिप्रेक्ष्य%' THEN 1 ELSE 0 END AS corr_q86,
    CASE WHEN q95 LIKE '%रुचियों और क्षमताओं%' THEN 1 ELSE 0 END AS corr_q95,
    CASE WHEN q96 LIKE '%सीखने का स्वाभाविक हिस्सा%' OR q96 LIKE '%संकेत देकर%' THEN 1 ELSE 0 END AS corr_q96,
    CASE WHEN q97 LIKE '%वास्तविक जिम्मेदारियों%' THEN 1 ELSE 0 END AS corr_q97,
    -- Classroom Application & Trust
    CASE WHEN q90 LIKE '%हाँ%' THEN 1 ELSE 0 END AS corr_q90,
    CASE WHEN q89 LIKE '%हाँ%' THEN 1 ELSE 0 END AS corr_q89,
    CASE WHEN q88 LIKE '%हाँ%' THEN 1 ELSE 0 END AS corr_q88,
    CASE WHEN q91 LIKE '%हाँ, पूरी तरह से%' THEN 1 ELSE 0 END AS corr_q91,
    -- Raw responses for misconception notes
    q82, q86, q95, q96, q97, q90, q89, q88, q91
FROM raw_participants_aug;
""")

# Scored September View
con.execute("""
CREATE VIEW v_scored_sep AS
SELECT 
    emp_code,
    emp_name,
    cluster_code,
    cluster_name,
    district,
    block,
    -- Core Pedagogy Correctness (1 or 0)
    CASE WHEN q82 LIKE '%सांस्कृतिक कार्यक्रम%' THEN 1 ELSE 0 END AS corr_q82,
    CASE WHEN q86 LIKE '%30:70%' OR q86 LIKE '%परिप्रेक्ष्य%' OR q86 LIKE '%गुणवत्ता पर फीडबैक%' THEN 1 ELSE 0 END AS corr_q86,
    CASE WHEN q177 LIKE '%अनुभव कराना%' AND q177 LIKE '%चिंतन%' AND q177 LIKE '%समेकन%' THEN 1 ELSE 0 END AS corr_q177,
    CASE WHEN q178 LIKE '%चिंतन के अवसर%' THEN 1 ELSE 0 END AS corr_q178,
    CASE WHEN q179 LIKE '%मुख्य सीख को स्पष्ट%' OR q179 LIKE '%जोड़कर%' THEN 1 ELSE 0 END AS corr_q179,
    -- Classroom Application & Trust
    CASE WHEN q90 LIKE '%हाँ%' THEN 1 ELSE 0 END AS corr_q90,
    CASE WHEN q89 LIKE '%हाँ%' THEN 1 ELSE 0 END AS corr_q89,
    CASE WHEN q88 LIKE '%हाँ%' THEN 1 ELSE 0 END AS corr_q88,
    CASE WHEN q91 LIKE '%हाँ, पूरी तरह से%' THEN 1 ELSE 0 END AS corr_q91,
    -- Raw responses for misconception notes
    q82, q86, q177, q178, q179, q90, q89, q88, q91
FROM raw_participants_sep;
""")

# Combined Master Teacher View
con.execute("""
CREATE VIEW v_master_teachers AS
WITH all_codes AS (
    SELECT emp_code FROM raw_participants_aug
    UNION
    SELECT emp_code FROM raw_participants_sep
)
SELECT 
    c.emp_code,
    COALESCE(s.emp_name, a.emp_name) AS emp_name,
    COALESCE(s.district, a.district) AS district,
    COALESCE(s.block, a.block) AS block,
    COALESCE(s.cluster_name, a.cluster_name) AS cluster_name,
    CASE 
        WHEN a.emp_code IS NOT NULL AND s.emp_code IS NOT NULL THEN 'BOTH'
        WHEN a.emp_code IS NOT NULL THEN 'AUG'
        ELSE 'SEP'
    END AS cycle_attendance,
    -- August Pedagogy Score (out of 5 core questions)
    CASE WHEN a.emp_code IS NOT NULL THEN 
        ROUND(((a.corr_q82 + a.corr_q86 + a.corr_q95 + a.corr_q96 + a.corr_q97) * 20.0), 1)
    ELSE NULL END AS aug_ped_score,
    -- September Pedagogy Score (out of 5 core questions)
    CASE WHEN s.emp_code IS NOT NULL THEN 
        ROUND(((s.corr_q82 + s.corr_q86 + s.corr_q177 + s.corr_q178 + s.corr_q179) * 20.0), 1)
    ELSE NULL END AS sep_ped_score,
    -- 10-Question Comprehensive Score (out of 100%)
    ROUND(
        (
            COALESCE((a.corr_q82 + a.corr_q86 + a.corr_q95 + a.corr_q96 + a.corr_q97 + a.corr_q90 + a.corr_q89 + a.corr_q88 + a.corr_q91) * 100.0 / 9.0, 0) +
            COALESCE((s.corr_q82 + s.corr_q86 + s.corr_q177 + s.corr_q178 + s.corr_q179 + s.corr_q90 + s.corr_q89 + s.corr_q88 + s.corr_q91) * 100.0 / 9.0, 0)
        ) / CASE WHEN a.emp_code IS NOT NULL AND s.emp_code IS NOT NULL THEN 2.0 ELSE 1.0 END
    , 1) AS overall_score,
    -- Misconception indicators
    a.corr_q82 AS a_q82, a.corr_q86 AS a_q86, a.corr_q95 AS a_q95, a.corr_q96 AS a_q96, a.corr_q97 AS a_q97,
    s.corr_q82 AS s_q82, s.corr_q86 AS s_q86, s.corr_q177 AS s_q177, s.corr_q178 AS s_q178, s.corr_q179 AS s_q179,
    a.q95 AS raw_a_q95, a.q96 AS raw_a_q96, a.q97 AS raw_a_q97,
    s.q177 AS raw_s_q177, s.q178 AS raw_s_q178, s.q179 AS raw_s_q179
FROM all_codes c
LEFT JOIN v_scored_aug a ON c.emp_code = a.emp_code
LEFT JOIN v_scored_sep s ON c.emp_code = s.emp_code;
""")

print("Querying summary stats from DuckDB...")
summary = con.execute("""
SELECT 
    COUNT(*) as total_teachers,
    COUNT(CASE WHEN cycle_attendance = 'BOTH' THEN 1 END) as persistent_teachers,
    COUNT(CASE WHEN cycle_attendance = 'AUG' THEN 1 END) as aug_only,
    COUNT(CASE WHEN cycle_attendance = 'SEP' THEN 1 END) as sep_only,
    ROUND(AVG(overall_score), 1) as avg_score,
    COUNT(CASE WHEN overall_score >= 80 THEN 1 END) as champions,
    COUNT(CASE WHEN overall_score >= 60 AND overall_score < 80 THEN 1 END) as proficient,
    COUNT(CASE WHEN overall_score >= 40 AND overall_score < 60 THEN 1 END) as developing,
    COUNT(CASE WHEN overall_score < 40 THEN 1 END) as priority_support
FROM v_master_teachers;
""").fetchone()

print(f"Total Unique Teachers in DuckDB: {summary[0]:,}")
print(f"Persistent (Both Cycles): {summary[1]:,}")
print(f"August Only: {summary[2]:,}")
print(f"September Only: {summary[3]:,}")
print(f"State Average Overall Score: {summary[4]}%")
print(f"Champions (80-100%): {summary[5]:,} ({(summary[5]*100/summary[0]):.1f}%)")
print(f"Proficient (60-79%): {summary[6]:,} ({(summary[6]*100/summary[0]):.1f}%)")
print(f"Developing (40-59%): {summary[7]:,} ({(summary[7]*100/summary[0]):.1f}%)")
print(f"Priority Support (<40%): {summary[8]:,} ({(summary[8]*100/summary[0]):.1f}%)")

# 5. Export to Parquet
con.execute("COPY v_master_teachers TO 'data/teachers.parquet' (FORMAT PARQUET);")
print("Saved DuckDB Parquet table to data/teachers.parquet")

# 6. Build Compact JSON for Frontend Search
print("Building compact searchable JSON for the dashboard...")
teachers_cur = con.execute("""
SELECT 
    emp_code,
    emp_name,
    district,
    block,
    cluster_name,
    cycle_attendance,
    COALESCE(aug_ped_score, -1) as aug_score,
    COALESCE(sep_ped_score, -1) as sep_score,
    overall_score,
    -- specific gaps
    CASE WHEN a_q95 = 0 OR s_q177 = 0 THEN 1 ELSE 0 END as gap_tlm,
    CASE WHEN s_q178 = 0 THEN 1 ELSE 0 END as gap_probing,
    CASE WHEN a_q96 = 0 THEN 1 ELSE 0 END as gap_safety,
    CASE WHEN a_q97 = 0 THEN 1 ELSE 0 END as gap_belonging,
    CASE WHEN COALESCE(s_q82, a_q82) = 0 THEN 1 ELSE 0 END as gap_purpose,
    COALESCE(raw_s_q178, '') as text_q178,
    COALESCE(raw_s_q177, '') as text_q177,
    COALESCE(raw_a_q95, '') as text_q95,
    COALESCE(raw_a_q97, '') as text_q97
FROM v_master_teachers
ORDER BY overall_score DESC, emp_name ASC;
""")

teacher_records = []
for r in teachers_cur.fetchall():
    score = float(r[8])
    tier = 'CHAMPION' if score >= 80 else ('PROFICIENT' if score >= 60 else ('DEVELOPING' if score >= 40 else 'SUPPORT_NEEDED'))
    
    # catalog gaps
    gaps = []
    if r[9] == 1: gaps.append('TLM_CYCLE')
    if r[10] == 1: gaps.append('PROBING')
    if r[11] == 1: gaps.append('SAFETY')
    if r[12] == 1: gaps.append('BELONGING')
    if r[13] == 1: gaps.append('PURPOSE')
    
    aug_sc = float(r[6]) if r[6] is not None and float(r[6]) >= 0 else None
    sep_sc = float(r[7]) if r[7] is not None and float(r[7]) >= 0 else None

    teacher_records.append({
        'c': str(r[0] or ''),               # EmployeeCode
        'n': str(r[1] or ''),               # EmployeeName
        'd': str(r[2] or ''),               # District
        'b': str(r[3] or ''),               # Block
        'cl': str(r[4] or ''),              # Cluster
        'cy': str(r[5] or ''),              # Cycles ('BOTH', 'AUG', 'SEP')
        'as': aug_sc,                       # Aug Pedagogy Score
        'ss': sep_sc,                       # Sep Pedagogy Score
        'sc': score,                        # Overall 10-Question Score
        't': tier,                          # Performance Tier
        'g': gaps,                          # Learning Gap Codes
        't178': str(r[14][:60]) if r[14] else '',
        't177': str(r[15][:60]) if r[15] else '',
        't95': str(r[16][:60]) if r[16] else '',
        't97': str(r[17][:60]) if r[17] else ''
    })

# Write JSON
diagnostic_export = {
    'summary': {
        'totalTeachers': int(summary[0]),
        'persistent': int(summary[1]),
        'augOnly': int(summary[2]),
        'sepOnly': int(summary[3]),
        'avgScore': float(summary[4]) if summary[4] is not None else 0.0,
        'champions': int(summary[5]),
        'proficient': int(summary[6]),
        'developing': int(summary[7]),
        'prioritySupport': int(summary[8])
    },
    'teachers': teacher_records
}

json_path = 'data/teacher_diagnostics.json'
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(diagnostic_export, f, ensure_ascii=False)

file_size_mb = os.path.getsize(json_path) / (1024 * 1024)
print(f"Exported {len(teacher_records):,} teachers to {json_path} ({file_size_mb:.2f} MB).")
print(f"Pipeline completed in {time.time() - start_time:.2f} seconds.")
con.close()
