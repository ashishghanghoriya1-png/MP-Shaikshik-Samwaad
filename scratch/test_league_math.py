import json
import re

with open(r'c:/Master Dashboard for CLSS/RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'const dataPackage = (\{.*?\});', html, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    dist_sum = data['districtSummary']
    print(f"Loaded {len(dist_sum)} districts")
    
    # Calculate state totals
    tot_blocks = sum(d.get('totalBlocks', 0) for d in dist_sum)
    tot_clusters = sum(d.get('totalClusters', 0) for d in dist_sum)
    tot_varg2 = sum(d.get('varg2Universe', 0) for d in dist_sum)
    tot_att = sum(d.get('attendees', 0) for d in dist_sum)
    tot_mon = sum(d.get('monitors', 0) for d in dist_sum)
    tot_fac = sum(d.get('facilitators', 0) for d in dist_sum)
    tot_clss = sum(d.get('total', 0) for d in dist_sum)
    
    sat = (tot_att / tot_varg2 * 100) if tot_varg2 > 0 else 0
    avg_per_cluster = (tot_att / tot_clusters) if tot_clusters > 0 else 0
    
    print(f"Blocks: {tot_blocks}, Clusters: {tot_clusters}")
    print(f"Universe: {tot_varg2}, Attendees: {tot_att}, Saturation: {sat:.1f}%")
    print(f"Monitors: {tot_mon}, Facilitators: {tot_fac}, Total CLSS: {tot_clss}")
    print(f"Avg per cluster: {avg_per_cluster:.1f}")
