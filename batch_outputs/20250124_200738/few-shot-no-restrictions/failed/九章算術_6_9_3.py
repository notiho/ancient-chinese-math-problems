"""
今有絡絲一斤為練絲一十二兩，練絲一斤為青絲一斤十二銖。今有青絲一斤，問︰本絡絲幾何？
術曰：以練絲十二兩乘青絲一斤一十二銖為法。以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之，為實。實如法得一斤。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of raw silk (絡絲), which produces 12 liang of refined silk (練絲).
1 jin of refined silk produces 1 jin and 12 zhu of pure silk (青絲).
Now, if there is 1 jin of pure silk, how much raw silk was originally required?

The procedure says:
Take the 12 liang of refined silk and multiply it by 1 jin and 12 zhu of pure silk to form the divisor.
Take the number of zhu in 1 jin of pure silk and multiply it by the number of liang in 1 jin of refined silk.
Then multiply this by the raw silk (1 jin), forming the dividend.
Divide the dividend by the divisor to obtain the result.

Answer: *a* jin of raw silk.
"""

from fractions import Fraction

# Definitions
絡絲_一斤 = 1  # 1 jin of raw silk
練絲_一斤_兩數 = 16  # 1 jin = 16 liang
練絲_一斤_青絲 = 1 + Fraction(12, 16)  # 1 jin and 12 zhu = 1 jin + 12/16 jin
青絲_一斤 = 1  # 1 jin of pure silk

# 法: 練絲 12 兩 * 青絲 (1 jin + 12 zhu)
法 = 12 * 練絲_一斤_青絲

# 實: 青絲 1 jin * 練絲 1 jin (16 liang) * 絡絲 1 jin
實 = 青絲_一斤 * 練絲_一斤_兩數 * 絡絲_一斤

# 實如法得一斤
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 16/21"""
