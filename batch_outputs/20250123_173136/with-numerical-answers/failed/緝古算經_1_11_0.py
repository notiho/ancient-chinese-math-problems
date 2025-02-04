"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
術曰：三十五乘粟，二十五而一，為率。多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實。並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法。又並多少，以乘一十四，如二十五而一，加多加之，為廉法，從。開立方除之，即窖深。各加差，即方、徑、高。
答曰：方徑各 a(=8/5)丈 ，高 b(=19/10)丈 ，深 c(=7/5)丈 。
"""

"""
Suppose there are 3072 shi of millet. It is desired to construct one square granary and one round silo, where the diameter of the silo equals the side length of the square granary. The square granary is 2 chi deeper than the silo, and 3 chi shorter than the granary's height. Both are filled to capacity, and the millet is exactly used up.
Question: What are the side length (square granary), diameter (round silo), height (granary), and depth (silo)?

The procedure says:
1. Multiply 35 by the millet, divide by 25, obtaining the base rate.
2. Multiply the larger dimension by itself, then multiply it by the combined dimensions, and multiply by 14. Divide by 25, and subtract the base rate. The remainder is the dividend.
3. Multiply the combined dimensions by the larger dimension, double it, multiply by 14, divide by 25, and add the square of the larger dimension. This gives the square method.
4. Multiply the combined dimensions by 14, divide by 25, and add the larger dimension. This gives the edge method.
5. Extract the cube root of the dividend divided by the square method, obtaining the depth of the silo.
6. Add the differences to obtain the side length, diameter, and height.

Answer: The side length and diameter are *a*(=8/5) zhang, the height is *b*(=19/10) zhang, and the depth is *c*(=7/5) zhang.
"""

from fractions import Fraction
from math import pow

# 粟三千七十二石
粟 = 3072

# 三十五乘粟，二十五而一，為率
率 = Fraction(35 * 粟, 25)

# 方於窖深二尺，少於倉高三尺
深差 = Fraction(2, 10)  # 2 chi = 2/10 zhang
高差 = Fraction(3, 10)  # 3 chi = 3/10 zhang

# 多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實
多 = 1  # Placeholder for the larger dimension (to be solved later)
並多少 = 深差 + 高差
實 = Fraction(14 * 多**2 * 並多少, 25) - 率

# 並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法
方法 = Fraction(14 * 並多少 * 多 * 2, 25) + 多**2

# 又並多少，以乘一十四，如二十五而一，加多加之，為廉法，從
廉法 = Fraction(14 * 並多少, 25) + 多

# 開立方除之，即窖深
窖深 = Fraction(pow(實 / 方法, Fraction(1, 3)))

# 各加差，即方、徑、高
方 = 窖深 + 深差
徑 = 方
高 = 窖深 + 高差

# 答案
a = 方  # 8/5 zhang
b = 高  # 19/10 zhang
c = 窖深  # 7/5 zhang
"""
Code error: math domain error"""
