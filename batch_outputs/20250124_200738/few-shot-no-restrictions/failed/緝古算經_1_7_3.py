"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex ancient Chinese math problem involving shared labor and geometry. Let's break it down step by step and translate it into Python code.

### Problem Explanation:
- A roof structure (芻甍) has the following dimensions:
  - Top length (上袤): 3 zhang
  - Bottom length (下袤): 9 zhang
  - Width (廣): 6 zhang
  - Height (高): 12 zhang
- Two counties, 甲縣 and 乙縣, are tasked with constructing this structure:
  - 甲縣 has 632 people.
  - 乙縣 has 243 people.
- Each person can complete 36 cubic chi of work per day (夏程人功當積三十六尺).
- The work must be completed in 8 days (限八日役).
- 甲縣 arrives first and begins the work. The task is to determine how much of the height, width, and length of the roof each county is responsible for.

The solution involves:
1. Calculating the total work required.
2. Dividing the work between the two counties based on their workforce.
3. Allocating the height, width, and length of the roof accordingly.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Roof dimensions
上袤 = 3  # Top length (zhang)
下袤 = 9  # Bottom length (zhang)
廣 = 6    # Width (zhang)
高 = 12   # Height (zhang)

# County populations
甲縣人數 = 632
乙縣人數 = 243

# Work parameters
夏程人功 = 36  # Cubic chi per person per day
限日 = 8       # Days to complete the work

# Step 1: Calculate the total work required (volume of the roof)
# The roof is a trapezoidal prism. Its volume is:
# V = (1/2) * 高 * (上袤 + 下袤) * 廣
總積尺 = Fraction(1, 2) * 高 * (上袤 + 下袤) * 廣 * 1000  # Convert zhang^3 to chi^3

# Step 2: Calculate the total work capacity of each county
乙縣積尺 = 夏程人功 * 乙縣人數 * 限日  # Total work capacity of 乙縣
甲縣積尺 = 總積尺 - 乙縣積尺          # Remaining work for 甲縣

# Step 3: Calculate the height (高) each county is responsible for
# Using the formula provided in the problem:
# 高乘上袤，袤差而一，為上袤之高
袤差 = 下袤 - 上袤
上袤之高 = 高 * 上袤 / 袤差

# 三因上袤之高，半之，為廉法，從
廉法 = Fraction(3, 2) * 上袤之高

# 開立方除之，得乙高
乙高 = pow(乙縣積尺 / 廉法, Fraction(1, 3))

# 以減甍高，余即甲高
甲高 = 高 - 乙高

# Step 4: Calculate the width (廣) and length (袤) for 甲縣
# The width and length are proportional to the height
甲廣 = 廣 * 甲高 / 高
甲袤 = (上袤 + (袤差 * 甲高 / 高))

# Final answers
a = 甲高  # Height for 甲縣
b = 甲廣  # Width for 甲縣
c = 甲袤  # Length for 甲縣

print(f"答曰：高 {a}丈 ，上廣 {b}丈 ，袤 {c}丈 。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Volume Calculation**:
   - The roof is a trapezoidal prism, so its volume is calculated using the formula for the volume of a trapezoid: \( V = \frac{1}{2} \times 高 \times (上袤 + 下袤) \times 廣 \).
   - The result is converted from zhang³ to chi³ by multiplying by 1000 (since 1 zhang = 10 chi).

2. **Work Allocation**:
   - The total work capacity of each county is calculated based on the number of people, their daily work rate, and the number of days.

3. **Height Allocation**:
   - The formula provided in the problem is used to calculate how much of the height each county is responsible for.

4. **Width and Length Allocation**:
   - The width and length are proportional to the height, so they are scaled accordingly.

---

### Example Output:
If you run the code, it will calculate the height, width, and length for 甲縣 based on the given inputs. The results will be in zhang.
"""


"""
Variable 'a' has wrong value. Expected: 24/5, Actual: -7.811563493367757
Variable 'b' has wrong value. Expected: 18/5, Actual: -3.9057817466838785
Variable 'c' has wrong value. Expected: 33/5, Actual: -0.9057817466838785"""
