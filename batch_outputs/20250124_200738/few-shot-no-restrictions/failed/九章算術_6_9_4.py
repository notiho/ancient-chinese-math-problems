"""
今有絡絲一斤為練絲一十二兩，練絲一斤為青絲一斤十二銖。今有青絲一斤，問︰本絡絲幾何？
術曰：以練絲十二兩乘青絲一斤一十二銖為法。以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之，為實。實如法得一斤。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of raw silk, which produces 12 liang of refined silk.
1 jin of refined silk produces 1 jin and 12 zhu of fine silk.
Now, given 1 jin of fine silk, how much raw silk was originally required?

The procedure says:
- Multiply the 12 liang of refined silk by 1 jin and 12 zhu of fine silk to obtain the divisor.
- Multiply the number of zhu in 1 jin of fine silk by the number of liang in 1 jin of refined silk.
- Then multiply by 1 jin of raw silk to obtain the dividend.
- Divide the dividend by the divisor to obtain the result.

The answer says: *a* jin of raw silk.
"""

from fractions import Fraction

# Constants
練絲_一斤_兩數 = 12  # 1 jin of refined silk = 12 liang
青絲_一斤_銖數 = 1 * 16 + 12  # 1 jin and 12 zhu = 16 zhu per liang * 1 liang + 12 zhu

# 法: 練絲十二兩乘青絲一斤一十二銖
法 = 練絲_一斤_兩數 * 青絲_一斤_銖數

# 實: 青絲一斤銖數乘練絲一斤兩數
實 = 青絲_一斤_銖數 * 練絲_一斤_兩數

# Divide 实 by 法 to get the amount of raw silk
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 1"""
