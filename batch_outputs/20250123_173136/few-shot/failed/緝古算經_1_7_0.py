"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex problem involving multiple steps and calculations. Let's break it down and translate the procedure into Python code step by step.

### Problem Description:
We are tasked with calculating the contributions of two counties, 甲縣 (County A) and 乙縣 (County B), in constructing a roof-like structure with specific dimensions. The goal is to determine how much of the height, width, and length (袤) County A is responsible for, based on the given work rate and constraints.

### Procedure:
1. Calculate the total volume of work (積尺) that County B is responsible for.
2. Use the volume to determine the height (高) that County B contributes.
3. Subtract County B's height from the total height to get County A's height.
4. Use the height to calculate the width (廣) and length (袤) for County A.

### Code Implementation:


"""


from fractions import Fraction
from math import pow

# Given data
上袤 = 3  # 上袤 (top length) in 丈
下袤 = 9  # 下袤 (bottom length) in 丈
廣 = 6    # 廣 (width) in 丈
高 = 12   # 高 (height) in 丈
甲縣人數 = 632  # Number of people in County A
乙縣人數 = 243  # Number of people in County B
夏程人功 = 36   # Work rate per person in cubic chi
限日 = 8        # Time limit in days

# Step 1: Calculate the total volume (積尺) that County B is responsible for
乙積尺 = 夏程人功 * 乙縣人數 * 限日

# Step 2: Calculate the "實" (intermediate value for volume distribution)
袤差 = 下袤 - 上袤  # Difference between bottom and top lengths
實 = Fraction(6 * 乙積尺 * 高**2 * 袤差 * 廣, 2)

# Step 3: Calculate the height contributed by County B (乙高)
廉法 = Fraction(3 * 高 * 上袤 * 袤差, 2)
乙高 = pow(實 / 廉法, 1/3)

# Step 4: Calculate the height contributed by County A (甲高)
甲高 = 高 - 乙高

# Step 5: Calculate the width (廣) and length (袤) for County A
甲廣 = Fraction(甲高 * 廣, 高)
甲袤 = Fraction(甲高 * 袤差, 高)

# Final results
a = Fraction(甲高)  # 高 (height) for County A
b = Fraction(甲廣)  # 廣 (width) for County A
c = Fraction(甲袤)  # 袤 (length) for County A

# Output the results
a, b, c


"""


### Explanation of the Code:
1. **Step 1:** We calculate the total volume of work (積尺) that County B is responsible for using the work rate, number of people, and time limit.
2. **Step 2:** The intermediate value "實" is calculated using the given formula, which involves the dimensions of the structure and the volume contributed by County B.
3. **Step 3:** Using the "實" value, we calculate the height (乙高) that County B contributes by solving the cubic equation.
4. **Step 4:** Subtract County B's height from the total height to get County A's height (甲高).
5. **Step 5:** Using the height, we calculate the width (廣) and length (袤) for County A based on the given ratios.

### Final Answer:
- 高 (height) for County A: `a` 丈
- 廣 (width) for County A: `b` 丈
- 袤 (length) for County A: `c` 丈
"""


"""
Code error: both arguments should be Rational instances"""
