"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This problem is quite complex and involves calculating the dimensions of a trapezoidal dam (referred to as the "Dragon Tail Dam") based on the contributions of three counties. Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:

1. **Dam Dimensions**:
   - The dam starts with a height of 1丈2尺 (12尺), and the width at the top is 6尺 more than the width at the bottom.
   - The dam tapers down from head to tail, with the height and width decreasing.

2. **Workforce**:
   - Three counties (甲, 乙, 丙) contribute workers:
     - 甲: 2375 people
     - 乙: 2378 people
     - 丙: 5247 people
   - Each person completes 1尺9寸8分 (1.98尺) of work per day.

3. **Goal**:
   - Calculate the total height, width, and length of the dam.
   - Determine the portion of the dam built by each county.

---

### Python Code:


"""


from fractions import Fraction

# Constants
甲人數 = 2375
乙人數 = 2378
丙人數 = 5247

每人日功 = Fraction(1, 1) + Fraction(9, 10) + Fraction(8, 100)  # 1尺9寸8分 = 1.98尺

# Total work completed by each county
甲總功 = 甲人數 * 每人日功
乙總功 = 乙人數 * 每人日功
丙總功 = 丙人數 * 每人日功

# Total work for all counties
總功 = 甲總功 + 乙總功 + 丙總功

# Dam dimensions
堤頭高 = 12  # 1丈2尺 = 12尺
堤頭上下廣差 = 6  # 6尺
堤尾高 = 0  # Tapers to 0 at the tail
堤尾袤 = 48  # 4丈8尺 = 48尺

# Calculate the total length (袤) of the dam
堤袤 = 總功 / ((堤頭高 + 堤尾高) / 2)  # Using the trapezoidal volume formula

# Calculate the portion of the dam built by each county
甲袤 = 甲總功 / 總功 * 堤袤
乙袤 = 乙總功 / 總功 * 堤袤
丙袤 = 丙總功 / 總功 * 堤袤

# Calculate the width at the top and bottom for each county
甲高 = 堤頭高 * (甲袤 / 堤袤)
乙高 = 堤頭高 * (乙袤 / 堤袤)
丙高 = 堤頭高 * (丙袤 / 堤袤)

甲上廣 = 堤頭上下廣差 * (甲袤 / 堤袤)
乙上廣 = 堤頭上下廣差 * (乙袤 / 堤袤)
丙上廣 = 堤頭上下廣差 * (丙袤 / 堤袤)

# Final Results
a = 堤頭高
b = 堤頭上下廣差
c = 堤尾高
d = 堤袤

e, f, g = 甲高, 甲袤, 甲上廣
h, i, j = 乙高, 乙袤, 乙上廣
k, l, m = 丙高, 丙袤, 丙上廣

print(f"總堤高: {a}丈, 上廣: {b}丈, 下廣: {c}丈, 袤: {d}丈")
print(f"甲縣: 高 {e}丈, 袤 {f}丈, 上廣 {g}丈")
print(f"乙縣: 高 {h}丈, 袤 {i}丈, 上廣 {j}丈")
print(f"丙縣: 高 {k}丈, 袤 {l}丈, 上廣 {m}丈")


"""


---

### Explanation of the Code:

1. **Workforce Calculations**:
   - Each person's daily work is converted into fractional units of 尺.
   - The total work for each county is calculated by multiplying the number of workers by their daily work.

2. **Dam Dimensions**:
   - The total length (袤) of the dam is calculated using the trapezoidal volume formula.
   - The height and width contributions of each county are proportional to the work they completed.

3. **Output**:
   - The total dimensions of the dam are printed.
   - The contributions of each county are broken down into height, length, and width.

---

This code provides a detailed breakdown of the dam's dimensions and the contributions of each county based on their workforce.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 12
Variable 'b' has wrong value. Expected: 17/5, Actual: 6
Variable 'c' has wrong value. Expected: 9/5, Actual: 0
Variable 'd' has wrong value. Expected: 33/5, Actual: 3300.0
Variable 'e' has wrong value. Expected: 3/2, Actual: 2.8499999999999996
Variable 'f' has wrong value. Expected: 33/10, Actual: 783.75
Variable 'g' has wrong value. Expected: 21/10, Actual: 1.4249999999999998
Variable 'h' has wrong value. Expected: 21/10, Actual: 2.8536
Variable 'i' has wrong value. Expected: 33/25, Actual: 784.74
Variable 'j' has wrong value. Expected: 111/50, Actual: 1.4268
Variable 'k' has wrong value. Expected: 3, Actual: 6.2964
Variable 'l' has wrong value. Expected: 99/50, Actual: 1731.5100000000002
Variable 'm' has wrong value. Expected: 12/5, Actual: 3.1482"""
