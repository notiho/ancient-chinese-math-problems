"""
今有絡絲一斤為練絲一十二兩，練絲一斤為青絲一斤十二銖。今有青絲一斤，問︰本絡絲幾何？
術曰：以練絲十二兩乘青絲一斤一十二銖為法。以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之，為實。實如法得一斤。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there is raw silk (絡絲), where 1 jin of raw silk produces 12 liang of refined silk (練絲), 
and 1 jin of refined silk produces 1 jin and 12 zhu of pure silk (青絲).
Now, given 1 jin of pure silk, how much raw silk was originally required?

The procedure says: Multiply the 12 liang of refined silk by 1 jin and 12 zhu of pure silk to obtain the divisor.
Multiply the number of zhu in 1 jin of pure silk by the number of liang in 1 jin of refined silk, 
and then multiply by the number of jin of raw silk to obtain the dividend.
Divide the dividend by the divisor to obtain the number of jin of raw silk.

Answer: *a* jin.
"""

from fractions import Fraction

# Constants
練絲_絡絲率 = 12  # 1 jin of raw silk produces 12 liang of refined silk
青絲_練絲率 = 1 + Fraction(12, 16)  # 1 jin of refined silk produces 1 jin and 12 zhu of pure silk (12 zhu = 12/16 jin)

# 青絲一斤
青絲 = 1  # 1 jin of pure silk

# 法：以練絲十二兩乘青絲一斤一十二銖
法 = 練絲_絡絲率 * 青絲_練絲率

# 實：以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之
實 = 青絲 * 16 * 練絲_絡絲率  # Convert 青絲 to zhu (1 jin = 16 zhu)

# 實如法得一斤
a = Fraction(實, 法)

a  # Result in jin of raw silk#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 64/7"""
