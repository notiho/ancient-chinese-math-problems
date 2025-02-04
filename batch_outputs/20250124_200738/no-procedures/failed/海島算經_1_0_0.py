"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
答曰：島高 a里 ；去表 b里 。
"""

#----- content starts here -----
This is a classic problem of surveying using similar triangles. Let's break it down and solve it step by step.

### Problem Description:
- Two poles (or markers) are erected, each 3 zhang tall.
- The distance between the two poles is 1000 bu.
- Observations are made from two positions:
  - From the first pole, walking back 123 bu, the line of sight from the observer's eye to the top of the island aligns with the top of the pole.
  - From the second pole, walking back 127 bu, the line of sight from the observer's eye to the top of the island also aligns with the top of the pole.
- We are tasked to find:
  - The height of the island (*a* in li).
  - The distance from the second pole to the island (*b* in li).

---

### Assumptions and Conversions:
1. **1 zhang = 10 chi**  
2. **1 li = 1800 chi**  
3. **1 bu = 6 chi**

---

### Solution:
We use similar triangles to solve this problem. Let:
- \( h \) = height of the island in chi.
- \( d \) = distance from the second pole to the island in chi.

From the geometry of the problem, we can set up two equations based on similar triangles.

---

### Step 1: Convert all measurements to chi
- Height of each pole = \( 3 \times 10 = 30 \) chi.
- Distance between poles = \( 1000 \times 6 = 6000 \) chi.
- Distance walked back from the first pole = \( 123 \times 6 = 738 \) chi.
- Distance walked back from the second pole = \( 127 \times 6 = 762 \) chi.

---

### Step 2: Set up equations using similar triangles
From the first observation:
\[
\frac{h}{d + 738} = \frac{30}{738}
\]
\[
h = \frac{30 \cdot (d + 738)}{738}
\]

From the second observation:
\[
\frac{h}{d - 6000 + 762} = \frac{30}{762}
\]
\[
h = \frac{30 \cdot (d - 5238)}{762}
\]

---

### Step 3: Equate the two expressions for \( h \)
\[
\frac{30 \cdot (d + 738)}{738} = \frac{30 \cdot (d - 5238)}{762}
\]

Cancel out \( 30 \) from both sides:
\[
\frac{d + 738}{738} = \frac{d - 5238}{762}
\]

Cross-multiply:
\[
762 \cdot (d + 738) = 738 \cdot (d - 5238)
\]

Expand both sides:
\[
762d + 562056 = 738d - 3863244
\]

Simplify:
\[
762d - 738d = -3863244 - 562056
\]
\[
24d = 4425300
\]

Solve for \( d \):
\[
d = \frac{4425300}{24} = 184387.5 \, \text{chi}
\]

---

### Step 4: Solve for \( h \)
Substitute \( d = 184387.5 \) into the first equation for \( h \):
\[
h = \frac{30 \cdot (184387.5 + 738)}{738}
\]
\[
h = \frac{30 \cdot 185125.5}{738}
\]
\[
h = \frac{5553765}{738} = 7527.5 \, \text{chi}
\]

---

### Step 5: Convert results to li
- Height of the island:
\[
a = \frac{7527.5}{1800} = 4.182 \, \text{li}
\]

- Distance from the second pole to the island:
\[
b = \frac{184387.5}{1800} = 102.438 \, \text{li}
\]

---

### Final Answer:
- Island height: \( a = 4.182 \, \text{li} \)
- Distance to the island: \( b = 102.438 \, \text{li} \)#----- content ends here -----

"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
