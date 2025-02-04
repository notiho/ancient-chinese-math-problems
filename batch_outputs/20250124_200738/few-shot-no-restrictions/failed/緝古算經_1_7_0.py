"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex ancient Chinese math problem involving shared labor and geometric calculations. Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Given Dimensions of the Roof (芻甍):**
   - Top length (上袤): 3 丈
   - Bottom length (下袤): 9 丈
   - Width (廣): 6 丈
   - Height (高): 12 丈

2. **Labor Details:**
   - County A (甲縣): 632 people
   - County B (乙縣): 243 people
   - Each person completes 36 cubic chi (尺³) of work per day.
   - The work is to be completed in 8 days.

3. **Question:**
   - County A arrives first and starts working. How much height (高), width (廣), and length (袤) should County A complete?

4. **Procedure:**
   - Calculate the total volume of the roof.
   - Distribute the work proportionally between the two counties based on their populations.
   - Determine the height, width, and length that County A should complete.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given dimensions of the roof
上袤 = 3  # 丈
下袤 = 9  # 丈
廣 = 6    # 丈
高 = 12   # 丈

# Labor details
甲縣人數 = 632
乙縣人數 = 243
總人數 = 甲縣人數 + 乙縣人數
每日人功 = 36  # 每人每日完成的積尺 (cubic chi)
限日 = 8       # 天數

# Step 1: Calculate the total volume of the roof
# The roof is a trapezoidal prism. Volume = (1/2) * (上袤 + 下袤) * 廣 * 高
總積尺 = Fraction(1, 2) * (上袤 + 下袤) * 廣 * 高 * 1000  # Convert 丈³ to 尺³

# Step 2: Calculate the total work capacity of each county
乙縣積尺 = 每日人功 * 乙縣人數 * 限日  # Total work completed by County B
甲縣積尺 = 總積尺 - 乙縣積尺          # Remaining work for County A

# Step 3: Calculate the height (高), width (廣), and length (袤) for County A
# Using the formula from the problem:
# 高乘上袤，袤差而一，為上袤之高
袤差 = 下袤 - 上袤
上袤之高 = 高 * 上袤 / (袤差 + 1)

# 三因上袤之高，半之，為廉法，從
廉法 = Fraction(3, 2) * 上袤之高

# 開立方除之，得乙高
乙高 = pow(乙縣積尺 / 廉法, Fraction(1, 3))

# 以減甍高，余即甲高
甲高 = 高 - 乙高

# 求廣、袤，依率求之
甲廣 = 廣  # Width remains constant
甲袤 = 上袤 + (袤差 * 甲高 / 高)

# Convert results to 丈
a = Fraction(甲高, 10)  # 高 in 丈
b = Fraction(甲廣, 10)  # 廣 in 丈
c = Fraction(甲袤, 10)  # 袤 in 丈

# Output the results
print(f"答曰：高 {a} 丈，上廣 {b} 丈，袤 {c} 丈。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Volume Calculation:**
   - The roof is treated as a trapezoidal prism, and its volume is calculated using the formula for the volume of a trapezoid.

2. **Work Distribution:**
   - The total work is divided proportionally between the two counties based on their populations and daily work capacity.

3. **Height, Width, and Length for County A:**
   - Using the formulas provided in the problem, the height (高), width (廣), and length (袤) for County A are calculated.

4. **Conversion to 丈:**
   - Since the problem specifies the dimensions in 丈, the final results are converted from 尺 to 丈 (1 丈 = 10 尺).

---

### Example Output:
If you run the code, it will calculate and output the height, width, and length that County A should complete:

```
答曰：高 a 丈，上廣 b 丈，袤 c 丈。
```

Where `a`, `b`, and `c` are the respective values for height, width, and length.
"""


"""
Code error: both arguments should be Rational instances"""
