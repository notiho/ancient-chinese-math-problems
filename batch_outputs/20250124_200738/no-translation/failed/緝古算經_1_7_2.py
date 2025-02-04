"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This problem is quite complex and involves multiple steps of ancient Chinese mathematical procedures. Let's break it down step by step and translate it into Python code accordingly.

### Problem Breakdown:
1. **Given Data:**
   - 上袤 (top length) = 3 丈
   - 下袤 (bottom length) = 9 丈
   - 廣 (width) = 6 丈
   - 高 (height) = 12 丈
   - 甲縣人數 = 632
   - 乙縣人數 = 243
   - 夏程人功當積 = 36 尺
   - 限日 = 8 日

2. **Procedure:**
   - Calculate the total work (積尺) for 乙縣.
   - Use the given dimensions and rates to calculate the contributions of 甲縣 and 乙縣.
   - Determine the height (高), width (廣), and length (袤) for 甲縣's contribution.

Here is the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given data
上袤 = 3  # 丈
下袤 = 9  # 丈
廣 = 6  # 丈
高 = 12  # 丈
甲縣人數 = 632
乙縣人數 = 243
夏程人功當積 = 36  # 尺
限日 = 8  # 日

# Step 1: Calculate 積尺 for 乙縣
乙積尺 = 夏程人功當積 * 乙縣人數 * 限日

# Step 2: Calculate 实 (實)
實 = Fraction(乙積尺 * 6 * 高**2 * (下袤 - 上袤), 2)

# Step 3: Calculate 上袤之高
上袤之高 = Fraction(高 * 上袤 * (下袤 - 上袤), 3)

# Step 4: Calculate 廉法
廉法 = Fraction(上袤之高, 2)

# Step 5: Calculate 乙高
乙高 = math.pow(float(實 / 廉法), 1/3)

# Step 6: Calculate 甲高
甲高 = 高 - 乙高

# Step 7: Calculate 甲縣's 廣 and 袤
甲廣 = 廣 * (甲高 / 高)
甲袤 = 上袤 + (下袤 - 上袤) * (甲高 / 高)

# Final results
a = Fraction(甲高).limit_denominator()  # 高 in 丈
b = Fraction(甲廣).limit_denominator()  # 廣 in 丈
c = Fraction(甲袤).limit_denominator()  # 袤 in 丈

# Output results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. **Step 1:** Calculate the total work (積尺) for 乙縣 based on the given formula: `夏程人功當積 * 乙縣人數 * 限日`.
2. **Step 2:** Use the formula provided in the procedure to calculate `實`, which is a key intermediate value.
3. **Step 3:** Calculate `上袤之高` using the given formula.
4. **Step 4:** Calculate `廉法`, which is derived from `上袤之高`.
5. **Step 5:** Solve for `乙高` by taking the cube root of `(實 / 廉法)`.
6. **Step 6:** Subtract `乙高` from the total height `高` to get `甲高`.
7. **Step 7:** Calculate `甲廣` and `甲袤` using the given ratios and formulas.

### Final Answer:
- 高 (a): Height contributed by 甲縣.
- 上廣 (b): Width contributed by 甲縣.
- 袤 (c): Length contributed by 甲縣.
"""


"""
Variable 'a' has wrong value. Expected: 24/5, Actual: -120566574/756191
Variable 'b' has wrong value. Expected: 18/5, Actual: -60283287/756191
Variable 'c' has wrong value. Expected: 33/5, Actual: -58014714/756191"""
