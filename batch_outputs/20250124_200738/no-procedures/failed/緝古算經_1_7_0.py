"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This problem involves calculating the contribution of two counties (甲縣 and 乙縣) in constructing a structure based on their respective populations and work capacity. Let's break it down step by step and solve it.

---

### Problem Breakdown:
1. The structure has the following dimensions:
   - Top length (上袤): 3 丈
   - Bottom length (下袤): 9 丈
   - Width (廣): 6 丈
   - Height (高): 12 丈

2. The total population of the two counties:
   - 甲縣: 632 people
   - 乙縣: 243 people

3. Work capacity:
   - Each person can complete 36 cubic chi (尺³) in 8 days.

4. The two counties will work together to construct the structure, but 甲縣 arrives first and starts working alone.

5. The question asks for the contribution of 甲縣 in terms of:
   - Height (高)
   - Top width (上廣)
   - Length (袤)

---

### Solution:


"""

#----- content starts here -----

from fractions import Fraction

# Structure dimensions
top_length = 3  # 上袤 (丈)
bottom_length = 9  # 下袤 (丈)
width = 6  # 廣 (丈)
height = 12  # 高 (丈)

# Population of the two counties
population_jia = 632  # 甲縣
population_yi = 243  # 乙縣

# Work capacity per person
work_capacity_per_person = 36  # 尺³ in 8 days

# Total work capacity for each county in 8 days
work_capacity_jia = population_jia * work_capacity_per_person
work_capacity_yi = population_yi * work_capacity_per_person

# Total volume of the structure (trapezoidal prism)
# Volume = (1/2) * (top_length + bottom_length) * width * height
volume = Fraction(1, 2) * (top_length + bottom_length) * width * height * 1000  # Convert 丈³ to 尺³

# Contribution of 甲縣
jia_contribution = Fraction(work_capacity_jia, work_capacity_jia + work_capacity_yi) * volume

# Calculate the height (高), top width (上廣), and length (袤) contributed by 甲縣
# Height contribution (proportional to total height)
height_contribution = Fraction(jia_contribution, volume) * height

# Top width contribution (proportional to total top length)
top_length_contribution = Fraction(jia_contribution, volume) * top_length

# Length contribution (proportional to total bottom length)
bottom_length_contribution = Fraction(jia_contribution, volume) * bottom_length

# Results
a = height_contribution  # 高
b = top_length_contribution  # 上廣
c = bottom_length_contribution  # 袤

# Output results
a, b, c
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Volume Calculation**: The volume of the structure is calculated using the formula for a trapezoidal prism:
   \[
   V = \frac{1}{2} \times (\text{top length} + \text{bottom length}) \times \text{width} \times \text{height}
   \]
   The result is converted from 丈³ to 尺³ by multiplying by 1000 (since 1 丈³ = 1000 尺³).

2. **Work Capacity**: The total work capacity for each county is calculated based on their population and the work capacity per person.

3. **Contribution of 甲縣**: The contribution of 甲縣 is proportional to its work capacity relative to the total work capacity of both counties.

4. **Height, Top Width, and Length Contribution**: The contributions of 甲縣 to the height, top width, and length are calculated proportionally based on its contribution to the total volume.

---

### Final Answer:
The values of \( a \), \( b \), and \( c \) represent the contributions of 甲縣 to the height, top width, and length, respectively, in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 24/5, Actual: 7584/875
Variable 'b' has wrong value. Expected: 18/5, Actual: 1896/875
Variable 'c' has wrong value. Expected: 33/5, Actual: 5688/875"""
