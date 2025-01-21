"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This problem involves calculating the contributions of two counties,甲縣 and 乙縣, to the construction of a roof-like structure with specific dimensions. The problem requires determining the height, width, and length of the portion of the structure that 甲縣 is responsible for, based on the work completed by 乙縣. Below is the solution encoded in Python:


"""


from fractions import Fraction
from math import pow

# Given dimensions of the structure
上袤 = 3  # Top length in zhang
下袤 = 9  # Bottom length in zhang
廣 = 6    # Width in zhang
高 = 12   # Height in zhang

# Population of the two counties
甲縣人數 = 632
乙縣人數 = 243

# Work rate and time limit
夏程人功 = 36  # Work rate in cubic chi per person per day
限日 = 8       # Time limit in days

# Step 1: Calculate the total volume of work (積尺) that 乙縣 is responsible for
乙積尺 = 夏程人功 * 乙縣人數 * 限日

# Step 2: Calculate the "實" (intermediate value for volume calculation)
袤差 = 下袤 - 上袤  # Difference between bottom and top lengths
實 = Fraction(乙積尺 * 6 * 高 * 袤差, 廣 * 2)

# Step 3: Calculate the height of the portion completed by 乙縣 (乙高)
上袤之高 = Fraction(高 * 上袤 * 袤差, 廣)
廉法 = Fraction(3 * 上袤之高, 2)
乙高 = pow(float(實 / 廉法), 1/3)

# Step 4: Calculate the height of the portion completed by 甲縣 (甲高)
甲高 = 高 - 乙高

# Step 5: Calculate the width and length of the portion completed by 甲縣
甲廣 = 廣
甲袤 = Fraction(甲高 * 廣, 高)

# Final results
a = Fraction(甲高).limit_denominator()  # Height in zhang
b = Fraction(甲廣).limit_denominator()  # Width in zhang
c = Fraction(甲袤).limit_denominator()  # Length in zhang

# Output the results
print(f"高 a丈 = {a}丈")
print(f"上廣 b丈 = {b}丈")
print(f"袤 c丈 = {c}丈")


"""


### Explanation of the Steps:
1. **Calculate 乙縣's contribution to the total volume (乙積尺):**
   - Multiply the work rate (夏程人功) by the population of 乙縣 and the time limit (限日).

2. **Calculate the intermediate value (實):**
   - Use the given formula involving the dimensions of the structure, the difference in lengths (袤差), and the width (廣).

3. **Determine the height of the portion completed by 乙縣 (乙高):**
   - Use the formula for 上袤之高 and 廉法 to calculate the cubic root of the ratio of 實 to 廉法.

4. **Calculate the height of the portion completed by 甲縣 (甲高):**
   - Subtract 乙高 from the total height (高).

5. **Determine the width and length of the portion completed by 甲縣:**
   - The width (甲廣) remains the same as the total width (廣).
   - The length (甲袤) is calculated proportionally based on the height (甲高).

### Final Answer:
- 高 `a` 丈: The height of the portion completed by 甲縣.
- 上廣 `b` 丈: The width of the portion completed by 甲縣.
- 袤 `c` 丈: The length of the portion completed by 甲縣.
"""


"""
Code error: both arguments should be Rational instances"""
