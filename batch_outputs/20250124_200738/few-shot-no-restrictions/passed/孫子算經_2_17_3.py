"""
今有溝，廣十丈，深五丈，長二十丈，欲以千尺作一方。問：得幾何？
術曰：置廣一十丈，以深五丈乘之，得五千尺，又以長二十丈乘之，得一百萬尺，以一千除之，即得。
答曰： a 方。
"""

#----- content starts here -----
"""
Suppose there is a trench with a width of 10 zhang, a depth of 5 zhang, and a length of 20 zhang.
It is desired to calculate its volume in cubic units, where 1000 cubic chi make 1 fang.

The procedure says: Take the width (10 zhang) and multiply it by the depth (5 zhang), obtaining 5000 cubic chi.
Then multiply this by the length (20 zhang), obtaining 100000 cubic chi.
Divide this by 1000 to convert to fang.

Answer: *a* fang.
"""

# 溝的尺寸
廣 = 10  # 丈
深 = 5   # 丈
長 = 20  # 丈

# 計算體積（以立方尺為單位）
體積_立方尺 = 廣 * 深 * 長 * 1000  # 1 丈 = 10 尺, 所以需要乘以 10^3

# 以一千除之，即得方
a = Fraction(體積_立方尺, 1000)

# 答案
a#----- content ends here -----

"""
"""
