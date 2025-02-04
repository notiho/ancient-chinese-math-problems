"""
今有芻甍，下廣三丈，袤四丈，上袤二丈，無廣，高一丈。問︰積幾何？
術曰：倍下袤，上袤從之，以廣乘之，又以高乘之，六而一。
荅曰： a(=5000)尺 。
"""

#----- content starts here -----
"""
Suppose there is a thatched roof. The lower width is 3 zhang, the lower length is 4 zhang, and the upper length is 2 zhang (with no width at the top). The height is 1 zhang.
Question: what is the volume?

The procedure says: Double the lower length, add the upper length to it, multiply by the width, then multiply by the height, and divide by 6.

Answer: *a*(=5000) chi.
"""

# 下廣三丈
下廣 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 袤四丈
下袤 = 4 * 10  # Convert zhang to chi

# 上袤二丈
上袤 = 2 * 10  # Convert zhang to chi

# 高一丈
高 = 1 * 10  # Convert zhang to chi

# 倍下袤
倍下袤 = 2 * 下袤

# 上袤從之
總袤 = 倍下袤 + 上袤

# 以廣乘之
積 = 總袤 * 下廣

# 又以高乘之
積 = 積 * 高

# 六而一
a = Fraction(積, 6)  # 5000 chi
#----- content ends here -----

"""
"""
