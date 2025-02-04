"""
今有絡絲一斤為練絲一十二兩，練絲一斤為青絲一斤十二銖。今有青絲一斤，問︰本絡絲幾何？
術曰：以練絲十二兩乘青絲一斤一十二銖為法。以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之，為實。實如法得一斤。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of raw silk (絡絲), which produces 12 liang of refined silk (練絲), and 1 jin of refined silk produces 1 jin and 12 zhu of pure silk (青絲).
Now, given 1 jin of pure silk, how much raw silk was originally required?

The procedure says: Multiply 12 liang of refined silk by 1 jin and 12 zhu of pure silk to obtain the divisor.
Multiply the number of zhu in 1 jin of pure silk by the number of liang in 1 jin of refined silk, and then multiply by the raw silk (1 jin), to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of raw silk.

The answer says: *a* jin.
"""

from fractions import Fraction

# 練絲一斤為青絲一斤一十二銖
青絲_一斤 = 1  # 1 jin
青絲_一十二銖 = Fraction(12, 16)  # 12 zhu = 12/16 liang
青絲總量 = 青絲_一斤 + 青絲_一十二銖  # Total pure silk in liang

# 絡絲一斤為練絲一十二兩
練絲_一斤 = 16  # 1 jin = 16 liang
練絲_一十二兩 = 12  # Refined silk from 1 jin of raw silk

# 以練絲十二兩乘青絲一斤一十二銖為法
法 = 練絲_一十二兩 * 青絲總量

# 以青絲一斤銖數乘練絲一斤兩數
青絲_銖數 = 青絲總量  # Total pure silk in liang
實 = 青絲_銖數 * 練絲_一斤

# 又以絡絲一斤乘之
絡絲_一斤 = 1  # 1 jin of raw silk
實 *= 絡絲_一斤

# 實如法得一斤
a = Fraction(實, 法)

# Output the result
a  # The amount of raw silk needed in jin#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 4/3"""
