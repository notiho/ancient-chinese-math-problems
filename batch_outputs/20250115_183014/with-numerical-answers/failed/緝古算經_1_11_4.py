"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
術曰：三十五乘粟，二十五而一，為率。多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實。並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法。又並多少，以乘一十四，如二十五而一，加多加之，為廉法，從。開立方除之，即窖深。各加差，即方、徑、高。
答曰：方徑各 a(=8/5)丈 ，高 b(=19/10)丈 ，深 c(=7/5)丈 。
"""

"""
Suppose there are 3072 shi of millet. It is desired to construct one square granary and one round pit.
Let the diameter of the pit equal the side of the square granary. Let the square granary be 2 chi deeper than the pit and 3 chi shorter than the granary's height.
Both are filled to capacity, and the millet is exactly used up.
Question: What are the side length of the square granary, the diameter of the pit, the height of the granary, and the depth of the pit?

The procedure says:
Multiply the millet by 35, then divide by 25 to get the initial rate.
Multiply the square side length by itself, then multiply by the combined height difference and multiply by 14.
Divide by 25 to get the adjustment. Subtract this from the rate to get the base.
Multiply the combined height difference by the square side length, double it, multiply by 14, and divide by 25.
Add the square side length squared to this to get the square method.
Multiply the combined height difference by 14, divide by 25, and add the square side length to get the edge method.
Take the cube root of the result and divide to get the pit depth.
Add the differences to get the square side, diameter, height, and depth.

Answer: The square side and diameter are *a*(=8/5) zhang, the height is *b*(=19/10) zhang, and the depth is *c*(=7/5) zhang.
"""

from fractions import Fraction
from math import pow

# 粟三千七十二石
粟 = 3072

# 方於窖深二尺，少於倉高三尺
深差 = Fraction(2, 10)  # 2 chi = 2/10 zhang
高差 = Fraction(3, 10)  # 3 chi = 3/10 zhang
並差 = 深差 + 高差  # Combined difference

# 三十五乘粟，二十五而一，為率
率 = Fraction(35 * 粟, 25)

# 多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實
多 = Fraction(1)  # Placeholder for the square side length (to be solved iteratively)
實 = 0
while True:
    多自乘 = 多 * 多
    調整 = Fraction(14 * 多自乘 * 並差, 25)
    新實 = 率 - 調整
    if 新實 == 實:  # Convergence check
        break
    實 = 新實
    多 = pow(實, Fraction(1, 3))  # Update 多 iteratively

# 並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法
方法 = 多 * 並差 * 2 * 14 / 25 + 多自乘

# 又並多少，以乘一十四，如二十五而一，加多加之，為廉法，從
廉法 = 並差 * 14 / 25 + 多

# 開立方除之，即窖深
窖深 = pow(方法, Fraction(1, 3))

# 各加差，即方、徑、高
方 = 多
徑 = 多
高 = 多 + 高差
深 = 窖深 + 深差

a = 方  # 8/5 zhang
b = 高  # 19/10 zhang
c = 深  # 7/5 zhang
"""
Code error: both arguments should be Rational instances"""
