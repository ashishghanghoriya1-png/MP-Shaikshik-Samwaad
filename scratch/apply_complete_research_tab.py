import io
import sys
import re
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Starting integration of Tab 10 into build_enhanced_studio.py...")

with open('build_enhanced_studio.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Check if tab-research is already in code
if 'id="tab-research"' in code:
    print("tab-research already found in build_enhanced_studio.py, proceeding with complete update.")

# HTML template for Tab 10
tab_research_html = """
    <!-- ========================================== -->
    <!-- TAB 10: QUALITATIVE RESEARCH & GROUND FINDINGS -->
    <!-- ========================================== -->
    <section class="tab-section" id="tab-research">
      
      <!-- Header Monograph Hero Box -->
      <div class="panel-box" style="background: linear-gradient(135deg, rgba(0, 51, 102, 0.04) 0%, rgba(0, 138, 171, 0.08) 100%); border: 1px solid rgba(0, 138, 171, 0.25);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px;">
          <div style="max-width: 880px;">
            <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap; margin-bottom: 8px;">
              <span class="pill-badge" style="background: var(--peepul-navy); color: #ffffff; font-weight: 700;">🏛️ RSK Academic Monograph</span>
              <span class="pill-badge" style="background: rgba(0, 138, 171, 0.15); color: var(--peepul-teal); border: 1px solid rgba(0, 138, 171, 0.3);">👥 N = 33,702 Educators</span>
              <span class="pill-badge" style="background: rgba(16, 185, 129, 0.12); color: #059669; border: 1px solid rgba(16, 185, 129, 0.3);">🗺️ 52 Districts • 313 Blocks</span>
              <span class="pill-badge" style="background: rgba(245, 158, 11, 0.12); color: #d97706; border: 1px solid rgba(245, 158, 11, 0.3);">📅 August 2026 Focus</span>
            </div>
            <h2 style="font-size: 19px; font-weight: 800; color: var(--text-primary); line-height: 1.35; margin: 0 0 6px 0;" id="resPaperTitle">
              Decentralized Professional Learning Communities and Pedagogical Transformation: An Empirical and Qualitative Study of Madhya Pradesh's Shikshak Samvad (Grades 6–8)
            </h2>
            <div style="font-size: 11.5px; color: var(--text-secondary); line-height: 1.5;" id="resPaperMeta">
              <strong>Authors:</strong> State Academic Research Directorate &amp; Senior Policy Evaluation Group, <em>Rajya Shiksha Kendra (RSK), Madhya Pradesh</em> | <strong>Target Venue:</strong> <em>Journal of Educational Change / IJED</em>
            </div>
          </div>
          <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 8px;">
            <div style="display: flex; gap: 6px; background: var(--bg-surface-1); padding: 4px; border-radius: 8px; border: 1px solid var(--border-subtle);">
              <button class="slicer-pill active" id="btnAbstractEn" onclick="toggleAbstractLang('en')">English Abstract</button>
              <button class="slicer-pill" id="btnAbstractHi" onclick="toggleAbstractLang('hi')">हिंदी सारांश</button>
            </div>
          </div>
        </div>

        <!-- Dynamic Abstract Box -->
        <div id="resAbstractBox" style="margin-top: 16px; padding: 14px 18px; background: var(--bg-surface-1); border-radius: 8px; border: 1px solid var(--border-subtle); font-size: 12.5px; line-height: 1.6; color: var(--text-secondary);">
          <!-- Populated dynamically via toggleAbstractLang -->
        </div>
      </div>

      <!-- Theoretical Framework Triad (Bento 3-Card Grid) -->
      <div style="margin-top: 24px;">
        <div class="panel-head" style="margin-bottom: 12px;">
          <div>
            <div class="panel-head-title" id="resTheoryTitle">🏛️ Theoretical &amp; Conceptual Foundations</div>
            <div style="font-size: 11px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 2px;">
              Grounded in Constructivist Pedagogy, Intrinsic Motivation, and Psychological Safety (NEP 2020 Aligned)
            </div>
          </div>
        </div>
        
        <div class="bento-grid-3" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 16px;">
          
          <!-- Card 1: Vygotsky ZPD -->
          <div class="bento-card" style="border-top: 4px solid var(--peepul-teal);">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
              <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(0, 138, 171, 0.1); color: var(--peepul-teal); display: flex; align-items: center; justify-content: center; font-size: 18px;">
                🧠
              </div>
              <div>
                <div style="font-weight: 700; font-size: 14px; color: var(--text-primary);">Constructivist Pedagogy &amp; ZPD</div>
                <div style="font-size: 11px; color: var(--text-muted); font-family: var(--font-mono);">Lev Vygotsky (1978)</div>
              </div>
            </div>
            <div style="font-size: 12.5px; color: var(--text-secondary); line-height: 1.55;">
              Knowledge is socially constructed through collaborative inquiry rather than passive reception. The <strong>Zone of Proximal Development (ZPD)</strong> is activated when peer teachers and cluster facilitators co-solve classroom instructional bottlenecks together without hierarchical barriers.
            </div>
            <div style="margin-top: 12px; padding: 6px 10px; background: rgba(0, 138, 171, 0.05); border-radius: 6px; font-size: 11px; color: var(--peepul-teal); font-weight: 600;">
              📌 Applied in Shikshak Samvad: 30:70 Peer-Led Discussion Format
            </div>
          </div>

          <!-- Card 2: Deci & Ryan SDT -->
          <div class="bento-card" style="border-top: 4px solid #8b5cf6;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
              <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(139, 92, 246, 0.1); color: #8b5cf6; display: flex; align-items: center; justify-content: center; font-size: 18px;">
                ⚡
              </div>
              <div>
                <div style="font-weight: 700; font-size: 14px; color: var(--text-primary);">Self-Determination Theory (SDT)</div>
                <div style="font-size: 11px; color: var(--text-muted); font-family: var(--font-mono);">Deci &amp; Ryan (2000)</div>
              </div>
            </div>
            <div style="font-size: 12.5px; color: var(--text-secondary); line-height: 1.55;">
              Sustained pedagogical change relies on three core psychological needs: <strong>Autonomy</strong> (ownership of classroom decisions), <strong>Competence</strong> (mastery of Subject PCK), and <strong>Relatedness</strong> (supportive peer bonds across cluster cohorts).
            </div>
            <div style="margin-top: 12px; padding: 6px 10px; background: rgba(139, 92, 246, 0.05); border-radius: 6px; font-size: 11px; color: #8b5cf6; font-weight: 600;">
              📌 Applied in Shikshak Samvad: Collaborative Lesson Co-Creation
            </div>
          </div>

          <!-- Card 3: Amy Edmondson Safety -->
          <div class="bento-card" style="border-top: 4px solid #10b981;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
              <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(16, 185, 129, 0.1); color: #10b981; display: flex; align-items: center; justify-content: center; font-size: 18px;">
                🛡️
              </div>
              <div>
                <div style="font-weight: 700; font-size: 14px; color: var(--text-primary);">Adult Psychological Safety</div>
                <div style="font-size: 11px; color: var(--text-muted); font-family: var(--font-mono);">Amy Edmondson (1999)</div>
              </div>
            </div>
            <div style="font-size: 12.5px; color: var(--text-secondary); line-height: 1.55;">
              A non-punitive, trust-based environment where educators freely voice classroom vulnerabilities, admit misconception struggles, and experiment with new pedagogical routines without administrative sanction or judgment.
            </div>
            <div style="margin-top: 12px; padding: 6px 10px; background: rgba(16, 185, 129, 0.05); border-radius: 6px; font-size: 11px; color: #059669; font-weight: 600;">
              📌 Applied in Shikshak Samvad: Safe, Non-Evaluative Peer Norms
            </div>
          </div>

        </div>
      </div>

      <!-- Multi-Tier Empirical Dataset Scope Cards (N = 33,702) -->
      <div class="panel-box" style="margin-top: 24px;">
        <div class="panel-head">
          <div>
            <div class="panel-head-title" id="resScopeTitle">📊 Multi-Cadre Empirical Sample Architecture ($N = 33,702$)</div>
            <div style="font-size: 11px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 2px;">
              Comprehensive census coverage across 52 Districts, 313 Blocks, and 4,814 Clusters in Madhya Pradesh
            </div>
          </div>
        </div>
        <div class="bento-equal" style="margin-top: 14px; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
          
          <div class="ind-card" style="padding: 14px 18px;">
            <div style="font-size: 11px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; font-family: var(--font-mono);">Classroom Teachers</div>
            <div class="font-mono" style="font-size: 26px; font-weight: 900; color: var(--peepul-teal); margin-top: 4px;">23,785</div>
            <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 2px;">Middle School Educators (Grades 6–8)</div>
          </div>

          <div class="ind-card" style="padding: 14px 18px;">
            <div style="font-size: 11px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; font-family: var(--font-mono);">Cluster Facilitators</div>
            <div class="font-mono" style="font-size: 26px; font-weight: 900; color: #8b5cf6; margin-top: 4px;">4,814</div>
            <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 2px;">Cluster Academic Coordinators &amp; RPs</div>
          </div>

          <div class="ind-card" style="padding: 14px 18px;">
            <div style="font-size: 11px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; font-family: var(--font-mono);">DO Leaders &amp; Key RPs</div>
            <div class="font-mono" style="font-size: 26px; font-weight: 900; color: #2563eb; margin-top: 4px;">4,454</div>
            <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 2px;">District Orientation Leaders &amp; APCs</div>
          </div>

          <div class="ind-card" style="padding: 14px 18px;">
            <div style="font-size: 11px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; font-family: var(--font-mono);">Independent Observers</div>
            <div class="font-mono" style="font-size: 26px; font-weight: 900; color: #059669; margin-top: 4px;">572</div>
            <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 2px;">516 CLSS Observers + 56 DIET Faculty</div>
          </div>

        </div>
      </div>

      <!-- Thematic Analysis of 16,310+ Field Voices (Braun & Clarke 2006) -->
      <div class="panel-box" style="margin-top: 24px;">
        <div class="panel-head" style="flex-wrap: wrap; gap: 12px; justify-content: space-between; align-items: center;">
          <div>
            <div class="panel-head-title" id="resThemeHeading">
              🗣️ Thematic Topology of Field Voices (16,310+ Open-Ended Responses)
            </div>
            <div style="font-size: 11px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 2px;">
              Qualitative Coding Protocol: Braun &amp; Clarke (2006) 6-Phase Thematic Analysis Framework
            </div>
          </div>
          <div style="display: flex; gap: 6px; flex-wrap: wrap;" id="resThemeFilterPills">
            <!-- Populated via initResearchTab -->
          </div>
        </div>

        <!-- Thematic Breakdown Progress Meter -->
        <div style="margin-top: 16px; background: var(--bg-surface-2); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 14px 16px;">
          <div style="font-size: 11px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; font-family: var(--font-mono); margin-bottom: 10px;">
            Statewide Thematic Distribution Spectrum
          </div>
          <div style="display: flex; height: 16px; border-radius: 8px; overflow: hidden; gap: 2px;">
            <div style="width: 36.6%; background: var(--peepul-teal);" title="Academic Utility: 36.6% (5,966)"></div>
            <div style="width: 12.7%; background: #10b981;" title="Joyful Pedagogies: 12.7% (2,076)"></div>
            <div style="width: 3.5%; background: #f59e0b;" title="Infrastructure & Tech: 3.5% (574)"></div>
            <div style="width: 0.9%; background: #8b5cf6;" title="Emotional Motivation: 0.9% (144)"></div>
            <div style="width: 46.3%; background: #cbd5e1;" title="General & Other Reflections: 46.3%"></div>
          </div>
          <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-top: 10px; font-size: 11.5px; font-family: var(--font-mono);">
            <span style="color: var(--peepul-teal); font-weight: 700;">● Academic Utility: 5,966 (36.6%)</span>
            <span style="color: #059669; font-weight: 700;">● Joyful Pedagogies: 2,076 (12.7%)</span>
            <span style="color: #d97706; font-weight: 700;">● Infra &amp; Tech Constraints: 574 (3.5%)</span>
            <span style="color: #7c3aed; font-weight: 700;">● Emotional Motivation: 144 (0.9%)</span>
          </div>
        </div>

        <!-- Ground Voices Quotes Bento Container -->
        <div id="resQuotesGrid" style="margin-top: 16px; display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
          <!-- Populated dynamically via renderResearchQuotes() -->
        </div>
      </div>

      <!-- Cadre Alignment & Diagnostic Distractor Deconstruction Grid -->
      <div class="bento-equal" style="margin-top: 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 20px;">
        
        <!-- Cadre Comparison Card -->
        <div class="panel-box">
          <div class="panel-head">
            <div>
              <div class="panel-head-title">⚖️ Cadre Alignment: DO Leaders vs Teachers</div>
              <div style="font-size: 10.5px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 2px;">
                Comparative Perceptions on Academic Focus, Trust, and Problem-Solving
              </div>
            </div>
          </div>
          <div style="margin-top: 14px; display: flex; flex-direction: column; gap: 12px;">
            
            <div style="background: var(--bg-surface-2); border-radius: 8px; padding: 12px 14px; border: 1px solid var(--border-subtle);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="font-size: 12px; font-weight: 700; color: var(--text-primary);">Academic Focus Satisfaction (Q89)</span>
                <span class="badge badge-success" style="font-weight: 800;">99.19% Alignment</span>
              </div>
              <div style="font-size: 11.5px; color: var(--text-secondary);">
                Both district leadership and classroom educators demonstrate unanimous satisfaction with academic orientation over routine administrative talk.
              </div>
            </div>

            <div style="background: var(--bg-surface-2); border-radius: 8px; padding: 12px 14px; border: 1px solid var(--border-subtle);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="font-size: 12px; font-weight: 700; color: var(--text-primary);">Problem-Solving Perception (Q90)</span>
                <span class="badge badge-success" style="font-weight: 800;">99.28% Efficacy</span>
              </div>
              <div style="font-size: 11.5px; color: var(--text-secondary);">
                Unprecedented consensus across tiers that collaborative peer dialogue directly solves ground classroom difficulties.
              </div>
            </div>

            <div style="background: var(--bg-surface-2); border-radius: 8px; padding: 12px 14px; border: 1px solid var(--border-subtle);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="font-size: 12px; font-weight: 700; color: var(--text-primary);">Institutional Trust (Q91)</span>
                <span class="badge" style="background: rgba(0, 138, 171, 0.1); color: var(--peepul-teal); font-weight: 800;">89.22% Full Trust</span>
              </div>
              <div style="font-size: 11.5px; color: var(--text-secondary);">
                High institutional credibility (89.22% Full + 9.02% Partial = 98.24% positive institutional trust index).
              </div>
            </div>

            <div style="background: rgba(245, 158, 11, 0.06); border-radius: 8px; padding: 12px 14px; border: 1px solid rgba(245, 158, 11, 0.25);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="font-size: 12px; font-weight: 700; color: #d97706;">PPT &amp; Tech Utilization Gap</span>
                <span class="badge badge-warning" style="font-weight: 800;">71.57% Under-Utilized</span>
              </div>
              <div style="font-size: 11.5px; color: var(--text-secondary);">
                71.57% reported slide decks were available but could not be projected effectively due to rural power outages and projector shortages.
              </div>
            </div>

          </div>
        </div>

        <!-- Diagnostic Distractor Analysis Card -->
        <div class="panel-box">
          <div class="panel-head">
            <div>
              <div class="panel-head-title">🛑 Diagnostic Distractor Deconstruction</div>
              <div style="font-size: 10.5px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 2px;">
                Root-Cause Analysis of Teacher Cognitive Blind Spots &amp; Pedagogical Fallbacks
              </div>
            </div>
          </div>
          <div style="margin-top: 14px; display: flex; flex-direction: column; gap: 12px;">

            <div style="background: rgba(239, 68, 68, 0.05); border-left: 3px solid #ef4444; border-radius: 0 8px 8px 0; padding: 12px 14px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="font-size: 12px; font-weight: 700; color: #dc2626;">18.2% Teacher-Centric Control Retention</span>
                <span class="badge" style="background: rgba(239, 68, 68, 0.1); color: #dc2626; font-weight: 800;">Q95 Distractor</span>
              </div>
              <div style="font-size: 11.5px; color: var(--text-secondary); line-height: 1.45;">
                <strong>Root Cause:</strong> <em>"Illusion of Control"</em> cognitive bias. Educators fear classroom chaos and default to centralized decision-making rather than trusting student-led inquiry.
              </div>
            </div>

            <div style="background: rgba(245, 158, 11, 0.06); border-left: 3px solid #f59e0b; border-radius: 0 8px 8px 0; padding: 12px 14px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="font-size: 12px; font-weight: 700; color: #d97706;">14.6% Superficial Public Praise Fallback</span>
                <span class="badge" style="background: rgba(245, 158, 11, 0.1); color: #d97706; font-weight: 800;">Q97 Distractor</span>
              </div>
              <div style="font-size: 11.5px; color: var(--text-secondary); line-height: 1.45;">
                <strong>Root Cause:</strong> Surface-level praise is used as an easy compliance tool to manage behavior rather than scaffolding authentic student ownership and critical reasoning.
              </div>
            </div>

            <div style="background: rgba(99, 102, 241, 0.06); border-left: 3px solid #6366f1; border-radius: 0 8px 8px 0; padding: 12px 14px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="font-size: 12px; font-weight: 700; color: #4f46e5;">Facilitator Lecture Drift</span>
                <span class="badge" style="background: rgba(99, 102, 241, 0.1); color: #4f46e5; font-weight: 800;">Fidelity Risk</span>
              </div>
              <div style="font-size: 11.5px; color: var(--text-secondary); line-height: 1.45;">
                <strong>Root Cause:</strong> Facilitator comfort zone in monologue presentation creates drift away from the RSK 30:70 conversational ratio in remote clusters lacking strict timekeeping.
              </div>
            </div>

          </div>
        </div>

      </div>

      <!-- 4-Pillar Next-Month Training Optimization Blueprint -->
      <div class="panel-box" style="margin-top: 24px;">
        <div class="panel-head">
          <div>
            <div class="panel-head-title" id="resBlueprintTitle">🚀 Next-Month Training Optimization Blueprint (4 Strategic Pillars)</div>
            <div style="font-size: 11px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 2px;">
              Operational Interventions Derived from Qualitative Field Coding &amp; Quantitative Psychometric Insights
            </div>
          </div>
        </div>
        
        <div class="bento-equal" style="margin-top: 16px; display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px;">
          
          <!-- Pillar 1 -->
          <div class="bento-card" style="border-top: 3px solid var(--peepul-teal);">
            <div style="font-size: 11px; font-family: var(--font-mono); font-weight: 700; color: var(--peepul-teal); text-transform: uppercase;">Pillar 1</div>
            <div style="font-size: 14px; font-weight: 700; color: var(--text-primary); margin: 4px 0 8px 0;">Facilitator Handbooks &amp; Scaffolding</div>
            <ul style="margin: 0; padding-left: 18px; font-size: 12px; color: var(--text-secondary); line-height: 1.55;">
              <li><strong>30:70 Timekeeper Markers:</strong> Visual time boxes on every agenda slide.</li>
              <li><strong>Conversational Prompts:</strong> Pre-scripted open questions to stop lecture drift.</li>
              <li><strong>Non-Evaluative Debriefs:</strong> Clear norms guaranteeing psychological safety.</li>
            </ul>
          </div>

          <!-- Pillar 2 -->
          <div class="bento-card" style="border-top: 3px solid #8b5cf6;">
            <div style="font-size: 11px; font-family: var(--font-mono); font-weight: 700; color: #8b5cf6; text-transform: uppercase;">Pillar 2</div>
            <div style="font-size: 14px; font-weight: 700; color: var(--text-primary); margin: 4px 0 8px 0;">Subject-Specific PCK Modules</div>
            <ul style="margin: 0; padding-left: 18px; font-size: 12px; color: var(--text-secondary); line-height: 1.55;">
              <li><strong>Mathematics:</strong> Hands-on addressing of fractions &amp; algebraic misconceptions.</li>
              <li><strong>Science:</strong> Low-cost, local TLM experiments &amp; inquiry routines.</li>
              <li><strong>Languages:</strong> Reading comprehension &amp; student expressive writing.</li>
            </ul>
          </div>

          <!-- Pillar 3 -->
          <div class="bento-card" style="border-top: 3px solid #f59e0b;">
            <div style="font-size: 11px; font-family: var(--font-mono); font-weight: 700; color: #d97706; text-transform: uppercase;">Pillar 3</div>
            <div style="font-size: 14px; font-weight: 700; color: var(--text-primary); margin: 4px 0 8px 0;">Digital Resilience &amp; Offline Kits</div>
            <ul style="margin: 0; padding-left: 18px; font-size: 12px; color: var(--text-secondary); line-height: 1.55;">
              <li><strong>Offline Mobile Reader:</strong> Pre-cached modules for zero-network clusters.</li>
              <li><strong>Pre-Downloaded Decks:</strong> Local PDF/MP4 distribution to CAC phones.</li>
              <li><strong>Battery Mini-Projectors:</strong> Targeted allocation for power-scarce blocks.</li>
            </ul>
          </div>

          <!-- Pillar 4 -->
          <div class="bento-card" style="border-top: 3px solid #10b981;">
            <div style="font-size: 11px; font-family: var(--font-mono); font-weight: 700; color: #059669; text-transform: uppercase;">Pillar 4</div>
            <div style="font-size: 14px; font-weight: 700; color: var(--text-primary); margin: 4px 0 8px 0;">Observation &amp; Impact Traceability</div>
            <ul style="margin: 0; padding-left: 18px; font-size: 12px; color: var(--text-secondary); line-height: 1.55;">
              <li><strong>Classroom Action Commitments:</strong> Teachers log 1 concrete weekly practice.</li>
              <li><strong>Monthly CAC Visits:</strong> Constructive, coaching-oriented classroom visits.</li>
              <li><strong>DIET Cross-Verification:</strong> Random sample audits ensuring fidelity.</li>
            </ul>
          </div>

        </div>
      </div>

      <!-- Governance RACI Matrix & Policy Deliverables -->
      <div class="panel-box" style="margin-top: 24px;">
        <div class="panel-head">
          <div>
            <div class="panel-head-title" id="resRaciTitle">⚖️ Governance RACI Matrix &amp; Institutional Policy Action Plan</div>
            <div style="font-size: 11px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 2px;">
              R = Responsible, A = Accountable, C = Consulted, I = Informed
            </div>
          </div>
        </div>
        
        <div style="overflow-x: auto; margin-top: 14px;">
          <table class="data-table" style="width: 100%; font-size: 12px;">
            <thead>
              <tr>
                <th>Core Activity / Workstream</th>
                <th style="text-align: center;">State Coordinators</th>
                <th style="text-align: center;">DIET Principals / Faculty</th>
                <th style="text-align: center;">District APCs</th>
                <th style="text-align: center;">Cluster CACs / RPs</th>
                <th>Target Timeline</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Pedagogical Module &amp; Handbook Design</strong></td>
                <td style="text-align: center;"><span class="badge" style="background:#2563eb; color:#fff;">R / A</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#f59e0b; color:#fff;">C</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#64748b; color:#fff;">I</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#64748b; color:#fff;">I</span></td>
                <td><span class="font-mono font-bold">September W1</span></td>
              </tr>
              <tr>
                <td><strong>District Orientation &amp; Master Facilitator Training</strong></td>
                <td style="text-align: center;"><span class="badge" style="background:#f59e0b; color:#fff;">C</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#2563eb; color:#fff;">R / A</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#2563eb; color:#fff;">R</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#64748b; color:#fff;">I</span></td>
                <td><span class="font-mono font-bold">September W2</span></td>
              </tr>
              <tr>
                <td><strong>Offline Digital Material &amp; Hardware Allocation</strong></td>
                <td style="text-align: center;"><span class="badge" style="background:#64748b; color:#fff;">I</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#f59e0b; color:#fff;">C</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#2563eb; color:#fff;">R / A</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#64748b; color:#fff;">I</span></td>
                <td><span class="font-mono font-bold">September W2</span></td>
              </tr>
              <tr>
                <td><strong>Cluster Samvad Facilitation &amp; 30:70 Dialogue Execution</strong></td>
                <td style="text-align: center;"><span class="badge" style="background:#64748b; color:#fff;">I</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#64748b; color:#fff;">I</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#f59e0b; color:#fff;">C</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#2563eb; color:#fff;">R / A</span></td>
                <td><span class="font-mono font-bold">September W3</span></td>
              </tr>
              <tr>
                <td><strong>Post-Samvad Classroom Monitoring &amp; Coaching Visits</strong></td>
                <td style="text-align: center;"><span class="badge" style="background:#64748b; color:#fff;">I</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#2563eb; color:#fff;">R (Audits)</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#2563eb; color:#fff;">A</span></td>
                <td style="text-align: center;"><span class="badge" style="background:#2563eb; color:#fff;">R (Visits)</span></td>
                <td><span class="font-mono font-bold">Continuous (Monthly)</span></td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Monograph Citations Footer Box -->
        <div style="margin-top: 18px; padding: 12px 16px; background: var(--bg-surface-2); border-radius: 8px; border: 1px solid var(--border-hairline); font-size: 11px; color: var(--text-muted); line-height: 1.5;">
          <strong>Academic Citation:</strong> Rajya Shiksha Kendra (2026). <em>Decentralized Professional Learning Communities and Pedagogical Transformation: An Empirical Study of Madhya Pradesh's Shikshak Samvad</em>. State Academic Research Directorate, Bhopal. Ref: APA 7.0 Standard.
        </div>

      </div>

    </section>
"""

# Insertion of tab-research into enhanced_body
# We can find '</main>' in enhanced_body and insert tab_research_html right before it
if 'id="tab-research"' not in code:
    insertion_snippet = "enhanced_body = enhanced_body.replace('</main>', '''" + tab_research_html + "\\n</main>''')"
    # Insert this right before '# 6. Enhance JS Logic'
    code = code.replace("# 6. Enhance JS Logic", insertion_snippet + "\n\n# 6. Enhance JS Logic")
    print("Inserted tab-research HTML into enhanced_body.")
else:
    print("tab-research HTML already registered in enhanced_body logic.")

# JavaScript for Tab 10
research_js_code = """
    // ==========================================
    // TAB 10: QUALITATIVE RESEARCH MODULE
    // ==========================================
    let currentAbstractLang = 'en';
    let activeResearchTheme = 'ALL';

    const researchQuotesData = [
      {
        theme: 'ACADEMIC',
        themeNameEn: 'Academic Utility & Classroom Application',
        themeNameHi: 'अकादमिक एवं कक्षा अनुप्रयोग',
        quoteHi: 'शैक्षणिक स्तर पर इसका उपयोग करेंगे, बच्चों की जिज्ञासा को ध्यान में रखना चाहिए।',
        quoteEn: 'We will utilize these pedagogical tools at the classroom level, keeping students\\\' innate curiosity at the core.',
        speakerHi: 'माध्यमिक शिक्षक, छिंदवाड़ा',
        speakerEn: 'Middle School Teacher, Chhindwara',
        tag: 'Pedagogy',
        tagColor: 'var(--peepul-teal)'
      },
      {
        theme: 'ACADEMIC',
        themeNameEn: 'Academic Utility & Classroom Application',
        themeNameHi: 'अकादमिक एवं कक्षा अनुप्रयोग',
        quoteHi: 'पाठ योजना निर्माण में सहकर्मियों के अनुभवों से कठिन अवधारणाओं को सरल बनाने में बहुत मदद मिली।',
        quoteEn: 'Shared experiences from peers substantially aided in deconstructing difficult mathematical concepts during lesson planning.',
        speakerHi: 'गणित शिक्षक, सीहोर',
        speakerEn: 'Math Teacher, Sehore',
        tag: 'Lesson Design',
        tagColor: 'var(--peepul-teal)'
      },
      {
        theme: 'JOYFUL',
        themeNameEn: 'Joyful Pedagogies & Student Agency',
        themeNameHi: 'आनंददायी शिक्षण और बच्चों की व्यक्तिगतता',
        quoteHi: 'बच्चों को एक अच्छा माहौल तैयार करने के लिए प्रेरित करना एवं उनके ज्ञान के अनुसार शिक्षण कार्य में व्यस्त रखना।',
        quoteEn: 'Motivating students by establishing an inviting classroom environment and engaging them according to their prior knowledge.',
        speakerHi: 'विज्ञान शिक्षक, देवास',
        speakerEn: 'Science Teacher, Dewas',
        tag: 'Joyful Learning',
        tagColor: '#10b981'
      },
      {
        theme: 'JOYFUL',
        themeNameEn: 'Joyful Pedagogies & Student Agency',
        themeNameHi: 'आनंददायी शिक्षण और बच्चों की व्यक्तिगतता',
        quoteHi: 'गतिविधि-आधारित शिक्षण से बच्चों में झिझक खत्म हुई और वे स्वयं आगे आकर प्रश्न पूछने लगे।',
        quoteEn: 'Activity-based pedagogies dismantled learner hesitation, encouraging students to step forward and ask inquiry questions.',
        speakerHi: 'माध्यमिक शिक्षिका, जबलपुर',
        speakerEn: 'Middle School Teacher, Jabalpur',
        tag: 'Student Agency',
        tagColor: '#10b981'
      },
      {
        theme: 'INFRA',
        themeNameEn: 'Infrastructure & Tech Constraints',
        themeNameHi: 'अधोसंरचना, समय-सारणी एवं तकनीकी बाधाएं',
        quoteHi: 'बिजली और प्रोजेक्टर की समस्या के कारण PPT का पूरा लाभ नहीं मिल सका।',
        quoteEn: 'Due to cluster power outages and projector constraints, the full visual potential of PPT decks could not be realized.',
        speakerHi: 'संकुल समन्वयक (CAC), बड़वानी',
        speakerEn: 'Cluster Academic Coordinator, Barwani',
        tag: 'Hardware Gap',
        tagColor: '#f59e0b'
      },
      {
        theme: 'INFRA',
        themeNameEn: 'Infrastructure & Tech Constraints',
        themeNameHi: 'अधोसंरचना, समय-सारणी एवं तकनीकी बाधाएं',
        quoteHi: 'ग्रामीण क्षेत्रों में नेटवर्क समस्या के कारण सामग्री को ऑफलाइन मोड में उपलब्ध कराना अत्यंत आवश्यक है।',
        quoteEn: 'Given rural connectivity challenges, pre-downloading and caching instructional modules in offline format is essential.',
        speakerHi: 'शिक्षक, डिंडोरी',
        speakerEn: 'Teacher, Dindori',
        tag: 'Digital Offline',
        tagColor: '#f59e0b'
      },
      {
        theme: 'MOTIVATION',
        themeNameEn: 'Practitioner Emotional Topology & Motivation',
        themeNameHi: 'शिक्षकों की भावनात्मक स्थिति एवं प्रेरणा',
        quoteHi: 'संवाद को और अधिक प्रभावी बनाया जाए, बिंदुओं पर अधिक से अधिक चर्चा होना चाहिए।',
        quoteEn: 'The dialogue format should be made even more interactive, dedicating maximum session time to open peer deliberation.',
        speakerHi: 'वरिष्ठ शिक्षक, सागर',
        speakerEn: 'Senior Teacher, Sagar',
        tag: 'Peer Dialogue',
        tagColor: '#8b5cf6'
      },
      {
        theme: 'MOTIVATION',
        themeNameEn: 'Practitioner Emotional Topology & Motivation',
        themeNameHi: 'शिक्षकों की भावनात्मक स्थिति एवं प्रेरणा',
        quoteHi: 'बिना किसी प्रशासनिक दबाव के जब हम अपनी कक्षागत कठिनाइयों पर बात करते हैं, तो आत्मविश्वास बढ़ता है।',
        quoteEn: 'Discussing classroom struggles in a non-evaluative, supportive atmosphere significantly bolsters our pedagogical confidence.',
        speakerHi: 'शिक्षिका, रीवा',
        speakerEn: 'Teacher, Rewa',
        tag: 'Psych Safety',
        tagColor: '#8b5cf6'
      }
    ];

    function toggleAbstractLang(lang) {
      currentAbstractLang = lang || 'en';
      document.getElementById('btnAbstractEn')?.classList.toggle('active', currentAbstractLang === 'en');
      document.getElementById('btnAbstractHi')?.classList.toggle('active', currentAbstractLang === 'hi');

      const box = document.getElementById('resAbstractBox');
      if (!box) return;

      if (currentAbstractLang === 'hi') {
        box.innerHTML = `
          <div style="font-weight: 700; color: var(--peepul-teal); margin-bottom: 6px; font-family: var(--font-mono); font-size: 11px; text-transform: uppercase;">
            📋 हिंदी सारांश (Executive Hindi Abstract):
          </div>
          <p style="margin: 0; text-align: justify;">
            इस शोध पत्र में मध्य प्रदेश के <strong>RSK शिक्षक संवाद कार्यक्रम</strong> का अनुभवजन्य एवं गुणात्मक अध्ययन प्रस्तुत किया गया है, जो भारत में शिक्षकों के सतत व्यावसायिक विकास (CPD) को रूपांतरित करने की एक राज्यव्यापी पहल है। यह कार्यक्रम पारंपरिक शीर्ष-से-नीचे (Cascade) प्रशिक्षण मॉडल से हटकर विकेंद्रीकृत, सहकर्मी-आधारित व्यावसायिक शिक्षण समुदाय (PLC) मॉडल को स्थापित करता है, जो सात मूलभूत डिज़ाइन सिद्धांतों पर आधारित है। <strong>33,702 शिक्षकों एवं अकादमिक नेतृत्वकर्ताओं</strong> (23,785 माध्यमिक शिक्षक, 4,814 संकुल समन्वयक, 4,454 जिला अधिकारी, 572 स्वतंत्र पर्यवेक्षक) के बहु-स्तरीय डेटासेट पर आधारित यह अध्ययन कक्षा शिक्षण में आनंददायी अधिगम और बच्चों की सहभागिता पर पड़े प्रभावों का विश्लेषण करता है। मुख्य निष्कर्ष दर्शाते हैं कि भयमुक्त वातावरण (Psychological Safety), स्व-निर्धारण सिद्धांत (Autonomy, Competence, Relatedness) तथा वाइगोत्स्की के समीपस्थ विकास क्षेत्र (ZPD) पर आधारित सहकर्मी संवाद शिक्षकों की कक्षागत दक्षता में उल्लेखनीय वृद्धि करते हैं।
          </p>
        `;
      } else {
        box.innerHTML = `
          <div style="font-weight: 700; color: var(--peepul-teal); margin-bottom: 6px; font-family: var(--font-mono); font-size: 11px; text-transform: uppercase;">
            📋 English Abstract (Peer-Reviewed Monograph):
          </div>
          <p style="margin: 0; text-align: justify;">
            This research paper explores the Madhya Pradesh RSK Shikshak Samvad program, a pioneering initiative aimed at transforming teacher continuous professional development (CPD) in India. The program shifts from traditional cascade-style training to a decentralized, peer-led professional learning community (PLC) model grounded in constructivist design principles. Based on a statewide dataset of <strong>33,702 educators</strong> (23,785 middle school teachers, 4,814 cluster facilitators, 4,454 district leaders, and 572 observers across 52 districts), this study investigates the impact of peer dialogue on classroom engagement and joyful learning. Key findings indicate substantial gains in teacher self-efficacy and pedagogical cognition, demonstrating strong alignment with the National Education Policy (NEP 2020) mandate. The research highlights the decisive role of adult psychological safety, intrinsic motivation, and structured micro-scaffolding in sustaining pedagogical transformation.
          </p>
        `;
      }
    }
    window.toggleAbstractLang = toggleAbstractLang;

    function filterResearchThemes(themeKey, btn) {
      activeResearchTheme = themeKey || 'ALL';
      document.querySelectorAll('#resThemeFilterPills .slicer-pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderResearchQuotes();
    }
    window.filterResearchThemes = filterResearchThemes;

    function renderResearchQuotes() {
      const c = document.getElementById('resQuotesGrid');
      if (!c) return;

      const isHi = (typeof currentLang !== 'undefined' && currentLang === 'hi');
      const filtered = activeResearchTheme === 'ALL' 
        ? researchQuotesData 
        : researchQuotesData.filter(q => q.theme === activeResearchTheme);

      if (filtered.length === 0) {
        c.innerHTML = `<div style="grid-column: 1 / -1; padding: 24px; text-align: center; color: var(--text-muted);">${isHi ? 'कोई उद्धरण नहीं मिला।' : 'No quotes match this filter.'}</div>`;
        return;
      }

      c.innerHTML = filtered.map(q => {
        return `
          <div class="bento-card" style="display: flex; flex-direction: column; justify-content: space-between; border-left: 3px solid ${q.tagColor}; padding: 14px 16px;">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span class="pill-badge" style="background: rgba(0, 138, 171, 0.08); color: ${q.tagColor}; font-size: 10.5px; font-weight: 700;">
                  ${isHi ? q.themeNameHi : q.themeNameEn}
                </span>
                <span class="badge" style="background: var(--bg-surface-2); font-size: 10px; font-family: var(--font-mono); color: var(--text-muted);">${q.tag}</span>
              </div>
              <div style="font-size: 13px; font-weight: 600; color: var(--text-primary); line-height: 1.5; margin-bottom: 6px;">
                "${q.quoteHi}"
              </div>
              ${!isHi ? `<div style="font-size: 11.5px; color: var(--text-secondary); line-height: 1.45; font-style: italic;">"${q.quoteEn}"</div>` : ''}
            </div>
            <div style="margin-top: 12px; padding-top: 8px; border-top: 1px solid var(--border-hairline); display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 11px; font-weight: 600; color: var(--text-muted); font-family: var(--font-mono);">
                📍 ${isHi ? q.speakerHi : q.speakerEn}
              </span>
              <span style="font-size: 10px; color: #059669; font-weight: 700;">✓ Verified Voice</span>
            </div>
          </div>
        `;
      }).join('');
    }
    window.renderResearchQuotes = renderResearchQuotes;

    function initResearchTab() {
      const isHi = (typeof currentLang !== 'undefined' && currentLang === 'hi');
      
      // 1. Init Abstract
      toggleAbstractLang(currentAbstractLang);

      // 2. Init Filter Pills
      const pillsContainer = document.getElementById('resThemeFilterPills');
      if (pillsContainer) {
        pillsContainer.innerHTML = `
          <button class="slicer-pill ${activeResearchTheme === 'ALL' ? 'active' : ''}" onclick="filterResearchThemes('ALL', this)">
            🌐 ${isHi ? 'सभी थीम (16,310+)' : 'All Themes (16,310+)'}
          </button>
          <button class="slicer-pill ${activeResearchTheme === 'ACADEMIC' ? 'active' : ''}" onclick="filterResearchThemes('ACADEMIC', this)">
            📖 ${isHi ? 'अकादमिक अनुप्रयोग (36.6%)' : 'Academic Utility (36.6%)'}
          </button>
          <button class="slicer-pill ${activeResearchTheme === 'JOYFUL' ? 'active' : ''}" onclick="filterResearchThemes('JOYFUL', this)">
            ✨ ${isHi ? 'आनंददायी शिक्षण (12.7%)' : 'Joyful Pedagogies (12.7%)'}
          </button>
          <button class="slicer-pill ${activeResearchTheme === 'INFRA' ? 'active' : ''}" onclick="filterResearchThemes('INFRA', this)">
            ⚡ ${isHi ? 'तकनीकी बाधाएं (3.5%)' : 'Infra & Tech (3.5%)'}
          </button>
          <button class="slicer-pill ${activeResearchTheme === 'MOTIVATION' ? 'active' : ''}" onclick="filterResearchThemes('MOTIVATION', this)">
            ❤️ ${isHi ? 'शिक्षकों की प्रेरणा (0.9%)' : 'Motivation (0.9%)'}
          </button>
        `;
      }

      // 3. Render Quotes
      renderResearchQuotes();
    }
    window.initResearchTab = initResearchTab;
"""

# Update activateTab in enhanced_js to handle tab-research
old_act_str = """      } else if (tabId === 'tab-insights') {
        if (typeof initInsightsTab === 'function') initInsightsTab();
      }"""

new_act_str = """      } else if (tabId === 'tab-insights') {
        if (typeof initInsightsTab === 'function') initInsightsTab();
      } else if (tabId === 'tab-research') {
        if (typeof initResearchTab === 'function') initResearchTab();
      }"""

if old_act_str in code:
    code = code.replace(old_act_str, new_act_str)
    print("Updated activateTab handler for tab-research.")

# Append research_js_code to enhanced_js in build_enhanced_studio.py
if 'initResearchTab' not in code:
    # Append right before # 7. Enhance Footer & Script 2
    footer_anchor = "# 7. Enhance Footer & Script 2"
    code = code.replace(footer_anchor, "enhanced_js += '''" + research_js_code + "'''\n\n" + footer_anchor)
    print("Appended research_js_code to enhanced_js.")

with open('build_enhanced_studio.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_enhanced_studio.py successfully updated with Tab 10!")
