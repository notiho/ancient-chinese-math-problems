"""
今有圓困，高一丈三尺三寸、少半寸，容米二千斛。問︰周幾何？
術曰：置米積尺，以十二乘之，令高而一，所得，開方除之，即周。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical container with a height of 1 zhang, 3 chi, 3 cun, and half a cun, which holds 2000 hu of rice.
Question: what is the circumference of the base?

The procedure says: Place the volume of rice in cubic chi, multiply it by 12, and treat the height as 1.
Take the square root of the result and divide it, obtaining the circumference.

Answer: *a* zhang.
"""

from fractions import Fraction

# 高一丈三尺三寸、少半寸
高 = 1 * 10 + 3 + Fraction(3, 10) + Fraction(1, 20)  # Convert to chi (1 zhang = 10 chi, 1 chi = 10 cun)

# 容米二千斛
米積 = 2000 * 10  # Convert hu to cubic chi (1 hu = 10 cubic chi)

# 置米積尺，以十二乘之
積尺 = 米積 * 12

# 令高而一
積尺 /= 高

# 所得，開方除之，即周
周 = Fraction(int(積尺**0.5), 10)  # Convert back to zhang (1 zhang = 10 chi)

a = 周#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 27/5, Actual: 67/5"""
