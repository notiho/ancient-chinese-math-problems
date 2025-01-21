"""
今有生絲三十斤，乾之，耗三斤十二兩。今有乾絲一十二斤，問︰生絲幾何？
荅曰： a斤 。
"""

"""
Suppose there are 30 jin of raw silk. After drying, it loses 3 jin and 12 liang in weight.
Now, given 12 jin of dried silk, how much raw silk was it originally?

Answer: *a* jin.
"""

# 生絲三十斤
raw_silk = 30

# 耗三斤十二兩 (1 jin = 16 liang, so 3 jin 12 liang = 3 + 12/16 jin)
loss = 3 + Fraction(12, 16)

# 乾絲重量 = 生絲重量 - 耗損
dried_silk = raw_silk - loss

# 現有乾絲一十二斤
current_dried_silk = 12

# 比例計算：生絲與乾絲的比例
raw_to_dried_ratio = raw_silk / dried_silk

# 求生絲重量
a = raw_to_dried_ratio * current_dried_silk

a
"""
"""
