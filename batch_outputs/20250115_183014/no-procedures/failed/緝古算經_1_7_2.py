"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex ancient Chinese math problem involving the construction of a roof (芻甍) and the division of labor between two counties (甲縣 and 乙縣). Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
- The roof has the following dimensions:
  - Top length (上袤): 3 丈
  - Bottom length (下袤): 9 丈
  - Width (廣): 6 丈
  - Height (高): 12 丈
- There are two counties:
  - 甲縣 has 632 people.
  - 乙縣 has 243 people.
- Each person can complete 36 cubic chi (尺³) of work in 8 days.
- The two counties must work together to construct the roof, starting with 甲縣.
- The task is to calculate how much of the height (高), top width (上廣), and length (袤) 甲縣 completes before 乙縣 joins.

---

### Assumptions and Calculations:
1. Convert the roof dimensions into cubic chi (尺³):
   - 1 丈 = 10 尺, so all dimensions must be converted to chi.
   - The volume of the roof is calculated as a frustum of a rectangular pyramid:
     \[
     V = \frac{1}{3} \times 高 \times (上袤 \times 廣 + 下袤 \times 廣 + \sqrt{(上袤 \times 廣) \times (下袤 \times 廣)})
     \]

2. Calculate the total work required in cubic chi.

3. Determine how much work 甲縣 completes before 乙縣 joins:
   - Each person completes 36 chi³ in 8 days.
   - Multiply the number of people in 甲縣 by their individual contribution to find the total work completed by 甲縣.

4. Use proportions to calculate how much of the height (高), top width (上廣), and length (袤) 甲縣 completes.

---

### Python Code:


"""


from fractions import Fraction
import math

# Roof dimensions in 丈
top_length = 3  # 上袤
bottom_length = 9  # 下袤
width = 6  # 廣
height = 12  # 高

# Convert dimensions to chi (1 丈 = 10 尺)
top_length_chi = top_length * 10
bottom_length_chi = bottom_length * 10
width_chi = width * 10
height_chi = height * 10

# Calculate the volume of the roof (frustum of a rectangular pyramid)
volume = Fraction(1, 3) * height_chi * (
    top_length_chi * width_chi +
    bottom_length_chi * width_chi +
    math.sqrt((top_length_chi * width_chi) * (bottom_length_chi * width_chi))
)

# Total volume in cubic chi
total_volume = volume

# County populations
county_A_population = 632  # 甲縣
county_B_population = 243  # 乙縣

# Work rate: each person completes 36 chi³ in 8 days
work_per_person = 36

# Total work completed by 甲縣 in 8 days
work_done_by_A = county_A_population * work_per_person

# Proportion of work completed by 甲縣
proportion_done_by_A = Fraction(work_done_by_A, total_volume)

# Calculate how much of the height, top width, and length 甲縣 completes
height_done_by_A = proportion_done_by_A * height_chi
top_length_done_by_A = proportion_done_by_A * top_length_chi
bottom_length_done_by_A = proportion_done_by_A * bottom_length_chi

# Convert results back to 丈
a = height_done_by_A / 10  # 高
b = top_length_done_by_A / 10  # 上廣
c = bottom_length_done_by_A / 10  # 袤

# Output results
a, b, c


"""


---

### Explanation of Results:
- `a`: The portion of the height (高) completed by 甲縣 in 丈.
- `b`: The portion of the top width (上廣) completed by 甲縣 in 丈.
- `c`: The portion of the length (袤) completed by 甲縣 in 丈.

This code calculates the exact proportions of the roof construction completed by 甲縣 before 乙縣 joins the work.
"""


"""
Code error: both arguments should be Rational instances"""
