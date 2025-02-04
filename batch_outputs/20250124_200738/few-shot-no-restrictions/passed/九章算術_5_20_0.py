"""
今有鱉臑下廣五尺，無袤，上袤四尺，無廣，高七尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，六而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a turtle-shell-shaped solid with the following dimensions:
- The lower width is 5 chi (no length),
- The upper length is 4 chi (no width),
- The height is 7 chi.

Question: what is the volume of the solid?

The procedure says: Multiply the width and length together, then multiply by the height, and divide by 6.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# 下廣 (lower width) = 5 尺
下廣 = 5

# 上袤 (upper length) = 4 尺
上袤 = 4

# 高 (height) = 7 尺
高 = 7

# 廣袤相乘
廣袤積 = 下廣 * 上袤

# 以高乘之
體積 = 廣袤積 * 高

# 六而一
a = Fraction(體積, 6)

# Output the result
a#----- content ends here -----

"""
"""
