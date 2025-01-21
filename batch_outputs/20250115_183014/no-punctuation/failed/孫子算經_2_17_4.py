"""
今有溝廣十丈深五丈長二十丈欲以千尺作一方問得幾何
術曰置廣一十丈以深五丈乘之得五千尺又以長二十丈乘之得一百萬尺以一千除之即得
答曰 a 方
"""

"""
Suppose there is a ditch with a width of 10 zhang, a depth of 5 zhang, and a length of 20 zhang.
It is desired to calculate how many cubic units (fang) it makes, where 1000 cubic chi equals 1 fang.

The procedure says: Place the width as 10 zhang, multiply it by the depth of 5 zhang, obtaining 500 chi².
Then multiply it by the length of 20 zhang, obtaining 1000000 cubic chi.
Divide it by 1000, and the result is the number of fang.

Answer: *a* fang.
"""

# 置廣十丈
廣 = 10

# 以深五丈乘之
深 = 5
積 = 廣 * 深  # 得五千尺 (500 chi²)

# 又以長二十丈乘之
長 = 20
體積 = 積 * 長  # 得一百萬尺 (1000000 cubic chi)

# 以一千除之，即得
a = Fraction(體積, 1000)  # 答曰 a 方
"""
Variable 'a' has wrong value. Expected: 1000, Actual: 1"""
