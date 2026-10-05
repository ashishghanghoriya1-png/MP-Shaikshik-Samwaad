import sys
import json

# Test script for complete RF Matrix Table replacement
with open('dataPackage.json', 'r', encoding='utf-8') as f:
    dp = json.load(f)

dists = dp.get('districtSummary', [])
print(f"Loaded {len(dists)} districts from dataPackage.")

print("All columns mapped:")
cols = [
    "District", "Clusters", "Attendees", 
    "Reach (Ind 7)", "Syllabus (Ind 8)", "Quality (Ind 10)", 
    "Clarity (Ind 12)", "Utility (Ind 13)", "Dialogue (Ind 14)", 
    "Teacher (Ind 15)", "Pedagogy (Ind 18)"
]
for i, c in enumerate(cols):
    print(f"  Col {i+1:2d}: {c}")
