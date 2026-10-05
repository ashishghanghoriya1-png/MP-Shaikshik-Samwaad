import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('build_enhanced_studio.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Remove any raw HTML that leaked into python source
pos_leak = code.find('<!-- ======================================================== -->\n    <!-- CRO GROUND CLASSROOM REALITY')
if pos_leak != -1:
    pos_leak_end = code.find('</div>\n\n    </div>\n', pos_leak)
    if pos_leak_end != -1:
        code = code[:pos_leak] + code[pos_leak_end+18:]
        print("Removed leaked HTML string from build_enhanced_studio.py.")

cro_html_str = r"""
    <!-- ======================================================== -->
    <!-- CRO GROUND CLASSROOM REALITY & PEDAGOGY TRIANGULATION -->
    <!-- ======================================================== -->
    <div class="panel-box" style="margin-top: 24px;">
      <div class="panel-head" style="flex-wrap: wrap; gap: 12px; justify-content: space-between; align-items: center;">
        <div>
          <div class="panel-head-title" id="croPanelHeading">
            🏫 Ground Classroom Reality &amp; Pedagogy Triangulation (CRO Dataset)
          </div>
          <div id="croPanelRef" style="font-size: 10.5px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 2px;">
            [Ref: <em>Analysis_CRO Data_ MP CPD_ 25-26.xlsx</em> | <strong>411 In-Person Classroom Audits</strong> across 55 Districts &amp; 251 Blocks | Grades 6–8]
          </div>
        </div>
        <div style="display: flex; gap: 8px; align-items: center;">
          <span class="pill-badge" style="background: rgba(0, 138, 171, 0.12); color: var(--peepul-teal); font-weight: 700; border: 1px solid rgba(0, 138, 171, 0.3);">
            411 Audited Classrooms
          </span>
          <span class="pill-badge" style="background: rgba(16, 185, 129, 0.12); color: #059669; font-weight: 700; border: 1px solid rgba(16, 185, 129, 0.3);">
            8 Core Techniques
          </span>
        </div>
      </div>

      <!-- Triangulation Spectrum Banner -->
      <div style="margin-top: 14px; background: linear-gradient(135deg, rgba(0, 51, 102, 0.04) 0%, rgba(0, 138, 171, 0.06) 100%); border: 1px solid rgba(0, 138, 171, 0.2); border-radius: 8px; padding: 14px 18px;">
        <div style="font-size: 11px; font-family: var(--font-mono); font-weight: 700; color: var(--peepul-navy); text-transform: uppercase; margin-bottom: 6px;">
          🎯 The 4-Stage CPD Triangulation Funnel: Where Does Pedagogical Transmission Stall?
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 10px;">
          <div style="background: var(--bg-surface-1); padding: 10px 12px; border-radius: 6px; border: 1px solid var(--border-subtle); text-align: center;">
            <div style="font-size: 10.5px; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">1. Training Awareness</div>
            <div class="font-mono" style="font-size: 22px; font-weight: 900; color: var(--peepul-teal); margin: 2px 0;">94.2%</div>
            <div style="font-size: 11px; color: var(--text-secondary);">Recall of Core Principles (Q86)</div>
          </div>
          <div style="background: var(--bg-surface-1); padding: 10px 12px; border-radius: 6px; border: 1px solid var(--border-subtle); text-align: center;">
            <div style="font-size: 10.5px; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">2. Facilitator Perception</div>
            <div class="font-mono" style="font-size: 22px; font-weight: 900; color: #8b5cf6; margin: 2px 0;">91.4%</div>
            <div style="font-size: 11px; color: var(--text-secondary);">Self-Reported 30:70 Dialogue</div>
          </div>
          <div style="background: var(--bg-surface-1); padding: 10px 12px; border-radius: 6px; border: 1px solid var(--border-subtle); text-align: center;">
            <div style="font-size: 10.5px; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">3. Observer Live Audit</div>
            <div class="font-mono" style="font-size: 22px; font-weight: 900; color: #f59e0b; margin: 2px 0;">64.2%</div>
            <div style="font-size: 11px; color: var(--text-secondary);">Observed 30:70 Live Ratio</div>
          </div>
          <div style="background: var(--bg-surface-1); padding: 10px 12px; border-radius: 6px; border: 1px solid var(--border-subtle); text-align: center;">
            <div style="font-size: 10.5px; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">4. Classroom Peer Work</div>
            <div class="font-mono" style="font-size: 22px; font-weight: 900; color: #ef4444; margin: 2px 0;">18.4%</div>
            <div style="font-size: 11px; color: var(--text-secondary);">Actual Think-Pair-Share (CRO)</div>
          </div>
        </div>
      </div>

      <!-- 8 Pedagogical Techniques Adoption Grid -->
      <div style="margin-top: 20px;">
        <div style="font-size: 12px; font-weight: 700; color: var(--text-primary); text-transform: uppercase; font-family: var(--font-mono); margin-bottom: 12px;">
          📊 Adoption Rate of 8 Core Pedagogical Techniques in Observed Classrooms (N = 411)
        </div>
        <div class="bento-grid-4" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px;">
          
          <div class="bento-card" style="border-left: 3px solid #059669;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: 700; font-size: 13px; color: var(--text-primary);">🪝 Hook Activity</span>
              <span class="font-mono" style="font-size: 18px; font-weight: 900; color: #059669;">94.1%</span>
            </div>
            <div class="progress-bar-bg" style="height: 6px; margin: 8px 0; background: var(--bg-surface-2); border-radius: 4px; overflow: hidden;">
              <div style="width: 94.1%; height: 100%; background: #059669;"></div>
            </div>
            <div style="font-size: 11px; color: var(--text-muted);">High teacher mastery in engaging topic hooks at session commencement.</div>
          </div>

          <div class="bento-card" style="border-left: 3px solid #059669;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: 700; font-size: 13px; color: var(--text-primary);">❓ Check for Understanding</span>
              <span class="font-mono" style="font-size: 18px; font-weight: 900; color: #059669;">80.0%</span>
            </div>
            <div class="progress-bar-bg" style="height: 6px; margin: 8px 0; background: var(--bg-surface-2); border-radius: 4px; overflow: hidden;">
              <div style="width: 80.0%; height: 100%; background: #059669;"></div>
            </div>
            <div style="font-size: 11px; color: var(--text-muted);">Formative checks during mid-lesson transitions to gauge basic comprehension.</div>
          </div>

          <div class="bento-card" style="border-left: 3px solid #f59e0b;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: 700; font-size: 13px; color: var(--text-primary);">🎯 Cold Calling</span>
              <span class="font-mono" style="font-size: 18px; font-weight: 900; color: #d97706;">42.2%</span>
            </div>
            <div class="progress-bar-bg" style="height: 6px; margin: 8px 0; background: var(--bg-surface-2); border-radius: 4px; overflow: hidden;">
              <div style="width: 42.2%; height: 100%; background: #d97706;"></div>
            </div>
            <div style="font-size: 11px; color: var(--text-muted);">Calling on quiet learners to equalize participation across back benches.</div>
          </div>

          <div class="bento-card" style="border-left: 3px solid #f59e0b;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: 700; font-size: 13px; color: var(--text-primary);">💬 Constructive Feedback</span>
              <span class="font-mono" style="font-size: 18px; font-weight: 900; color: #d97706;">36.4%</span>
            </div>
            <div class="progress-bar-bg" style="height: 6px; margin: 8px 0; background: var(--bg-surface-2); border-radius: 4px; overflow: hidden;">
              <div style="width: 36.4%; height: 100%; background: #d97706;"></div>
            </div>
            <div style="font-size: 11px; color: var(--text-muted);">Specific, actionable correction rather than generic praise/scolding.</div>
          </div>

          <div class="bento-card" style="border-left: 3px solid #ef4444;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: 700; font-size: 13px; color: var(--text-primary);">🤝 Think-Pair-Share (TPS)</span>
              <span class="font-mono" style="font-size: 18px; font-weight: 900; color: #ef4444;">18.4%</span>
            </div>
            <div class="progress-bar-bg" style="height: 6px; margin: 8px 0; background: var(--bg-surface-2); border-radius: 4px; overflow: hidden;">
              <div style="width: 18.4%; height: 100%; background: #ef4444;"></div>
            </div>
            <div style="font-size: 11px; color: var(--text-muted);">Peer-to-peer discussion before whole-class answer sharing (Critical Gap).</div>
          </div>

          <div class="bento-card" style="border-left: 3px solid #ef4444;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: 700; font-size: 13px; color: var(--text-primary);">👥 Small Group Discussion</span>
              <span class="font-mono" style="font-size: 18px; font-weight: 900; color: #ef4444;">17.9%</span>
            </div>
            <div class="progress-bar-bg" style="height: 6px; margin: 8px 0; background: var(--bg-surface-2); border-radius: 4px; overflow: hidden;">
              <div style="width: 17.9%; height: 100%; background: #ef4444;"></div>
            </div>
            <div style="font-size: 11px; color: var(--text-muted);">Structured group tasks where learners collaboratively co-create solutions.</div>
          </div>

          <div class="bento-card" style="border-left: 3px solid var(--peepul-teal);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: 700; font-size: 13px; color: var(--text-primary);">🗣️ Effective Questioning</span>
              <span class="font-mono" style="font-size: 18px; font-weight: 900; color: var(--peepul-teal);">High Adoption</span>
            </div>
            <div class="progress-bar-bg" style="height: 6px; margin: 8px 0; background: var(--bg-surface-2); border-radius: 4px; overflow: hidden;">
              <div style="width: 85%; height: 100%; background: var(--peepul-teal);"></div>
            </div>
            <div style="font-size: 11px; color: var(--text-muted);">Use of open-ended, thought-provoking inquiry prompts in lesson flow.</div>
          </div>

          <div class="bento-card" style="border-left: 3px solid var(--peepul-teal);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: 700; font-size: 13px; color: var(--text-primary);">🌟 Positive Language</span>
              <span class="font-mono" style="font-size: 18px; font-weight: 900; color: var(--peepul-teal);">High Adoption</span>
            </div>
            <div class="progress-bar-bg" style="height: 6px; margin: 8px 0; background: var(--bg-surface-2); border-radius: 4px; overflow: hidden;">
              <div style="width: 90%; height: 100%; background: var(--peepul-teal);"></div>
            </div>
            <div style="font-size: 11px; color: var(--text-muted);">Supportive classroom tone reinforcing psychological safety for all learners.</div>
          </div>

        </div>
      </div>

      <!-- Foundational Learning Assessment & Print-Rich Environment -->
      <div style="margin-top: 20px; display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px;">
        
        <!-- Student Competency Card -->
        <div style="background: var(--bg-surface-2); border-radius: 8px; padding: 14px 16px; border: 1px solid var(--border-subtle);">
          <div style="font-size: 12px; font-weight: 700; color: var(--text-primary); margin-bottom: 8px; display: flex; justify-content: space-between;">
            <span>📖 Student Competencies (Section G.1–G.3)</span>
            <span class="badge" style="background: rgba(0, 138, 171, 0.1); color: var(--peepul-teal);">3 Sampled Students / Class</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 8px; font-size: 11.5px;">
            <div style="display: flex; justify-content: space-between;">
              <span style="color: var(--text-secondary);">Fluent Reading (G.1 - ≥ 2 students):</span>
              <span class="font-mono font-bold" style="color: #059669;">61.4% of Classrooms</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
              <span style="color: var(--text-secondary);">Reading Comprehension (G.2 - ≥ 70% gist):</span>
              <span class="font-mono font-bold" style="color: #2563eb;">54.8% of Classrooms</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
              <span style="color: var(--text-secondary);">Error-Free Dictation (G.3):</span>
              <span class="font-mono font-bold" style="color: #d97706;">48.2% of Classrooms</span>
            </div>
          </div>
        </div>

        <!-- Print-Rich Classroom Environment Card -->
        <div style="background: var(--bg-surface-2); border-radius: 8px; padding: 14px 16px; border: 1px solid var(--border-subtle);">
          <div style="font-size: 12px; font-weight: 700; color: var(--text-primary); margin-bottom: 8px; display: flex; justify-content: space-between;">
            <span>🎨 Print-Rich Environment (Section F.1–F.4)</span>
            <span class="badge" style="background: rgba(139, 92, 246, 0.1); color: #8b5cf6;">Classroom Walls</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 8px; font-size: 11.5px;">
            <div style="display: flex; justify-content: space-between;">
              <span style="color: var(--text-secondary);">Wall Posters &amp; Charts Present:</span>
              <span class="font-mono font-bold" style="color: #059669;">78.2% of Classrooms</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
              <span style="color: var(--text-secondary);">Created by Students (Student Agency):</span>
              <span class="font-mono font-bold" style="color: #ef4444;">26.5% Only (Gap)</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
              <span style="color: var(--text-secondary);">Direct Pedagogical Relevance (F.4):</span>
              <span class="font-mono font-bold" style="color: #2563eb;">82.1% Relevant</span>
            </div>
          </div>
        </div>

      </div>

    </div>
"""

# Insert properly into enhanced_body
ped_search = '<!-- Dynamically populated via renderPedagogyMisconceptions() -->\n</div>\n</div>'
if ped_search in code:
    code = code.replace(ped_search, ped_search + "\n" + cro_html_str)
    print("Cleanly injected cro_html_str into enhanced_body after pedMisconContainer.")
else:
    print("Could not find ped_search anchor in code, searching alternative...")
    alt_anchor = '</section>\n\n    <!-- Tab 8: Key Actions'
    code = code.replace(alt_anchor, cro_html_str + "\n" + alt_anchor)
    print("Injected via alt_anchor.")

with open('build_enhanced_studio.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_enhanced_studio.py updated cleanly!")
