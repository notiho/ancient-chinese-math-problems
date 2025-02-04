"""
今有生絲三十斤，乾之，耗三斤十二兩。今有乾絲一十二斤，問︰生絲幾何？
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there are 30 jin of raw silk. After drying, it loses 3 jin and 12 liang in weight.
Now, given 12 jin of dried silk, how much raw silk was it originally?

Answer: it was *a* jin of raw silk.
"""

# 生絲三十斤
生絲 = 30

# 耗三斤十二兩 (1 jin = 16 liang, so 3 jin 12 liang = 3 * 16 + 12 = 60 liang)
耗損 = 3 * 16 + 12

# 乾絲重量 after drying (in liang)
乾絲 = 生絲 * 16 - 耗損

# 乾絲一十二斤 (convert to liang: 12 jin = 12 * 16 liang)
已知乾絲 = 12 * 16

# Calculate the proportion of raw silk to dried silk
比例 = Fraction(生絲 * 16, 乾絲)

# Use the proportion to calculate the raw silk equivalent of 12 jin dried silk
a = Fraction(比例 * 已知乾絲, 16)  # Convert back to jin

a#----- content ends here -----

"""
"""
