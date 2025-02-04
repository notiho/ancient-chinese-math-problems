"""
今有絡絲一斤為練絲一十二兩，練絲一斤為青絲一斤十二銖。今有青絲一斤，問︰本絡絲幾何？
荅曰： a斤 。
"""

"""
Suppose 1 jin of raw silk (絡絲) produces 12 liang of refined silk (練絲), and 1 jin of refined silk produces 1 jin and 12 zhu of fine silk (青絲).
Now, if there is 1 jin of fine silk, how much raw silk was originally required?

Answer: *a* jin.
"""

from fractions import Fraction

# Conversion rates
絡絲_to_練絲 = Fraction(12, 16)  # 1 jin of raw silk produces 12 liang of refined silk (1 jin = 16 liang)
練絲_to_青絲 = Fraction(16 + 12 / 16, 16)  # 1 jin of refined silk produces 1 jin and 12 zhu of fine silk (1 jin = 16 liang, 1 liang = 24 zhu)

# 青絲 given
青絲 = 1  # 1 jin of fine silk

# Calculate the amount of 練絲 needed to produce 1 jin of 青絲
練絲 = Fraction(青絲) / 練絲_to_青絲

# Calculate the amount of 絡絲 needed to produce the required 練絲
絡絲 = 練絲 / 絡絲_to_練絲

# Result
a = 絡絲
a
"""
Code error: both arguments should be Rational instances"""
