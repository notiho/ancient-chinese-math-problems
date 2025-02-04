"""
今有芻甍下廣三丈袤四丈上袤二丈無廣高一丈問積幾何
術曰倍下袤上袤從之以廣乘之又以高乘之六而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a thatched roof. The bottom width is 3 zhang, the bottom length is 4 zhang, and the top length is 2 zhang (with no width at the top). The height is 1 zhang.
Question: what is the volume?

The procedure says: Double the bottom length, add the top length to it, multiply by the width, then multiply by the height, and divide by 6.

The answer says: *a* chi.
"""

# 下廣三丈
下廣 = 3

# 下袤四丈
下袤 = 4

# 上袤二丈
上袤 = 2

# 高一丈
高 = 1

# 倍下袤
倍下袤 = 2 * 下袤

# 上袤從之
總袤 = 倍下袤 + 上袤

# 以廣乘之
積 = 總袤 * 下廣

# 又以高乘之
積 = 積 * 高

# 六而一
a = Fraction(積, 6) * 10  # Convert from zhang^3 to chi^3 (1 zhang = 10 chi)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5000, Actual: 50"""
