"""
今有生絲一斤為練絲一十二两，有練絲一千五百八十七两。問：生絲㡬何？
答曰： a 两。
"""

"""
Suppose 1 jin of raw silk produces 12 liang of refined silk. 
Now, there are 1587 liang of refined silk.
Question: how much raw silk is required?

Answer: *a* liang.
"""

# 1斤生絲 produces 12两練絲
生絲_to_練絲_ratio = 12

# Total 練絲
練絲 = 1587

# Calculate 生絲 required
a = Fraction(練絲 * 1, 生絲_to_練絲_ratio)  # Convert refined silk back to raw silk in liang
"""
Variable 'a' has wrong value. Expected: 2116, Actual: 529/4"""
