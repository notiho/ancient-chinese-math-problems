"""
今有圓材徑二尺五寸，欲為方版，令厚七寸。問︰廣幾何？
術曰：令徑二尺五寸自乘，以七寸自乘減之，其餘開方除之，即廣。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical log with a diameter of 2 chi 5 cun. It is desired to make a square plank with a thickness of 7 cun.
Question: what is the width of the square plank?

The procedure says: Take the diameter of 2 chi 5 cun and square it. Then take the thickness of 7 cun and square it, subtract the latter from the former. Take the square root of the remainder and divide it, obtaining the width.

Answer: *a* chi.
"""

from fractions import Fraction
import math

# 圓材徑二尺五寸
徑 = 2 + Fraction(5, 10)  # Convert 2 chi 5 cun to chi

# 厚七寸
厚 = Fraction(7, 10)  # Convert 7 cun to chi

# 令徑二尺五寸自乘
徑平方 = 徑 ** 2

# 以七寸自乘
厚平方 = 厚 ** 2

# 減之
餘 = 徑平方 - 厚平方

# 其餘開方
廣 = math.sqrt(float(餘))

# 荅曰：a 尺
a = round(廣, 2)  # Round to 2 decimal places for chi
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 12/5, Actual: 2.4"""
