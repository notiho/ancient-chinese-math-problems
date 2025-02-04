"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
術曰：半鐻道自乘，如深寸而一，以深寸增之，即材徑。
荅曰：材徑 a(=13/5)尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical object buried in a wall, and its size is unknown.
Using a measuring tool, it is pressed into the wall to a depth of 1 cun, and the length of the chord (the "measuring path") is 1 chi.
Question: what is the diameter of the cylinder?

The procedure says: Take half of the chord length, square it, and divide by the depth (1 cun).
Add the depth to the result, and this gives the diameter of the cylinder.

Answer: the diameter of the cylinder is *a*(=13/5) chi.
"""

from fractions import Fraction

# 鐻道長一尺
鐻道 = 1  # in chi

# 深一寸
深 = Fraction(1, 10)  # 1 cun = 1/10 chi

# 半鐻道
半鐻道 = 鐻道 / 2

# 半鐻道自乘
半鐻道平方 = 半鐻道 ** 2

# 如深寸而一
深分之一 = 半鐻道平方 / 深

# 以深寸增之，即材徑
a = 深分之一 + 深  # 13/5 chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 13/5, Actual: 2.6"""
