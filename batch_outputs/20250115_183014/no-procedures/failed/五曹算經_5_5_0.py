"""
今有生絲一斤為練絲一十二两，有練絲一千五百八十七两。問：生絲㡬何？
答曰： a 两。
"""

"""
Suppose there is 1 jin of raw silk that produces 12 liang of refined silk.  
Now, there are 1587 liang of refined silk.  
Question: how much raw silk is required?

Answer: *a* liang.
"""

# Conversion rate: 1 jin of raw silk produces 12 liang of refined silk
raw_to_refined_ratio = 12

# Refined silk amount
refined_silk = 1587

# Calculate raw silk required
a = Fraction(refined_silk, raw_to_refined_ratio)

# Result is in liang (兩)
"""
Variable 'a' has wrong value. Expected: 2116, Actual: 529/4"""
