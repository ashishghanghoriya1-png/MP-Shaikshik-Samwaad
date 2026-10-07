---
name: rsk-dashboard-template
description: Authoritative Executive BI Dashboard Design System, Typography, Layout, and Component Specification. Use whenever building, styling, or refactoring executive dashboards, BI portals, KPI ribbons, bento cards, Chart.js visuals, or analytics interfaces matching the signature Peepul/RSK Executive Studio design.
---

# RSK / Peepul Executive Dashboard Design System & Template

Use this skill whenever asked to create, design, format, or refactor a dashboard to match the **RSK / Peepul Executive Studio Dashboard** design language.

## 🎨 Design Philosophy & Visual Language

- **Visual Style**: High-taste, modern Swiss editorial meets executive BI studio.
- **60-30-10 Rule**: Slate-50 background canvas (`60%`), pure white bento cards (`30%`), signature Peepul Teal & Executive Cobalt accents (`10%`).
- **Elevation**: Subtle layered shadows (`box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05)`), rounded `16px`–`20px` corners, hairline borders (`1px solid rgba(15, 23, 42, 0.1)`).

---

## 🔤 Font Stacks & Typography Scale

```css
:root {
  --font-sans: 'Plus Jakarta Sans', 'Open Sans', 'Noto Sans Devanagari', -apple-system, sans-serif;
  --font-display: 'Comfortaa', cursive, sans-serif;
  --font-editorial: 'Newsreader', Georgia, serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

- **Headers**: Comfortaa (`800` weight, `26px`–`30px`).
- **Card Micro-Labels**: Plus Jakarta Sans (`700` weight, `11px`–`12px`, letter-spacing `+0.08em`, UPPERCASE).
- **KPI Huge Numbers**: Plus Jakarta Sans (`800` weight, `32px`–`36px`, tracking `-0.02em`).
- **Dual-Metric Split**: `32px` Equal Typography for both Gross and Net Unique values (`46,954 Gross | 33,866 Net Unique`).
- **Descriptions**: Plus Jakarta Sans (`500` weight, `12.5px`, line-height `1.45`, color `#475569`).
- **Academic / Data Footnotes**: JetBrains Mono (`10.5px`, color `#94a3b8`).
- **Qualitative Quotes**: Newsreader Italic (`16px`, line-height `1.6`).

---

## 🎨 Color Tokens (Pantone Calibrated)

```css
:root {
  --peepul-teal: #008aab;       /* Pantone 3135 C - Primary Brand Teal */
  --peepul-cyan: #63d0df;       /* Pantone 3105 C - Light Accent Cyan */
  --peepul-brown: #985f35;      /* Pantone 4635 C - Earth Tan */
  --peepul-gray: #77777a;       /* Pantone Gray 9C */
  --peepul-blue: #1d4ed8;       /* Executive Cobalt - Teachers */
  --peepul-indigo: #4f46e5;     /* Deep Indigo - Facilitators */
  --peepul-emerald: #059669;    /* Target Exceeded - Emerald */
  --peepul-amber: #d97706;      /* Moderate Watch - Amber */
  --peepul-rose: #e11d48;       /* Bottleneck Alert - Rose */

  --bg-canvas: #f8fafc;
  --bg-surface-card: #ffffff;
  --bg-surface-subtle: #f1f5f9;

  --border-subtle: rgba(15, 23, 42, 0.12);
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-muted: #64748b;
  --text-dim: #94a3b8;
}
```

---

## 🧱 Component Layout Specifications

### 1. Bento KPI Card Structure
Every card must contain:
1. `.kpi-micro-label` + Status Badge in a flex row.
2. Isolated `.kpi-huge-val` container (never mutate `.parentElement.innerHTML`).
3. `.kpi-sub-desc` with quantitative breakdown.
4. `.kpi-ref` citation in monospace.

```html
<div class="bento-card">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
    <span class="kpi-micro-label">ATTENDING TEACHERS</span>
    <span class="kpi-badge badge-teal">49.5% NET UNIQUE</span>
  </div>
  <div class="kpi-huge-val" id="kpiTeachersContainer">
    <span style="font-size: 32px; font-weight: 800; color: var(--text-primary);">46,954 Gross</span>
    <span style="color: var(--text-dim); margin: 0 6px;">|</span>
    <span style="font-size: 32px; font-weight: 800; color: var(--peepul-teal);">33,866 Net Unique</span>
  </div>
  <div class="kpi-sub-desc">
    33,866 Net Unique Teachers (49.5% Saturation) • 46,954 Gross Touchpoints • 13,088 Repeat Champions (55.0%)
  </div>
  <div class="kpi-ref">[Ref: SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx]</div>
</div>
```

---

## ⚙️ Mandatory Front-End Safeguards

1. **DOM Targeting**: JS value updates must target dedicated inner spans/divs directly (`#kpiValContainer`), never reassigning `.parentElement.innerHTML` on composite card elements.
2. **Animation Safety**: Number count-up animations must check:
   `if (target.querySelectorAll('*').length > 0 || text.includes('|')) return;`
3. **Chart Visuals**: Include `chartjs-plugin-datalabels` for instant readability without hover dependency.
4. **Bilingual Support**: Provide seamless toggle between English and Hindi (`Noto Sans Devanagari`).

---

## 📂 Reference Documentation
- Complete Design System Guide: [`docs/RSK_Executive_Dashboard_Design_System_Template.md`](file:///c:/Users/Ashish/OneDrive%20-%20Absolute%20Return%20For%20Kids/Master%20Dashboard%20for%20CLSS%20-%20Copy/docs/RSK_Executive_Dashboard_Design_System_Template.md)
- Production Reference Implementation: [`index.html`](file:///c:/Users/Ashish/OneDrive%20-%20Absolute%20Return%20For%20Kids/Master%20Dashboard%20for%20CLSS%20-%20Copy/index.html)
