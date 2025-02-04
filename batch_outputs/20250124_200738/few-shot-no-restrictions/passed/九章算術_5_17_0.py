"""
今有圓錐下周三丈五尺，高五丈一尺。問︰積幾何？
術曰：下周自乘，以高乘之，三十六而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a cone with a base circumference of 3 zhang and 5 chi, and a height of 5 zhang and 1 chi.
Question: what is the volume of the cone?

The procedure says: Multiply the base circumference by itself, then multiply by the height, and divide by 36.

Answer: the volume is *a* cubic chi.
"""

from fractions import Fraction

# 下周三丈五尺 (convert to chi: 1 zhang = 10 chi)
下周 = 3 * 10 + 5  # in chi

# 高五丈一尺 (convert to chi)
高 = 5 * 10 + 1  # in chi

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
體積乘積 = 下周平方 * 高

# 三十六而一
a = Fraction(體積乘積, 36)  # volume in cubic chi

a#----- content ends here -----

"""
"""
