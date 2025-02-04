"""
今有塹堵下廣二丈，袤一十八丈六尺，高二丈五尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，二而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a trench wall with a bottom width of 2 zhang, a length of 18 zhang 6 chi, and a height of 2 zhang 5 chi.
Question: what is the total volume?

The procedure says: Multiply the width and the length, then multiply by the height, and finally divide by 2.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# 下廣二丈 (convert to chi: 1 zhang = 10 chi)
廣 = 2 * 10  # in chi

# 袤一十八丈六尺 (convert to chi: 1 zhang = 10 chi)
袤 = 18 * 10 + 6  # in chi

# 高二丈五尺 (convert to chi: 1 zhang = 10 chi)
高 = 2 * 10 + 5  # in chi

# 廣袤相乘
底面積 = 廣 * 袤  # in square chi

# 以高乘之
體積 = 底面積 * 高  # in cubic chi

# 二而一 (divide by 2)
a = Fraction(體積, 2)

a  # The total volume in cubic chi#----- content ends here -----

"""
"""
