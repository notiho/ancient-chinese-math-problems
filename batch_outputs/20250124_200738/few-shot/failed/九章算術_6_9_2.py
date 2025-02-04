"""
今有絡絲一斤為練絲一十二兩，練絲一斤為青絲一斤十二銖。今有青絲一斤，問︰本絡絲幾何？
術曰：以練絲十二兩乘青絲一斤一十二銖為法。以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之，為實。實如法得一斤。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of raw silk, which produces 12 liang of refined silk.
1 jin of refined silk produces 1 jin and 12 zhu of pure silk.
Now suppose there is 1 jin of pure silk.
Question: how much raw silk was originally required?

The procedure says: Multiply 12 liang of refined silk by 1 jin and 12 zhu of pure silk to obtain the divisor.
Multiply the number of zhu in 1 jin of pure silk by the number of liang in 1 jin of refined silk, and then multiply by 1 jin of raw silk to obtain the dividend.
Divide the dividend by the divisor to obtain the result.

Answer: *a* jin.
"""

from fractions import Fraction

# 練絲一斤為青絲一斤十二銖
練絲一斤 = 1  # in jin
青絲一斤 = 1  # in jin
青絲餘銖 = 12  # in zhu

# 統一單位：1 斤 = 16 兩, 1 兩 = 24 銖
青絲一斤銖數 = (青絲一斤 * 16 * 24) + (青絲餘銖)

# 統一單位：練絲一斤 = 16 兩
練絲一斤兩數 = 練絲一斤 * 16

# 統一單位：絡絲一斤 = 16 兩
絡絲一斤 = 16  # in liang

# 以練絲十二兩乘青絲一斤一十二銖為法
練絲十二兩 = 12  # in liang
法 = 練絲十二兩 * 青絲一斤銖數

# 以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之，為實
實 = 青絲一斤銖數 * 練絲一斤兩數 * 絡絲一斤

# 實如法得一斤
a = Fraction(實, 法) / 16  # Convert back to jin
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 4/3"""
