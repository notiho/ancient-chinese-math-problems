"""
今有溝，廣十丈，深五丈，長二十丈，欲以千尺作一方。問：得幾何？
術曰：置廣一十丈，以深五丈乘之，得五千尺，又以長二十丈乘之，得一百萬尺，以一千除之，即得。
答曰： a 方。
"""

"""
Suppose there is a trench with a width of 10 zhang, a depth of 5 zhang, and a length of 20 zhang.
It is desired to calculate the volume in units where 1000 cubic chi make 1 fang.
Question: how many fang does it make?

The procedure says: Place the width as 10 zhang. Multiply it by the depth, 5 zhang, obtaining 5000 cubic chi.
Then multiply it by the length, 20 zhang, obtaining 100000 cubic chi.
Divide it by 1000, obtaining the result.

Answer: it makes *a* fang.
"""

# 廣十丈
廣 = 10

# 深五丈
深 = 5

# 長二十丈
長 = 20

# 置廣一十丈，以深五丈乘之，得五千尺
積尺 = 廣 * 深

# 又以長二十丈乘之，得一百萬尺
積尺 = 積尺 * 長

# 以一千除之，即得
a = Fraction(積尺, 1000)
"""
Variable 'a' has wrong value. Expected: 1000, Actual: 1"""
