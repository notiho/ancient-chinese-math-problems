"""
今有塹堵下廣二丈，袤一十八丈六尺，高二丈五尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，二而一。
荅曰： a(=46500)尺 。
"""

"""
Suppose there is a trench wall with a bottom width of 2 zhang, a length of 18 zhang 6 chi, and a height of 2 zhang 5 chi.
Question: what is the volume?

The procedure says: Multiply the width and the length. Multiply the result by the height. Divide by 2 to get the volume.

Answer: *a*(=46500) chi³.
"""

# 下廣二丈 (convert to chi)
廣 = 2 * 10  # 1 zhang = 10 chi

# 袤一十八丈六尺 (convert to chi)
袤 = 18 * 10 + 6  # 1 zhang = 10 chi

# 高二丈五尺 (convert to chi)
高 = 2 * 10 + 5  # 1 zhang = 10 chi

# 廣袤相乘
廣袤積 = 廣 * 袤

# 以高乘之
體積 = 廣袤積 * 高

# 二而一
a = Fraction(體積, 2)  # 46500 chi³
"""
"""
