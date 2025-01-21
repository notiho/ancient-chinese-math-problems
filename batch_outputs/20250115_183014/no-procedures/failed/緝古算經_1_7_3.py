"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex ancient Chinese math problem involving the construction of a roof (芻甍) with specific dimensions and labor contributions from two counties (甲縣 and 乙縣). Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Roof Dimensions**:
   - Top length (上袤): 3 丈
   - Bottom length (下袤): 9 丈
   - Width (廣): 6 丈
   - Height (高): 12 丈

2. **Labor Contributions**:
   - County 甲 has 632 people.
   - County 乙 has 243 people.
   - Each person can complete 36 cubic chi (尺³) of work in 8 days.

3. **Task**:
   - County 甲 arrives first and starts working.
   - Determine how much of the roof (in terms of height, width, and length) County 甲 completes before County 乙 joins.

---

### Assumptions:
- The roof is a trapezoidal prism.
- The total volume of the roof is calculated using the formula for a trapezoidal prism:
  \[
  V = \frac{(上袤 + 下袤)}{2} \times 廣 \times 高
  \]
- Work is distributed proportionally to the labor contribution of each county.

---

### Python Code:


"""


from fractions import Fraction

# Roof dimensions
top_length = 3  # 上袤 (丈)
bottom_length = 9  # 下袤 (丈)
width = 6  # 廣 (丈)
height = 12  # 高 (丈)

# Convert dimensions to chi (1 丈 = 10 尺)
top_length_chi = top_length * 10
bottom_length_chi = bottom_length * 10
width_chi = width * 10
height_chi = height * 10

# Calculate total volume of the roof (in cubic chi)
volume = Fraction((top_length_chi + bottom_length_chi), 2) * width_chi * height_chi

# Labor contributions
county_A_people = 632  # 甲縣
county_B_people = 243  # 乙縣
work_per_person = 36  # 每人功當積 36 尺³
days = 8  # 限 8 日役

# Total work completed by each county
county_A_work = county_A_people * work_per_person
county_B_work = county_B_people * work_per_person

# Total work completed in 8 days
total_work = county_A_work + county_B_work

# Proportion of work completed by County A
county_A_ratio = Fraction(county_A_work, total_work)

# Volume completed by County A
county_A_volume = county_A_ratio * volume

# Determine how much of the roof County A completes
# Start with height (高), then adjust width (廣) and length (袤) proportionally

# Proportion of height completed by County A
height_completed = county_A_volume / (Fraction((top_length_chi + bottom_length_chi), 2) * width_chi)

# Convert back to 丈
a = height_completed / 10  # 高 a 丈

# Proportion of width completed by County A
width_completed = width_chi  # Width remains constant
b = width_completed / 10  # 上廣 b 丈

# Proportion of length completed by County A
length_completed = county_A_volume / (width_chi * height_completed)
c = length_completed / 10  # 袤 c 丈

# Results
print(f"高 a 丈: {a}")
print(f"上廣 b 丈: {b}")
print(f"袤 c 丈: {c}")


"""


---

### Explanation of the Code:
1. **Volume Calculation**:
   - The roof's volume is calculated using the trapezoidal prism formula.
   - All dimensions are converted from 丈 to 尺 for consistency.

2. **Labor Contribution**:
   - The total work completed by each county is calculated based on the number of people and their productivity.

3. **Proportional Work**:
   - The proportion of the roof completed by County 甲 is determined based on its labor contribution.

4. **Roof Dimensions**:
   - The height, width, and length of the roof completed by County 甲 are calculated proportionally.

---

### Output:
The code will output the height (高), width (廣), and length (袤) of the roof completed by County 甲 in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 24/5, Actual: 7584/875
Variable 'b' has wrong value. Expected: 18/5, Actual: 6.0
Variable 'c' has wrong value. Expected: 33/5, Actual: 6"""
