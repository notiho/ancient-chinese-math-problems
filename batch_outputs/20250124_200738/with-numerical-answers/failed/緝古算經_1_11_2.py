"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
術曰：三十五乘粟，二十五而一，為率。多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實。並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法。又並多少，以乘一十四，如二十五而一，加多加之，為廉法，從。開立方除之，即窖深。各加差，即方、徑、高。
答曰：方徑各 a(=8/5)丈 ，高 b(=19/10)丈 ，深 c(=7/5)丈 。
"""

#----- content starts here -----
"""
Suppose there are 3072 shi of millet. It is desired to construct one square granary and one circular pit.
Let the diameter of the circular pit be equal to the side length of the square granary.
The square granary is 2 chi deeper than the circular pit, and 3 chi shorter than the granary's height.
Both are filled completely, and the millet is exactly used up.

Question: What are the side length (方), diameter (徑), height (高), and depth (深)?

The procedure says:
Multiply the millet by 35, then divide by 25 to obtain the base ratio.
Multiply the larger dimension by itself, then multiply by the sum of the larger and smaller dimensions.
Multiply this by 14, then divide by 25 to obtain the result.
Subtract this result from the base ratio to get the remainder, which is the actual value.
Take the sum of the larger and smaller dimensions, multiply by the larger dimension, double it, and multiply by 14.
Divide by 25, then add the square of the larger dimension to obtain the square method.
Take the sum of the larger and smaller dimensions, multiply by 14, divide by 25, and add the larger dimension to obtain the edge method.
Extract the cube root of the result to find the depth of the circular pit.
Add the differences to find the side length, diameter, and height.

Answer: The side length and diameter are *a*(=8/5) zhang, the height is *b*(=19/10) zhang, and the depth is *c*(=7/5) zhang.
"""

from fractions import Fraction
from math import pow

# 粟三千七十二石
粟 = 3072

# 三十五乘粟，二十五而一，為率
率 = Fraction(35 * 粟, 25)

# 方於窖深二尺，少於倉高三尺
差深 = Fraction(2, 10)  # 2 chi = 2/10 zhang
差高 = Fraction(3, 10)  # 3 chi = 3/10 zhang

# 初始估計，並多少
並多少 = Fraction(1)  # Assume initial guess for 方徑 (side length/diameter)

# 多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實
多 = 並多少
實 = 率 - Fraction(14 * 多 * 多 * 並多少, 25)

# 並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法
方法 = Fraction(14 * 並多少 * 多 * 2, 25) + 多 * 多

# 又並多少，以乘一十四，如二十五而一，加多加之，為廉法，從
廉法 = Fraction(14 * 並多少, 25) + 多

# 開立方除之，即窖深
深 = pow(float(實 / 方法), 1/3)
深 = Fraction(round(深 * 100), 100)  # Convert back to Fraction for precision

# 各加差，即方、徑、高
方 = 並多少
徑 = 並多少
高 = 深 + 差高

# 答案
a = 方  # 8/5 zhang
b = 高  # 19/10 zhang
c = 深  # 7/5 zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 8/5, Actual: 1
Variable 'b' has wrong value. Expected: 19/10, Actual: 324/25
Variable 'c' has wrong value. Expected: 7/5, Actual: 633/50"""
