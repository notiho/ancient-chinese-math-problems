"""
今有生絲三十斤，乾之，耗三斤十二兩。今有乾絲一十二斤，問︰生絲幾何？
術曰：置生絲兩數，除耗數，餘，以為法。三十斤乘乾絲兩數為實。實如法得生絲數。
荅曰： a(=96/7)斤 。
"""

#----- content starts here -----
"""
Suppose there are 30 jin of raw silk. When dried, it loses 3 jin and 12 liang.
Now suppose there are 12 jin of dried silk.
Question: how much raw silk does it correspond to?

The procedure says: Place the number of raw silk in liang and subtract the number of loss in liang. The remainder becomes the divisor.
Multiply 30 jin by the number of dried silk in liang to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of raw silk.

Answer: *a*(=96/7) jin.
"""

# 生絲三十斤
生絲 = 30

# 乾之，耗三斤十二兩
耗斤 = 3
耗兩 = 12
耗總兩 = 耗斤 * 16 + 耗兩  # Convert to liang (1 jin = 16 liang)

# 乾絲一十二斤
乾絲 = 12

# 置生絲兩數
生絲總兩 = 生絲 * 16  # Convert to liang

# 除耗數，餘，以為法
法 = 生絲總兩 - 耗總兩

# 三十斤乘乾絲兩數為實
實 = 生絲 * (乾絲 * 16)  # Convert dried silk to liang and multiply

# 實如法得生絲數
a = Fraction(實, 法)  # 96/7 jin#----- content ends here -----

"""
"""
