function calculateDistrictPedagogyScore(dname) {
      let q82 = getDistrictSurveyVal("CLSS", "Participant", "Q82", "82_Correct", dname);
      let q84 = getDistrictSurveyVal("CLSS", "Participant", "Q84", "84_Correct", dname);
      let q95 = getDistrictSurveyVal("CLSS", "Participant", "Q95", "95_Correct", dname);
      let q96 = getDistrictSurveyVal("CLSS", "Participant", "Q96", "96_Correct", dname);
      let q97 = getDistrictSurveyVal("CLSS", "Participant", "Q97", "97_Correct", dname);
      
      const d = dataPackage.districtSummary.find(x => x.district === dname);
      const tot = (d && d.attendees > 0) ? d.attendees : 1;
      
      const p84 = Math.min(100, Math.round(q84 / tot * 100));
      const p82 = Math.min(100, Math.round(q82 / tot * 100));
      const p96 = Math.min(100, Math.round(q96 / tot * 100));
      const p95 = Math.min(100, Math.round(q95 / tot * 100));
      const p97 = Math.min(100, Math.round(q97 / tot * 100));
      
      return Math.round((p84 + p82 + p96 + p95 + p97) / 5);
    }

    function getDistrictQuadrantInfo(turnout, pedScore) {
      if (turnout >= TURNOUT_BENCHMARK && pedScore >= PEDAGOGY_BENCHMARK) {
        return {
          quad: 'Q1',
          label: 'Q1: Benchmark Champion',
          color: 'var(--accent-emerald)',
          bgChip: 'background: rgba(5, 150, 105, 0.12); color: var(--accent-emerald); border: 1px solid rgba(5, 150, 105, 0.3);',
          action: 'Document & scale peer dialogue best practices'
        };
      } else if (turnout >= TURNOUT_BENCHMARK && pedScore < PEDAGOGY_BENCHMARK) {
        return {
          quad: 'Q2',
          label: 'Q2: Scale, Pedagogy Gap',
          color: 'var(--peepul-teal)',
          bgChip: 'background: rgba(0, 138, 171, 0.12); color: var(--peepul-teal); border: 1px solid rgba(0, 138, 171, 0.3);',
          action: 'Conduct targeted refresher on Q95 & Q97'
        };
      } else if (turnout < TURNOUT_BENCHMARK && pedScore >= PEDAGOGY_BENCHMARK) {
        return {
          quad: 'Q3',
          label: 'Q3: Mobilization Need',
          color: 'var(--accent-indigo)',
          bgChip: 'background: rgba(79, 70, 229, 0.12); color: var(--accent-indigo); border: 1px solid rgba(79, 70, 229, 0.3);',
          action: 'Drive teacher attendance & CAC monitoring'
        };
      } else {
        return {
          quad: 'Q4',
          label: 'Q4: Targeted Support Zone',
          color: 'var(--accent-rose)',
          bgChip: 'background: rgba(220, 38, 38, 0.12); color: var(--accent-rose); border: 1px solid rgba(29, 78, 216, 0.3);',
          action: 'Urgent administrative resolution & CAC appointment'
        };
      }
    }

    