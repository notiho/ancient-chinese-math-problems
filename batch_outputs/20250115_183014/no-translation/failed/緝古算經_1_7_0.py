"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This problem is quite complex and involves multiple steps of calculation. Let's break it down systematically and translate the procedure into Python code step by step.


"""


from fractions import Fraction
from math import pow

# Given data
上袤 = 3  # 上袤 (top length) in 丈
下袤 = 9  # 下袤 (bottom length) in 丈
廣 = 6    # 廣 (width) in 丈
高 = 12   # 高 (height) in 丈
甲縣人數 = 632  # 人數 (population of 甲縣)
乙縣人數 = 243  # 人數 (population of 乙縣)
夏程人功 = 36   # 夏程人功 (work per person per day) in 積尺
限日 = 8         # 限日 (days of work)

# Step 1: Calculate the total work (積尺) required for 乙縣
# 以程功乘乙縣人數，又以限日乘之，為積尺
乙積尺 = 夏程人功 * 乙縣人數 * 限日

# Step 2: Calculate the "實" (intermediate value)
# 以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實
袤差 = 下袤 - 上袤
實 = Fraction(6 * 高**2 * 袤差 * 廣, 2)

# Step 3: Calculate the "上袤之高" (height corresponding to the top length)
# 高乘上袤，袤差而一，為上袤之高
上袤之高 = Fraction(高 * 上袤, 袤差)

# Step 4: Calculate the "廉法" (intermediate value for height calculation)
# 三因上袤之高，半之，為廉法
廉法 = Fraction(3 * 上袤之高, 2)

# Step 5: Calculate the height for 乙縣 (乙高)
# 開立方除之，得乙高
乙高 = pow(Fraction(乙積尺, 實), 1/3)

# Step 6: Calculate the height for 甲縣 (甲高)
# 以減甍高，余即甲高
甲高 = 高 - 乙高

# Step 7: Calculate the width (廣) and length (袤) for 甲縣
# 求廣、袤，依率求之
甲廣 = Fraction(甲高 * 廣, 高)
甲袤 = Fraction(甲高 * 下袤, 高)

# Final results
a = 甲高  # 高 for 甲縣
b = 甲廣  # 廣 for 甲縣
c = 甲袤  # 袤 for 甲縣

# Output the results
a, b, c


"""


### Explanation of the Code:
1. **Step 1**: Calculate the total work required for 乙縣 based on its population, work rate, and days of work.
2. **Step 2**: Compute the intermediate value "實" using the given formula.
3. **Step 3**: Calculate the height corresponding to the top length ("上袤之高").
4. **Step 4**: Compute the intermediate value "廉法" for further calculations.
5. **Step 5**: Derive the height for 乙縣 ("乙高") by solving the cubic equation.
6. **Step 6**: Subtract 乙高 from the total height to get the height for 甲縣 ("甲高").
7. **Step 7**: Use the proportional relationships to calculate the width ("廣") and length ("袤") for 甲縣.

### Final Answer:
- 高 \(a\) 丈
- 上廣 \(b\) 丈
- 袤 \(c\) 丈
"""


"""
Code error: both arguments should be Rational instances"""
