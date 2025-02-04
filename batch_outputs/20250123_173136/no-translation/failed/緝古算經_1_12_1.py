"""
假令有粟五千一百四十石，欲作方窖、圓窖各一，令口小底大，方面於圓徑等，兩深亦同，其深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問：方、徑、深各多少？
術曰：以四十二乘斛法，以乘粟，七十五而一，為方亭積。令方差自乘，三而一，為隅陽冪，以截多乘之，減積，余為實。以多乘差，加冪，為方法。多加差，為廉法，從。開立方除之，即上方。加差，即合所問。
答曰：上方徑各 a尺 ，下方徑各 b丈 ，深各 c丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving volumetric calculations for irregularly shaped storage pits. Translating this into Python code requires careful adherence to the procedure ("術") described. Here's the solution:


"""


from fractions import Fraction
from math import pow

# 粟五千一百四十石
粟 = 5140

# 以四十二乘斛法
斛法 = 42

# 以乘粟，七十五而一，為方亭積
方亭積 = Fraction(斛法 * 粟, 75)

# 深少於下方七尺，多於上方一丈四尺
深差 = Fraction(7, 10)  # 7尺 = 0.7丈
深多 = 1 + Fraction(4, 10)  # 1丈4尺 = 1.4丈

# 令方差自乘，三而一，為隅陽冪
方差 = 深多 - 深差
隅陽冪 = Fraction(pow(方差, 2), 3)

# 以截多乘之，減積，余為實
截多 = 深多
實 = 方亭積 - 隅陽冪 * 截多

# 以多乘差，加冪，為方法
方法 = 截多 * 方差 + 隅陽冪

# 多加差，為廉法，從
廉法 = 截多 + 方差

# 開立方除之，即上方
上方 = pow(Fraction(實, 方法), Fraction(1, 3))

# 加差，即合所問
下方 = 上方 + 方差
深 = 深多

# 答案
a = 上方  # 上方徑
b = 下方  # 下方徑
c = 深    # 深


"""


### Explanation of Variables:
1. **粟**: Total amount of grain in 石.
2. **斛法**: Conversion factor for the volumetric calculation.
3. **方亭積**: The intermediate calculated volume based on the given formula.
4. **深差** and **深多**: The depth differences as described in the problem.
5. **方差**: The difference between the depths of the top and bottom.
6. **隅陽冪**: A calculated value based on the square of the depth difference.
7. **截多**: The larger depth value.
8. **實**: The remaining volume after subtracting certain calculated values.
9. **方法**: A calculated divisor for determining the top diameter.
10. **廉法**: A calculated divisor for determining the bottom diameter.

### Final Results:
- `a` is the top diameter in 尺.
- `b` is the bottom diameter in 丈.
- `c` is the depth in 丈.

This code adheres to the ancient procedure and uses Python's `Fraction` class for precise calculations.
"""


"""
Code error: both arguments should be Rational instances"""
