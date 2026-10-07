---
id: 1
title: "DOM Container Overwrite in Dynamic KPI Renderers"
status: open
type: open-source
skill: [rsk-metric-auditor, frontend-design]
proposes_skill: []
target_file: []
siblings_checked: "none"
area: "Dynamic DOM updates and KPI card rendering"
date: 2026-10-07
session_context: "Restoring missing KPI card headers, sub-descriptions, and reference footnotes across cycle slicers"
parked_until: ""
resolved: ""
resolution: ""
reference: "scratch_inspect_kpi_playwright.js"
---

**Issue:** In JavaScript DOM update routines (such as `updateKPIs()`), mutating `.parentElement.innerHTML` when querying an element inside a composite card overwrites the entire outer card container (`.bento-card`). This silently destroys surrounding elements such as micro-label headers, status badges, sub-descriptions, and reference citations.

**Suggested improvement:** In `rsk-metric-auditor`, add an explicit rule in §3 (Pre-Delivery Inspection) mandating that dynamic value updaters must target dedicated inner value containers (`#kpiValContainer`), never reassigning `.parentElement.innerHTML` of card containers.

**Principle:** Dynamic metric renderers must isolate mutable value slots into discrete container elements rather than rewriting composite parent card markup.
