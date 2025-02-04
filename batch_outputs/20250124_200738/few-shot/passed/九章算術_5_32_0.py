"""
今有穿地，袤一丈六尺，深一丈，上廣六尺，為垣積五百七十六尺。問︰穿地下廣幾何？
術曰：置垣積尺，四之為實。以深、袤相乘，又三之，為法。所得倍之，減上廣，餘即下廣。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a dug-out area with:
Length (mào) of 1 zhang and 6 chi,
Depth of 1 zhang,
Top width of 6 chi,
And a wall volume of 576 chi³.
Question: what is the bottom width of the dug-out area?

The procedure says:
Place the wall volume in chi³, multiply it by 4 to get the dividend.
Multiply the depth and length together, then multiply by 3 to get the divisor.
Double the result, subtract the top width, and the remainder is the bottom width.

Answer: the bottom width is *a* chi.
"""

# Input values
袤 = 1 * 10 + 6  # Convert 1 zhang 6 chi to chi
深 = 1 * 10      # Convert 1 zhang to chi
上廣 = 6         # Top width in chi
垣積 = 576       # Wall volume in chi³

# 置垣積尺，四之為實
實 = 4 * 垣積

# 以深、袤相乘，又三之，為法
法 = 3 * (深 * 袤)

# 所得倍之
倍之 = Fraction(實, 法) * 2

# 減上廣，餘即下廣
a = 倍之 - 上廣#----- content ends here -----

"""
"""
