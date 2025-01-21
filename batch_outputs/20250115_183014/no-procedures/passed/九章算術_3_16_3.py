"""
今有生絲三十斤，乾之，耗三斤十二兩。今有乾絲一十二斤，問︰生絲幾何？
荅曰： a斤 。
"""

"""
Suppose there are 30 jin of raw silk. After drying, it loses 3 jin and 12 liang in weight.
Now, given 12 jin of dried silk, how much raw silk was it originally?

Answer: it was *a* jin of raw silk.
"""

# 生絲三十斤
生絲重量 = 30

# 耗三斤十二兩 (1 jin = 16 liang, so 3 jin 12 liang = 3 * 16 + 12 = 60 liang)
耗重量 = 3 * 16 + 12

# 乾絲重量 = 生絲重量 - 耗重量 (convert everything to liang for precision)
乾絲重量 = 生絲重量 * 16 - 耗重量

# 每斤乾絲對應的生絲重量 (in liang)
每斤乾絲對應生絲 = Fraction(生絲重量 * 16, 乾絲重量)

# 現有乾絲一十二斤 (convert to liang)
現有乾絲 = 12 * 16

# 計算對應的生絲重量 (convert back to jin)
a = Fraction(每斤乾絲對應生絲 * 現有乾絲, 16)

# Result
a
"""
"""
