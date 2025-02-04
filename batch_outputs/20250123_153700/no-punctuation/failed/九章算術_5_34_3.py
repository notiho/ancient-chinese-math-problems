"""
今有圓困高一丈三尺三寸少半寸容米二千斛問周幾何
術曰置米積尺以十二乘之令高而一所得開方除之即周
荅曰 a丈 
"""

"""
Suppose there is a cylindrical container with a height of 1 zhang, 3 chi, 3 cun, and a half cun less (1丈3尺2寸5分).
It can hold 2000 hu of rice.
Question: what is the circumference of the base?

The procedure says: Place the volume of rice in chi, multiply it by 12, and treat the height as 1.
Take the square root of the result, and divide it. This gives the circumference.

Answer: *a* zhang.
"""

from fractions import Fraction

# 高一丈三尺三寸少半寸
高 = 1 * 10 + 3 + Fraction(3, 10) - Fraction(1, 20)  # Convert to chi (1丈 = 10尺, 1尺 = 10寸)

# 容米二千斛
米積 = 2000 * 10  # Convert hu to chi^3 (1斛 = 10立方尺)

# 置米積尺以十二乘之
積尺 = 米積 * 12

# 令高而一
積尺 /= 高

# 所得開方
周 = 積尺 ** Fraction(1, 2)

# 即周
a = Fraction(周, 10)  # Convert chi to zhang (1丈 = 10尺)
"""
Code error: both arguments should be Rational instances"""
