"""
今有溝，廣十丈，深五丈，長二十丈，欲以千尺作一方。問：得幾何？
術曰：置廣一十丈，以深五丈乘之，得五千尺，又以長二十丈乘之，得一百萬尺，以一千除之，即得。
答曰： a 方。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 廣十丈
廣 = 10

# 深五丈
深 = 5

# 長二十丈
長 = 20

# 置廣一十丈，以深五丈乘之，得五千尺
積1 = 廣 * 深

# 又以長二十丈乘之，得一百萬尺
積2 = 積1 * 長

# 以一千除之，即得
a = Fraction(積2, 1000)
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 1000, Actual: 1"""
