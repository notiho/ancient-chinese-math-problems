"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This problem is a complex ancient Chinese mathematical problem involving the construction of a "Dragon Tail Dam" with varying dimensions and contributions from three counties. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
1. The dam has a trapezoidal cross-section:
   - The height decreases from the head to the tail.
   - The width at the top and bottom also decreases from the head to the tail.
   - The difference between the top and bottom widths at the head is 6 chi.
   - The bottom width at the tail is 1 zhang 2 chi (12 chi).
   - The length at the tail is 4 zhang 8 chi (48 chi).

2. Three counties (甲, 乙, 丙) contribute labor:
   - 甲县: 2375 people
   - 乙县: 2378 people
   - 丙县: 5247 people
   - Each person completes 1 chi 9 cun 8 fen (1.98 chi) of work per day.

3. The dam is constructed from the tail to the head, with each county contributing sequentially.

4. The task is to calculate:
   - The total height, top width, bottom width, and length of the dam.
   - The height, length, and top width contributed by each county.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
甲縣人數 = 2375
乙縣人數 = 2378
丙縣人數 = 5247
每人每日功 = Fraction(198, 100)  # 1 chi 9 cun 8 fen = 1.98 chi

# Total work done by each county
甲縣總功 = 甲縣人數 * 每人每日功
乙縣總功 = 乙縣人數 * 每人每日功
丙縣總功 = 丙縣人數 * 每人每日功
總功 = 甲縣總功 + 乙縣總功 + 丙縣總功

# Dimensions of the dam
尾下廣 = 12  # 1 zhang 2 chi = 12 chi
尾袤 = 48  # 4 zhang 8 chi = 48 chi
頭上下廣差 = 6  # Difference between top and bottom width at the head

# Calculate the total bottom width, top width, and height
總下廣 = 尾下廣 + 頭上下廣差
總上廣 = 總下廣 + 頭上下廣差
總袤 = 總功 / ((總上廣 + 總下廣) / 2)  # Using the trapezoidal area formula
總高 = 總袤 / 尾袤  # Proportional to the length

# Contributions by each county
甲縣袤 = 甲縣總功 / ((總上廣 + 總下廣) / 2)
乙縣袤 = 乙縣總功 / ((總上廣 + 總下廣) / 2)
丙縣袤 = 丙縣總功 / ((總上廣 + 總下廣) / 2)

甲縣高 = 甲縣袤 / 總袤 * 總高
乙縣高 = 乙縣袤 / 總袤 * 總高
丙縣高 = 丙縣袤 / 總袤 * 總高

甲縣上廣 = 總上廣 * (甲縣袤 / 總袤)
乙縣上廣 = 總上廣 * (乙縣袤 / 總袤)
丙縣上廣 = 總上廣 * (丙縣袤 / 總袤)

# Results
a = 總高
b = 總上廣
c = 總下廣
d = 總袤

e = 甲縣高
f = 甲縣袤
g = 甲縣上廣

h = 乙縣高
i = 乙縣袤
j = 乙縣上廣

k = 丙縣高
l = 丙縣袤
m = 丙縣上廣

# Output
print(f"總高: {a}丈, 總上廣: {b}丈, 總下廣: {c}丈, 總袤: {d}丈")
print(f"甲縣: 高 {e}丈, 袤 {f}丈, 上廣 {g}丈")
print(f"乙縣: 高 {h}丈, 袤 {i}丈, 上廣 {j}丈")
print(f"丙縣: 高 {k}丈, 袤 {l}丈, 上廣 {m}丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Work Calculation**:
   - Each county's total work is calculated by multiplying the number of people by the work done per person per day.

2. **Dam Dimensions**:
   - The total bottom width, top width, and length are calculated using the given proportions and the trapezoidal area formula.

3. **County Contributions**:
   - Each county's contribution to the length, height, and top width is proportional to the work they contributed.

4. **Output**:
   - The results are printed in terms of zhang (丈), chi (尺), and cun (寸) where necessary.

This code provides a step-by-step solution to the problem while adhering to the ancient mathematical principles described in the problem statement.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 19.642857142857142
Variable 'b' has wrong value. Expected: 17/5, Actual: 24
Variable 'c' has wrong value. Expected: 9/5, Actual: 18
Variable 'd' has wrong value. Expected: 33/5, Actual: 942.8571428571429
Variable 'e' has wrong value. Expected: 3/2, Actual: 4.665178571428571
Variable 'f' has wrong value. Expected: 33/10, Actual: 223.92857142857142
Variable 'g' has wrong value. Expected: 21/10, Actual: 5.699999999999999
Variable 'h' has wrong value. Expected: 21/10, Actual: 4.671071428571428
Variable 'i' has wrong value. Expected: 33/25, Actual: 224.21142857142854
Variable 'j' has wrong value. Expected: 111/50, Actual: 5.7071999999999985
Variable 'k' has wrong value. Expected: 3, Actual: 10.30660714285714
Variable 'l' has wrong value. Expected: 99/50, Actual: 494.71714285714285
Variable 'm' has wrong value. Expected: 12/5, Actual: 12.592799999999999"""
