"""
今有絡絲一斤為練絲一十二兩，練絲一斤為青絲一斤十二銖。今有青絲一斤，問︰本絡絲幾何？
術曰：以練絲十二兩乘青絲一斤一十二銖為法。以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之，為實。實如法得一斤。
荅曰： a(=128/99)斤 。
"""

"""
Suppose there is 1 jin of raw silk, which produces 12 liang of refined silk. 
1 jin of refined silk produces 1 jin and 12 zhu of pure silk.
Now, suppose there is 1 jin of pure silk. 
Question: how much raw silk was originally required?

The procedure says: Multiply 12 liang of refined silk by 1 jin and 12 zhu of pure silk to obtain the divisor.
Multiply the number of zhu in 1 jin of pure silk by the number of liang in 1 jin of refined silk, and then multiply by 1 jin of raw silk to obtain the dividend.
Divide the dividend by the divisor to obtain the number of jin of raw silk.

The answer says: *a*(=128/99) jin.
"""

# 練絲一十二兩
練絲每斤出 = 12  # liang

# 練絲一斤為青絲一斤十二銖
青絲每斤出 = 1 + Fraction(12, 16)  # 1 jin 12 zhu = 1 + 12/16 jin

# 青絲一斤
青絲 = 1  # jin

# 以練絲十二兩乘青絲一斤一十二銖為法
法 = 練絲每斤出 * 青絲每斤出

# 以青絲一斤銖數乘練絲一斤兩數
青絲銖數 = 青絲  # 1 jin = 1 jin in this case
實 = 青絲銖數 * 練絲每斤出

# 又以絡絲一斤乘之
絡絲每斤 = 1  # jin
實 *= 絡絲每斤

# 實如法得一斤
a = Fraction(實, 法)  # 128/99 jin
"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 4/7"""
