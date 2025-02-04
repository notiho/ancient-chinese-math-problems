"""
今有絡絲一斤為練絲一十二兩，練絲一斤為青絲一斤十二銖。今有青絲一斤，問︰本絡絲幾何？
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there is raw silk (絡絲), and 1 jin of raw silk produces 12 liang of refined silk (練絲). 
Then, 1 jin of refined silk produces 1 jin and 12 zhu of fine silk (青絲). 
Now, if there is 1 jin of fine silk, how much raw silk was originally required?

Answer: *a* jin.
"""

from fractions import Fraction

# Conversion rates
# 1 jin of raw silk produces 12 liang of refined silk
raw_to_refined_ratio = Fraction(12, 16)  # 12 liang = 12/16 jin

# 1 jin of refined silk produces 1 jin and 12 zhu of fine silk
refined_to_fine_ratio = Fraction(1, 1) + Fraction(12, 16 * 24)  # 12 zhu = 12/(16*24) jin

# Given: 1 jin of fine silk
fine_silk = 1

# Calculate the amount of refined silk required to produce 1 jin of fine silk
refined_silk = Fraction(fine_silk) / refined_to_fine_ratio

# Calculate the amount of raw silk required to produce the refined silk
raw_silk = refined_silk / raw_to_refined_ratio

# Result
a = raw_silk
a#----- content ends here -----

"""
"""
