import sys
import json
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load dataPackage
with open('dataPackage.json', 'r', encoding='utf-8') as f:
    dp = json.load(f)

# 2. Load Excel files
df_dists = pd.DataFrame(dp.get('districtSummary', []))
df_blocks = pd.DataFrame(dp.get('blockSummary', []))

print("=== TAB 1: OVERVIEW & STATE SUMMARY ===")
tot_univ = dp.get('varg2Metrics', {}).get('totalUniverse', 68427)
target_cohort = dp.get('varg2Metrics', {}).get('targetCohort', 35374)
act_attendees = dp.get('varg2Metrics', {}).get('actualAttendees', 23785)
cadre_sat = dp.get('varg2Metrics', {}).get('cadreSaturationPct', 34.8)
cohort_sat = dp.get('varg2Metrics', {}).get('cohortTurnoutPct', 67.2)
tot_clusters = df_dists['totalClusters'].sum()
tot_districts = len(df_dists)
tot_blocks = len(df_blocks)

print(f"Total Varg-2 Universe: {tot_univ:,}")
print(f"Target Subject Cohort (Math & Sci): {target_cohort:,}")
print(f"Actual Teacher Attendees: {act_attendees:,}")
print(f"Cadre Saturation %: {cadre_sat}% (Actual / Universe)")
print(f"Target Cohort Saturation %: {cohort_sat}% (Actual / Target)")
print(f"Total Active Clusters: {tot_clusters:,}")
print(f"Total Districts: {tot_districts} | Total Blocks: {tot_blocks}")

print("\n=== TAB 2: RESULTS FRAMEWORK (12 INDICATORS) ===")
# Sourced from rfData in dashboard
rf_indicators = [
    {"id": 7, "name": "DO Facilitator Reach", "score": "96.0%", "status": "Shine ✨", "desc": "Facilitator attendance at state in-person orientation"},
    {"id": 8, "name": "DO Syllabus & Knowledge", "score": "86.5%", "status": "Flag 🛠️", "desc": "Understanding of DO facilitation and CLSS pedagogy"},
    {"id": 9, "name": "DO Facilitator Skills", "score": "91.2%", "status": "Shine ✨", "desc": "Observation of facilitation delivery and pacing"},
    {"id": 10, "name": "CLSS Facilitator Skills", "score": "82.4%", "status": "Flag 🛠️", "desc": "Facilitator questioning and session adherence"},
    {"id": 11, "name": "Session Consistency", "score": "89.6%", "status": "Shine ✨", "desc": "Adherence to 30:70 talk time ratio"},
    {"id": 12, "name": "CLSS Session Clarity", "score": "88.0%", "status": "Shine ✨", "desc": "Clarity on session objectives and purpose"},
    {"id": 13, "name": "Pedagogical Utility", "score": "91.2%", "status": "Shine ✨", "desc": "Usefulness of TLM and activities for classroom"},
    {"id": 14, "name": "Dialogue Quality", "score": "51.5%", "status": "Flag 🛠️", "desc": "Quality of peer exchange and teacher discussions"},
    {"id": 15, "name": "Teacher Trust & Safety", "score": "67.8%", "status": "Flag 🛠️", "desc": "Psychological safety to share challenges and doubts"},
    {"id": 16, "name": "Peer Learning Community", "score": "78.4%", "status": "Shine ✨", "desc": "Willingness to continue peer sharing networks"},
    {"id": 17, "name": "Systemic Teacher Trust", "score": "72.1%", "status": "Shine ✨", "desc": "Trust in departmental support systems"},
    {"id": 18, "name": "Pedagogy Diagnostic", "score": "58.0%", "status": "Flag 🛠️", "desc": "Composite 5-metric classroom pedagogy accuracy"}
]
for ind in rf_indicators:
    print(f"  Ind {ind['id']:2d}: {ind['name']:25s} | Score: {ind['score']:6s} | {ind['status']}")

print("\n=== TAB 4: 52-DISTRICT 4-QUADRANT LEAGUE ===")
q1 = ["Chhindwara (863 | 61%)", "Indore (459 | 63%)", "Narsinghpur (471 | 61%)", "Narmadapuram (585 | 62%)", "Raisen (412)", "Ratlam (398)", "Shajapur (376)", "Seoni (512)"]
q2 = ["Balaghat (802)", "Betul (951)", "Chhatarpur (720)", "Dhar (880)", "Khargone (776)", "Sagar (796)", "Rewa (648)", "Satna (715) + 18 more"]
q3 = ["Agar Malwa (239 | 62%)", "Sheopur (234 | 62%)", "Harda (181 | 59%)", "Neemuch (263 | 58%)", "Dewas (1 | 60%)"]
q4 = ["Alirajpur (339)", "Anuppur (278)", "Ashoknagar (347)", "Bhopal (321)", "Burhanpur (147)", "Jhabua (288)", "Sehore (3) + 6 more"]
print(f"Q1 Champions: {len(q1)} districts | Q2 Scale Gap: 26 districts | Q3 Mobilization: {len(q3)} districts | Q4 Support Zone: 13 districts")

print("\n=== TAB 7: TEACHING & LEARNING QUALITY DEEP-DIVE ===")
print("Q95 (Student Agency): 48.1% in 'Activity Trap' (fun vs agency) | 35.9% Correct (Authentic Responsibility)")
print("Q97 (Belongingness):  66.1% Confuse Belonging with Praise/Games | 33.9% Correct (Real Classroom Duties)")
print("Q96 (Error Safety):  62.0% Normalize Errors Correctly | 23.0% Dumb Down Questions for Shy Kids")
print("Q82 (Goal Clarity):   88.0% Understand Session Learning Purpose")

print("\n=== TAB 8: GOVERNANCE, LOGISTICS & FIELD CHALLENGES ===")
print("Monitoring Gap (Q76): 35.1% of clusters (1,688 clusters) had ZERO monitors present")
print("ICT Projection Gap (Q65): 59.1% of sessions had PPT idle/bypassed despite 71.6% availability")
print("Guide Availability (Q71): 11.0% lacking physical print guides (334 soft-copy only, 173 zero guides)")
print("Core Committee Meetings (DO Q51): 6 districts postponed mandatory same-day review meetings")

print("\n=== TAB 10: QUALITATIVE RESEARCH THEMATIC SPLIT (1,600+ Quotes) ===")
themes = [
    {"name": "Classroom & Pedagogy", "pct": "46.2%", "desc": "Practical application of TLM and student engagement techniques"},
    {"name": "Facilitation & Process", "pct": "24.1%", "desc": "30:70 talk ratio, role-play execution, and time management"},
    {"name": "Operations & Logistics", "pct": "14.3%", "desc": "Printed guide distribution, tea/refreshments, cluster distance"},
    {"name": "Monitoring & Governance", "pct": "8.8%", "desc": "Need for regular observer presence and administrative support"},
    {"name": "Infra & Technology", "pct": "3.5%", "desc": "Smart screen hardware, projector bulbs, and electricity reliability"},
    {"name": "Teacher Motivation", "pct": "0.9%", "desc": "Recognition, peer trust, and professional community appreciation"}
]
for t in themes:
    print(f"  Theme: {t['name']:25s} | Share: {t['pct']:6s} | {t['desc']}")
