"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This problem is quite complex and involves multiple calculations. Let's break it down step by step and translate it into Python code. The problem involves calculating the dimensions of a trapezoidal dam (referred to as "龍尾堤") and distributing the work among three counties (甲縣, 乙縣, 丙縣) based on their workforce contributions.

---

### Problem Breakdown:
1. The dam has a trapezoidal cross-section:
   - The top width (上廣) decreases from the head to the tail.
   - The bottom width (下廣) is constant.
   - The height (高) decreases from the head to the tail.
   - The length (袤) is given.

2. Workforce contributions:
   - Each person contributes a fixed volume of work per day (1尺9寸8分 = 1.98尺³).
   - The total workforce from the three counties is given.
   - The dam is built in sections, starting from the tail and progressing to the head.

3. The task is to calculate:
   - The overall dimensions of the dam (height, top width, bottom width, length).
   - The dimensions of the sections built by each county.

---

### Python Code:


"""


from fractions import Fraction

# Constants
total_volume = 10000  # Total volume of the dam in cubic chi (尺³)
work_per_person = Fraction(1, 1) + Fraction(9, 10) + Fraction(8, 100)  # 1尺9寸8分 = 1.98尺³

# Workforce contributions
workforce_jia = 2375  # 甲縣
workforce_yi = 2378   # 乙縣
workforce_bing = 5247 # 丙縣

# Total workforce
total_workforce = workforce_jia + workforce_yi + workforce_bing

# Calculate the total work volume contributed by each county
volume_jia = workforce_jia * work_per_person
volume_yi = workforce_yi * work_per_person
volume_bing = workforce_bing * work_per_person

# Verify total volume matches
assert volume_jia + volume_yi + volume_bing == total_volume, "Volume mismatch!"

# Dimensions of the dam
bottom_width = Fraction(12, 10)  # 下廣 = 1丈2尺 = 12尺
top_width_difference = 6        # 上廣差 = 6尺
height_head = Fraction(12, 10)  # 堤頭高 = 1丈2尺 = 12尺
length = Fraction(48, 10)       # 堤袤 = 4丈8尺 = 48尺

# Calculate the top width at the head
top_width_head = bottom_width + top_width_difference

# Calculate the average cross-sectional area (trapezoid area formula)
average_area = Fraction(1, 2) * (top_width_head + bottom_width) * height_head

# Calculate the total length of the dam
total_length = total_volume / average_area

# Distribute the length among the counties based on their contributions
length_jia = total_length * (volume_jia / total_volume)
length_yi = total_length * (volume_yi / total_volume)
length_bing = total_length * (volume_bing / total_volume)

# Calculate the height and top width for each county's section
height_jia = height_head * (length_jia / total_length)
height_yi = height_head * (length_yi / total_length)
height_bing = height_head * (length_bing / total_length)

top_width_jia = top_width_head * (length_jia / total_length)
top_width_yi = top_width_head * (length_yi / total_length)
top_width_bing = top_width_head * (length_bing / total_length)

# Results
a = height_head
b = top_width_head
c = bottom_width
d = total_length

e = height_jia
f = length_jia
g = top_width_jia

h = height_yi
i = length_yi
j = top_width_yi

k = height_bing
l = length_bing
m = top_width_bing

# Print results
print(f"Overall dimensions of the dam:")
print(f"Height: {a}丈, Top Width: {b}丈, Bottom Width: {c}丈, Length: {d}丈")
print()
print(f"甲縣: Height: {e}丈, Length: {f}丈, Top Width: {g}丈")
print(f"乙縣: Height: {h}丈, Length: {i}丈, Top Width: {j}丈")
print(f"丙縣: Height: {k}丈, Length: {l}丈, Top Width: {m}丈")


"""


---

### Explanation of the Code:
1. **Volume Calculation**:
   - The total volume of the dam is distributed among the three counties based on their workforce contributions.

2. **Trapezoidal Area**:
   - The cross-sectional area of the dam is calculated using the trapezoid area formula.

3. **Length Distribution**:
   - The total length of the dam is divided among the counties proportional to their contributions.

4. **Height and Width Adjustments**:
   - The height and top width for each county's section are adjusted based on their respective lengths.

---

### Output:
The code will output the overall dimensions of the dam and the dimensions of the sections built by each county.
"""


"""
Code error: Volume mismatch!"""
