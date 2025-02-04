"""
今有溝，廣十丈，深五丈，長二十丈，欲以千尺作一方。問：得幾何？
術曰：置廣一十丈，以深五丈乘之，得五千尺，又以長二十丈乘之，得一百萬尺，以一千除之，即得。
答曰： a 方。
"""

#----- content starts here -----
"""
Suppose there is a ditch with a width of 10 zhang, a depth of 5 zhang, and a length of 20 zhang.
It is desired to calculate how many cubic units (fang) it makes, where 1000 cubic chi equals 1 fang.

The procedure says: Place the width of 10 zhang, multiply it by the depth of 5 zhang, obtaining 500 chi².
Then multiply it by the length of 20 zhang, obtaining 100,000 chi³.
Divide it by 1000, and the result is the number of fang.

Answer: *a* fang.
"""

# 廣十丈
廣 = 10

# 深五丈
深 = 5

# 長二十丈
長 = 20

# 置廣一十丈，以深五丈乘之，得五千尺
積尺平方 = 廣 * 深

# 又以長二十丈乘之，得一百萬尺
積尺立方 = 積尺平方 * 長

# 以一千除之，即得
a = Fraction(積尺立方, 1000)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1000, Actual: 1"""
