# Executive BI Dashboard Design System & Template Specification
## "Peepul / RSK Executive Studio" Design Language & Component System

This document serves as the **authoritative master design system, typography guideline, color token registry, and layout template** for all future executive dashboards, BI portals, and analytics suites. When requested to build a new dashboard or match this styling, reference this template.

---

## 1. Typography & Font Hierarchy

### Font Stack Definitions
```css
:root {
  /* Primary Sans & Numbers (Clean, ultra-legible, modern geometric) */
  --font-sans: 'Plus Jakarta Sans', 'Open Sans', 'Noto Sans Devanagari', -apple-system, BlinkMacSystemFont, sans-serif;

  /* Brand / Display Header (Approachable, premium executive) */
  --font-display: 'Comfortaa', cursive, sans-serif;
  --font-brand: 'Comfortaa', cursive, sans-serif;

  /* Editorial & Qualitative Quotes (Rich, trustworthy, academic) */
  --font-editorial: 'Newsreader', Georgia, 'Times New Roman', serif;

  /* Monospace & Badges (Code, data provenance, precise figures) */
  --font-mono: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
}
```

### Google Fonts CDN Import
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=Noto+Sans+Devanagari:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

### Typography Scale & Rules
| Role / Element | Font Family | Size | Weight | Tracking / Line Height | Color Token |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Main Portal Title** | `--font-display` | `26px` – `30px` | `800` | `-0.02em` / `1.2` | `--text-primary` (`#0f172a`) |
| **Section / Tab Header** | `--font-display` | `20px` – `22px` | `700` | `-0.01em` / `1.3` | `--peepul-teal` (`#008aab`) |
| **Card Micro-Label (Header)** | `--font-sans` | `11px` – `12px` | `700` | `+0.08em` (UPPERCASE) | `--text-muted` (`#64748b`) |
| **KPI Huge Metric Value** | `--font-sans` | `32px` – `36px` | `800` | `-0.02em` / `1.0` | `--text-primary` (`#0f172a`) |
| **Dual-Metric Split (Gross \| Net)** | `--font-sans` | `32px` | `800` (Equal) | `gap: 8px` with pipe `\|` | `--text-primary` (`#0f172a`) |
| **Sub-Description / Details** | `--font-sans` | `12.5px` – `13px` | `500` | Normal / `1.45` | `--text-secondary` (`#475569`) |
| **Reference / Provenance Footnote** | `--font-mono` | `10.5px` – `11px` | `500` | Normal / `1.4` | `--text-dim` (`#94a3b8`) |
| **Narrative / Field Quote** | `--font-editorial` | `15px` – `17px` | `400` (Italic) | Normal / `1.6` | `--text-secondary` (`#334155`) |

---

## 2. Color Tokens & 60-30-10 Palette

```css
:root {
  /* Signature Brand Palette (Pantone Formulations) */
  --peepul-teal: #008aab;       /* Pantone 3135 C - Primary Brand Teal */
  --peepul-cyan: #63d0df;       /* Pantone 3105 C - Light Cyan / Accent */
  --peepul-brown: #985f35;      /* Pantone 4635 C - Earth Tan */
  --peepul-gray: #77777a;       /* Pantone Gray 9C */
  
  /* Executive Semantic Role Colors */
  --peepul-blue: #1d4ed8;       /* Primary Executive Cobalt (Teachers / Core Turnout) */
  --peepul-indigo: #4f46e5;     /* State Master Cadre (Facilitators & Observers) */
  --peepul-emerald: #059669;    /* Benchmark Exceeded / High Attendance (Green) */
  --peepul-amber: #d97706;      /* Moderate / Watch Status (Amber) */
  --peepul-rose: #e11d48;       /* Bottleneck Alert / Low Attendance (Rose/Red) */

  /* 60-30-10 Surface Architecture */
  --bg-canvas: #f8fafc;         /* Slate-50: Main Background (60%) */
  --bg-surface-1: #ffffff;      /* Pure White: Bento Cards & Panels (30%) */
  --bg-surface-2: #f1f5f9;      /* Slate-100: Secondary containers, pills, table headers */
  --bg-surface-3: #e2e8f0;      /* Slate-200: Input borders & dividers */
  --bg-surface-card: #ffffff;

  /* Borders & Hairlines */
  --border-hairline: rgba(15, 23, 42, 0.07);
  --border-subtle: rgba(15, 23, 42, 0.12);
  --border-focus: #008aab;

  /* Typography Colors */
  --text-primary: #0f172a;      /* Slate-900: High-contrast primary headlines & figures */
  --text-secondary: #475569;    /* Slate-600: Descriptions & body text */
  --text-muted: #64748b;        /* Slate-500: Micro-labels & headers */
  --text-dim: #94a3b8;          /* Slate-400: Citations & metadata footnotes */

  /* Shadows & Elevation */
  --shadow-sm: 0 1px 2px 0 rgba(15, 23, 42, 0.05);
  --shadow-card: 0 4px 20px -2px rgba(15, 23, 42, 0.05), 0 2px 6px -1px rgba(15, 23, 42, 0.02);
  --shadow-hover: 0 10px 25px -3px rgba(15, 23, 42, 0.08), 0 4px 10px -2px rgba(15, 23, 42, 0.04);
  --shadow-glow: 0 0 20px rgba(0, 138, 171, 0.15);

  /* Radius */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 20px;
  --radius-full: 9999px;
}
```

---

## 3. Structural Component Hierarchy

### A. Navigation Ribbon & Slicer Bar
- **Sticky / Floating Navigation Shell**:
  - `background: rgba(255, 255, 255, 0.92); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border-subtle);`
- **Tab Buttons (`.nav-tab-btn`)**:
  - Unselected: `background: transparent; color: var(--text-secondary); font-weight: 600; padding: 10px 18px; border-radius: var(--radius-full);`
  - Selected (Active): `background: var(--peepul-teal); color: #ffffff; box-shadow: 0 4px 12px rgba(0, 138, 171, 0.3); font-weight: 700;`
- **Cycle Slicer Pills (`.slicer-btn`)**:
  - `padding: 6px 14px; border-radius: var(--radius-full); border: 1px solid var(--border-subtle); background: var(--bg-surface-2); font-size: 13px;`
  - Active: `background: #0f172a; color: #ffffff; border-color: #0f172a; font-weight: 700;`

### B. Bento KPI Card Specification
```html
<div class="bento-card">
  <!-- 1. Header with Micro-label and Status Badge -->
  <div class="kpi-header-row" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
    <span class="kpi-micro-label">ATTENDING TEACHERS</span>
    <span class="kpi-badge badge-teal" style="font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 9999px; background: rgba(0, 138, 171, 0.1); color: var(--peepul-teal);">49.5% NET UNIQUE</span>
  </div>

  <!-- 2. Huge Value Slot (Dedicated Container) -->
  <div class="kpi-huge-val" id="kpiTeachersContainer" style="font-size: 32px; font-weight: 800; color: var(--text-primary); margin: 6px 0;">
    <span style="font-size: 32px; font-weight: 800; color: var(--text-primary);">46,954 Gross</span>
    <span style="color: var(--text-dim); margin: 0 6px; font-weight: 300;">|</span>
    <span style="font-size: 32px; font-weight: 800; color: var(--peepul-teal);">33,866 Net Unique</span>
  </div>

  <!-- 3. Sub-Description (Quantitative context) -->
  <div class="kpi-sub-desc" style="font-size: 12.5px; color: var(--text-secondary); line-height: 1.45; margin-bottom: 8px;">
    33,866 Net Unique Teachers (49.5% Saturation) • 46,954 Gross Touchpoints • 13,088 Repeat Champions (55.0%)
  </div>

  <!-- 4. Data Provenance Footnote -->
  <div class="kpi-ref" style="font-family: var(--font-mono); font-size: 10.5px; color: var(--text-dim);">
    [Ref: SS_ResponseDetail_Cluster Level_Grades 6-8_September.xlsx]
  </div>
</div>
```

### C. Bento Card CSS
```css
.bento-card {
  background: var(--bg-surface-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-xl);
  padding: 20px 24px;
  box-shadow: var(--shadow-card);
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.bento-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-hover);
  border-color: rgba(0, 138, 171, 0.3);
}
```

---

## 4. Key Engineering & Interaction Rules

### Rule 1: Strict Value Container Isolation
- **NEVER** overwrite `.parentElement.innerHTML` when mutating card figures via JavaScript.
- **ALWAYS** assign inner HTML strictly to `#kpiValContainer` / inner elements so headers, badges, descriptions, and citations remain intact across slicer updates.

### Rule 2: Dual-Metric Typography Parity
- Gross session volume and Net unique human reach must have **equal font size (`32px`) and font weight (`800`)**.
- Separate using a styled vertical bar (`|`) with distinct color accents (e.g., Primary Dark for Gross, Brand Teal for Unique).

### Rule 3: Animation Bypass Guardrails
- Number count-up animation scripts must never strip compound HTML strings:
```javascript
function animateNumbersInContainer(container) {
  container.querySelectorAll('.kpi-huge-val').forEach(el => {
    // Bypass if element contains child spans or pipe separator
    if (el.querySelectorAll('*').length > 0 || el.innerText.includes('|')) return;
    // Otherwise animate single number
    runCountUp(el);
  });
}
```

### Rule 4: ChartDataLabels Integration
- Charts must include direct data labels on bars and donuts (`plugin: ChartDataLabels`) with contrasting font colors (`#ffffff` inside dark bars, `#475569` on light areas) so users do not need to hover to read key figures.

---

## 5. Full Reusable HTML Starter Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Executive BI Dashboard</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@700;800&family=JetBrains+Mono:wght@500;700&family=Newsreader:ital,wght@1,400;1,600&family=Noto+Sans+Devanagari:wght@500;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Chart.js & Plugins -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.2.0/dist/chartjs-plugin-datalabels.min.js"></script>

  <style>
    /* Insert Section 2 Color Tokens and Section 3 Bento Card Styles here */
  </style>
</head>
<body style="background: var(--bg-canvas); font-family: var(--font-sans); color: var(--text-primary); margin: 0; padding: 24px;">
  <!-- Main Dashboard Container -->
  <div style="max-width: 1440px; margin: 0 auto;">
    <!-- Header -->
    <header style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
      <div>
        <h1 style="font-family: var(--font-display); font-size: 26px; font-weight: 800; margin: 0; color: var(--text-primary);">
          State Educational Intelligence Dashboard
        </h1>
        <p style="font-size: 13px; color: var(--text-muted); margin: 4px 0 0 0;">
          Continuous Professional Development & Academic Monitoring Telemetry
        </p>
      </div>
      <!-- Slicer Controls -->
      <div style="display: flex; gap: 8px;">
        <button class="slicer-btn active">📅 August</button>
        <button class="slicer-btn">📅 September</button>
        <button class="slicer-btn">🌐 Consolidated</button>
      </div>
    </header>

    <!-- 6-Card KPI Ribbon Grid -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 28px;">
      <!-- Insert Bento KPI Cards here -->
    </div>
  </div>
</body>
</html>
```
