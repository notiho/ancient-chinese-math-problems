"""
今有穿地，袤一丈六尺，深一丈，上廣六尺，為垣積五百七十六尺。問︰穿地下廣幾何？
術曰：置垣積尺，四之為實。以深、袤相乘，又三之，為法。所得倍之，減上廣，餘即下廣。
荅曰： a(=18/5)尺 。
"""

#----- content starts here -----
"""
Suppose there is a dug-out earth area with the following dimensions:
Length (袤) = 1 zhang 6 chi, Depth (深) = 1 zhang, Top width (上廣) = 6 chi, and the wall volume (垣積) = 576 chi³.
Question: what is the bottom width (下廣)?

The procedure says:
Place the wall volume in chi³ and multiply it by 4 to obtain the dividend.
Multiply the depth and length together, then multiply by 3 to obtain the divisor.
Double the result of the division, subtract the top width, and the remainder is the bottom width.

Answer: *a*(=18/5) chi.
"""

# Dimensions
袤 = 1 * 10 + 6  # 1丈6尺 = 16尺
深 = 1 * 10      # 1丈 = 10尺
上廣 = 6         # 6尺
垣積 = 576       # 576尺³

# 術曰：置垣積尺，四之為實
實 = 4 * 垣積

# 以深、袤相乘，又三之，為法
法 = 3 * (深 * 袤)

# 所得倍之，減上廣，餘即下廣
下廣 = 2 * Fraction(實, 法) - 上廣

a = 下廣  # 18/5 chi#----- content ends here -----

"""
"""
