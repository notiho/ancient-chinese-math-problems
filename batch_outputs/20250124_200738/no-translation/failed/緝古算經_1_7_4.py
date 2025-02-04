"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving multiple steps and calculations. Below is the Python code that follows the procedure ("術") step by step:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given values
上袤 = 3  # 上袤 (top length) in 丈
下袤 = 9  # 下袤 (bottom length) in 丈
廣 = 6    # 廣 (width) in 丈
高 = 12   # 高 (height) in 丈
甲縣人數 = 632  # 甲縣人數
乙縣人數 = 243  # 乙縣人數
夏程人功 = 36   # 夏程人功當積 (work per person per day in cubic 尺)
限日 = 8         # 限日 (days)

# Step 1: Calculate the total work (積尺) for 乙縣
乙積尺 = 夏程人功 * 乙縣人數 * 限日

# Step 2: Calculate the "實"
實 = Fraction(乙積尺 * 6 * 高**2 * (下袤 - 上袤) * 廣, 2)

# Step 3: Calculate "上袤之高"
上袤之高 = Fraction(高 * 上袤 * (下袤 - 上袤), 2)

# Step 4: Calculate "廉法"
廉法 = Fraction(3 * 上袤之高, 2)

# Step 5: Solve for 乙高 (乙縣的高)
乙高 = pow(實 / 廉法, 1/3)

# Step 6: Calculate 甲高
甲高 = 高 - 乙高

# Step 7: Calculate 甲縣的廣 and 袤
甲廣 = 廣 * (甲高 / 高)
甲袤 = 上袤 + (下袤 - 上袤) * (甲高 / 高)

# Final results
a = Fraction(甲高).limit_denominator()  # 高
b = Fraction(甲廣).limit_denominator()  # 上廣
c = Fraction(甲袤).limit_denominator()  # 袤

# Output
print(f"高 a丈 = {a}")
print(f"上廣 b丈 = {b}")
print(f"袤 c丈 = {c}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Step 1:** Calculate the total work (積尺) for 乙縣 using the formula `夏程人功 * 乙縣人數 * 限日`.
2. **Step 2:** Calculate the "實" using the formula provided in the procedure.
3. **Step 3:** Calculate "上袤之高" based on the given formula.
4. **Step 4:** Calculate "廉法" as described in the procedure.
5. **Step 5:** Solve for 乙高 by taking the cube root of `(實 / 廉法)`.
6. **Step 6:** Calculate 甲高 by subtracting 乙高 from the total height (高).
7. **Step 7:** Calculate 甲縣的廣 and 袤 based on the proportional relationships described in the procedure.

### Final Output:
The values of `a`, `b`, and `c` represent the height (高), top width (上廣), and length (袤) for 甲縣, respectively. These are expressed as fractions to maintain precision.
"""


"""
Variable 'a' has wrong value. Expected: 24/5, Actual: -84222490/476659
Variable 'b' has wrong value. Expected: 18/5, Actual: -42111245/476659
Variable 'c' has wrong value. Expected: 33/5, Actual: -40681268/476659"""
