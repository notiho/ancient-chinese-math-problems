"""
今有生絲一斤為練絲一十二两，有練絲一千五百八十七两。問：生絲㡬何？
答曰： a两 。
"""

"""
Suppose there is 1 jin (16 liang) of raw silk that produces 12 liang of refined silk.
Now, there are 1587 liang of refined silk.
Question: how much raw silk is needed?

Answer: *a* liang.
"""

# 生絲 1 斤 = 16 liang produces 練絲 12 liang
raw_silk_per_refined_silk = Fraction(16, 12)

# 練絲 1587 liang
refined_silk = 1587

# Calculate raw silk needed
a = raw_silk_per_refined_silk * refined_silk
"""
"""
