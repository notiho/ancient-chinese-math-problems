"""
今有芻甍，下廣三丈，袤四丈，上袤二丈，無廣，高一丈。問︰積幾何？
術曰：倍下袤，上袤從之，以廣乘之，又以高乘之，六而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a thatched roof. The bottom width is 3 zhang, the bottom length is 4 zhang, and the top length is 2 zhang (with no width at the top). The height is 1 zhang.
Question: what is the volume?

The procedure says: Double the bottom length, add the top length to it, multiply by the width, then multiply by the height, and divide by 6.

Answer: *a* chi³.
"""

from fractions import Fraction

# 下廣三丈
下廣 = 3  # in zhang

# 袤四丈
下袤 = 4  # in zhang

# 上袤二丈
上袤 = 2  # in zhang

# 高一丈
高 = 1  # in zhang

# 倍下袤
倍下袤 = 2 * 下袤

# 上袤從之
總袤 = 倍下袤 + 上袤

# 以廣乘之
底積 = 總袤 * 下廣

# 又以高乘之
體積 = 底積 * 高

# 六而一
體積 = Fraction(體積, 6)

# Convert zhang³ to chi³ (1 zhang = 10 chi, so 1 zhang³ = 1000 chi³)
體積_in_尺 = 體積 * 1000

a = 體積_in_尺
a#----- content ends here -----

"""
"""
