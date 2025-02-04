"""
今有圓困，高一丈三尺三寸、少半寸，容米二千斛。問︰周幾何？
術曰：置米積尺，以十二乘之，令高而一，所得，開方除之，即周。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical container with a height of 1 zhang, 3 chi, 3 cun, and half a cun, which can hold 2000 hu of rice.
Question: what is the circumference of the base?

The procedure says: Place the volume of rice in cubic chi, multiply it by 12, and let the height be the divisor.
Take the square root of the result, and that is the circumference.

Answer: the circumference is *a* zhang.
"""

from fractions import Fraction
import math

# 高一丈三尺三寸、少半寸
# Convert height to chi (1 zhang = 10 chi, 1 chi = 10 cun)
height = 10 + 3 + Fraction(3.5, 10)  # 1 zhang 3 chi 3.5 cun

# 容米二千斛
# Convert hu to cubic chi (1 hu = 10 cubic chi)
volume = 2000 * 10  # in cubic chi

# 置米積尺，以十二乘之
volume_times_12 = volume * 12

# 令高而一
base_area = volume_times_12 / height

# 所得，開方除之，即周
circumference = math.sqrt(base_area)

# Convert circumference to zhang (1 zhang = 10 chi)
a = circumference / 10  # in zhang

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
