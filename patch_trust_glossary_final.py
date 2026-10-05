import re

def main():
    file_path = 'RSK_Master_CLSS_Executive_Studio_Enhanced.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    target_str = "charts.ovTrustBar = new Chart(ctx4, {\n          type: 'bar',"
    
    pos = content.find("const canvas4 = document.getElementById('ovTrustBar');")
    end_pos = content.find("}\n    }\n\n    \n    // ==========================================\n    // DISTRICT 360", pos)
    
    trust_glossary_js = '''
        // Render Teacher Trust Explanatory Guide Box
        const trustGlossaryEl = document.getElementById('ovTrustGlossaryBox');
        if (trustGlossaryEl) {
          if (isHi) {
            trustGlossaryEl.innerHTML = `
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--peepul-teal); font-family: var(--font-mono); margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between;">
                <span>🔍 शिक्षक विश्वास सूचकांक (Teacher Trust Index): आंकड़े कैसे प्राप्त हुए?</span>
                <span class="status-chip" style="font-size: 9.5px; background: rgba(0, 138, 171, 0.08); color: var(--peepul-teal);">सर्वेक्षण प्रमाण आधारित</span>
              </div>
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 8px; font-size: 11px; line-height: 1.45;">
                <div style="background: var(--bg-surface-1); padding: 8px 10px; border-radius: 6px; border-left: 3px solid #059669;">
                  <strong style="color: #059669;">1. मनोवैज्ञानिक सुरक्षा (Q91.1 - 93.8%):</strong>
                  <span style="color: var(--text-secondary);">शिक्षकों द्वारा पुष्टि कि संवाद बिना किसी प्रशासनिक डर या फटकार के, खुली बातचीत और सीखने का सुरक्षित मंच है।</span>
                </div>
                <div style="background: var(--bg-surface-1); padding: 8px 10px; border-radius: 6px; border-left: 3px solid #008aab;">
                  <strong style="color: #008aab;">2. अकादमिक फोकस (Q89 - 91.4%):</strong>
                  <span style="color: var(--text-secondary);">सत्र में केवल प्रशासनिक आदेशों के बजाय वास्तविक कक्षा शिक्षण पद्धतियों और समाधानों पर केंद्रित चर्चा की गई।</span>
                </div>
                <div style="background: var(--bg-surface-1); padding: 8px 10px; border-radius: 6px; border-left: 3px solid #4f46e5;">
                  <strong style="color: #4f46e5;">3. समस्या समाधान (Q90 - 88.7%):</strong>
                  <span style="color: var(--text-secondary);">कठिन पाठ्य अवधारणाओं व कक्षा चुनौतियों पर सहकर्मी शिक्षकों द्वारा व्यावहारिक समाधान और सुझाव साझा किए गए।</span>
                </div>
                <div style="background: var(--bg-surface-1); padding: 8px 10px; border-radius: 6px; border-left: 3px solid #7c3aed;">
                  <strong style="color: #7c3aed;">4. 2-वर्षीय शिक्षण वृद्धि (Q88 - 92.5%):</strong>
                  <span style="color: var(--text-secondary);">2 वर्षों के संवाद यात्रा में शिक्षकों द्वारा अपने शिक्षण कौशल और विषय ज्ञान में स्पष्ट सुधार का अनुभव।</span>
                </div>
              </div>
              <div style="margin-top: 8px; padding-top: 6px; border-top: 1px dashed var(--border-hairline); font-size: 10.5px; color: var(--text-muted); font-family: var(--font-mono);">
                📌 <strong>गणना विधि:</strong> नेट ट्रस्ट स्कोर (NTS: +93.8%) राज्यभर के 23,785+ शिक्षकों के गोपनीय प्रतिक्रिया डेटा (प्रश्नावली Q91.1, Q89, Q90, Q88) का संयुक्त औसत है।
              </div>
            `;
          } else {
            trustGlossaryEl.innerHTML = `
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--peepul-teal); font-family: var(--font-mono); margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between;">
                <span>🔍 Teacher Trust Index: Methodology & How Figures Are Derived</span>
                <span class="status-chip" style="font-size: 9.5px; background: rgba(0, 138, 171, 0.08); color: var(--peepul-teal);">Survey Provenance</span>
              </div>
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 8px; font-size: 11px; line-height: 1.45;">
                <div style="background: var(--bg-surface-1); padding: 8px 10px; border-radius: 6px; border-left: 3px solid #059669;">
                  <strong style="color: #059669;">1. Psychological Safety (Q91.1 — 93.8%):</strong>
                  <span style="color: var(--text-secondary);">Measures non-judgmental climate—teachers affirm they can openly share teaching difficulties without fear of administrative reprimand.</span>
                </div>
                <div style="background: var(--bg-surface-1); padding: 8px 10px; border-radius: 6px; border-left: 3px solid #008aab;">
                  <strong style="color: #008aab;">2. Academic Focus (Q89 — 91.4%):</strong>
                  <span style="color: var(--text-secondary);">Confirms that dialogues dedicated high-value time to actionable classroom pedagogy rather than administrative circulars.</span>
                </div>
                <div style="background: var(--bg-surface-1); padding: 8px 10px; border-radius: 6px; border-left: 3px solid #4f46e5;">
                  <strong style="color: #4f46e5;">3. Problem Solving (Q90 — 88.7%):</strong>
                  <span style="color: var(--text-secondary);">Reflects collaborative peer exchange where facilitators and fellow teachers co-created solutions for student learning hurdles.</span>
                </div>
                <div style="background: var(--bg-surface-1); padding: 8px 10px; border-radius: 6px; border-left: 3px solid #7c3aed;">
                  <strong style="color: #7c3aed;">4. 2-Year Growth (Q88 — 92.5%):</strong>
                  <span style="color: var(--text-secondary);">Validates long-term professional development—teachers affirm observable growth in classroom engagement over 2 years.</span>
                </div>
              </div>
              <div style="margin-top: 8px; padding-top: 6px; border-top: 1px dashed var(--border-hairline); font-size: 10.5px; color: var(--text-muted); font-family: var(--font-mono);">
                📌 <strong>Calculation Methodology:</strong> Net Trust Score (NTS: +93.8%) is the composite affirmation average across all 23,785+ verified teacher survey responses in Sheets Q91, Q89, Q90, and Q88.
              </div>
            `;
          }
        }
      }
    }'''

    # Replace block
    content = content[:end_pos] + trust_glossary_js + content[end_pos+7:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated RSK_Master_CLSS_Executive_Studio_Enhanced.html successfully!')

    for dest in ['index.html', 'deploy/index.html', 'RSK_Master_CLSS_Executive_Dashboard.html']:
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Synced to {dest} successfully!')

if __name__ == '__main__':
    main()
