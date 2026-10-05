import json

cohort_html = """
    <!-- ========================================== -->
    <!-- TAB 11: TEACHER ATTENDANCE & TRAJECTORY   -->
    <!-- ========================================== -->
    <section id="tab-cohort" class="tab-section">
      <!-- Section Hero Banner with Plain Words Explanation -->
      <div class="section-hero-banner" style="margin-bottom: 24px; padding: 24px 28px; background: linear-gradient(135deg, rgba(0,138,171,0.08) 0%, rgba(99,208,223,0.03) 100%); border: 1px solid rgba(0,138,171,0.25); border-radius: 14px; position: relative; overflow: hidden;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px;">
          <div>
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
              <span style="font-size: 22px;">👥</span>
              <h2 id="lblCohortTitle" style="font-size: 22px; font-weight: 800; color: var(--text-primary); margin: 0; font-family: var(--font-brand);">
                In Plain Words: What Happened in August vs. September?
              </h2>
              <span class="badge" style="background: rgba(0,138,171,0.15); color: var(--peepul-teal); font-weight: 700; border: 1px solid rgba(0,138,171,0.3); font-size: 11px;">
                CLEAR &amp; SIMPLE ATTENDANCE TRACKER
              </span>
            </div>
            <p id="lblCohortSubtitle" style="font-size: 13.5px; color: var(--text-secondary); margin: 0; max-width: 980px; line-height: 1.55;">
              Clear, easy-to-understand breakdown of teacher participation across August and September using verified <code style="color: var(--peepul-teal); font-family: var(--font-mono);">EmployeeCode</code> records. Designed for teachers, block officers, and district officials to take immediate action.
            </p>
          </div>
          <div style="display: flex; align-items: center; gap: 10px;">
            <button class="btn-tactile gold" onclick="downloadCohortMatrixCSV()" style="font-size: 12px; padding: 8px 16px;">
              📥 Export District Matrix (.CSV)
            </button>
          </div>
        </div>

        <!-- 4 Plain Words Takeaway Cards -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-top: 20px;">
          
          <div style="background: var(--bg-surface-1); border: 1px solid rgba(5,150,105,0.3); border-left: 4px solid #059669; border-radius: 8px; padding: 12px 14px;">
            <div style="font-weight: 800; font-size: 12.5px; color: #059669; margin-bottom: 4px;">🔄 Regular Teachers</div>
            <div style="font-size: 17px; font-weight: 900; font-family: var(--font-mono); color: var(--text-primary);">13,088 Teachers</div>
            <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 3px; line-height: 1.4;">
              Came in August and came back again in September.
            </div>
          </div>

          <div style="background: var(--bg-surface-1); border: 1px solid rgba(37,99,235,0.3); border-left: 4px solid #2563eb; border-radius: 8px; padding: 12px 14px;">
            <div style="font-weight: 800; font-size: 12.5px; color: #2563eb; margin-bottom: 4px;">🌱 Fresh Faces</div>
            <div style="font-size: 17px; font-weight: 900; font-family: var(--font-mono); color: var(--text-primary);">10,081 Teachers</div>
            <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 3px; line-height: 1.4;">
              Attended for the very first time in September.
            </div>
          </div>

          <div style="background: var(--bg-surface-1); border: 1px solid rgba(217,119,6,0.3); border-left: 4px solid #d97706; border-radius: 8px; padding: 12px 14px;">
            <div style="font-weight: 800; font-size: 12.5px; color: #d97706; margin-bottom: 4px;">⚠️ Need Follow-up Call</div>
            <div style="font-size: 17px; font-weight: 900; font-family: var(--font-mono); color: var(--text-primary);">10,697 Teachers</div>
            <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 3px; line-height: 1.4;">
              Attended August, missed September. Calling list ready.
            </div>
          </div>

          <div style="background: var(--bg-surface-1); border: 1px solid rgba(0,138,171,0.3); border-left: 4px solid var(--peepul-teal); border-radius: 8px; padding: 12px 14px;">
            <div style="font-weight: 800; font-size: 12.5px; color: var(--peepul-teal); margin-bottom: 4px;">🌟 Total Reached So Far</div>
            <div style="font-size: 17px; font-weight: 900; font-family: var(--font-mono); color: var(--text-primary);">33,866 Teachers (96%)</div>
            <div style="font-size: 11.5px; color: var(--text-secondary); margin-top: 3px; line-height: 1.4;">
              96% of all targeted Math &amp; Science teachers in MP!
            </div>
          </div>

        </div>
      </div>

      <!-- Hero KPI Ribbon (5 Cards) -->
      <div class="bento-grid" style="grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 24px;">
        
        <!-- Card 1: Total Reached So Far -->
        <div class="bento-card" style="border-top: 3px solid var(--peepul-teal); background: var(--bg-surface-1); padding: 18px 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-size: 11px; font-weight: 800; letter-spacing: 0.05em; color: var(--text-muted); text-transform: uppercase;">TOTAL TEACHERS REACHED SO FAR</span>
            <span style="font-size: 16px;">🌟</span>
          </div>
          <div style="font-size: 32px; font-weight: 900; font-family: var(--font-mono); color: var(--peepul-teal); line-height: 1;">
            33,866
          </div>
          <div style="margin-top: 8px; font-size: 12px; color: var(--text-secondary); display: flex; align-items: center; justify-content: space-between;">
            <span>Statewide Coverage:</span>
            <strong style="color: #059669; font-weight: 800;">95.7% (of 35,374 Target)</strong>
          </div>
          <div style="margin-top: 6px; width: 100%; height: 5px; background: var(--bg-surface-3); border-radius: 999px; overflow: hidden;">
            <div style="width: 95.7%; height: 100%; background: linear-gradient(90deg, #008aab, #059669); border-radius: 999px;"></div>
          </div>
        </div>

        <!-- Card 2: Teachers Coming Back -->
        <div class="bento-card" style="border-top: 3px solid #059669; background: var(--bg-surface-1); padding: 18px 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-size: 11px; font-weight: 800; letter-spacing: 0.05em; color: var(--text-muted); text-transform: uppercase;">TEACHERS COMING BACK</span>
            <span style="font-size: 16px;">🔄</span>
          </div>
          <div style="font-size: 32px; font-weight: 900; font-family: var(--font-mono); color: #059669; line-height: 1;">
            13,088
          </div>
          <div style="margin-top: 8px; font-size: 12px; color: var(--text-secondary); display: flex; align-items: center; justify-content: space-between;">
            <span>Regular Repeaters:</span>
            <strong style="color: #059669; font-weight: 800;">55.0% of August (56.5% of Sep)</strong>
          </div>
          <div style="margin-top: 6px; width: 100%; height: 5px; background: var(--bg-surface-3); border-radius: 999px; overflow: hidden;">
            <div style="width: 55.0%; height: 100%; background: #059669; border-radius: 999px;"></div>
          </div>
        </div>

        <!-- Card 3: New Teachers Joining -->
        <div class="bento-card" style="border-top: 3px solid #2563eb; background: var(--bg-surface-1); padding: 18px 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-size: 11px; font-weight: 800; letter-spacing: 0.05em; color: var(--text-muted); text-transform: uppercase;">NEW TEACHERS JOINING</span>
            <span style="font-size: 16px;">🌱</span>
          </div>
          <div style="font-size: 32px; font-weight: 900; font-family: var(--font-mono); color: #2563eb; line-height: 1;">
            10,081
          </div>
          <div style="margin-top: 8px; font-size: 12px; color: var(--text-secondary); display: flex; align-items: center; justify-content: space-between;">
            <span>Fresh Faces:</span>
            <strong style="color: #2563eb; font-weight: 800;">43.5% New in September</strong>
          </div>
          <div style="margin-top: 6px; width: 100%; height: 5px; background: var(--bg-surface-3); border-radius: 999px; overflow: hidden;">
            <div style="width: 43.5%; height: 100%; background: #2563eb; border-radius: 999px;"></div>
          </div>
        </div>

        <!-- Card 4: Missed Last Month -->
        <div class="bento-card" style="border-top: 3px solid #d97706; background: var(--bg-surface-1); padding: 18px 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-size: 11px; font-weight: 800; letter-spacing: 0.05em; color: var(--text-muted); text-transform: uppercase;">MISSED LAST MONTH (CALLING LIST)</span>
            <span style="font-size: 16px;">⚠️</span>
          </div>
          <div style="font-size: 32px; font-weight: 900; font-family: var(--font-mono); color: #d97706; line-height: 1;">
            10,697
          </div>
          <div style="margin-top: 8px; font-size: 12px; color: var(--text-secondary); display: flex; align-items: center; justify-content: space-between;">
            <span>Follow-up Target:</span>
            <strong style="color: #d97706; font-weight: 800;">45.0% to Invite Back</strong>
          </div>
          <div style="margin-top: 6px; width: 100%; height: 5px; background: var(--bg-surface-3); border-radius: 999px; overflow: hidden;">
            <div style="width: 45.0%; height: 100%; background: #d97706; border-radius: 999px;"></div>
          </div>
        </div>

        <!-- Card 5: Remaining to Reach -->
        <div class="bento-card" style="border-top: 3px solid #7c3aed; background: var(--bg-surface-1); padding: 18px 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-size: 11px; font-weight: 800; letter-spacing: 0.05em; color: var(--text-muted); text-transform: uppercase;">REMAINING TO REACH</span>
            <span style="font-size: 16px;">🎯</span>
          </div>
          <div style="font-size: 32px; font-weight: 900; font-family: var(--font-mono); color: #7c3aed; line-height: 1;">
            1,508
          </div>
          <div style="margin-top: 8px; font-size: 12px; color: var(--text-secondary); display: flex; align-items: center; justify-content: space-between;">
            <span>Gap to 100%:</span>
            <strong style="color: #7c3aed; font-weight: 800;">4.3% Left in Universe</strong>
          </div>
          <div style="margin-top: 6px; width: 100%; height: 5px; background: var(--bg-surface-3); border-radius: 999px; overflow: hidden;">
            <div style="width: 4.3%; height: 100%; background: #7c3aed; border-radius: 999px;"></div>
          </div>
        </div>

      </div>

      <!-- Actionable Segment Calling Lists & Download Center -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 24px;">
        
        <!-- Left: Month-over-Month Flow -->
        <div class="panel-box" style="background: var(--bg-surface-1); padding: 22px 24px;">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px;">
            <h3 style="font-size: 15px; font-weight: 700; margin: 0; color: var(--text-primary);">
              🔄 Month-Over-Month Teacher Flow (August ➔ September)
            </h3>
            <span class="badge" style="background: var(--bg-surface-2); border: 1px solid var(--border-subtle); font-size: 11px;">
              VERIFIED COUNTS
            </span>
          </div>

          <div style="display: flex; flex-direction: column; gap: 16px;">
            
            <!-- August Row -->
            <div style="background: var(--bg-surface-2); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 14px 16px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 700; font-size: 13px; color: var(--text-primary);">📅 August 2026 Attendees</span>
                <strong style="font-family: var(--font-mono); color: var(--peepul-teal); font-size: 15px;">23,785 Teachers</strong>
              </div>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                <div style="background: rgba(5,150,105,0.08); border: 1px solid rgba(5,150,105,0.25); border-radius: 8px; padding: 10px;">
                  <div style="font-size: 11px; color: #059669; font-weight: 700;">➔ CAME BACK IN SEPT</div>
                  <div style="font-size: 18px; font-weight: 900; font-family: var(--font-mono); color: #059669;">13,088 <span style="font-size: 12px; font-weight: 600;">(55.0%)</span></div>
                  <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">Regular Teachers</div>
                </div>
                <div style="background: rgba(217,119,6,0.08); border: 1px solid rgba(217,119,6,0.25); border-radius: 8px; padding: 10px;">
                  <div style="font-size: 11px; color: #d97706; font-weight: 700;">➔ MISSED IN SEPT</div>
                  <div style="font-size: 18px; font-weight: 900; font-family: var(--font-mono); color: #d97706;">10,697 <span style="font-size: 12px; font-weight: 600;">(45.0%)</span></div>
                  <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">Need Follow-up Call</div>
                </div>
              </div>
            </div>

            <!-- September Row -->
            <div style="background: var(--bg-surface-2); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 14px 16px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 700; font-size: 13px; color: var(--text-primary);">📅 September 2026 Attendees</span>
                <strong style="font-family: var(--font-mono); color: #2563eb; font-size: 15px;">23,169 Teachers</strong>
              </div>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                <div style="background: rgba(5,150,105,0.08); border: 1px solid rgba(5,150,105,0.25); border-radius: 8px; padding: 10px;">
                  <div style="font-size: 11px; color: #059669; font-weight: 700;">⬅ REGULAR REPEATERS</div>
                  <div style="font-size: 18px; font-weight: 900; font-family: var(--font-mono); color: #059669;">13,088 <span style="font-size: 12px; font-weight: 600;">(56.5%)</span></div>
                  <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">From August Base</div>
                </div>
                <div style="background: rgba(37,99,235,0.08); border: 1px solid rgba(37,99,235,0.25); border-radius: 8px; padding: 10px;">
                  <div style="font-size: 11px; color: #2563eb; font-weight: 700;">⬅ NEW TEACHERS JOINING</div>
                  <div style="font-size: 18px; font-weight: 900; font-family: var(--font-mono); color: #2563eb;">10,081 <span style="font-size: 12px; font-weight: 600;">(43.5%)</span></div>
                  <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">Fresh Faces in Sept</div>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- Right: Ready-to-Use Calling Lists -->
        <div class="panel-box" style="background: var(--bg-surface-1); padding: 22px 24px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
              <h3 style="font-size: 15px; font-weight: 700; margin: 0; color: var(--text-primary);">
                📋 Actionable Calling Sheets for Blocks &amp; Districts
              </h3>
              <span class="badge gold" style="font-size: 10px;">READY FOR OUTREACH</span>
            </div>
            <p style="font-size: 12px; color: var(--text-secondary); margin-bottom: 16px; line-height: 1.5;">
              Download clean spreadsheets formatted with Employee Code, Name, District, Block, Cluster, and Designation for calling and follow-up.
            </p>

            <!-- List Action Buttons -->
            <div style="display: flex; flex-direction: column; gap: 10px;">
              
              <a href="data/exports/August_Lapsed_Dropout_Calling_List.csv" download="Missed_September_Followup_Calling_List.csv" class="btn-tactile" style="display: flex; align-items: center; justify-content: space-between; background: rgba(217,119,6,0.08); border: 1px solid rgba(217,119,6,0.3); color: var(--text-primary); text-decoration: none; padding: 10px 14px; border-radius: 8px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                  <span style="font-size: 16px;">⚠️</span>
                  <div style="text-align: left;">
                    <div style="font-weight: 700; font-size: 12.5px;">Missed Last Month (Calling List)</div>
                    <div style="font-size: 11px; color: var(--text-muted);">10,697 teachers who need a call for next session</div>
                  </div>
                </div>
                <span style="font-size: 12px; font-weight: 800; color: #d97706;">📥 .CSV</span>
              </a>

              <a href="data/exports/September_New_Teachers_Intake.csv" download="New_Teachers_Joining_September.csv" class="btn-tactile" style="display: flex; align-items: center; justify-content: space-between; background: rgba(37,99,235,0.08); border: 1px solid rgba(37,99,235,0.3); color: var(--text-primary); text-decoration: none; padding: 10px 14px; border-radius: 8px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                  <span style="font-size: 16px;">🌱</span>
                  <div style="text-align: left;">
                    <div style="font-weight: 700; font-size: 12.5px;">New Teachers Joining (Fresh Faces)</div>
                    <div style="font-size: 11px; color: var(--text-muted);">10,081 new first-time attendee profiles</div>
                  </div>
                </div>
                <span style="font-size: 12px; font-weight: 800; color: #2563eb;">📥 .CSV</span>
              </a>

              <a href="data/exports/August_September_Persistent_Champions.csv" download="Regular_Teachers_Both_Months.csv" class="btn-tactile" style="display: flex; align-items: center; justify-content: space-between; background: rgba(5,150,105,0.08); border: 1px solid rgba(5,150,105,0.3); color: var(--text-primary); text-decoration: none; padding: 10px 14px; border-radius: 8px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                  <span style="font-size: 16px;">🔄</span>
                  <div style="text-align: left;">
                    <div style="font-weight: 700; font-size: 12.5px;">Regular Teachers (Both Months)</div>
                    <div style="font-size: 11px; color: var(--text-muted);">13,088 teachers attending consistently</div>
                  </div>
                </div>
                <span style="font-size: 12px; font-weight: 800; color: #059669;">📥 .CSV</span>
              </a>

            </div>
          </div>

          <div style="margin-top: 14px; padding-top: 12px; border-top: 1px solid var(--border-hairline); display: flex; align-items: center; justify-content: space-between; font-size: 11px; color: var(--text-muted);">
            <span>🚀 Automated monthly intake script:</span>
            <code style="background: var(--bg-surface-2); padding: 2px 6px; border-radius: 4px; font-size: 10.5px; color: var(--peepul-teal);">scripts/track_monthly_teacher_cohorts.py</code>
          </div>
        </div>

      </div>

      <!-- 52-District Attendance Matrix -->
      <div class="panel-box" style="background: var(--bg-surface-1); padding: 24px; margin-bottom: 24px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; margin-bottom: 18px;">
          <div>
            <h3 style="font-size: 16px; font-weight: 800; margin: 0; color: var(--text-primary);">
              🗺️ 52-District Teacher Attendance &amp; Reach Matrix
            </h3>
            <p style="font-size: 12px; color: var(--text-secondary); margin: 3px 0 0;">
              District-by-district breakdown of regular teachers, fresh joiners, and total teachers reached so far.
            </p>
          </div>

          <!-- Controls: Search & Filter Pills -->
          <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
            <input type="text" id="cohortDistrictSearch" onkeyup="filterCohortTable()" placeholder="🔍 Search district..." style="background: var(--bg-surface-2); border: 1px solid var(--border-subtle); color: var(--text-primary); font-size: 12px; padding: 6px 12px; border-radius: 6px; outline: none; width: 170px;">
            <div class="slicer-pills" id="cohortFilterPills">
              <button class="slicer-btn active" onclick="setCohortFilter('ALL', this)">All (52)</button>
              <button class="slicer-btn" onclick="setCohortFilter('HIGH_RET', this)">Coming Back &gt;60%</button>
              <button class="slicer-btn" onclick="setCohortFilter('HIGH_NEW', this)">New Joining &gt;50%</button>
              <button class="slicer-btn" onclick="setCohortFilter('LAGGING', this)">Reached &lt;80%</button>
            </div>
          </div>
        </div>

        <!-- Data Table Container -->
        <div style="overflow-x: auto; max-height: 520px; border: 1px solid var(--border-subtle); border-radius: 8px;">
          <table id="cohortMatrixTable" class="data-table" style="width: 100%; border-collapse: collapse; font-size: 12.5px; text-align: left;">
            <thead style="position: sticky; top: 0; background: var(--bg-surface-2); z-index: 10; border-bottom: 2px solid var(--border-subtle);">
              <tr>
                <th onclick="sortCohortTable(0)" style="cursor: pointer; padding: 10px 14px; font-weight: 800; color: var(--text-muted);">DISTRICT ⬍</th>
                <th onclick="sortCohortTable(1)" style="cursor: pointer; padding: 10px 12px; font-weight: 800; color: var(--text-muted); text-align: right;">AUG ATTENDED ⬍</th>
                <th onclick="sortCohortTable(2)" style="cursor: pointer; padding: 10px 12px; font-weight: 800; color: var(--text-muted); text-align: right;">SEP ATTENDED ⬍</th>
                <th onclick="sortCohortTable(3)" style="cursor: pointer; padding: 10px 12px; font-weight: 800; color: #059669; text-align: right;">REGULAR TEACHERS ⬍</th>
                <th onclick="sortCohortTable(4)" style="cursor: pointer; padding: 10px 12px; font-weight: 800; color: #059669; text-align: right;">COMING BACK % ⬍</th>
                <th onclick="sortCohortTable(5)" style="cursor: pointer; padding: 10px 12px; font-weight: 800; color: #2563eb; text-align: right;">NEW TEACHERS ⬍</th>
                <th onclick="sortCohortTable(6)" style="cursor: pointer; padding: 10px 12px; font-weight: 800; color: #2563eb; text-align: right;">NEW JOINING % ⬍</th>
                <th onclick="sortCohortTable(7)" style="cursor: pointer; padding: 10px 12px; font-weight: 800; color: #d97706; text-align: right;">MISSED LAST MONTH ⬍</th>
                <th onclick="sortCohortTable(8)" style="cursor: pointer; padding: 10px 12px; font-weight: 800; color: var(--peepul-teal); text-align: right;">TOTAL REACHED SO FAR ⬍</th>
                <th onclick="sortCohortTable(9)" style="cursor: pointer; padding: 10px 12px; font-weight: 800; color: var(--text-muted); text-align: right;">TARGET UNIVERSE ⬍</th>
                <th onclick="sortCohortTable(10)" style="cursor: pointer; padding: 10px 14px; font-weight: 800; color: var(--text-primary); text-align: right;">TOTAL REACH % ⬍</th>
              </tr>
            </thead>
            <tbody id="cohortMatrixBody">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>

        <div style="margin-top: 12px; display: flex; justify-content: space-between; align-items: center; font-size: 11.5px; color: var(--text-muted);">
          <span>Showing <strong id="cohortVisibleCount" style="color: var(--text-primary);">52</strong> of 52 districts</span>
          <span>Click any column header to sort • Reach % based on Target Math &amp; Science Varg-2 Universe</span>
        </div>
      </div>

    </section>
"""

with open(r'c:\Master Dashboard for CLSS\scratch\cohort_tab_block.py', 'w', encoding='utf-8') as f:
    f.write(f'cohort_html = """{cohort_html}"""')

print("Updated cohort_tab_block.py with Plain Words labels.")
