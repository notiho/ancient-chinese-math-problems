"""
今有絡絲一斤為練絲一十二兩，練絲一斤為青絲一斤十二銖。今有青絲一斤，問︰本絡絲幾何？
術曰：以練絲十二兩乘青絲一斤一十二銖為法。以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之，為實。實如法得一斤。
荅曰： a斤 。
"""

"""
Suppose there is 1 jin of raw silk, which produces 12 liang of refined silk.
1 jin of refined silk produces 1 jin and 12 zhu of finished silk.
Now, suppose there is 1 jin of finished silk.
Question: how much raw silk was originally required?

The procedure says: Multiply the 12 liang of refined silk by 1 jin and 12 zhu of finished silk to obtain the divisor.
Multiply the zhu count of 1 jin of finished silk by the liang count of 1 jin of refined silk, and also multiply by 1 jin of raw silk to obtain the dividend.
Divide the dividend by the divisor to obtain the jin of raw silk.

The answer says: *a* jin.
"""

from fractions import Fraction

# 練絲一斤為青絲一斤十二銖
青絲_一斤 = 1  # in jin
青絲_一斤_銖數 = 1 * 16 + 12  # Convert to zhu (1 jin = 16 liang, 1 liang = 24 zhu)

# 絡絲一斤為練絲一十二兩
練絲_一斤_兩數 = 12  # in liang

# 以練絲十二兩乘青絲一斤一十二銖為法
法 = 練絲_一斤_兩數 * 青絲_一斤_銖數

# 以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之，為實
實 = 青絲_一斤_銖數 * 練絲_一斤_兩數 * 1  # 1 jin of raw silk

# 實如法得一斤
a = Fraction(實, 法)  # Result in jin of raw silk
"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 1"""
