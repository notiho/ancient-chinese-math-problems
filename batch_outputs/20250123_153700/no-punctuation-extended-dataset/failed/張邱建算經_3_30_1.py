"""
今有立圓徑一百三十二尺問為立方幾何
術曰令徑再自乘九之十六而一開立方除之得立方
答曰 a尺
"""

"""
Suppose there is a vertical cylinder with a diameter of 132 chi.
Question: what is its volume?

The procedure says: Take the diameter, square it, and multiply it by 9.
Divide it by 16, then take the cube root of the result.
The result is the volume of the cylinder.

Answer: *a* cubic chi.
"""

# 圓徑一百三十二尺
徑 = 132

# 令徑再自乘
徑平方 = 徑 * 徑

# 九之
積 = 9 * 徑平方

# 十六而一
積 = Fraction(積, 16)

# 開立方
a = 積 ** Fraction(1, 3)  # Cube root of the result
"""
Variable 'a' has wrong value. Expected: 1044652/4999, Actual: 21.400477469184917"""
