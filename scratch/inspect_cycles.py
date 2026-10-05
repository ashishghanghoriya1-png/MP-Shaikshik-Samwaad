import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\dataPackage.json', 'r', encoding='utf-8') as f:
    pkg = json.load(f)

# Sum for August in districtSummary
dist_sum = pkg['districtSummary']
aug_attendees = sum(d.get('attendees', 0) for d in dist_sum)
aug_facil = sum(d.get('facilitators', 0) for d in dist_sum)
aug_mon = sum(d.get('monitors', 0) for d in dist_sum)
aug_clss_total = sum(d.get('total', 0) for d in dist_sum)
aug_do_part = sum(d.get('do_participants', 0) for d in dist_sum)
aug_do_total = sum(d.get('do_total', 0) for d in dist_sum)
aug_comb_total = sum(d.get('combined_total', 0) for d in dist_sum)

print("--- AUGUST (districtSummary in dataPackage.json) ---")
print(f"CLSS Attendees: {aug_attendees:,}")
print(f"CLSS Facilitators: {aug_facil:,}")
print(f"CLSS Monitors: {aug_mon:,}")
print(f"CLSS Total: {aug_clss_total:,}")
print(f"DO Participants: {aug_do_part:,}")
print(f"DO Total: {aug_do_total:,}")
print(f"Combined Total: {aug_comb_total:,}")

print("\n--- CYCLES in dataPackage.json ---")
cycles = pkg.get('cycles', {})
print("Cycle keys:", cycles.keys())
for cname, cdata in cycles.items():
    print(f"\nCycle '{cname}': keys = {cdata.keys()}")
    if 'districtSummary' in cdata:
        c_dist = cdata['districtSummary']
        c_att = sum(d.get('attendees', 0) for d in c_dist)
        c_fac = sum(d.get('facilitators', 0) for d in c_dist)
        c_mon = sum(d.get('monitors', 0) for d in c_dist)
        c_tot = sum(d.get('total', 0) for d in c_dist)
        c_do_part = sum(d.get('do_participants', 0) for d in c_dist)
        c_comb = sum(d.get('combined_total', 0) for d in c_dist)
        print(f"  CLSS Attendees: {c_att:,}")
        print(f"  CLSS Facilitators: {c_fac:,}")
        print(f"  CLSS Monitors: {c_mon:,}")
        print(f"  CLSS Total: {c_tot:,}")
        print(f"  DO Participants: {c_do_part:,}")
        print(f"  Combined Total: {c_comb:,}")
