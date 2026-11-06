import openpyxl
import os
import unittest

class TestKPIDictionary(unittest.TestCase):
    def test_overview_sheet_structure(self):
        from scripts.generate_kpi_dictionary import build_workbook
        wb = build_workbook()
        self.assertIn("Overview & Summary", wb.sheetnames)
        sheet = wb["Overview & Summary"]
        self.assertIsNotNone(sheet.cell(row=1, column=1).value)
        found_lineage = any("Source ID" in str(sheet.cell(row=r, column=1).value or sheet.cell(row=r, column=2).value) for r in range(1, 25))
        self.assertTrue(found_lineage)

    def test_kpi_dictionary_sheet(self):
        from scripts.generate_kpi_dictionary import build_workbook
        wb = build_workbook()
        self.assertIn("KPIs & Visuals Dictionary", wb.sheetnames)
        sheet = wb["KPIs & Visuals Dictionary"]
        headers = [sheet.cell(row=4, column=c).value for c in range(1, 13)]
        self.assertIn("Component Name", headers)
        self.assertIn("Derivation & Calculation Formula", headers)
        self.assertIn("Raw Source File & Sheet", headers)
        self.assertGreaterEqual(sheet.max_row, 18)

    def test_pedagogy_sheet(self):
        from scripts.generate_kpi_dictionary import build_workbook
        wb = build_workbook()
        self.assertIn("Pedagogy & Survey Questions", wb.sheetnames)
        sheet = wb["Pedagogy & Survey Questions"]
        self.assertGreaterEqual(sheet.max_row, 28)
        headers = [sheet.cell(row=4, column=c).value for c in range(1, 10)]
        self.assertIn("Question Text (Hindi)", headers)
        self.assertIn("Academic Domain", headers)

    def test_cohorts_quadrants_sheet(self):
        from scripts.generate_kpi_dictionary import build_workbook
        wb = build_workbook()
        self.assertIn("Cohorts & Quadrants Logic", wb.sheetnames)
        sheet = wb["Cohorts & Quadrants Logic"]
        content = [str(sheet.cell(row=r, column=c).value) for r in range(1, 45) for c in range(1, 10)]
        joined = " ".join(content)
        self.assertTrue("35.0%" in joined or "0.35" in joined)
        self.assertTrue("56.0%" in joined or "0.56" in joined)
        self.assertTrue("33,866" in joined or "33866" in joined)

    def test_full_workbook_output(self):
        from scripts.generate_kpi_dictionary import main
        main()
        self.assertTrue(os.path.exists("CLSS_Dashboard_KPI_Dictionary.xlsx"))
        wb = openpyxl.load_workbook("CLSS_Dashboard_KPI_Dictionary.xlsx")
        self.assertEqual(len(wb.sheetnames), 4)
        for sname in wb.sheetnames:
            sheet = wb[sname]
            self.assertIsNotNone(sheet.freeze_panes)
            self.assertGreater(len(sheet.column_dimensions), 0)

if __name__ == "__main__":
    unittest.main()
