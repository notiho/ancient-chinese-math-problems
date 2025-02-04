"""
今有絡絲一斤為練絲一十二兩，練絲一斤為青絲一斤十二銖。今有青絲一斤，問︰本絡絲幾何？
術曰：以練絲十二兩乘青絲一斤一十二銖為法。以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之，為實。實如法得一斤。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of raw silk (絡絲), which produces 12 liang of refined silk (練絲). 
1 jin of refined silk produces 1 jin and 12 zhu of pure silk (青絲).
Now, given 1 jin of pure silk, how much raw silk was originally required?

The procedure says: Multiply the 12 liang of refined silk by the 1 jin and 12 zhu of pure silk to form the divisor.
Multiply the number of zhu in 1 jin of pure silk by the number of liang in 1 jin of refined silk, and also multiply by 1 jin of raw silk to form the dividend.
Divide the dividend by the divisor to obtain the amount of raw silk.

The answer says: *a* jin.
"""

# 練絲一斤為青絲一斤十二銖
青絲_一斤 = 1
青絲_銖 = 12  # 1 jin 12 zhu

# 統一青絲為銖數 (1 jin = 16 liang, 1 liang = 24 zhu)
青絲_銖數 = (青絲_一斤 * 16 * 24) + 青絲_銖

# 統一練絲為銖數 (1 jin = 16 liang, 1 liang = 24 zhu)
練絲_一斤_銖數 = 16 * 24  # 1 jin = 16 liang, 1 liang = 24 zhu

# 練絲一斤為絡絲一十二兩
練絲_一斤_兩數 = 16  # 1 jin = 16 liang
絡絲_一斤_練絲 = 12  # 12 liang

# 以練絲十二兩乘青絲一斤一十二銖為法
法 = 練絲_一斤_兩數 * 青絲_銖數

# 以青絲一斤銖數乘練絲一斤兩數，又以絡絲一斤乘之，為實
實 = 青絲_銖數 * 練絲_一斤_兩數 * 1  # 給定青絲 1 jin

# 實如法得一斤
a = Fraction(實, 法)  # 結果為絡絲的斤數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 1"""
