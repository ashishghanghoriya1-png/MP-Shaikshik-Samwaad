# Cross-Cutting Principles

Live repository principles accumulated from task observations.

## Principles Index

- [1. Subagents must have complete inputs and verified outputs](#1-subagents-must-have-complete-inputs-and-verified-outputs)
- [2. Use canonical identifiers from source data, never reconstruct from derived fields](#2-use-canonical-identifiers-from-source-data-never-reconstruct-from-derived-fields)
- [3. Fetch the instance before describing it](#3-fetch-the-instance-before-describing-it)
- [4. Dynamic metric renderers must isolate mutable value slots into discrete container elements](#4-dynamic-metric-renderers-must-isolate-mutable-value-slots-into-discrete-container-elements)

---

### 1. Subagents must have complete inputs and verified outputs
**Applies to:** all skills that delegate content generation to subagents
**Status:** active
**Added:** 2026-10-07
**Origin:** imported from starter set (#7)

### 2. Use canonical identifiers from source data, never reconstruct from derived fields
**Applies to:** all skills that join, match, or cross-reference data from more than one source
**Status:** active
**Added:** 2026-10-07
**Origin:** imported from starter set (#12)

### 3. Fetch the instance before describing it
**Applies to:** all skills that describe, classify, or verify a specific artefact
**Status:** active
**Added:** 2026-10-07
**Origin:** imported from starter set (#24)

### 4. Dynamic metric renderers must isolate mutable value slots into discrete container elements
**Applies to:** all BI dashboards, executive KPI cards, and UI template engines
**Status:** active
**Added:** 2026-10-07
**Origin:** local observation from CLSS multi-cycle dashboard fixes (#0001)
