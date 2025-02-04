"""
今有穿地袤一丈六尺深一丈上廣六尺為垣積五百七十六尺問穿地下廣幾何
術曰置垣積尺四之為實以深袤相乘又三之為法所得倍之減上廣餘即下廣
荅曰 a尺 
"""

"""
Suppose there is an excavation with a length (mao) of 1 zhang 6 chi, a depth of 1 zhang, and an upper width of 6 chi.
The volume of the wall (yuan) is 576 chi³.
Question: what is the lower width of the excavation?

The procedure says: Place the volume of the wall in chi³, multiply it by 4 to obtain the dividend.
Multiply the depth and length together, then multiply by 3 to obtain the divisor.
Divide the dividend by the divisor, double the result, subtract the upper width, and the remainder is the lower width.

Answer: the lower width is *a* chi.
"""

# 袤一丈六尺
袤 = 1 * 10 + 6  # Convert zhang and chi to chi

# 深一丈
深 = 1 * 10  # Convert zhang to chi

# 上廣六尺
上廣 = 6

# 垣積五百七十六尺³
垣積 = 576

# 置垣積尺，四之，為實
實 = 4 * 垣積

# 以深袤相乘，又三之，為法
法 = 3 * (深 * 袤)

# 所得倍之
所得 = Fraction(實, 法)
倍之 = 2 * 所得

# 減上廣，餘即下廣
a = 倍之 - 上廣
"""
"""
