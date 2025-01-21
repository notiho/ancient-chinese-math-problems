"""
今有芻甍，下廣三丈，袤四丈，上袤二丈，無廣，高一丈。問︰積幾何？
術曰：倍下袤，上袤從之，以廣乘之，又以高乘之，六而一。
荅曰： a(=5000)尺 。
"""

"""
Suppose there is a thatched roof with a lower width of 3 zhang, a lower length of 4 zhang, and an upper length of 2 zhang (with no width at the top). The height is 1 zhang.
Question: what is the volume?

The procedure says: Double the lower length, add the upper length to it, then multiply by the width, and then multiply by the height. Divide the result by 6.

Answer: *a*(=5000) chi³.
"""

# 下廣三丈
下廣 = 3 * 10  # Convert to chi

# 袤四丈
下袤 = 4 * 10  # Convert to chi

# 上袤二丈
上袤 = 2 * 10  # Convert to chi

# 高一丈
高 = 1 * 10  # Convert to chi

# 倍下袤
倍下袤 = 2 * 下袤

# 上袤從之
總袤 = 倍下袤 + 上袤

# 以廣乘之
積 = 總袤 * 下廣

# 又以高乘之
積 = 積 * 高

# 六而一
a = Fraction(積, 6)  # 5000 chi³
"""
"""
