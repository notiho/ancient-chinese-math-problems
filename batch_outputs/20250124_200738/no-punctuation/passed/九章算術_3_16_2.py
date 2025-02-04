"""
今有生絲三十斤乾之耗三斤十二兩今有乾絲一十二斤問生絲幾何
術曰置生絲兩數除耗數餘以為法三十斤乘乾絲兩數為實實如法得生絲數
荅曰 a斤 
"""

#----- content starts here -----
"""
Suppose there are 30 jin of raw silk, and drying it causes a loss of 3 jin and 12 liang.
Now, there are 12 jin of dried silk.
Question: how much raw silk does it correspond to?

The procedure says: Place the total amount of raw silk in liang and subtract the amount lost in liang. The remainder becomes the divisor.
Multiply 30 jin by the total amount of dried silk in liang, which becomes the dividend.
Divide the dividend by the divisor to obtain the amount of raw silk.

The answer says: *a* jin.
"""

# 生絲三十斤
生絲 = 30

# 耗三斤十二兩
耗 = 3 + Fraction(12, 16)  # Convert 12 liang to jin (16 liang = 1 jin)

# 乾絲一十二斤
乾絲 = 12

# 置生絲兩數除耗數餘以為法
法 = 生絲 - 耗

# 三十斤乘乾絲兩數為實
實 = 生絲 * 乾絲

# 實如法得生絲數
a = Fraction(實, 法)#----- content ends here -----

"""
"""
