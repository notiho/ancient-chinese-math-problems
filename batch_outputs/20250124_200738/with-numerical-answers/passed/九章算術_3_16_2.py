"""
今有生絲三十斤，乾之，耗三斤十二兩。今有乾絲一十二斤，問︰生絲幾何？
術曰：置生絲兩數，除耗數，餘，以為法。三十斤乘乾絲兩數為實。實如法得生絲數。
荅曰： a(=96/7)斤 。
"""

#----- content starts here -----
"""
Suppose there are 30 jin of raw silk. After drying, it loses 3 jin and 12 liang.
Now, suppose there are 12 jin of dried silk.
Question: how much raw silk does it correspond to?

The procedure says: Place the weight of raw silk as the dividend and subtract the weight lost during drying. The remainder becomes the divisor.
Multiply the 30 jin of raw silk by the weight of dried silk to obtain the dividend.
Divide the dividend by the divisor to obtain the weight of raw silk.

Answer: *a*(=96/7) jin.
"""

# 生絲三十斤
生絲 = 30

# 耗三斤十二兩
耗 = 3 + Fraction(12, 16)  # 1 jin = 16 liang

# 置生絲兩數，除耗數，餘，以為法
法 = 生絲 - 耗

# 乾絲一十二斤
乾絲 = 12

# 三十斤乘乾絲兩數為實
實 = 生絲 * 乾絲

# 實如法得生絲數
a = Fraction(實, 法)  # 96/7 jin#----- content ends here -----

"""
"""
