"""
今有絡絲一斤為練絲一十二兩練絲一斤為青絲一斤十二銖今有青絲一斤問本絡絲幾何
術曰以練絲十二兩乘青絲一斤一十二銖為法以青絲一斤銖數乘練絲一斤兩數又以絡絲一斤乘之為實實如法得一斤
荅曰 a斤 
"""

#----- content starts here -----
"""
Suppose there is 1 jin of raw silk, which produces 12 liang of refined silk.
1 jin of refined silk produces 1 jin and 12 zhu of finished silk.
Now, suppose there is 1 jin of finished silk.
Question: how much raw silk is required?

The procedure says: Multiply 12 liang of refined silk by 1 jin and 12 zhu of finished silk to obtain the divisor.
Multiply the zhu count of 1 jin of finished silk by the liang count of 1 jin of refined silk, and then multiply by 1 jin of raw silk to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of raw silk.

The answer says: *a* jin of raw silk.
"""

# 練絲一斤為青絲一斤十二銖
練絲_一斤_青絲 = 1 + Fraction(12, 16)  # 1 jin and 12 zhu (16 zhu = 1 liang)

# 絡絲一斤為練絲一十二兩
絡絲_一斤_練絲 = 12  # 12 liang

# 青絲一斤
青絲 = 1

# 以練絲十二兩乘青絲一斤一十二銖，為法
法 = 練絲_一斤_青絲 * 絡絲_一斤_練絲

# 以青絲一斤銖數乘練絲一斤兩數
實 = 青絲 * 16 * 絡絲_一斤_練絲  # 青絲 in zhu (16 zhu = 1 liang)

# 又以絡絲一斤乘之，為實
實 = 實

# 實如法得一斤
a = Fraction(實, 法)  # Amount of raw silk in jin#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 64/7"""
