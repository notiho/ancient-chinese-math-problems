"""
今有圓材徑二尺五寸欲為方版令厚七寸問廣幾何
術曰令徑二尺五寸自乘以七寸自乘減之其餘開方除之即廣
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a cylindrical log with a diameter of 2 chi 5 cun. It is desired to make it into a square plank with a thickness of 7 cun.
Question: how wide is the plank?

The procedure says: Take the diameter of 2 chi 5 cun, square it, and take the thickness of 7 cun, square it, and subtract the latter from the former.
Take the square root of the remainder, and divide it by 2. This gives the width.

The answer says: *a* chi.
"""

from fractions import Fraction
import math

# 圓材徑二尺五寸
徑 = 2 + Fraction(5, 10)  # 2 chi 5 cun = 2.5 chi

# 厚七寸
厚 = Fraction(7, 10)  # 7 cun = 0.7 chi

# 令徑二尺五寸自乘
徑平方 = 徑 * 徑

# 以七寸自乘
厚平方 = 厚 * 厚

# 減之
餘 = 徑平方 - 厚平方

# 其餘開方
開方餘 = math.sqrt(float(餘))  # Convert to float for square root

# 除之
a = Fraction(開方餘, 2)  # Divide by 2 to get the width in chi

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
