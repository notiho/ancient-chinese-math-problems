"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This problem involves calculating the portion of work that County A (甲縣) completes before County B (乙縣) arrives, based on the given dimensions of the structure and the work rate of the counties.

---

### Problem Breakdown:
1. **Structure Dimensions**:
   - Top length (上袤): 3 丈
   - Bottom length (下袤): 9 丈
   - Width (廣): 6 丈
   - Height (高): 12 丈

2. **Workforce**:
   - County A (甲縣): 632 people
   - County B (乙縣): 243 people

3. **Work Rate**:
   - Each person completes 36 cubic chi (尺³) of work in 8 days.

4. **Question**:
   - County A starts working first. How much of the height (高), top length (上廣), and length (袤) does County A complete before County B arrives?

---

### Solution in Python:


"""


from fractions import Fraction

# Structure dimensions
top_length = 3  # 上袤 (丈)
bottom_length = 9  # 下袤 (丈)
width = 6  # 廣 (丈)
height = 12  # 高 (丈)

# Workforce
county_a_people = 632  # 甲縣人數
county_b_people = 243  # 乙縣人數

# Work rate
work_per_person = Fraction(36, 8)  # 每人每日完成的尺³

# Total work volume of the structure (trapezoidal prism volume formula)
total_volume = Fraction(1, 2) * (top_length + bottom_length) * width * height * 1000  # Convert 丈³ to 尺³

# County A's daily work capacity
county_a_daily_work = county_a_people * work_per_person

# County A works alone for 1 day
county_a_work_done = county_a_daily_work * 1  # Work completed by County A before County B arrives

# Proportion of work completed by County A
work_proportion = county_a_work_done / total_volume

# Calculate the portion of height, top length, and length completed by County A
a = work_proportion * height  # 高
b = work_proportion * width  # 上廣
c = work_proportion * (top_length + bottom_length) / 2  # 袤 (average of top and bottom lengths)

# Results
a = float(a)  # 高 (in 丈)
b = float(b)  # 上廣 (in 丈)
c = float(c)  # 袤 (in 丈)

print(f"高 a = {a} 丈")
print(f"上廣 b = {b} 丈")
print(f"袤 c = {c} 丈")


"""


---

### Explanation of the Code:
1. **Volume Calculation**:
   - The structure is a trapezoidal prism, so its volume is calculated using the formula:
     \[
     V = \frac{1}{2} \times (\text{Top Length} + \text{Bottom Length}) \times \text{Width} \times \text{Height}
     \]
   - The result is converted from 丈³ to 尺³ by multiplying by 1000 (since 1 丈³ = 1000 尺³).

2. **Work Rate**:
   - Each person completes 36 尺³ of work in 8 days, so the daily work rate is \( \frac{36}{8} \) 尺³ per person.

3. **County A's Work**:
   - County A works alone for 1 day, so the total work completed is:
     \[
     \text{County A Work} = \text{County A People} \times \text{Daily Work Rate}
     \]

4. **Proportion of Work**:
   - The proportion of the total work completed by County A is:
     \[
     \text{Work Proportion} = \frac{\text{County A Work}}{\text{Total Volume}}
     \]

5. **Dimensions Completed**:
   - The proportion of work completed is applied to the height, width, and average length (袤) to determine how much of each dimension is completed by County A.

---

### Final Answer:
The values of \( a \), \( b \), and \( c \) will be printed as the portions of the height, width, and length completed by County A before County B arrives.
"""


"""
Variable 'a' has wrong value. Expected: 24/5, Actual: 0.079
Variable 'b' has wrong value. Expected: 18/5, Actual: 0.0395
Variable 'c' has wrong value. Expected: 33/5, Actual: 0.0395"""
