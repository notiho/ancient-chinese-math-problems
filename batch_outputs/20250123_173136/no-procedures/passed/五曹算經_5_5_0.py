"""
今有生絲一斤為練絲一十二两，有練絲一千五百八十七两。問：生絲㡬何？
答曰： a两 。
"""

"""
Suppose there is 1 jin of raw silk that produces 12 liang of refined silk.
If there are 1587 liang of refined silk, how much raw silk is required?

Answer: *a* liang.
"""

# 生絲一斤為練絲一十二两
raw_silk_per_jin = 16  # 1 jin = 16 liang
refined_silk_per_raw_silk = 12

# 練絲一千五百八十七两
refined_silk = 1587

# Calculate the raw silk required
# For every 12 liang of refined silk, 16 liang of raw silk is needed
a = Fraction(refined_silk * raw_silk_per_jin, refined_silk_per_raw_silk)

# Output the result
a
"""
"""
