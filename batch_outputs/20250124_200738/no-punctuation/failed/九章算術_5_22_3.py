"""
今有芻甍下廣三丈袤四丈上袤二丈無廣高一丈問積幾何
術曰倍下袤上袤從之以廣乘之又以高乘之六而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a thatched roof with a lower width of 3 zhang, a lower length of 4 zhang, an upper length of 2 zhang (with no width), and a height of 1 zhang.
Question: what is the volume?

The procedure says: Double the lower length, add the upper length to it.
Multiply it by the width, then multiply it by the height.
Finally, divide by 6.

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
廣積 = 總袤 * 下廣

# 又以高乘之
體積 = 廣積 * 高

# 六而一
a = Fraction(體積, 6)  # Convert to chi (cubic units)
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5000, Actual: 5"""
