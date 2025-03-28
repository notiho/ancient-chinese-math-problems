"""
今有立方九十六尺欲為立圓問徑幾何
術曰立方再自乘又以十六乘之九而一所得開立方除之徑得圓徑
答曰 a尺
"""

#----- content starts here -----
"""
Suppose there is a cube with a volume of 96 cubic chi. It is desired to transform it into a sphere.
Question: what is the diameter of the sphere?

The procedure says: Take the volume of the cube, multiply it by itself (square it), and then multiply it by 16.
Divide the result by 9.
Take the cube root of the result, and that is the diameter of the sphere.

Answer: the diameter is *a* chi.
"""

# 立方九十六尺
立方 = 96

# 立方再自乘
平方 = 立方 * 立方

# 又以十六乘之
乘十六 = 平方 * 16

# 九而一
結果 = Fraction(乘十六, 9)

# 所得開立方 (開立方即為立方根)
# Since Python does not have a direct cube root function, we use exponentiation.
圓徑 = 結果 ** Fraction(1, 3)

a = 圓徑#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4694772/40369, Actual: 25.398416831491186"""
