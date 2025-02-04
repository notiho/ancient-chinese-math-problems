"""
今有穿地，袤一丈六尺，深一丈，上廣六尺，為垣積五百七十六尺。問︰穿地下廣幾何？
術曰：置垣積尺，四之為實。以深、袤相乘，又三之，為法。所得倍之，減上廣，餘即下廣。
荅曰： a尺 。
"""

"""
Suppose there is a dug-out earth structure with the following dimensions:
Length (mào) = 1 zhang 6 chi, Depth = 1 zhang, Upper Width = 6 chi, and Wall Volume = 576 chi³.
Question: what is the lower width of the dug-out earth?

The procedure says: Place the wall volume in chi³ and multiply it by 4 to get the dividend.
Multiply the depth and length together, then multiply by 3 to get the divisor.
Double the result of the division, subtract the upper width, and the remainder is the lower width.

Answer: the lower width is *a* chi.
"""

# Dimensions
袤 = 1 * 10 + 6  # Convert 1 zhang 6 chi to chi
深 = 1 * 10      # Convert 1 zhang to chi
上廣 = 6         # Upper width in chi
垣積 = 576       # Wall volume in chi³

# 術曰：置垣積尺，四之為實
實 = 4 * 垣積

# 以深、袤相乘，又三之，為法
法 = 3 * (深 * 袤)

# 所得倍之
倍之 = Fraction(實, 法) * 2

# 減上廣，餘即下廣
a = 倍之 - 上廣
"""
"""
