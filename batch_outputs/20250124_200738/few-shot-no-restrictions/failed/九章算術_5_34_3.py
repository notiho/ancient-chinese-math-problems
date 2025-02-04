"""
今有圓困，高一丈三尺三寸、少半寸，容米二千斛。問︰周幾何？
術曰：置米積尺，以十二乘之，令高而一，所得，開方除之，即周。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical container with a height of 1 zhang, 3 chi, 3 cun, and half a cun. It can hold 2000 hu of rice.
Question: what is the circumference of the base?

The procedure says: Place the volume of rice in cubic chi, multiply it by 12, and divide it by the height. Take the square root of the result, and that is the circumference.

Answer: the circumference is *a* zhang.
"""

from fractions import Fraction
import math

# 高一丈三尺三寸、少半寸
height = 1 * 10 + 3 + Fraction(3.5, 10)  # Convert to chi (1 zhang = 10 chi, 1 chi = 10 cun)

# 容米二千斛
volume_hu = 2000

# Convert hu to cubic chi (1 hu = 10 cubic chi)
volume_chi3 = volume_hu * 10

# 置米積尺，以十二乘之
volume_scaled = volume_chi3 * 12

# 令高而一
base_area = volume_scaled / height

# 所得，開方除之，即周
circumference = math.sqrt(base_area)

# Convert circumference to zhang (1 zhang = 10 chi)
a = circumference / 10

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
