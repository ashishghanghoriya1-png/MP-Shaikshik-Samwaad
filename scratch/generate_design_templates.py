import os
from playwright.sync_api import sync_playwright

# Template C: Ultra-Clean Swiss Grid (Clean White, Black Typography, Minimalist Ticks, Zero Color Clutter)
html_template_c = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Template C: Minimalist Swiss Grid</title>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body { font-family: 'Space Grotesk', sans-serif; background: #ffffff; color: #09090b; width: 1200px; margin: 0 auto; padding: 32px; }
    .font-mono { font-family: 'JetBrains Mono', monospace; font-variant-numeric: tabular-nums; }
  </style>
</head>
<body class="space-y-4">
  <div class="border-b border-zinc-200 pb-3 flex justify-between items-baseline">
    <div>
      <div class="text-[10px] font-mono uppercase tracking-widest text-zinc-400">RSK MADHYA PRADESH • EVALUATION BRIEFING</div>
      <h1 class="text-2xl font-bold tracking-tight text-zinc-950">Shaikshik Samwaad: 2-Cycle Operational & Pedagogy Briefing</h1>
    </div>
    <div class="text-xs font-mono text-zinc-500">Universe: <strong>68,427</strong> Varg-2 Middle Teachers</div>
  </div>

  <div class="grid grid-cols-3 gap-3">
    <div class="border border-zinc-200 p-4 rounded-md">
      <div class="text-[10px] font-mono text-zinc-400 uppercase">August 2026 Cycle</div>
      <div class="text-2xl font-bold font-mono mt-1">23,785 <span class="text-xs font-normal text-zinc-500">/ 68,369 (34.8%)</span></div>
      <div class="text-xs text-zinc-500 mt-1">50/52 Active Districts (Dewas & Sehore Vacant)</div>
    </div>
    <div class="border border-zinc-200 p-4 rounded-md">
      <div class="text-[10px] font-mono text-zinc-400 uppercase">September 2026 Cycle</div>
      <div class="text-2xl font-bold font-mono mt-1">23,169 <span class="text-xs font-normal text-zinc-500">/ 67,222 (34.5%)</span></div>
      <div class="text-xs text-zinc-500 mt-1">52/52 Active Districts (100% Full Saturation)</div>
    </div>
    <div class="border border-zinc-900 bg-zinc-950 text-white p-4 rounded-md">
      <div class="text-[10px] font-mono text-zinc-400 uppercase">Consolidated 2-Cycle Total</div>
      <div class="text-2xl font-bold font-mono mt-1">46,954 <span class="text-xs font-normal text-zinc-400">/ 135,591 (34.6%)</span></div>
      <div class="text-xs text-zinc-400 mt-1">5,735 Sessions • 8,974 DO • 4,891 Leads</div>
    </div>
  </div>

  <div class="border border-zinc-200 rounded-md overflow-hidden text-xs">
    <table class="w-full text-left border-collapse">
      <thead class="bg-zinc-50 border-b border-zinc-200 font-mono text-[10px] text-zinc-500 uppercase">
        <tr>
          <th class="p-2.5">Domain</th>
          <th class="p-2.5">Constructive Option</th>
          <th class="p-2.5">Misconception Trap</th>
          <th class="p-2.5 text-right">Mastery</th>
          <th class="p-2.5 text-right">Trap %</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-zinc-100 font-mono text-[11px]">
        <tr><td class="p-2.5 font-bold">Q95: TLM Purpose</td><td class="p-2.5 text-zinc-700">Structured reflection</td><td class="p-2.5 text-zinc-500">Activity Fallacy</td><td class="p-2.5 text-right font-bold">51.9%</td><td class="p-2.5 text-right text-zinc-500">48.1%</td></tr>
        <tr><td class="p-2.5 font-bold">Q97: Struggle</td><td class="p-2.5 text-zinc-700">Normalize errors</td><td class="p-2.5 text-zinc-500">Praise right answers only</td><td class="p-2.5 text-right font-bold text-red-600">33.9%</td><td class="p-2.5 text-right text-red-600">66.1%</td></tr>
        <tr><td class="p-2.5 font-bold">Q96: Misconceptions</td><td class="p-2.5 text-zinc-700">Diagnostic entry point</td><td class="p-2.5 text-zinc-500">Immediate correction</td><td class="p-2.5 text-right font-bold">62.0%</td><td class="p-2.5 text-right text-zinc-500">38.0%</td></tr>
        <tr><td class="p-2.5 font-bold">Q98: Peer Dialogue</td><td class="p-2.5 text-zinc-700">Small-group debate</td><td class="p-2.5 text-zinc-500">Teacher monologue</td><td class="p-2.5 text-right font-bold">54.2%</td><td class="p-2.5 text-right text-zinc-500">45.8%</td></tr>
      </tbody>
    </table>
  </div>

  <div class="grid grid-cols-4 gap-2 text-xs font-mono">
    <div class="border border-zinc-200 p-2.5 rounded"><strong>Q1 Champions:</strong> Harda, Dewas, Sehore, Narsinghpur, Raisen.</div>
    <div class="border border-zinc-200 p-2.5 rounded"><strong>Q2 Scale Gap:</strong> Chhatarpur, Damoh, Panna, Rewa, Satna.</div>
    <div class="border border-zinc-200 p-2.5 rounded"><strong>Q3 Reach Gap:</strong> Bhopal, Indore, Ujjain, Gwalior, Sagar.</div>
    <div class="border border-zinc-200 p-2.5 rounded"><strong>Q4 Priority:</strong> Alirajpur, Barwani, Jhabua, Singrauli.</div>
  </div>
</body>
</html>
"""

# Template D: Executive Slide Deck Card (Presentation Slide 16:9 / Landscape Style)
html_template_d = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Template D: Executive Slide Deck Layout</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; background: #0f172a; color: #f8fafc; width: 1200px; margin: 0 auto; padding: 28px; }
    .font-mono { font-family: 'JetBrains Mono', monospace; }
  </style>
</head>
<body class="space-y-4">
  <div class="flex justify-between items-center border-b border-slate-800 pb-3">
    <div>
      <span class="text-xs font-mono uppercase text-teal-400 font-semibold tracking-wider">RSK Madhya Pradesh • Executive Briefing</span>
      <h1 class="text-2xl font-extrabold text-white">Shaikshik Samwaad: 2-Cycle Comparative Review</h1>
    </div>
    <div class="text-right text-xs font-mono text-slate-400">
      Cadre Universe: <strong class="text-teal-400 text-sm">68,427</strong> Teachers
    </div>
  </div>

  <div class="grid grid-cols-3 gap-3">
    <div class="bg-slate-800/90 border border-slate-700 p-4 rounded-xl">
      <div class="text-xs font-mono text-amber-400 font-bold uppercase">August 2026 Cycle</div>
      <div class="text-2xl font-black font-mono text-white mt-1">23,785 <span class="text-xs font-normal text-slate-300">/ 68,369</span></div>
      <div class="text-xs text-amber-300 mt-1">34.8% Turnout • 50/52 Dists (Dewas/Sehore Vacant)</div>
    </div>
    <div class="bg-slate-800/90 border border-slate-700 p-4 rounded-xl">
      <div class="text-xs font-mono text-teal-400 font-bold uppercase">September 2026 Cycle</div>
      <div class="text-2xl font-black font-mono text-teal-300 mt-1">23,169 <span class="text-xs font-normal text-slate-300">/ 67,222</span></div>
      <div class="text-xs text-teal-300 mt-1">34.5% Turnout • 52/52 Dists (100% Saturation)</div>
    </div>
    <div class="bg-indigo-950/80 border border-indigo-700 p-4 rounded-xl">
      <div class="text-xs font-mono text-indigo-300 font-bold uppercase">Consolidated Impact</div>
      <div class="text-2xl font-black font-mono text-white mt-1">46,954 <span class="text-xs font-normal text-indigo-200">/ 135,591</span></div>
      <div class="text-xs text-indigo-200 mt-1">34.6% Overall Turnout • 5,735 Total Sessions</div>
    </div>
  </div>

  <div class="grid grid-cols-2 gap-3">
    <div class="bg-slate-800/60 border border-slate-700 p-4 rounded-xl space-y-2 text-xs">
      <div class="text-xs font-mono text-slate-300 font-bold uppercase mb-1">Pedagogy Diagnostic Telemetry</div>
      <div class="flex justify-between"><span>Q95 TLM Purpose:</span><span class="text-emerald-400 font-bold">51.9% Mastery</span></div>
      <div class="flex justify-between"><span>Q97 Normalizing Struggle:</span><span class="text-rose-400 font-bold">33.9% Mastery (66.1% Trap)</span></div>
      <div class="flex justify-between"><span>Q96 Intellectual Safety:</span><span class="text-emerald-400 font-bold">62.0% Mastery</span></div>
      <div class="flex justify-between"><span>Q98 Peer Dialogue:</span><span class="text-emerald-400 font-bold">54.2% Mastery</span></div>
    </div>
    <div class="bg-slate-800/60 border border-slate-700 p-4 rounded-xl text-xs space-y-2">
      <div class="text-xs font-mono text-slate-300 font-bold uppercase mb-1">52-District Strategic Quadrants</div>
      <div class="text-emerald-300"><strong>Q1 Champions:</strong> Harda, Dewas, Sehore, Narsinghpur, Raisen, Neemuch.</div>
      <div class="text-amber-300"><strong>Q2 Scale Gap:</strong> Chhatarpur, Damoh, Panna, Rewa, Satna, Bhind.</div>
      <div class="text-indigo-300"><strong>Q3 Reach Gap:</strong> Bhopal, Indore, Ujjain, Gwalior, Sagar, Ratlam.</div>
      <div class="text-rose-300"><strong>Q4 Priority Support:</strong> Alirajpur, Barwani, Jhabua, Singrauli, Sheopur.</div>
    </div>
  </div>
</body>
</html>
"""

with open('scratch/template_c.html', 'w', encoding='utf-8') as f:
    f.write(html_template_c)

with open('scratch/template_d.html', 'w', encoding='utf-8') as f:
    f.write(html_template_d)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    # Template C render
    page_c = browser.new_page(viewport={'width': 1200, 'height': 800}, device_scale_factor=2)
    page_c.goto(f"file:///{os.path.abspath('scratch/template_c.html')}", wait_until='networkidle')
    page_c.wait_for_timeout(500)
    page_c.screenshot(path='scratch/template_c_preview.png', full_page=True)
    page_c.screenshot(path='scratch/template_c_preview.jpg', type='jpeg', quality=90, full_page=True)

    # Template D render
    page_d = browser.new_page(viewport={'width': 1200, 'height': 800}, device_scale_factor=2)
    page_d.goto(f"file:///{os.path.abspath('scratch/template_d.html')}", wait_until='networkidle')
    page_d.wait_for_timeout(500)
    page_d.screenshot(path='scratch/template_d_preview.png', full_page=True)
    page_d.screenshot(path='scratch/template_d_preview.jpg', type='jpeg', quality=90, full_page=True)

    browser.close()
    print('All 4 template previews generated successfully!')
