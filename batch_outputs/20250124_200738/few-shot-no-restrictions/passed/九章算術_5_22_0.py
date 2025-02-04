"""
今有芻甍，下廣三丈，袤四丈，上袤二丈，無廣，高一丈。問︰積幾何？
術曰：倍下袤，上袤從之，以廣乘之，又以高乘之，六而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a thatched roof with the following dimensions:
- Bottom width: 3 zhang
- Bottom length: 4 zhang
- Top length: 2 zhang (no width)
- Height: 1 zhang

Question: What is the volume of the roof?

The procedure says:
Double the bottom length, add the top length to it, multiply by the width, then multiply by the height, and divide by 6.

Answer: *a* chi³.
"""

from fractions import Fraction

# Dimensions in zhang
下廣 = 3  # Bottom width
下袤 = 4  # Bottom length
上袤 = 2  # Top length
高 = 1    # Height

# Convert zhang to chi (1 zhang = 10 chi)
下廣 *= 10
下袤 *= 10
上袤 *= 10
高 *= 10

# Procedure
# 倍下袤
倍下袤 = 2 * 下袤

# 上袤從之
總袤 = 倍下袤 + 上袤

# 以廣乘之
積 = 總袤 * 下廣

# 又以高乘之
積 *= 高

# 六而一
a = Fraction(積, 6)

# Answer
a#----- content ends here -----

"""
"""
