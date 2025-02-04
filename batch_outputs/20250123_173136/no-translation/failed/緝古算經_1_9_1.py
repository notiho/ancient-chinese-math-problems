"""
假令有粟二萬三千一百二十斛七斗三升，欲作方倉一，圓窖一，盛各滿中而粟適盡。令高、深等，使方面少於圓徑九寸，多於高二丈九尺八寸，率徑七，周二十二。問：方、徑、深多少？
求方、徑高深，術曰：十四乘斛法，以乘粟數，二十五而一，為實。又倍多加少，以乘少數，又十一乘之，二十五而一，多自乘加之，為方法。又倍少數，十一乘之，二十五而一，又倍多加之，為廉法，從。開立方除之，即高、深。各加差，即方徑。還元，術曰：倉方自乘，以高乘之，為實。圓徑自乘，以深乘之，一十一乘，一十四而一，為實。皆為斛法除之，即得容粟。
答曰：倉方 a丈 ，窖徑 b丈 ，高與深各 c丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The procedure involves calculating the dimensions of a square granary (倉) and a circular silo (窖) based on the given conditions.


"""


from fractions import Fraction
from math import isqrt

# 粟數：二萬三千一百二十斛七斗三升
粟數 = 23120 + Fraction(7, 10) + Fraction(3, 100)

# 令高、深等
高 = 深 = None

# 方面少於圓徑九寸，多於高二丈九尺八寸
少 = Fraction(9, 10)  # 9寸 = 9/10尺
多 = 2 * 10 + 9 + Fraction(8, 10)  # 2丈9尺8寸 = 29.8尺

# 率徑七，周二十二
率徑 = Fraction(7, 22)

# 求方、徑高深，術曰：
# 1. 十四乘斛法，以乘粟數，二十五而一，為實。
十四 = 14
二十五 = 25
實 = Fraction(十四 * 粟數, 二十五)

# 2. 又倍多加少，以乘少數，又十一乘之，二十五而一，多自乘加之，為方法。
倍多加少 = 2 * 多 + 少
方法 = Fraction(11 * 倍多加少 * 少, 二十五) + 倍多加少**2

# 3. 又倍少數，十一乘之，二十五而一，又倍多加之，為廉法，從。
倍少數 = 2 * 少
廉法 = Fraction(11 * 倍少數, 二十五) + 2 * 多

# 4. 開立方除之，即高、深。
高 = 深 = isqrt(isqrt(Fraction(實, 方法)))

# 5. 各加差，即方徑。
方 = 高 + 多
徑 = 高 + 少

# 還元，術曰：
# 倉方自乘，以高乘之，為實。
倉方實 = 方**2 * 高

# 圓徑自乘，以深乘之，一十一乘，一十四而一，為實。
圓徑實 = Fraction(徑**2 * 深 * 11, 14)

# 皆為斛法除之，即得容粟。
倉容粟 = Fraction(倉方實, 二十五)
圓容粟 = Fraction(圓徑實, 二十五)

# 答：
a = 方 / 10  # Convert to 丈
b = 徑 / 10  # Convert to 丈
c = 高 / 10  # Convert to 丈

print(f"倉方 {a}丈 ，窖徑 {b}丈 ，高與深各 {c}丈 。")


"""


This Python code follows the ancient procedure step by step, using the `Fraction` class to handle fractional arithmetic and ensuring all calculations are precise. The final dimensions of the square granary (倉), circular silo (窖), and their heights/depths are printed in 丈 (1 丈 = 10 尺).
"""


"""
Code error: 'Fraction' object cannot be interpreted as an integer"""
