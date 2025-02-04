"""
今有立圓徑一百三十二尺問為立方幾何
術曰令徑再自乘九之十六而一開立方除之得立方
答曰 a尺
"""

#----- content starts here -----
"""
Suppose there is a standing cylinder with a diameter of 132 chi.
Question: what is its volume in cubic chi?

The procedure says: Take the diameter, multiply it by itself, then multiply by 9.
Divide by 16, then take the cube root, and divide it by 1 to obtain the volume.

Answer: it makes *a* cubic chi.
"""

from fractions import Fraction

# 圓徑一百三十二尺
徑 = 132

# 令徑再自乘
徑平方 = 徑 * 徑

# 九之
積 = 9 * 徑平方

# 十六而一
積 = Fraction(積, 16)

# 開立方 (cube root)
立方根 = 積 ** Fraction(1, 3)

# 除之得立方
a = 立方根#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1044652/4999, Actual: 21.400477469184917"""
