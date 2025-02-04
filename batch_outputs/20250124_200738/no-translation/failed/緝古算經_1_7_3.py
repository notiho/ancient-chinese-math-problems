"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving multiple steps and calculations. Below is the Python code that follows the procedure ("術") described in the problem:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given values
上袤 = 3  # 上袤 (top length) in 丈
下袤 = 9  # 下袤 (bottom length) in 丈
廣 = 6    # 廣 (width) in 丈
高 = 12   # 高 (height) in 丈
甲縣人數 = 632  # 甲縣 people
乙縣人數 = 243  # 乙縣 people
夏程人功 = 36   # Summer work per person per day in cubic 尺
限日 = 8        # Limit in days

# Step 1: Calculate the total work (積尺) for 乙縣
乙積尺 = 夏程人功 * 乙縣人數 * 限日

# Step 2: Calculate the "實" (intermediate value)
實 = Fraction(乙積尺 * 6 * 高**2 * (下袤 - 上袤), 2)

# Step 3: Calculate the "上袤之高" (height corresponding to top length)
上袤之高 = Fraction(高 * 上袤 * (下袤 - 上袤), 1)

# Step 4: Calculate the "廉法" (diagonal law)
廉法 = Fraction(3 * 上袤之高, 2)

# Step 5: Solve for 乙高 (height for 乙縣)
乙高 = pow(實 / 廉法, 1/3)

# Step 6: Calculate 甲高 (height for 甲縣)
甲高 = 高 - 乙高

# Step 7: Calculate 甲縣's 廣 and 袤
甲廣 = 廣
甲袤 = Fraction(甲高 * 上袤, 高)

# Final answers
a = 甲高  # 高 (height for 甲縣)
b = 甲廣  # 廣 (width for 甲縣)
c = 甲袤  # 袤 (length for 甲縣)

# Print results
print(f"高 a丈 = {a}")
print(f"上廣 b丈 = {b}")
print(f"袤 c丈 = {c}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Step 1**: Calculate the total work (積尺) required for 乙縣 based on the number of people, their daily work capacity, and the number of days.
2. **Step 2**: Use the formula provided to calculate the intermediate value "實".
3. **Step 3**: Compute the height corresponding to the top length (上袤之高).
4. **Step 4**: Calculate the diagonal law (廉法) based on the height and other parameters.
5. **Step 5**: Solve for the height of the work assigned to 乙縣 (乙高) using the cubic root.
6. **Step 6**: Subtract 乙高 from the total height to get 甲高.
7. **Step 7**: Use the proportions to calculate the width (廣) and length (袤) for 甲縣.

### Notes:
- The use of `Fraction` ensures precision in calculations involving fractions.
- The cubic root (`pow(x, 1/3)`) is used to solve for 乙高.
- The final results are stored in variables `a`, `b`, and `c` for the height, width, and length of 甲縣, respectively.
"""


"""
Code error: both arguments should be Rational instances"""
