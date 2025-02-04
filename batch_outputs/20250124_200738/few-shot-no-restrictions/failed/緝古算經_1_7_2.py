"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex ancient Chinese math problem involving the division of labor and geometry. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
1. **Given Dimensions of the Roof (芻甍):**
   - Top length (上袤): 3 丈
   - Bottom length (下袤): 9 丈
   - Width (廣): 6 丈
   - Height (高): 12 丈

2. **Labor Details:**
   - County 甲 has 632 people.
   - County 乙 has 243 people.
   - Each person completes 36 cubic chi (尺³) of work per day.
   - The work is to be completed in 8 days.

3. **Objective:**
   - Determine how much height (高), width (廣), and length (袤) County 甲 is responsible for.

4. **Procedure:**
   - Calculate the total volume of the roof.
   - Determine the total work capacity of both counties.
   - Allocate the work proportionally based on the number of people in each county.
   - Calculate the height, width, and length for County 甲 based on its allocated volume.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given dimensions of the roof (in zhang)
top_length = 3  # 上袤 (丈)
bottom_length = 9  # 下袤 (丈)
width = 6  # 廣 (丈)
height = 12  # 高 (丈)

# Labor details
county_A_people = 632  # 甲縣人數
county_B_people = 243  # 乙縣人數
work_per_person_per_day = 36  # 每人每天完成的積尺 (尺³)
work_days = 8  # 限日 (天)

# Step 1: Calculate the total volume of the roof
# The roof is a trapezoidal prism. Volume formula:
# V = (1/2) * height * (top_length + bottom_length) * width
roof_volume = Fraction(1, 2) * height * (top_length + bottom_length) * width * 1000  # Convert from 丈³ to 尺³

# Step 2: Calculate the total work capacity of both counties
total_people = county_A_people + county_B_people
total_work_capacity = total_people * work_per_person_per_day * work_days

# Step 3: Allocate the work proportionally
county_B_work = county_B_people * work_per_person_per_day * work_days
county_A_work = total_work_capacity - county_B_work

# Step 4: Calculate the height (高), width (廣), and length (袤) for County 甲
# Using the procedure described in the problem:
# 以程功乘乙縣人數，又以限日乘之，為積尺
# 以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實

# Calculate the "袤差" (difference in length between top and bottom)
length_difference = bottom_length - top_length

# Calculate the "實" (allocated volume for County 甲)
allocated_volume = county_A_work

# 高乘上袤，袤差而一，為上袤之高
top_length_height = height * top_length / length_difference

# 三因上袤之高，半之，為廉法，從
lianfa = Fraction(3) * top_length_height / 2

# 開立方除之，得乙高
county_B_height = pow(allocated_volume / lianfa, 1/3)

# Subtract from total height to get County 甲's height
county_A_height = height - county_B_height

# 求廣、袤，依率求之
county_A_width = width  # Width remains the same
county_A_length = top_length + (county_A_height / height) * length_difference

# Convert results to zhang
a = county_A_height
b = county_A_width
c = county_A_length

# Output the results
print(f"高 a = {a} 丈")
print(f"上廣 b = {b} 丈")
print(f"袤 c = {c} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Volume Calculation:** The roof is treated as a trapezoidal prism, and its volume is calculated using the formula for the volume of a trapezoid.
2. **Work Allocation:** The total work capacity of both counties is calculated based on the number of people, their daily work rate, and the number of days. The work is then allocated proportionally to each county.
3. **Height, Width, and Length Calculation:** Using the formulas provided in the problem, the height, width, and length for County 甲 are calculated based on its allocated volume.

---

### Final Answer:
The output will provide the height (`a`), width (`b`), and length (`c`) for County 甲 in zhang.
"""


"""
Variable 'a' has wrong value. Expected: 24/5, Actual: -15.245138430756313
Variable 'b' has wrong value. Expected: 18/5, Actual: 6
Variable 'c' has wrong value. Expected: 33/5, Actual: -4.622569215378157"""
