"""
假令有粟五千一百四十石欲作方窖圓窖各一令口小底大方面於圓徑等兩深亦同其深少於下方七尺多於上方一丈四尺盛各滿中而粟適盡問方徑深各多少
術曰以四十二乘斛法以乘粟七十五而一為方亭積令方差自乘三而一為隅陽冪以截多乘之減積余為實以多乘差加冪為方法多加差為廉法從開立方除之即上方加差即合所問
答曰上方徑各 a尺 下方徑各 b丈 深各 c丈 
"""

"""
This is a complex ancient Chinese mathematical problem involving the calculation of dimensions for square and circular granaries based on a given volume of grain. Let's translate the procedure into Python step by step:


"""


from fractions import Fraction
from math import isqrt

# 粟五千一百四十石
粟 = 5140

# 斛法 (1石 = 10斗, 1斗 = 10升, 1斛 = 10升)
斛法 = 10 * 10

# 粟轉換為升
粟升 = 粟 * 斛法

# 以四十二乘斛法
四十二斛法 = 42 * 斛法

# 以乘粟七十五而一，為方亭積
方亭積 = Fraction(四十二斛法 * 粟升, 75)

# 方差自乘三而一，為隅陽冪
方差 = 7 + 14  # 差 = 下方多於上方 7 尺, 上方多於下方 14 尺
隅陽冪 = Fraction(方差**2, 3)

# 以截多乘之，減積余，為實
截多 = 14  # 下方多於上方 14 尺
實 = 方亭積 - 截多 * 隅陽冪

# 以多乘差，加冪，為方法
方法 = 截多 * 方差 + 隅陽冪

# 多加差，為廉法
廉法 = 截多 + 方差

# 從開立方除之，即上方
上方徑 = isqrt(Fraction(實, 方法))

# 加差，即合所問
下方徑 = 上方徑 + 方差

# 深各
深 = Fraction(實, 廉法)

# 答案
a = 上方徑  # 上方徑各 a 尺
b = Fraction(下方徑, 10)  # 下方徑各 b 丈
c = Fraction(深, 10)  # 深各 c 丈

a, b, c


"""


### Explanation of the Code:
1. **粟轉換為升**: The total volume of grain is converted into sheng (升) using the given conversion rates.
2. **方亭積**: The intermediate calculation for the square granary's volume.
3. **隅陽冪**: The square of the difference between the top and bottom diameters, divided by 3.
4. **實**: The adjusted volume after subtracting the excess due to the difference in diameters.
5. **方法**: The divisor for calculating the top diameter.
6. **廉法**: The divisor for calculating the depth.
7. **上方徑**: The top diameter is calculated by taking the square root of the adjusted volume divided by 方法.
8. **下方徑**: The bottom diameter is the top diameter plus the difference.
9. **深**: The depth is calculated using the adjusted volume and 廉法.

### Final Answer:
- `a`: Top diameter in chi (尺).
- `b`: Bottom diameter in zhang (丈).
- `c`: Depth in zhang (丈).
"""


"""
Code error: 'Fraction' object cannot be interpreted as an integer"""
