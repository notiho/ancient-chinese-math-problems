"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex ancient Chinese problem involving multiple steps and calculations. Let's break it down and translate it into Python code step by step, adhering to the procedure ("術") provided.


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
夏程人功 = 36   # 夏程人功 (work per person per day in cubic 尺)
限日 = 8         # 限日 (limit in days)

# Step 1: Calculate the total work (積尺) required for 乙縣
乙積尺 = 夏程人功 * 乙縣人數 * 限日

# Step 2: Calculate the "實" (intermediate value)
袤差 = 下袤 - 上袤  # 袤差 (difference in length)
實 = Fraction(乙積尺 * 6 * 高**2 * 袤差 * 廣, 2)

# Step 3: Calculate the "上袤之高" (height corresponding to the top length)
上袤之高 = Fraction(高 * 上袤 * 袤差, 1)

# Step 4: Calculate the "廉法" (intermediate value for height calculation)
廉法 = Fraction(3 * 上袤之高, 2)

# Step 5: Solve for 乙高 (height for 乙縣's contribution)
乙高 = pow(實 / 廉法, 1/3)

# Step 6: Calculate 甲高 (height for 甲縣's contribution)
甲高 = 高 - 乙高

# Step 7: Calculate the corresponding 廣 (width) and 袤 (length) for 甲縣
甲廣 = 廣  # 廣 remains the same
甲袤 = Fraction(甲高 * 袤差, 高) + 上袤

# Final results
a = Fraction(甲高)  # 高 (height for 甲縣)
b = Fraction(甲廣)  # 廣 (width for 甲縣)
c = Fraction(甲袤)  # 袤 (length for 甲縣)

# Output
print(f"高 a = {a} 丈")
print(f"上廣 b = {b} 丈")
print(f"袤 c = {c} 丈")


"""


### Explanation of the Code:
1. **Input Data**: The given dimensions of the structure, populations of the two counties, work rate, and time limit are used as inputs.
2. **乙積尺 Calculation**: The total work required for 乙縣 is calculated based on its population, work rate, and time.
3. **實 Calculation**: This intermediate value is calculated using the formula provided in the procedure.
4. **上袤之高 Calculation**: The height corresponding to the top length is calculated.
5. **廉法 Calculation**: Another intermediate value used for solving the cubic equation for height.
6. **乙高 and 甲高 Calculation**: The heights for 乙縣 and 甲縣 are determined.
7. **廣 and 袤 Calculation**: The width and length for 甲縣 are calculated based on the height ratio.

### Output:
The code will output the height (`a`), width (`b`), and length (`c`) for 甲縣 in 丈.
"""


"""
Code error: both arguments should be Rational instances"""
