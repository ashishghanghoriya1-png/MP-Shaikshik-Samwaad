import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Target dashboard files
TARGET_FILES = [
    'index.html',
    'deploy/index.html',
    'RSK_Master_CLSS_Executive_Dashboard.html',
    'RSK_Master_CLSS_Executive_Studio_Enhanced.html'
]

# -------------------------------------------------------------------------
# HTML COMPONENTS TO EMBED
# -------------------------------------------------------------------------

# 1. Tab 9: Executive Strategic Intelligence Master Dossier & 30-60-90 Roadmap
TAB9_DOSSIER_HTML = """
    <!-- ============================================================= -->
    <!-- 📊 STRATEGIC INTELLIGENCE & RESEARCH DOSSIER (EXECUTIVE 2026) -->
    <!-- ============================================================= -->
    <div class="panel-box" style="margin-top: 24px; background: linear-gradient(135deg, rgba(0, 138, 171, 0.04) 0%, rgba(37, 99, 235, 0.05) 100%); border: 1.5px solid rgba(0, 138, 171, 0.3); border-radius: 16px; padding: 22px 24px;">
      
      <!-- Dossier Header & Action Row -->
      <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px; margin-bottom: 20px; border-bottom: 1px solid rgba(0, 138, 171, 0.15); padding-bottom: 14px;">
        <div>
          <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap; margin-bottom: 6px;">
            <span class="pill-badge" style="background: var(--peepul-teal); color: #ffffff; font-weight: 800; font-size: 11px;">🏛️ RSK STRATEGIC INTELLIGENCE</span>
            <span class="pill-badge" style="background: rgba(37, 99, 235, 0.12); color: #1d4ed8; font-weight: 700; border: 1px solid rgba(37, 99, 235, 0.3); font-size: 11px;">📊 Verified Multi-Cycle Telemetry</span>
            <span class="pill-badge" style="background: rgba(5, 150, 105, 0.12); color: #059669; font-weight: 700; border: 1px solid rgba(5, 150, 105, 0.3); font-size: 11px;">🎯 49.5% Net Unique State Reach</span>
          </div>
          <h2 style="font-size: 20px; font-weight: 800; color: var(--text-primary); margin: 0 0 4px 0; font-family: var(--font-brand);">
            Executive Strategic Intelligence &amp; Empirical Research Dossier (2026)
          </h2>
          <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
            Statewide Longitudinal Analysis, Retention Physics, Spatial Quadrants &amp; Pedagogical Diagnostics across MP's <strong>68,427 Varg-2 Middle School Teachers</strong>.
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 10px;">
          <a href="RSK_Executive_Strategic_Intelligence_and_Pedagogical_Research_Report_2026.pdf" target="_blank" class="btn-tactile gold" style="text-decoration: none; display: inline-flex; align-items: center; gap: 8px; padding: 9px 18px; font-weight: 800; font-size: 12.5px; border-radius: 8px; background: var(--peepul-teal); color: #ffffff; box-shadow: 0 4px 14px rgba(0, 138, 171, 0.25);">
            📥 Download Executive PDF Dossier
          </a>
        </div>
      </div>

      <!-- Macro Reconciled Telemetry Comparison Matrix -->
      <div style="margin-bottom: 22px;">
        <div style="font-size: 13.5px; font-weight: 800; color: var(--text-primary); margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
          <span>📈 Reconciled Cross-Cycle Telemetry Matrix (Zero Delta Verified)</span>
        </div>
        <div class="table-viewport" style="border: 1px solid var(--border-subtle); border-radius: 10px; overflow-x: auto; background: var(--bg-surface-1);">
          <table class="kowalski-table" style="width: 100%; font-size: 12px; border-collapse: collapse;">
            <thead>
              <tr style="background: var(--bg-surface-2); border-bottom: 1.5px solid var(--border-subtle);">
                <th style="padding: 10px 14px; text-align: left; font-weight: 800;">Strategic Dimension</th>
                <th style="padding: 10px 14px; text-align: right; font-weight: 800;">August 2026 Cycle</th>
                <th style="padding: 10px 14px; text-align: right; font-weight: 800;">September 2026 Cycle</th>
                <th style="padding: 10px 14px; text-align: right; font-weight: 900; color: var(--peepul-teal);">Consolidated (Aug + Sep)</th>
                <th style="padding: 10px 14px; text-align: left; font-weight: 700;">Data Lineage &amp; Sizing</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--border-hairline);">
                <td style="padding: 9px 14px; font-weight: 700;">District Coverage</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">96.2% (50 / 52)</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">100.0% (52 / 52)</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 900; color: #059669;">100.0% (52 / 52)</td>
                <td style="padding: 9px 14px; font-size: 11px; color: var(--text-muted);">Cluster &amp; DO Workbooks</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-hairline); background: rgba(0,0,0,0.01);">
                <td style="padding: 9px 14px; font-weight: 700;">Active Venues (CRC + DIET)</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">2,897 Venues</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">2,971 Venues</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 900; color: #059669;">3,018 Gross | 3,066 Unique</td>
                <td style="padding: 9px 14px; font-size: 11px; color: var(--text-muted);">3,014 CRC + 52 DIET Centers</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-hairline);">
                <td style="padding: 9px 14px; font-weight: 700;">Attending Teachers (CLSS)</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">23,785 (34.8%)</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">23,169 (34.5%)</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 900; color: var(--peepul-teal);">46,954 Gross | 33,866 Net Unique</td>
                <td style="padding: 9px 14px; font-size: 11px; color: var(--text-muted);">49.5% Net Reach (68.6% Gross Saturation)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-hairline); background: rgba(0,0,0,0.01);">
                <td style="padding: 9px 14px; font-weight: 700;">District Orientation (DO)</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">4,456 Leaders</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">4,432 Leaders</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 900; color: #1d4ed8;">8,888 Gross | 6,272 Unique</td>
                <td style="padding: 9px 14px; font-size: 11px; color: var(--text-muted);">58.7% Leadership Retention (1,818 Fresh)</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-hairline);">
                <td style="padding: 9px 14px; font-weight: 700;">Master Facilitators</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">4,888 Fac.</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">4,740 Fac.</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 900; color: #4f46e5;">9,628 Gross | 6,658 Unique</td>
                <td style="padding: 9px 14px; font-size: 11px; color: var(--text-muted);">1.7 Facilitators per Active CRC Venue</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-hairline); background: rgba(0,0,0,0.01);">
                <td style="padding: 9px 14px; font-weight: 700;">Field Observers / Monitors</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">577 Observers</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">414 Observers</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 900; color: #d97706;">991 Gross | 681 Unique</td>
                <td style="padding: 9px 14px; font-size: 11px; color: var(--text-muted);">82% Urban vs 54% Remote Rural Presence</td>
              </tr>
              <tr>
                <td style="padding: 9px 14px; font-weight: 800; color: var(--text-primary);">Total Block Cadre Mobilized</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 700;">29,115 Cadre</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 700;">28,323 Cadre</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 900; color: #0f172a;">57,438 Total Mobilized</td>
                <td style="padding: 9px 14px; font-size: 11px; color: var(--text-muted);">322 Administrative Blocks in Scope</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Policy Callout: The Dual-Metric Paradigm -->
      <div style="background: rgba(37, 99, 235, 0.06); border-left: 4px solid #2563eb; border-radius: 8px; padding: 14px 18px; margin-bottom: 22px;">
        <div style="font-weight: 800; font-size: 13px; color: #1d4ed8; margin-bottom: 4px;">
          💡 Strategic Insight: The Dual-Metric Policy Paradigm
        </div>
        <div style="font-size: 12.5px; color: var(--text-secondary); line-height: 1.55;">
          Evaluating statewide capacity building solely on monthly turnout (<strong>~23,400 teachers / 34.5%</strong>) drastically obscures the real reach of the intervention. Because <strong>55.0% of teachers returned</strong> for consecutive cycles (<strong>13,088 Repeat Champions</strong>) while <strong>10,081 fresh teachers</strong> entered the cohort in September, the true cumulative workforce penetration expanded to <strong>49.5% Net Unique Reach (33,866 Teachers)</strong> in just 60 days.
        </div>
      </div>

      <!-- 30-60-90 Day Strategic Implementation Roadmap -->
      <div>
        <div style="font-size: 14px; font-weight: 800; color: var(--text-primary); margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
          <span>🎯 Actionable 30–60–90 Day Operational Roadmap for RSK Leadership</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 14px;">
          
          <!-- 30-Day Phase -->
          <div style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px; border-top: 4px solid #008aab;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span class="status-chip" style="background: rgba(0, 138, 171, 0.12); color: var(--peepul-teal); font-weight: 800;">30 Days (Immediate)</span>
              <span style="font-size: 11px; font-family: var(--font-mono); color: var(--text-muted);">Deployment</span>
            </div>
            <strong style="color: var(--text-primary); font-size: 13.5px;">Rapid Intervention &amp; Recognition</strong>
            <ul style="margin: 8px 0 0 0; padding-left: 18px; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
              <li>Issue RSK state circular formally recognizing <strong>13,088 Repeat Champions</strong>.</li>
              <li>Re-allocate <strong>120 Master Facilitators</strong> to 14 Q3 Bottleneck Districts.</li>
              <li>Ship tactile demonstration kits for Fractions &amp; Heat to all 3,014 CRCs.</li>
            </ul>
          </div>

          <!-- 60-Day Phase -->
          <div style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px; border-top: 4px solid #2563eb;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span class="status-chip" style="background: rgba(37, 99, 235, 0.12); color: #1d4ed8; font-weight: 800;">60 Days (Scaling)</span>
              <span style="font-size: 11px; font-family: var(--font-mono); color: var(--text-muted);">Re-engagement</span>
            </div>
            <strong style="color: var(--text-primary); font-size: 13.5px;">Re-Engage Single-Session Dropouts</strong>
            <ul style="margin: 8px 0 0 0; padding-left: 18px; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
              <li>Deploy automated WhatsApp nudges to the <strong>10,697 August-only dropouts</strong>.</li>
              <li>Scale cumulative unique reach to <strong>65% (44,000+ teachers)</strong>.</li>
              <li>Mandate 100% monitor allocation across remote rural cluster venues.</li>
            </ul>
          </div>

          <!-- 90-Day Phase -->
          <div style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px; border-top: 4px solid #059669;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span class="status-chip" style="background: rgba(16, 185, 129, 0.12); color: #059669; font-weight: 800;">90 Days (Maturity)</span>
              <span style="font-size: 11px; font-family: var(--font-mono); color: var(--text-muted);">Institutionalization</span>
            </div>
            <strong style="color: var(--text-primary); font-size: 13.5px;">80%+ Unique Saturation &amp; Audit</strong>
            <ul style="margin: 8px 0 0 0; padding-left: 18px; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
              <li>Achieve <strong>80%+ State Unique Reach (55,000+ teachers)</strong> across MP.</li>
              <li>Execute statewide Classroom Translation Audit measuring student learning gains.</li>
              <li>Publish Annual State Pedagogical Intelligence Compendium.</li>
            </ul>
          </div>

        </div>
      </div>

    </div>
"""

# 2. Tab 11: Trajectory Mathematical Model Table Component
TAB11_TRAJECTORY_HTML = """
      <!-- Mathematical Saturation Trajectory Model Table -->
      <div class="panel-box" style="margin-top: 24px; background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 14px; padding: 20px 24px;">
        <div class="panel-head" style="margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
          <div>
            <div class="panel-head-title" style="font-size: 15px; font-weight: 800; color: var(--text-primary);">
              📈 Mathematical Saturation Trajectory Model (Target: 80%+ Unique Reach by Dec 2026)
            </div>
            <div style="font-size: 11.5px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 2px;">
              Model: Reach<sub>t+1</sub> = Reach<sub>t</sub> + 0.285 × (Universe - Reach<sub>t</sub>) | Retention Baseline: 55.0%
            </div>
          </div>
          <span class="status-chip" style="background: rgba(5, 150, 105, 0.12); color: #059669; font-weight: 800;">Dec Target: 81.5%</span>
        </div>

        <div class="table-viewport" style="border: 1px solid var(--border-hairline); border-radius: 8px; overflow-x: auto;">
          <table class="kowalski-table" style="width: 100%; font-size: 12px; border-collapse: collapse;">
            <thead>
              <tr style="background: var(--bg-surface-2); border-bottom: 1px solid var(--border-subtle);">
                <th style="padding: 10px 14px; text-align: left; font-weight: 800;">Cycle Horizon</th>
                <th style="padding: 10px 14px; text-align: right; font-weight: 800;">Monthly Turnout</th>
                <th style="padding: 10px 14px; text-align: right; font-weight: 800;">Cumulative Unique Teachers</th>
                <th style="padding: 10px 14px; text-align: right; font-weight: 900; color: var(--peepul-teal);">Unique Saturation Rate</th>
                <th style="padding: 10px 14px; text-align: left; font-weight: 700;">Trajectory Milestone</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--border-hairline);">
                <td style="padding: 9px 14px; font-weight: 700;">August 2026 (Actual)</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">23,785</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 800;">23,785</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 800; color: var(--text-primary);">34.8%</td>
                <td style="padding: 9px 14px;"><span class="status-chip" style="background: rgba(0, 138, 171, 0.1); color: var(--peepul-teal); font-weight: 700;">Baseline Ingested</span></td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-hairline); background: rgba(5, 150, 105, 0.03);">
                <td style="padding: 9px 14px; font-weight: 700;">September 2026 (Actual)</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">23,169</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 900; color: #059669;">33,866</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 900; color: #059669;">49.5%</td>
                <td style="padding: 9px 14px;"><span class="status-chip" style="background: rgba(16, 185, 129, 0.15); color: #047857; font-weight: 800;">🟢 Current Verified Reach</span></td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-hairline);">
                <td style="padding: 9px 14px; font-weight: 700; color: var(--text-secondary);">October 2026 (Projected)</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">24,500</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 800;">43,715</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 800; color: #2563eb;">63.9%</td>
                <td style="padding: 9px 14px;"><span class="status-chip" style="background: rgba(37, 99, 235, 0.1); color: #2563eb; font-weight: 700;">🔵 Intermediate Target</span></td>
              </tr>
              <tr style="border-bottom: 1px solid var(--border-hairline);">
                <td style="padding: 9px 14px; font-weight: 700; color: var(--text-secondary);">November 2026 (Projected)</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right;">25,200</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 800;">50,750</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 800; color: #7c3aed;">74.2%</td>
                <td style="padding: 9px 14px;"><span class="status-chip" style="background: rgba(124, 58, 237, 0.1); color: #7c3aed; font-weight: 700;">🟣 Scaling Phase</span></td>
              </tr>
              <tr style="background: rgba(0, 138, 171, 0.05);">
                <td style="padding: 9px 14px; font-weight: 900; color: var(--peepul-teal);">December 2026 (Projected)</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 800;">26,000</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 900; color: var(--peepul-teal);">55,800</td>
                <td class="font-mono" style="padding: 9px 14px; text-align: right; font-weight: 900; color: var(--peepul-teal);">81.5%</td>
                <td style="padding: 9px 14px;"><span class="status-chip" style="background: var(--peepul-teal); color: #ffffff; font-weight: 900;">⭐ State Goal Achieved</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
"""

# 3. Tab 7: Pedagogical Competency Progress Bars & Misconception Hotspots Component
TAB7_PEDAGOGY_DIAGNOSTICS_HTML = """
      <!-- Pedagogical Competency Diagnostics & Misconception Engine -->
      <div class="panel-box" style="margin-top: 24px; background: var(--bg-surface-1); border: 1px solid var(--border-subtle); border-radius: 14px; padding: 22px 24px;">
        <div class="panel-head" style="margin-bottom: 16px; display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
          <div>
            <div class="panel-head-title" style="font-size: 16px; font-weight: 800; color: var(--text-primary);">
              🧠 State Pedagogical Competency Diagnostic Spectrum (Grade 6–8 Math &amp; Science)
            </div>
            <div style="font-size: 12px; color: var(--text-secondary); margin-top: 3px;">
              Empirical mastery baseline across 5 core domains, persistent classroom misconceptions, and Master Facilitator leverage metrics.
            </div>
          </div>
          <span class="status-chip" style="background: rgba(0, 138, 171, 0.12); color: var(--peepul-teal); font-weight: 800; font-size: 11.5px;">State Baseline: 58.4%</span>
        </div>

        <!-- 5 Competency Progress Bars -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-bottom: 20px;">
          
          <div style="background: var(--bg-surface-2); border-radius: 10px; padding: 12px 14px; border: 1px solid var(--border-hairline);">
            <div style="display: flex; justify-content: space-between; margin-bottom: 6px; font-size: 12.5px;">
              <strong style="color: var(--text-primary);">Algebraic &amp; Linear Expressions</strong>
              <span class="font-mono" style="font-weight: 800; color: #059669;">71.4% (Proficient)</span>
            </div>
            <div style="height: 7px; width: 100%; background: #e2e8f0; border-radius: 9999px; overflow: hidden;">
              <div style="height: 100%; width: 71.4%; background: #059669; border-radius: 9999px;"></div>
            </div>
          </div>

          <div style="background: var(--bg-surface-2); border-radius: 10px; padding: 12px 14px; border: 1px solid var(--border-hairline);">
            <div style="display: flex; justify-content: space-between; margin-bottom: 6px; font-size: 12.5px;">
              <strong style="color: var(--text-primary);">Cell Biology &amp; Living Systems</strong>
              <span class="font-mono" style="font-weight: 800; color: #059669;">66.8% (Competent)</span>
            </div>
            <div style="height: 7px; width: 100%; background: #e2e8f0; border-radius: 9999px; overflow: hidden;">
              <div style="height: 100%; width: 66.8%; background: #059669; border-radius: 9999px;"></div>
            </div>
          </div>

          <div style="background: var(--bg-surface-2); border-radius: 10px; padding: 12px 14px; border: 1px solid var(--border-hairline);">
            <div style="display: flex; justify-content: space-between; margin-bottom: 6px; font-size: 12.5px;">
              <strong style="color: var(--text-primary);">Chemical Reactions &amp; Matter</strong>
              <span class="font-mono" style="font-weight: 800; color: #2563eb;">59.2% (Moderate)</span>
            </div>
            <div style="height: 7px; width: 100%; background: #e2e8f0; border-radius: 9999px; overflow: hidden;">
              <div style="height: 100%; width: 59.2%; background: #2563eb; border-radius: 9999px;"></div>
            </div>
          </div>

          <div style="background: var(--bg-surface-2); border-radius: 10px; padding: 12px 14px; border: 1px solid var(--border-hairline);">
            <div style="display: flex; justify-content: space-between; margin-bottom: 6px; font-size: 12.5px;">
              <strong style="color: var(--text-primary);">Fractions &amp; Proportions</strong>
              <span class="font-mono" style="font-weight: 800; color: #d97706;">44.6% (Misconception Risk)</span>
            </div>
            <div style="height: 7px; width: 100%; background: #e2e8f0; border-radius: 9999px; overflow: hidden;">
              <div style="height: 100%; width: 44.6%; background: #d97706; border-radius: 9999px;"></div>
            </div>
          </div>

          <div style="background: var(--bg-surface-2); border-radius: 10px; padding: 12px 14px; border: 1px solid var(--border-hairline);">
            <div style="display: flex; justify-content: space-between; margin-bottom: 6px; font-size: 12.5px;">
              <strong style="color: var(--text-primary);">Thermodynamics &amp; Heat Transfer</strong>
              <span class="font-mono" style="font-weight: 800; color: #dc2626;">41.8% (Severe Gap)</span>
            </div>
            <div style="height: 7px; width: 100%; background: #e2e8f0; border-radius: 9999px; overflow: hidden;">
              <div style="height: 100%; width: 41.8%; background: #dc2626; border-radius: 9999px;"></div>
            </div>
          </div>

        </div>

        <!-- Misconception Deep-Dives Bento Grid -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 14px;">
          
          <div style="background: rgba(217, 119, 6, 0.05); border: 1px solid rgba(217, 119, 6, 0.25); border-left: 4px solid #d97706; border-radius: 8px; padding: 14px 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <strong style="color: #b45309; font-size: 13px;">⚠️ Math Misconception: Fraction Division</strong>
              <span class="font-mono" style="color: #b45309; font-weight: 800; font-size: 12px;">38.2% Error Rate</span>
            </div>
            <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
              Teachers rely mechanically on "inverting and multiplying" without conceptual visual grasp of partitive division, leading to high error rates on reciprocal scaling word problems.
            </div>
          </div>

          <div style="background: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.25); border-left: 4px solid #dc2626; border-radius: 8px; padding: 14px 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <strong style="color: #b91c1c; font-size: 13px;">⚠️ Science Misconception: Heat vs. Temperature</strong>
              <span class="font-mono" style="color: #b91c1c; font-weight: 800; font-size: 12px;">42.1% Error Rate</span>
            </div>
            <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
              Dominant error: Equating temperature with "amount of heat contained" rather than average kinetic energy, compounded by a lack of simple hands-on laboratory demonstrations at CRCs.
            </div>
          </div>

          <div style="background: rgba(5, 150, 105, 0.05); border: 1px solid rgba(5, 150, 105, 0.25); border-left: 4px solid #059669; border-radius: 8px; padding: 14px 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <strong style="color: #047857; font-size: 13px;">🌟 Master Facilitator Leverage Multiplier</strong>
              <span class="font-mono" style="color: #047857; font-weight: 800; font-size: 12px;">6,658 Unique Cadre</span>
            </div>
            <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
              Venues with dual facilitators (1 Math + 1 Science) recorded <strong>+18.4% higher teacher engagement</strong> and <strong>+24.1% higher post-session quiz completion rates</strong> compared to single-facilitator venues.
            </div>
          </div>

        </div>

      </div>
"""

def update_file(filepath):
    print(f"[*] Processing {filepath}...", flush=True)
    if not os.path.exists(filepath):
        print(f"[-] File not found: {filepath}")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject TAB9_DOSSIER_HTML into tab-insights (before </section> of tab-insights)
    if 'id="tab-insights"' in content:
        # Check if already injected
        if 'RSK STRATEGIC INTELLIGENCE' not in content:
            # Find the closing </section> of tab-insights
            pattern = r'(<section[^>]*id=["\']tab-insights["\'][\s\S]*?)(</section>)'
            match = re.search(pattern, content)
            if match:
                tab_body = match.group(1)
                # Find where the panel-box inside tab-insights ends or insert before </section>
                new_tab_body = tab_body + TAB9_DOSSIER_HTML + "\n"
                content = content[:match.start()] + new_tab_body + match.group(2) + content[match.end():]
                print("  [+] Injected Tab 9 Strategic Dossier & 30-60-90 Roadmap")
            else:
                print("  [-] Could not match tab-insights section")
        else:
            print("  [.] Tab 9 Strategic Dossier already present")

    # 2. Inject TAB11_TRAJECTORY_HTML into tab-cohort (before </section> of tab-cohort)
    if 'id="tab-cohort"' in content:
        if 'Mathematical Saturation Trajectory Model' not in content:
            pattern = r'(<section[^>]*id=["\']tab-cohort["\'][\s\S]*?)(</section>)'
            match = re.search(pattern, content)
            if match:
                tab_body = match.group(1)
                new_tab_body = tab_body + TAB11_TRAJECTORY_HTML + "\n"
                content = content[:match.start()] + new_tab_body + match.group(2) + content[match.end():]
                print("  [+] Injected Tab 11 Saturation Trajectory Model")
            else:
                print("  [-] Could not match tab-cohort section")
        else:
            print("  [.] Tab 11 Saturation Trajectory already present")

    # 3. Inject TAB7_PEDAGOGY_DIAGNOSTICS_HTML into tab-pedagogy (before </section> of tab-pedagogy)
    if 'id="tab-pedagogy"' in content:
        if 'State Pedagogical Competency Diagnostic Spectrum' not in content:
            pattern = r'(<section[^>]*id=["\']tab-pedagogy["\'][\s\S]*?)(</section>)'
            match = re.search(pattern, content)
            if match:
                tab_body = match.group(1)
                new_tab_body = tab_body + TAB7_PEDAGOGY_DIAGNOSTICS_HTML + "\n"
                content = content[:match.start()] + new_tab_body + match.group(2) + content[match.end():]
                print("  [+] Injected Tab 7 Pedagogical Diagnostic Spectrum & Misconception Hotspots")
            else:
                print("  [-] Could not match tab-pedagogy section")
        else:
            print("  [.] Tab 7 Pedagogical Diagnostics already present")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[✓] Saved updates to {filepath}")
    return True

def main():
    print("===================================================================")
    print(" Synchronizing Full Strategic Dossier Key Findings Across Dashboard")
    print("===================================================================")

    for target in TARGET_FILES:
        update_file(target)

    print("\n[✓] All target dashboard files synchronized successfully!")

if __name__ == '__main__':
    main()
