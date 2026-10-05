import sys
import io
import json
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

prompt = """You are Qwen, the lead pedagogical data scientist and AI advisor for Madhya Pradesh Rajya Shiksha Kendra (RSK) and Peepul.

The state leadership has posed the following critical strategic questions:
"How can we improve the attendance data capture for CLSS and the Block level training to cover the unique beneficiary gap of 80 k currently? 
Our avg CLSS figures are 23 k as of now, approx 35 percent of the universe. 
Can we identify the regular attendees vs the others? 
How can we make it easier to fill the feedback form? 
QR code? Represented number analysis and directions from RSK ?"

Provide your strategic recommendations structured across 4 clear pillars:
1. Telemetry & Identity Architecture (80k Beneficiary Gap vs 23k monthly average)
2. Cohort Analytics (Regulars vs Rotational vs Dark Cadre)
3. Frictionless Feedback Capture (Dynamic QR Codes, Pre-filled Form Schemas)
4. Represented Number Analysis & RSK Policy Directives (Rotational Quorum Circular, CAC Scorecards, DPC Escalation)
"""

url = "http://localhost:11434/api/generate"
payload = {
    "model": "qwen3.5:9b-q4_K_M",
    "prompt": prompt,
    "stream": True,
    "options": {
        "temperature": 0.2,
        "num_ctx": 2048,
        "num_predict": 1200
    }
}

req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})

with open("qwen_strategy_stream.md", "w", encoding="utf-8") as out_f:
    with urllib.request.urlopen(req, timeout=120) as resp:
        for line in resp:
            if line:
                chunk = json.loads(line.decode('utf-8'))
                tok = chunk.get('response', '')
                out_f.write(tok)
                out_f.flush()
                sys.stdout.write(tok)
                sys.stdout.flush()

print("\n\nDone streaming Qwen analysis!")
