"""
今有穿地，袤一丈六尺，深一丈，上廣六尺，為垣積五百七十六尺。問︰穿地下廣幾何？
術曰：置垣積尺，四之為實。以深、袤相乘，又三之，為法。所得倍之，減上廣，餘即下廣。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a dug-out area with the following dimensions:
- Length (袤) = 1 zhang 6 chi
- Depth (深) = 1 zhang
- Top width (上廣) = 6 chi
The total volume (垣積) is 576 chi³.
Question: what is the bottom width (下廣)?

The procedure says:
1. Place the volume (垣積) and multiply it by 4 to get the dividend (實).
2. Multiply the depth (深) and length (袤) together, then multiply the result by 3 to get the divisor (法).
3. Divide the dividend by the divisor, double the result, and subtract the top width (上廣). The remainder is the bottom width (下廣).

Answer: *a* chi.
"""

from fractions import Fraction

# Given values
袤 = 1 * 10 + 6  # Convert 1 zhang 6 chi to chi
深 = 1 * 10  # Convert 1 zhang to chi
上廣 = 6  # Top width in chi
垣積 = 576  # Volume in chi³

# Step 1: Multiply the volume by 4 to get the dividend (實)
實 = 4 * 垣積

# Step 2: Multiply depth and length, then multiply by 3 to get the divisor (法)
法 = 3 * (深 * 袤)

# Step 3: Divide the dividend by the divisor
result = Fraction(實, 法)

# Step 4: Double the result and subtract the top width
a = 2 * result - 上廣

# Output the bottom width
a#----- content ends here -----

"""
"""
