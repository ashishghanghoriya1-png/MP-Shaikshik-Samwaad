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

url = "http://localhost:11434/api/generate"
payload = {
    "model": "qwen3.5:9b-q4_K_M",
    "prompt": prompt,
    "stream": False,
    "options": {
        "temperature": 0.3,
        "num_ctx": 4096
    }
}

print("Connecting to Ollama qwen3.5:9b-q4_K_M...")
req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})

try:
    with urllib.request.urlopen(req, timeout=300) as resp:
        result = json.loads(resp.read().decode('utf-8'))
        response_text = result.get('response', '')
        print("\n=== QWEN STRATEGIC INTELLIGENCE RESPONSE ===\n")
        print(response_text)
        with open("qwen_attendance_strategy_output.txt", "w", encoding="utf-8") as f:
            f.write(response_text)
        print("\nSuccessfully saved to qwen_attendance_strategy_output.txt")
except Exception as e:
    print(f"Error querying Ollama: {e}")
