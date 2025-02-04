"""
今有絡絲一斤為練絲一十二兩練絲一斤為青絲一斤十二銖今有青絲一斤問本絡絲幾何
術曰以練絲十二兩乘青絲一斤一十二銖為法以青絲一斤銖數乘練絲一斤兩數又以絡絲一斤乘之為實實如法得一斤
荅曰 a斤 
"""

"""
Suppose there is 1 jin of raw silk (luo si). It produces 12 liang of refined silk (lian si).
1 jin of refined silk produces 1 jin and 12 zhu of fine silk (qing si).
Now, suppose there is 1 jin of fine silk. Question: how much raw silk was originally required?

The procedure says: Multiply the 12 liang of refined silk by the 1 jin and 12 zhu of fine silk to obtain the divisor.
Multiply the number of zhu in 1 jin of fine silk by the number of liang in 1 jin of refined silk, and then multiply by the 1 jin of raw silk to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of raw silk.

Answer: *a* jin of raw silk.
"""

# 練絲一十二兩
練絲每斤_兩 = 12

# 練絲一斤為青絲一斤十二銖
青絲每斤 = 1
青絲每斤_銖 = 12

# 青絲一斤
青絲 = 1

# 以練絲十二兩乘青絲一斤一十二銖，為法
法 = 練絲每斤_兩 * (青絲每斤 * 16 + 青絲每斤_銖)

# 以青絲一斤銖數乘練絲一斤兩數
實 = (青絲 * 16 + 青絲每斤_銖) * 練絲每斤_兩

# 又以絡絲一斤乘之
絡絲 = 1
實 *= 絡絲

# 實如法得一斤
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 1"""
