import sys
import io
import json
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

prompt = """You are Qwen, the lead pedagogical data scientist and strategic AI advisor for the Madhya Pradesh Rajya Shiksha Kendra (RSK) Shaikshik Samwaad (CLSS) and District Orientation (DO) program.

The state leadership and project directors have asked you for your expert strategic analysis on the following core challenges:

"How can we improve the attendance data capture for CLSS and the Block level training to cover the unique beneficiary gap of 80 k currently? 
Our avg CLSS figures are 23 k as of now, approx 35 percent of the universe. 
Can we identify the regular attendees vs the others? 
How can we make it easier to fill the feedback form? 
QR code? Represented number analysis and directions from RSK ?"

Please provide your comprehensive strategic breakdown and expert recommendations structured across 4 clear pillars:
1. Telemetry & Identity Architecture: Bridging the 80k Unique Beneficiary Gap from 23k monthly average.
2. Cohort Analytics: Tracking Persistent Core vs. Rotational vs. Dark/Unreached Cadre across monthly cycles.
3. Frictionless Feedback Capture: Dynamic Cluster QR Codes, URL parameter pre-filling, micro-survey vs deep-dive split.
4. Represented Number Analysis & RSK Administrative Directives Playbook: Rotational quotas, CAC scorecards, automated DPC escalations.

Please provide sharp, actionable, evidence-based recommendations for RSK leadership.
"""

def query_qwen():
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "qwen2.5:14b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_ctx": 4096
        }
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    try:
        print("Querying local Ollama Qwen model...")
        with urllib.request.urlopen(req, timeout=180) as resp:
            res_json = json.loads(resp.read().decode('utf-8'))
            return res_json.get('response', '')
    except Exception as e:
        print(f"Ollama qwen2.5:14b failed ({e}), trying fallback...")
        payload["model"] = "qwen2.5:7b"
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                res_json = json.loads(resp.read().decode('utf-8'))
                return res_json.get('response', '')
        except Exception as e2:
            print(f"Ollama query failed: {e2}")
            return ""

if __name__ == "__main__":
    response = query_qwen()
    print("\n" + "="*80)
    print("QWEN'S STRATEGIC RESPONSE:")
    print("="*80)
    print(response)
    
    with open("qwen_attendance_strategy_output.txt", "w", encoding="utf-8") as f:
        f.write(response)
