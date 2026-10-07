---
id: 3
title: "Multi-Cycle Longitudinal Aggregation Sourcing in Granular Directories"
status: open
type: open-source
skill: [rsk-metric-auditor]
proposes_skill: []
target_file: []
siblings_checked: "none"
area: "Longitudinal data modeling and multi-level BI directories"
date: 2026-10-07
session_context: "Reconciling Consolidated mode block directory metrics against raw August and September telemetry"
parked_until: ""
resolved: ""
resolution: ""
reference: "dataPackage.json"
---

**Issue:** Slicing between monthly cycles (`AUG`, `SEP`) and Consolidated mode left subordinate drill-down views (Block Directory) rendering single-cycle August data because the multi-cycle data structure lacked pre-aggregated cycle keys for lower-level geographic entities.

**Suggested improvement:** Enforce that every cycle slicer state (`AUG`, `SEP`, `CONSOLIDATED`) provides dedicated, pre-reconciled JSON matrices for all breakdown hierarchies (Districts, Blocks, Roles) in `dataPackage.json` with zero-delta cross-validation against raw survey workbooks.

**Principle:** Longitudinal dashboards with composite cycle states must provide dedicated pre-computed datasets for every drill-down level rather than lazily inheriting defaults.
