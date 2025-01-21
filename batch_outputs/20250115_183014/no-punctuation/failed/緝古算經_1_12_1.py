"""
假令有粟五千一百四十石欲作方窖圓窖各一令口小底大方面於圓徑等兩深亦同其深少於下方七尺多於上方一丈四尺盛各滿中而粟適盡問方徑深各多少
術曰以四十二乘斛法以乘粟七十五而一為方亭積令方差自乘三而一為隅陽冪以截多乘之減積余為實以多乘差加冪為方法多加差為廉法從開立方除之即上方加差即合所問
答曰上方徑各 a尺 下方徑各 b丈 深各 c丈 
"""

"""
This is a complex ancient Chinese mathematical problem involving the calculation of dimensions for square and circular granaries based on given constraints. Below is the translation of the procedure into Python code:


"""


"""
Suppose there are 5140 shi of millet, and it is desired to construct both a square granary and a circular granary.
The granaries should have a smaller opening at the top and a larger base, with the square's side equal to the circle's diameter.
The depth is the same for both granaries, and the depth is 7 chi less than the bottom side/diameter and 1 zhang 4 chi more than the top side/diameter.
Both granaries are filled to capacity, and the millet is exactly used up.
Question: What are the dimensions of the top side/diameter, bottom side/diameter, and depth?

The procedure says:
1. Multiply 42 by the hu divisor (斛法) and then multiply by the millet (粟), dividing by 75 to get the cubic volume (方亭積).
2. Let the difference between the top and bottom sides/diameters (方差) be the variable.
3. Square the difference and multiply by 3, dividing by 1 to get the corner excess volume (隅陽冪).
4. Multiply the corner excess volume by the excess (截多) and subtract it from the cubic volume to get the remainder (實).
5. Multiply the excess by the difference and add the corner excess volume to get the divisor (方法).
6. Add the excess to the difference to get the edge divisor (廉法).
7. Take the cube root of the remainder divided by the divisor to get the top side/diameter.
8. Add the difference to the top side/diameter to get the bottom side/diameter.
9. The depth is the same as the top side/diameter plus the given excess.

Answer: The top side/diameter is *a* chi, the bottom side/diameter is *b* zhang, and the depth is *c* zhang.
"""

from fractions import Fraction

# 粟五千一百四十石
粟 = 5140

# 斛法
斛法 = 42

# Multiply 42 by the hu divisor and millet, dividing by 75 to get 方亭積
方亭積 = Fraction(斛法 * 粟, 75)

# 方差 (difference between top and bottom sides/diameters)
方差 = Fraction(1)  # Assume an initial guess for 方差

# 隅陽冪: Square the difference and multiply by 3
隅陽冪 = Fraction(方差**2 * 3, 1)

# 截多 (excess)
截多 = Fraction(7 + 14, 1)  # 7 chi less than bottom, 1 zhang 4 chi more than top

# Multiply 隅陽冪 by 截多 and subtract from 方亭積 to get 實
實 = 方亭積 - 隅陽冪 * 截多

# 方法: Multiply 截多 by 方差 and add 隅陽冪
方法 = 截多 * 方差 + 隅陽冪

# 廉法: Add 截多 to 方差
廉法 = 截多 + 方差

# Take the cube root of 實 divided by 方法 to get the top side/diameter
上方徑 = (實 / 方法) ** Fraction(1, 3)

# Add 方差 to 上方徑 to get the bottom side/diameter
下方徑 = 上方徑 + 方差

# The depth is the same as the top side/diameter plus the given excess
深 = 上方徑 + 截多

# Convert units where necessary
a = 上方徑  # Top side/diameter in chi
b = 下方徑 / 10  # Bottom side/diameter in zhang
c = 深 / 10  # Depth in zhang

# Output results
a, b, c


"""


This code follows the ancient procedure step by step. Note that the exact values for `方差` and other variables might require iterative refinement or additional constraints to solve fully.
"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: 4.895265916836644
Variable 'b' has wrong value. Expected: 14/5, Actual: 0.5895265916836644
Variable 'c' has wrong value. Expected: 21/10, Actual: 2.589526591683664"""
