"""
今有圓困，高一丈三尺三寸、少半寸，容米二千斛。問︰周幾何？
術曰：置米積尺，以十二乘之，令高而一，所得，開方除之，即周。
荅曰： a丈 。
"""

"""
Suppose there is a cylindrical container with a height of 1 zhang, 3 chi, 3 cun, and half a cun, which can hold 2000 hu of rice.
Question: what is the circumference of the base?

The procedure says: Place the volume of rice in cubic chi, multiply it by 12, and let the height be the divisor.
Take the square root of the result, and that is the circumference.

Answer: *a* zhang.
"""

from fractions import Fraction

# 高一丈三尺三寸、少半寸
高 = 1 * 10 + 3 + Fraction(3.5, 10)  # Convert to chi (1 zhang = 10 chi, 1 chi = 10 cun)

# 容米二千斛
米積 = 2000 * 10  # Convert hu to cubic chi (1 hu = 10 cubic chi)

# 置米積尺，以十二乘之
積尺 = 米積 * 12

# 令高而一
積除高 = Fraction(積尺, 高)

# 所得，開方除之，即周
周 = 積除高 ** Fraction(1, 2)  # Square root

# Convert to zhang (1 zhang = 10 chi)
a = 周 / 10
"""
Code error: both arguments should be Rational instances"""
