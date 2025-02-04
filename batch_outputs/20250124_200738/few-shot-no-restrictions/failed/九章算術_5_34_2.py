"""
今有圓困，高一丈三尺三寸、少半寸，容米二千斛。問︰周幾何？
術曰：置米積尺，以十二乘之，令高而一，所得，開方除之，即周。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical granary with a height of 1 zhang, 3 chi, 3 cun, and half a cun, which can hold 2000 hu of rice.
Question: what is the circumference of the base?

The procedure says: Take the volume of the rice in cubic chi, multiply it by 12, and let the height be 1.
Take the square root of the result and divide it, obtaining the circumference.

Answer: *a* zhang.
"""

from fractions import Fraction
import math

# 高一丈三尺三寸、少半寸
height = 1 * 10 + 3 + Fraction(3, 10) + Fraction(1, 20)  # Convert to chi (1 zhang = 10 chi, 1 chi = 10 cun)

# 容米二千斛
volume_hu = 2000

# Convert hu to cubic chi (1 hu = 10 cubic chi)
volume_chi3 = volume_hu * 10

# 置米積尺，以十二乘之
adjusted_volume = volume_chi3 * 12

# 令高而一
adjusted_base_area = adjusted_volume / height

# 所得，開方除之，即周
circumference = 2 * math.sqrt(adjusted_base_area)  # Circumference = sqrt(base area) * 2 (π approximated as 3)

# Convert circumference to zhang (1 zhang = 10 chi)
a = circumference / 10

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 27/5, Actual: 26.81606092615964"""
