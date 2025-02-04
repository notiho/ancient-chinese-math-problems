"""
假令有粟二萬三千一百二十斛七斗三升欲作方倉一圓窖一盛各滿中而粟適盡令高深等使方面少於圓徑九寸多於高二丈九尺八寸率徑七周二十二問方徑深多少
求方徑高深術曰十四乘斛法以乘粟數二十五而一為實又倍多加少以乘少數又十一乘之二十五而一多自乘加之為方法又倍少數十一乘之二十五而一又倍多加之為廉法從開立方除之即高深各加差即方徑還元術曰倉方自乘以高乘之為實圓徑自乘以深乘之一十一乘一十四而一為實皆為斛法除之即得容粟
答曰倉方 a丈 窖徑 b丈 高與深各 c丈 
"""

"""
This is a complex problem involving the calculation of dimensions for a square granary and a circular pit, both of which must hold a given amount of grain. The problem also involves specific relationships between the dimensions of the granary and the pit, as well as the use of approximations for π (22/7). Below is the Python implementation of the procedure:


"""


from fractions import Fraction
from math import isqrt

# 粟二萬三千一百二十斛七斗三升
粟 = Fraction(23120, 1) + Fraction(7, 10) + Fraction(3, 100)

# 方倉少於圓徑九寸 (converted to 丈)
少 = Fraction(9, 10)

# 方倉多於高二丈九尺八寸 (converted to 丈)
多 = 2 + Fraction(9, 10) + Fraction(8, 100)

# 率徑七周二十二 (π approximation)
π = Fraction(22, 7)

# 求方徑高深術
# Step 1: 14乘斛法以乘粟數，25而1為實
實 = Fraction(14, 1) * Fraction(25, 1) * 粟

# Step 2: 倍多加少以乘少數，又11乘之，25而1
廉法 = Fraction(2, 1) * 多 + 少
廉法 = Fraction(11, 1) * 廉法 * Fraction(25, 1)

# Step 3: 多自乘加之為方法
方法 = 多**2 + 廉法

# Step 4: 倍少數，11乘之，25而1
少法 = Fraction(2, 1) * 少
少法 = Fraction(11, 1) * 少法 * Fraction(25, 1)

# Step 5: 倍多加之為廉法
廉法 = Fraction(2, 1) * 多 + 少法

# Step 6: 開立方除之，即高深各
高深 = isqrt(實 // 方法)

# 高深各加差，即方徑
方徑 = 高深 + 多

# 圓徑
圓徑 = 高深 + 少

# 還元術驗算
# 倉方自乘以高乘之為實
倉方容積 = 方徑**2 * 高深

# 圓徑自乘以深乘之，11乘14而1為實
圓窖容積 = 圓徑**2 * 高深 * Fraction(11, 1) * Fraction(14, 1)

# 皆為斛法除之，即得容粟
倉方容積斛 = 倉方容積 / Fraction(25, 1)
圓窖容積斛 = 圓窖容積 / Fraction(25, 1)

# 答案
a = 方徑
b = 圓徑
c = 高深


"""


### Explanation of Variables:
- `粟`: The total amount of grain in hu, dou, and sheng.
- `少`: The difference between the square granary's side and the circular pit's diameter.
- `多`: The difference between the square granary's side and the height/depth.
- `π`: The approximation of π as 22/7.
- `實`: The intermediate calculation for the total volume.
- `方法`: The divisor for calculating the height/depth.
- `高深`: The height/depth of both the granary and the pit.
- `方徑`: The side length of the square granary.
- `圓徑`: The diameter of the circular pit.
- `倉方容積`: The volume of the square granary.
- `圓窖容積`: The volume of the circular pit.

### Final Answer:
- `a`: The side length of the square granary in 丈.
- `b`: The diameter of the circular pit in 丈.
- `c`: The height/depth of both the granary and the pit in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 453/100, Actual: 3399/50
Variable 'b' has wrong value. Expected: 231/50, Actual: 659/10
Variable 'c' has wrong value. Expected: 31/20, Actual: 65"""
