"""
假令有粟五千一百四十石欲作方窖圓窖各一令口小底大方面於圓徑等兩深亦同其深少於下方七尺多於上方一丈四尺盛各滿中而粟適盡問方徑深各多少
術曰以四十二乘斛法以乘粟七十五而一為方亭積令方差自乘三而一為隅陽冪以截多乘之減積余為實以多乘差加冪為方法多加差為廉法從開立方除之即上方加差即合所問
答曰上方徑各 a尺 下方徑各 b丈 深各 c丈 
"""

"""
This is a complex ancient Chinese mathematical problem involving the calculation of dimensions for square and circular granaries. Let's break it down step by step and translate the procedure into Python code.

### Problem Breakdown:
- There are 5140 石 (shi) of grain.
- Two granaries are to be constructed: one square and one circular.
- Both granaries must have the same depth, and their openings (top) are smaller than their bases (bottom).
- The depth is 7 尺 (chi) less than the bottom and 1 丈 4 尺 (14 尺) more than the top.
- The granaries are filled to capacity, and the grain is just enough to fill both.

The procedure involves:
1. Calculating the square granary's dimensions.
2. Using the given relationships between the top, bottom, and depth to solve for the dimensions.

### Translation of the Procedure into Python Code:


"""


from fractions import Fraction
from math import isqrt

# 粟五千一百四十石
粟 = 5140

# 以四十二乘斛法
斛法 = 42

# 以乘粟七十五而一
粟積 = Fraction(粟 * 75, 1)

# 方差自乘三而一
方差 = Fraction(斛法, 3)

# 方差自乘
方差平方 = 方差 ** 2

# 隅陽冪以截多乘之
隅陽冪 = Fraction(3, 1) * 方差平方

# 減積余為實
實 = 粟積 - 隅陽冪

# 多乘差加冪為方法
方法 = 方差 * 斛法 + 方差平方

# 多加差為廉法
廉法 = 斛法 + 方差

# 從開立方除之即上方
上方徑 = isqrt(實 * 斛法 // 方法)

# 加差即合所問
下方徑 = 上方徑 + 方差
深 = 下方徑 - 7

# 答案
a = 上方徑  # 上方徑 (top diameter)
b = 下方徑  # 下方徑 (bottom diameter)
c = 深      # 深 (depth)

print(f"上方徑各 {a} 尺, 下方徑各 {b} 丈, 深各 {c} 丈")


"""


### Explanation of the Code:
1. **斛法 and 粟積**: These are constants derived from the problem. The `斛法` is used to scale the volume of grain, and `粟積` represents the total volume in a specific unit.
2. **方差 and 方差平方**: These represent the difference between the top and bottom dimensions of the granary, squared.
3. **隅陽冪**: This is an intermediate calculation for the cubic volume.
4. **實, 方法, 廉法**: These are intermediate values used to calculate the dimensions.
5. **isqrt**: The integer square root is used to simplify the cubic root calculation for the top diameter.

### Final Output:
The program calculates the top diameter (`a`), bottom diameter (`b`), and depth (`c`) of the granaries.
"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: 143
Variable 'b' has wrong value. Expected: 14/5, Actual: 157
Variable 'c' has wrong value. Expected: 21/10, Actual: 150"""
