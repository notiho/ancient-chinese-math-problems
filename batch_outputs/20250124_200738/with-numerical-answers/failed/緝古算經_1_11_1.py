"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
術曰：三十五乘粟，二十五而一，為率。多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實。並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法。又並多少，以乘一十四，如二十五而一，加多加之，為廉法，從。開立方除之，即窖深。各加差，即方、徑、高。
答曰：方徑各 a(=8/5)丈 ，高 b(=19/10)丈 ，深 c(=7/5)丈 。
"""

#----- content starts here -----
"""
Suppose there are 3072 shi of millet. It is desired to construct one square granary and one round silo, such that the diameter of the silo equals the side length of the square granary. 
The square granary is 2 chi deeper than the round silo, and the round silo is 3 chi shorter than the height of the square granary. 
Both are filled to capacity, and the millet is exactly used up.

Question: What are the side length (方), diameter (徑), height (高), and depth (深)?

The procedure says:
Multiply 35 by the millet and divide by 25 to get the initial ratio. 
Take the larger dimension (多), square it, and multiply it by the sum of the smaller dimension (少) and the larger dimension. 
Multiply by 14, and divide by 25. Subtract the result from the initial ratio to get the remainder (實). 

Take the sum of the smaller and larger dimensions, multiply by the larger dimension, double it, and multiply by 14. Divide by 25. Add the square of the larger dimension to this to get the square method (方法). 

Take the sum of the smaller and larger dimensions, multiply by 14, divide by 25, and add the larger dimension to this to get the edge method (廉法). Solve for the cube root to get the depth of the silo (窖深). 

Add the differences to get the side length (方), diameter (徑), and height (高).

Answer: The side length and diameter are *a*(=8/5) zhang, the height is *b*(=19/10) zhang, and the depth is *c*(=7/5) zhang.
"""

from fractions import Fraction
from math import pow

# 粟三千七十二石
粟 = 3072

# 術曰：三十五乘粟，二十五而一，為率
率 = Fraction(35 * 粟, 25)

# 方於窖深二尺，少於倉高三尺
差深 = Fraction(2, 10)  # 2 chi = 2/10 zhang
差高 = Fraction(3, 10)  # 3 chi = 3/10 zhang

# 初始假設多與少
多 = Fraction(1)  # Initial guess for the larger dimension
少 = Fraction(1)  # Initial guess for the smaller dimension

# 迭代求解
while True:
    # 多自乘，以並多少乘之，以乘一十四，如二十五而一，所得以減率，余為實
    實 = 率 - Fraction(14 * 多 * 多 * (多 + 少), 25)

    # 並多少，以乘多，倍之，乘一十四，如二十五而一，多自乘加之，為方法
    方法 = Fraction(14 * (多 + 少) * 多 * 2, 25) + 多 * 多

    # 又並多少，以乘一十四，如二十五而一，加多加之，為廉法
    廉法 = Fraction(14 * (多 + 少), 25) + 多

    # 從。開立方除之，即窖深
    窖深 = pow(Fraction(實, 方法), Fraction(1, 3))

    # 各加差，即方、徑、高
    方 = 窖深 + 差深
    徑 = 方
    高 = 窖深 + 差高

    # 檢查是否滿足條件
    if abs(多 - 方) < Fraction(1, 1000) and abs(少 - 窖深) < Fraction(1, 1000):
        break

    # 更新多與少
    多 = 方
    少 = 窖深

# 答案
a = 方  # 8/5 zhang
b = 高  # 19/10 zhang
c = 窖深  # 7/5 zhang#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
