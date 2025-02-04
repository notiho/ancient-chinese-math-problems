"""
今有溝廣十丈深五丈長二十丈欲以千尺作一方問得幾何
術曰置廣一十丈以深五丈乘之得五千尺又以長二十丈乘之得一百萬尺以一千除之即得
答曰 a 方
"""

"""
Suppose there is a ditch with a width of 10 zhang, a depth of 5 zhang, and a length of 20 zhang.
It is desired to calculate how many cubic units (fang) it makes, where 1000 cubic chi equals 1 fang.

The procedure says: Place the width as 10 zhang and multiply it by the depth, 5 zhang, obtaining 5000 cubic chi.
Then multiply it by the length, 20 zhang, obtaining 100000 cubic chi.
Divide it by 1000, and the result is the number of fang.

Answer: *a* fang.
"""

# 置廣十丈
廣 = 10

# 深五丈
深 = 5

# 長二十丈
長 = 20

# 以廣乘深，得五千尺
積尺 = 廣 * 深

# 再以長乘之
積尺 = 積尺 * 長

# 以一千除之，即得
a = Fraction(積尺, 1000)
"""
Variable 'a' has wrong value. Expected: 1000, Actual: 1"""
