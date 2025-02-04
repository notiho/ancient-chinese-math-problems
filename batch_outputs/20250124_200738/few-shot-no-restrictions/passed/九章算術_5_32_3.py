"""
今有穿地，袤一丈六尺，深一丈，上廣六尺，為垣積五百七十六尺。問︰穿地下廣幾何？
術曰：置垣積尺，四之為實。以深、袤相乘，又三之，為法。所得倍之，減上廣，餘即下廣。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a dug-out space with the following dimensions:
- Length (袤) = 1 zhang 6 chi (16 chi),
- Depth (深) = 1 zhang (10 chi),
- Top width (上廣) = 6 chi,
and the wall volume (垣積) = 576 chi³.

Question: What is the bottom width (下廣)?

The procedure says:
1. Place the wall volume in chi³ and multiply it by 4 to get the dividend.
2. Multiply the depth and length together, then multiply the result by 3 to get the divisor.
3. Divide the dividend by the divisor, double the result, and subtract the top width. The remainder is the bottom width.

Answer: The bottom width is *a* chi.
"""

from fractions import Fraction

# Given dimensions
袤 = 16  # Length in chi
深 = 10  # Depth in chi
上廣 = 6  # Top width in chi
垣積 = 576  # Wall volume in chi³

# Step 1: Multiply the wall volume by 4 to get the dividend
實 = 4 * 垣積

# Step 2: Multiply depth and length, then multiply by 3 to get the divisor
法 = 3 * (深 * 袤)

# Step 3: Divide the dividend by the divisor
中間值 = Fraction(實, 法)

# Step 4: Double the result and subtract the top width
下廣 = 2 * 中間值 - 上廣

# Final answer
a = 下廣
a#----- content ends here -----

"""
"""
