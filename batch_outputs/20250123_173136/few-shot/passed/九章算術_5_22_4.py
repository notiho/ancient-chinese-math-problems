"""
今有芻甍，下廣三丈，袤四丈，上袤二丈，無廣，高一丈。問︰積幾何？
術曰：倍下袤，上袤從之，以廣乘之，又以高乘之，六而一。
荅曰： a尺 。
"""

"""
Suppose there is a straw-covered roof. The bottom width is 3 zhang, the bottom length is 4 zhang, and the top length is 2 zhang (with no width at the top). The height is 1 zhang.
Question: what is the volume?

The procedure says: Double the bottom length, add the top length to it, and multiply by the width. Then multiply by the height. Finally, divide by 6.

Answer: *a* chi.
"""

# 下廣三丈
下廣 = 3 * 10  # Convert to chi (1 zhang = 10 chi)

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
a = Fraction(積, 6)  # Final volume in chi³
"""
"""
