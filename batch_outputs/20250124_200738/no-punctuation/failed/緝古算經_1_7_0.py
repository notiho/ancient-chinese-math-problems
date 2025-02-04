"""
假令芻甍上袤三丈下袤九丈廣六丈高一十二丈有甲縣六百三十二人乙縣二百四十三人夏程人功當積三十六尺限八日役自穿築二縣共造今甲縣先到問自下給高廣袤各多少
求甲縣均給積尺受廣袤術曰以程功乘乙縣人數又以限日乘之為積尺以六因之又高冪乘之又袤差乘廣而一所得又半之為實高乘上袤袤差而一為上袤之高三因上袤之高半之為廉法從開立方除之得乙高以減甍高余即甲高求廣袤依率求之
答曰高 a丈 上廣 b丈 袤 c丈 
"""

"""
This is a complex problem involving the distribution of labor between two counties (甲縣 and 乙縣) for constructing a trapezoidal structure (芻甍). The goal is to calculate how much of the structure's dimensions (height, width, and length) are assigned to 甲縣 based on the given parameters.

Here is the translation of the problem and its solution into Python code:


"""

#----- content starts here -----

"""
Suppose there is a trapezoidal structure (芻甍) with the following dimensions:
- Top length (上袤): 3 zhang
- Bottom length (下袤): 9 zhang
- Width (廣): 6 zhang
- Height (高): 12 zhang

There are:
- 632 people in 甲縣
- 243 people in 乙縣

The summer labor standard (夏程) is 36 cubic chi per person per day, and the work is limited to 8 days.
The two counties are jointly responsible for constructing the structure, starting from the bottom.

Question: If 甲縣 arrives first, how much of the structure's height, width, and length should they be assigned?

Procedure:
1. Multiply the labor standard (程功) by the number of people in 乙縣, then multiply by the number of days (限日) to get the total volume (積尺) for 乙縣.
2. Multiply this volume by 6 (the width of the structure), then by the square of the height (高冪), and then by the difference in lengths (袤差).
3. Divide by the width and halve the result to get the effective volume (實).
4. Multiply the height by the top length (上袤) and divide by the difference in lengths to get the height corresponding to the top length.
5. Multiply this height by 3 and halve it to get the slant height (廉法).
6. Take the cube root of the effective volume divided by the slant height to get the height assigned to 乙縣.
7. Subtract this height from the total height to get the height assigned to 甲縣.
8. Use the ratios to calculate the width and length assigned to 甲縣.

Answer:
- Height assigned to 甲縣: *a* zhang
- Width assigned to 甲縣: *b* zhang
- Length assigned to 甲縣: *c* zhang
"""

from fractions import Fraction
import math

# Given data
上袤 = 3  # Top length in zhang
下袤 = 9  # Bottom length in zhang
廣 = 6    # Width in zhang
高 = 12   # Height in zhang
甲縣人數 = 632
乙縣人數 = 243
夏程 = 36  # Labor standard in cubic chi per person per day
限日 = 8   # Number of days

# Step 1: Calculate the total volume (積尺) for 乙縣
乙積尺 = 夏程 * 乙縣人數 * 限日

# Step 2: Multiply by width, height squared, and length difference
袤差 = 下袤 - 上袤
實 = Fraction(乙積尺 * 廣 * 高**2 * 袤差, 1)

# Step 3: Divide by width and halve the result
實 = Fraction(實, 廣 * 2)

# Step 4: Calculate the height corresponding to the top length
上袤之高 = Fraction(高 * 上袤, 袤差)

# Step 5: Calculate the slant height (廉法)
廉法 = Fraction(3 * 上袤之高, 2)

# Step 6: Calculate the height assigned to 乙縣
乙高 = Fraction(math.pow(float(實 / 廉法), 1/3))

# Step 7: Calculate the height assigned to 甲縣
甲高 = 高 - 乙高

# Step 8: Calculate the width and length assigned to 甲縣
甲廣 = Fraction(甲高 * 廣, 高)
甲袤 = Fraction(甲高 * 袤差, 高) + 上袤

# Final answers
a = 甲高
b = 甲廣
c = 甲袤

# Print the results
print(f"甲縣分得的高: {a} 丈")
print(f"甲縣分得的廣: {b} 丈")
print(f"甲縣分得的袤: {c} 丈")
#----- content ends here -----


"""


This Python code follows the procedure outlined in the problem and calculates the height, width, and length assigned to 甲縣. Note that the calculations use fractions to ensure precision, and the cube root is calculated using `math.pow`.
"""


"""
Variable 'a' has wrong value. Expected: 24/5, Actual: -2423605722890869/17592186044416
Variable 'b' has wrong value. Expected: 18/5, Actual: -2423605722890869/35184372088832
Variable 'c' has wrong value. Expected: 33/5, Actual: -2318052606624373/35184372088832"""
