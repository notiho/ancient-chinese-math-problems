"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex ancient Chinese math problem involving shared labor and geometry. Let's break it down step by step and translate it into Python code.

### Problem Description:
- A roof structure (芻甍) has the following dimensions:
  - Top length (上袤): 3 zhang
  - Bottom length (下袤): 9 zhang
  - Width (廣): 6 zhang
  - Height (高): 12 zhang
- Two counties, 甲縣 and 乙縣, are tasked with building this structure:
  - 甲縣 has 632 people.
  - 乙縣 has 243 people.
- Each person can complete 36 cubic chi of work per day.
- The work must be completed in 8 days.
- 甲縣 arrives first and starts working. The task is to calculate how much height (高), width (廣), and length (袤) 甲縣 must complete before 乙縣 arrives.

The procedure involves calculating the shared workload based on the number of people, their productivity, and the geometric properties of the roof.

---

### Step-by-Step Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given dimensions of the roof (in zhang)
上袤 = 3  # Top length (zhang)
下袤 = 9  # Bottom length (zhang)
廣 = 6    # Width (zhang)
高 = 12   # Height (zhang)

# Given labor details
甲縣人數 = 632  # Number of people in 甲縣
乙縣人數 = 243  # Number of people in 乙縣
每日人功 = 36    # Cubic chi per person per day
限日 = 8         # Number of days

# Step 1: Calculate the total workload (積尺) for 乙縣
乙積尺 = 每日人功 * 乙縣人數 * 限日

# Step 2: Calculate the total volume of the roof (實)
# Formula: ((下袤 - 上袤) * 廣 * 高) / 2
袤差 = 下袤 - 上袤
實 = Fraction(袤差 * 廣 * 高, 2)

# Step 3: Calculate the height contributed by 乙縣 (乙高)
# Formula: 乙高 = ((6 * 乙積尺) / ((袤差 * 廣) / 2))^(1/3)
廉法 = Fraction(袤差 * 廣, 2)
乙高 = pow((6 * 乙積尺) / 廉法, 1/3)

# Step 4: Calculate the height contributed by 甲縣 (甲高)
甲高 = 高 - 乙高

# Step 5: Calculate the width (廣) and length (袤) for 甲縣
# The width and length are proportional to the height
甲廣 = 廣 * (甲高 / 高)
甲袤 = 上袤 + (袤差 * (甲高 / 高))

# Final Answer
a = Fraction(甲高).limit_denominator()  # Height (zhang)
b = Fraction(甲廣).limit_denominator()  # Width (zhang)
c = Fraction(甲袤).limit_denominator()  # Length (zhang)

print(f"答曰：高 {a}丈 ，上廣 {b}丈 ，袤 {c}丈 。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Roof Geometry**:
   - The roof is a trapezoidal prism, so its volume is calculated using the formula for the volume of a trapezoid:  
     \[
     \text{Volume} = \frac{(\text{Bottom Length} - \text{Top Length}) \times \text{Width} \times \text{Height}}{2}
     \]

2. **Labor Distribution**:
   - The workload is divided proportionally between the two counties based on their population and productivity.

3. **Height Calculation**:
   - The height completed by 乙縣 is calculated using the cubic root of the ratio of their workload to the roof's geometry.

4. **Width and Length**:
   - The width and length for 甲縣 are proportional to the height they complete.

---

### Example Output:
If you run the code, it will calculate the height, width, and length completed by 甲縣 in terms of zhang. The results will be expressed as fractions for precision.
"""


"""
Variable 'a' has wrong value. Expected: 24/5, Actual: -12532519/756191
Variable 'b' has wrong value. Expected: 18/5, Actual: -7679259/926707
Variable 'c' has wrong value. Expected: 33/5, Actual: -4899138/926707"""
