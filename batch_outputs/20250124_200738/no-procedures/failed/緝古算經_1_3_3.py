"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This is a complex problem involving the construction of a "Dragon Tail Dike" with varying dimensions and contributions from three counties. Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. The dike has a trapezoidal cross-section:
   - The top width (`上廣`) is greater than the bottom width (`下廣`) by 6 chi.
   - The bottom width (`下廣`) is 1 zhang 2 chi (12 chi).
   - The height (`高`) decreases from the head to the tail.

2. The length of the dike (`袤`) is 4 zhang 8 chi (48 chi).

3. The total number of workers from three counties:
   - County A: 2375 workers
   - County B: 2378 workers
   - County C: 5247 workers

4. Each worker completes a volume of **1 chi 9 cun 8 fen** (1.98 chi³) per day.

5. The dike is constructed in order:
   - County A starts from the tail.
   - County B continues from where County A stops.
   - County C finishes the remaining portion.

6. The task is to calculate:
   - The total dimensions of the dike: height (`高`), top width (`上廣`), bottom width (`下廣`), and length (`袤`).
   - The portion of the dike constructed by each county: height, length, and top width.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
下廣 = 12  # Bottom width in chi (1 zhang 2 chi)
上廣差 = 6  # Difference between top and bottom width in chi
袤 = 48  # Total length of the dike in chi
每人程功 = Fraction(198, 100)  # Volume completed by each worker in chi³ (1 chi 9 cun 8 fen)

# Workers from each county
甲縣人數 = 2375
乙縣人數 = 2378
丙縣人數 = 5247

# Total volume completed by each county
甲縣體積 = 甲縣人數 * 每人程功
乙縣體積 = 乙縣人數 * 每人程功
丙縣體積 = 丙縣人數 * 每人程功

# Total volume of the dike
總體積 = 甲縣體積 + 乙縣體積 + 丙縣體積

# Dimensions of the dike
上廣 = 下廣 + 上廣差  # Top width in chi
高 = Fraction(總體積, 袤 * (上廣 + 下廣) / 2)  # Height in chi

# Portion of the dike constructed by each county
甲縣袤 = Fraction(甲縣體積, 高 * (上廣 + 下廣) / 2)
乙縣袤 = Fraction(乙縣體積, 高 * (上廣 + 下廣) / 2)
丙縣袤 = Fraction(丙縣體積, 高 * (上廣 + 下廣) / 2)

# Results
a = 高 / 10  # Total height in zhang
b = 上廣 / 10  # Top width in zhang
c = 下廣 / 10  # Bottom width in zhang
d = 袤 / 10  # Total length in zhang

e = 高 / 10  # Height for County A in zhang (same for all counties)
f = 甲縣袤 / 10  # Length for County A in zhang
g = 上廣 / 10  # Top width for County A in zhang (same for all counties)

h = 高 / 10  # Height for County B in zhang
i = 乙縣袤 / 10  # Length for County B in zhang
j = 上廣 / 10  # Top width for County B in zhang

k = 高 / 10  # Height for County C in zhang
l = 丙縣袤 / 10  # Length for County C in zhang
m = 上廣 / 10  # Top width for County C in zhang

# Output
print(f"Total dimensions of the dike:")
print(f"Height: {a} zhang, Top Width: {b} zhang, Bottom Width: {c} zhang, Length: {d} zhang")

print(f"County A contribution:")
print(f"Height: {e} zhang, Length: {f} zhang, Top Width: {g} zhang")

print(f"County B contribution:")
print(f"Height: {h} zhang, Length: {i} zhang, Top Width: {j} zhang")

print(f"County C contribution:")
print(f"Height: {k} zhang, Length: {l} zhang, Top Width: {m} zhang")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Volume Calculation**:
   - The volume of a trapezoidal prism is calculated as:
     \[
     V = \text{Length} \times \frac{\text{Top Width} + \text{Bottom Width}}{2} \times \text{Height}
     \]
   - Using this formula, the total height of the dike is calculated based on the total volume.

2. **County Contributions**:
   - Each county's contribution is proportional to the volume they excavated.
   - The length of the dike constructed by each county is calculated by dividing their volume by the cross-sectional area of the dike.

3. **Unit Conversion**:
   - All dimensions are converted from chi to zhang (1 zhang = 10 chi) for the final output.

---

### Output:
The code will output the total dimensions of the dike and the contributions of each county in terms of height, length, and top width.
"""


"""
Code error: both arguments should be Rational instances"""
