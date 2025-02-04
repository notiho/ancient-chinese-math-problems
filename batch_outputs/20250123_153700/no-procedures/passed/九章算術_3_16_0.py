"""
今有生絲三十斤，乾之，耗三斤十二兩。今有乾絲一十二斤，問︰生絲幾何？
荅曰： a斤 。
"""

"""
Suppose there are 30 jin of raw silk. After drying, it loses 3 jin and 12 liang in weight.
Now, given 12 jin of dried silk, how much raw silk did it originally weigh?

Answer: *a* jin.
"""

# 生絲三十斤
生絲 = 30

# 耗三斤十二兩 (1 jin = 16 liang, so 3 jin 12 liang = 3 + 12/16 jin)
耗 = 3 + Fraction(12, 16)

# 乾絲重量 = 生絲重量 - 耗損重量
乾絲 = 生絲 - 耗

# 比例關係：乾絲重量 / 生絲重量 = 已知乾絲重量 / 求生絲重量
已知乾絲 = 12

# 求生絲重量
a = Fraction(已知乾絲 * 生絲, 乾絲)

# Output the result
a
"""
"""
