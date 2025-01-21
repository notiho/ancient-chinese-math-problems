"""
今有絡絲一斤為練絲一十二兩練絲一斤為青絲一斤十二銖今有青絲一斤問本絡絲幾何
術曰以練絲十二兩乘青絲一斤一十二銖為法以青絲一斤銖數乘練絲一斤兩數又以絡絲一斤乘之為實實如法得一斤
荅曰 a斤 
"""

"""
Suppose there is 1 jin of raw silk (絡絲). It produces 12 liang of refined silk (練絲), and 1 jin of refined silk produces 1 jin and 12 zhu of finished silk (青絲).
Now, suppose there is 1 jin of finished silk. 
Question: how much raw silk is required?

The procedure says: Multiply the 12 liang of refined silk by the 1 jin and 12 zhu of finished silk to obtain the divisor.
Multiply the number of zhu in 1 jin of finished silk by the number of liang in 1 jin of refined silk, and then multiply by the raw silk.
This gives the dividend.
Divide the dividend by the divisor to obtain the amount of raw silk.

The answer says: *a* jin.
"""

# 練絲一斤為十二兩
練絲每斤兩數 = 12

# 練絲一斤為青絲一斤十二銖
青絲每斤銖數 = 1 * 16 + 12  # 1 jin = 16 zhu, so 1 jin and 12 zhu = 16 + 12 = 28 zhu

# 青絲一斤
青絲 = 1 * 16  # 1 jin = 16 zhu

# 以練絲十二兩乘青絲一斤一十二銖，為法
法 = 練絲每斤兩數 * 青絲每斤銖數

# 以青絲一斤銖數乘練絲一斤兩數
實 = 青絲 * 練絲每斤兩數

# 又以絡絲一斤乘之，為實
實 = 實  # This step is already included above since we are solving for raw silk.

# 實如法得一斤
a = Fraction(實, 法) / 16  # Convert zhu back to jin (1 jin = 16 zhu)
"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 1/28"""
