"""
今有絡絲一斤為練絲一十二兩，練絲一斤為青絲一斤十二銖。今有青絲一斤，問︰本絡絲幾何？
術曰：以練絲十二兩乘青絲一斤一十二銖為法。以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之，為實。實如法得一斤。
荅曰： a(=128/99)斤 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of raw silk, which produces 12 liang of refined silk.
1 jin of refined silk produces 1 jin and 12 zhu of pure silk.
Now, suppose there is 1 jin of pure silk.
Question: how much raw silk was originally required?

The procedure says: Multiply the 12 liang of refined silk by 1 jin and 12 zhu of pure silk to obtain the divisor.
Multiply the number of zhu in 1 jin of pure silk by the number of liang in 1 jin of refined silk.
Also multiply by 1 jin of raw silk to obtain the dividend.
Divide the dividend by the divisor to obtain the result.

The answer says: *a*(=128/99) jin of raw silk.
"""

# 練絲一十二兩
練絲_每絡絲 = 12  # liang per jin of raw silk

# 練絲一斤為青絲一斤一十二銖
青絲_每練絲 = 1 + Fraction(12, 16)  # 1 jin and 12 zhu (12 zhu = 12/16 jin)

# 青絲一斤
青絲 = 1  # jin

# 以練絲十二兩乘青絲一斤一十二銖為法
法 = 練絲_每絡絲 * 青絲_每練絲

# 以青絲一斤銖數乘練絲一斤兩數
青絲_銖數 = 青絲 * 16  # Convert 1 jin of pure silk to zhu (1 jin = 16 zhu)
實 = 青絲_銖數 * 練絲_每絡絲

# 又以絡絲一斤乘之，為實
絡絲 = 1  # Assume 1 jin of raw silk initially
實 *= 絡絲

# 實如法得一斤
a = Fraction(實, 法)  # 128/99 jin of raw silk#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 64/7"""
