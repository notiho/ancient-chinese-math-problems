"""
今有圓困高一丈三尺三寸少半寸容米二千斛問周幾何
術曰置米積尺以十二乘之令高而一所得開方除之即周
荅曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a circular granary with a height of 1 zhang, 3 chi, 3 cun, and slightly less than half a cun. It can hold 2000 hu of rice.
Question: what is the circumference of the granary?

The procedure says: Place the volume of rice in cubic chi, multiply it by 12, and treat the height as 1.
Take the square root of the result and divide it, obtaining the circumference.

Answer: *a* zhang.
"""

from fractions import Fraction

# 容米二千斛
米容 = 2000  # in hu

# Convert hu to cubic chi (1 hu = 10 cubic chi)
米容積尺 = 10 * 米容

# 高一丈三尺三寸少半寸
高 = 1 * 10 + 3 + Fraction(3, 10) - Fraction(1, 20)  # Convert height to chi

# 置米積尺以十二乘之
積尺乘十二 = 12 * 米容積尺

# 令高而一 (divide by height)
積尺除高 = Fraction(積尺乘十二, 高)

# 所得開方 (square root of the result)
開方 = 積尺除高 ** Fraction(1, 2)

# 即周 (circumference in chi, convert to zhang)
a = Fraction(開方, 10)  # Convert chi to zhang#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
