"""
今有穿地，袤一丈六尺，深一丈，上廣六尺，為垣積五百七十六尺。問︰穿地下廣幾何？
術曰：置垣積尺，四之為實。以深、袤相乘，又三之，為法。所得倍之，減上廣，餘即下廣。
荅曰： a尺 。
"""

"""
Suppose there is a dug-out space with a length (mao) of 1 zhang and 6 chi, a depth of 1 zhang, and an upper width of 6 chi.
The wall volume is 576 chi³.
Question: what is the lower width of the dug-out space?

The procedure says: Place the wall volume in chi³ and multiply it by 4 to obtain the dividend.
Multiply the depth and length together, then multiply by 3 to obtain the divisor.
Double the result, subtract the upper width, and the remainder is the lower width.

Answer: *a* chi.
"""

# 袤一丈六尺
袤 = 1 * 10 + 6  # Convert zhang and chi to chi

# 深一丈
深 = 1 * 10  # Convert zhang to chi

# 上廣六尺
上廣 = 6

# 垣積五百七十六尺
垣積 = 576

# 置垣積尺，四之為實
實 = 4 * 垣積

# 以深、袤相乘
法 = 深 * 袤

# 又三之，為法
法 = 3 * 法

# 所得倍之
下廣 = 2 * Fraction(實, 法)

# 減上廣，餘即下廣
a = 下廣 - 上廣
"""
"""
