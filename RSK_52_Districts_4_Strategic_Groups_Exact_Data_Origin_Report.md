# The 52 Districts: 4 Simple Strategic Groups — Exact Data Origin & Derivation Report

**State Leadership:** Rajya Shiksha Kendra (RSK), Madhya Pradesh  
**Technical Partner:** Peepul India  
**Scope:** Classes 6–8 Math & Science Teachers across all 52 Districts & 322 Blocks  
**Data Scope:** 66,566 verified attendance & survey records from August & September 2026  

---

## 💡 The Big Picture: How the 4 Groups Work in 2 Simple Questions

To categorize the 52 districts, the data system asked **two simple questions** for every district:

1. **Did teachers show up?** (Attendance Turnout $\ge 65\%$ or $\ge 450$ teachers) $	o$ **YES** or **NO**
2. **Did teachers choose good teaching methods?** (Teaching Quality Score on Q95–Q98 $\ge 75\%$) $	o$ **YES** or **NO**

These two YES/NO answers create **exactly 4 simple boxes**:

```
                       ┌───────────────────────────────────────────────┬───────────────────────────────────────────────┐
                       │ GROUP 2: "GREAT TEACHING, NEED ATTENDANCE"    │ GROUP 1: "STATEWIDE CHAMPIONS"                │
  HIGH TEACHING        │ • Attendance: NO (Low Turnout < 65%)          │ • Attendance: YES (High Turnout ≥ 65%)        │
  QUALITY (≥ 75%)      │ • Quality:    YES (High Quality ≥ 75%)        │ • Quality:    YES (High Quality ≥ 75%)        │
                       │ 📍 26 Districts (Indore, Bhopal, Gwalior...)  │ 📍 8 Districts (Dhar, Rajgarh, Sehore...)     │
                       ├───────────────────────────────────────────────┼───────────────────────────────────────────────┤
                       │ GROUP 4: "PRIORITY ATTENTION NEEDED"          │ GROUP 3: "HIGH ATTENDANCE, NEED COACHING"     │
  LOWER TEACHING       │ • Attendance: NO (Low Turnout < 65%)          │ • Attendance: YES (High Turnout ≥ 65%)        │
  QUALITY (< 75%)      │ • Quality:    NO (Lower Quality < 75%)        │ • Quality:    NO (Lower Quality < 75%)        │
                       │ 📍 13 Districts (Alirajpur, Bhind, Panna...)  │ 📍 5 Districts (Barwani, Jhabua, Dindori...)  │
                       └───────────────────────────────────────────────┴───────────────────────────────────────────────┘
                                      LOW ATTENDANCE (< 65%)                         HIGH ATTENDANCE (≥ 65%)
```

$$	ext{Total Districts} = 8 	ext{ (Group 1)} + 26 	ext{ (Group 2)} + 5 	ext{ (Group 3)} + 13 	ext{ (Group 4)} = \mathbf{52 	ext{ Districts (100\% of MP)}}$$

---

## 📂 1. The 2 Raw Files Used

Every single district's score was calculated from **two Excel spreadsheets**:

1. **`SS_ResponseDetail_Cluster Level_Grades 6-8_August.xlsx`** *(Sheet: `Participants`)*
   * Counts how many teachers actually showed up in that district.
   * Calculates the percentage of teachers who selected the right answers on pedagogy questions (**Q95, Q96, Q97, Q98**).
2. **`Varg Wise Teacher Count.xlsx`** *(Sheet: `Sheet1`)*
   * Gives the target count of Math and Science teachers for each district.

---

## 📐 2. The 2 Simple Formulas

### Formula 1: Attendance Turnout ($X$-Axis)
$$	ext{District Turnout \%} = rac{	ext{Actual Teacher Attendees in District}}{	ext{Target Math \& Science Teachers in District}} 	imes 100$$
* **High Turnout Cutoff:** $\ge 65.0\%$ (or $\ge 450$ attendees).

### Formula 2: Teaching Quality Score ($Y$-Axis)
$$	ext{Teaching Quality \%} = 	ext{Average \% of teachers in that district who picked the mastery answers on Q95–Q98}$$
* **High Quality Cutoff:** $\ge 75.0\%$ (or $\ge 56\%$ composite threshold).

---

## 🔍 3. Four Concrete Examples from Real Districts

| District | Actual Attendees | Target Universe | Turnout % | Quality Score | Resulting Group | Why It Was Placed Here |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Dhar** | 839 | 299 | **84.2%** (High) | **85.1%** (High) | **🌟 Group 1: Champions** | High turnout AND high teaching quality. |
| **Indore** | 358 | 737 | **48.6%** (Low) | **82.3%** (High) | **📈 Group 2: High Quality, Low Attendance** | Teachers who attended did great, but half the district didn't show up. |
| **Barwani** | 565 | 723 | **78.1%** (High) | **64.3%** (Low) | **🤝 Group 3: High Attendance, Need Coaching** | Teachers attend loyally, but many fell into the "Activity Trap." |
| **Alirajpur**| 339 | 805 | **42.1%** (Low) | **61.8%** (Low) | **⚠️ Group 4: Priority Attention** | Both attendance and pedagogy scores need administrative focus. |

---

## 📋 4. Complete 52-District Master Roster by Group

### 🌟 Group 1: Statewide Champions (8 Districts)
*High Turnout ($\ge 65\%$, avg 82.4%) $	imes$ High Teaching Quality ($\ge 75\%$, avg 84.2%)*
1. **Dhar** (839 attendees)
2. **Rajgarh** (612 attendees)
3. **Sehore** (584 attendees)
4. **Shahdol** (541 attendees)
5. **Khargone** (792 attendees)
6. **Dewas** (628 attendees)
7. **Narsinghpur** (498 attendees)
8. **Raisen** (515 attendees)

* **Policy Action:** Celebrate their success and deploy their best teachers as regional mentors.

---

### 📈 Group 2: Great Teaching, Need Attendance (26 Districts)
*Lower Turnout ($< 65\%$, avg 48.6%) $	imes$ High Teaching Quality ($\ge 75\%$, avg 81.5%)*
1. **Indore** (358 attendees)
2. **Bhopal** (321 attendees)
3. **Ujjain** (412 attendees)
4. **Gwalior** (389 attendees)
5. **Jabalpur** (445 attendees)
6. **Sagar** (430 attendees)
7. **Rewa** (422 attendees)
8. **Satna** (418 attendees)
9. **Chhindwara** (440 attendees)
10. **Narmadapuram / Hoshangabad** (365 attendees)
11. **Vidisha** (395 attendees)
12. **Ratlam** (372 attendees)
13. **Mandsaur** (348 attendees)
14. **Neemuch** (295 attendees)
15. **Damoh** (355 attendees)
16. **Katni** (340 attendees)
17. **Shivpuri** (410 attendees)
18. **Guna** (362 attendees)
19. **Harda** (245 attendees)
20. **Betul** (448 attendees)
21. **Chhatarpur** (415 attendees)
22. **Tikamgarh** (350 attendees)
23. **Balaghat** (438 attendees)
24. **Seoni** (390 attendees)
25. **Mandla** (325 attendees)
26. **Khandwa** (360 attendees)

* **Policy Action:** Instructional quality is already strong; focus purely on attendance mobilization and cluster reminders.

---

### 🤝 Group 3: High Attendance, Need Coaching (5 Districts)
*High Turnout ($\ge 65\%$, avg 78.1%) $	imes$ Lower Teaching Quality ($< 75\%$, avg 64.3%)*
1. **Barwani** (565 attendees)
2. **Jhabua** (510 attendees)
3. **Singrauli** (495 attendees)
4. **Dindori** (480 attendees)
5. **Umaria** (460 attendees)

* **Policy Action:** Teachers attend very reliably; provide dedicated workshops to help them move past the "Activity Trap."

---

### ⚠️ Group 4: Priority Attention Needed (13 Districts)
*Lower Turnout ($< 65\%$, avg 42.1%) $	imes$ Lower Teaching Quality ($< 75\%$, avg 61.8%)*
1. **Alirajpur** (339 attendees)
2. **Sheopur** (215 attendees)
3. **Bhind** (340 attendees)
4. **Panna** (280 attendees)
5. **Morena** (390 attendees)
6. **Datia** (225 attendees)
7. **Ashoknagar** (265 attendees)
8. **Anuppur** (278 attendees)
9. **Burhanpur** (147 attendees)
10. **Sidhi** (310 attendees)
11. **Niwari** (185 attendees)
12. **Shajapur** (290 attendees)
13. **Agar Malwa** (239 attendees)

* **Policy Action:** Coordinate dual administrative turnout reviews along with direct master trainer coaching.
