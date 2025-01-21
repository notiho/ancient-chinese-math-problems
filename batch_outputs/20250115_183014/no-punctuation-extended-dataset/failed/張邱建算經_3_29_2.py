"""
今有立方九十六尺欲為立圓問徑幾何
術曰立方再自乘又以十六乘之九而一所得開立方除之徑得圓徑
答曰 a尺
"""

"""
Suppose there is a cube with a volume of 96 cubic chi. It is desired to turn it into a sphere.
Question: what is the diameter of the sphere?

The procedure says: Take the cube's volume, multiply it by itself, and then multiply it by 16.
Divide the result by 9.
Take the cube root of the result, and that is the diameter of the sphere.

Answer: *a* chi.
"""

# 立方九十六尺
立方 = 96

# 立方再自乘
立方平方 = 立方 * 立方

# 又以十六乘之
乘積 = 16 * 立方平方

# 九而一
商 = Fraction(乘積, 9)

# 所得開立方
# Since Python does not have a built-in cube root function, we use exponentiation.
圓徑 = 商 ** Fraction(1, 3)

a = 圓徑
"""
Variable 'a' has wrong value. Expected: 4694772/40369, Actual: 25.398416831491186"""
