---
id: 2
title: "Dual-Metric Layout Protection Against Unchecked Count-Up Animations"
status: open
type: open-source
skill: [rsk-metric-auditor, frontend-design]
proposes_skill: []
target_file: []
siblings_checked: "none"
area: "Numeric animation and multi-metric UI formatting"
date: 2026-10-07
session_context: "Preventing count-up animation scripts from stripping dual-metric Gross | Net Unique typography spans"
parked_until: ""
resolved: ""
resolution: ""
reference: "scratch_inspect_kpi_playwright.js"
---

**Issue:** Generic count-up animation functions (`animateNumbersInContainer`) selecting metric containers (`.kpi-huge-val`) parse inner text as floating-point numbers. When applied to dual-metric layouts (e.g. `46,954 Gross | 33,866 Net Unique`), the animation strips all inner HTML tags, spans, and delimiters, collapsing complex typography into `NaN` or a single overwritten integer.

**Suggested improvement:** Require all number animation utility scripts to implement defensive guards: `if (el.querySelectorAll('*').length > 0 || el.innerText.includes('|')) return;` before attempting string replacement or numeric parsing.

**Principle:** Format-altering utility scripts (animations, formatters) must inspect element structure and bypass compound, segmented, or rich-HTML metrics.
