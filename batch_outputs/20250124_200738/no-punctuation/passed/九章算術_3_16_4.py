"""
今有生絲三十斤乾之耗三斤十二兩今有乾絲一十二斤問生絲幾何
術曰置生絲兩數除耗數餘以為法三十斤乘乾絲兩數為實實如法得生絲數
荅曰 a斤 
"""

#----- content starts here -----
"""
Suppose there are 30 jin of raw silk, which loses 3 jin and 12 liang when dried.
Now, suppose there are 12 jin of dried silk.
Question: how much raw silk does it correspond to?

The procedure says: Place the total amount of raw silk in liang and subtract the amount lost in liang. The remainder becomes the divisor.
Multiply 30 jin by the total amount of dried silk in liang, which becomes the dividend.
Divide the dividend by the divisor to obtain the amount of raw silk.

The answer says: *a* jin.
"""

# 生絲三十斤
生絲 = 30

# 乾之耗三斤十二兩
耗斤 = 3
耗兩 = 12
# 1 斤 = 16 兩
耗數 = 耗斤 * 16 + 耗兩

# 生絲兩數
生絲兩數 = 生絲 * 16

# 除耗數餘以為法
法 = 生絲兩數 - 耗數

# 乾絲一十二斤
乾絲 = 12
乾絲兩數 = 乾絲 * 16

# 三十斤乘乾絲兩數為實
實 = 生絲兩數 * 乾絲兩數

# 實如法得生絲數
生絲數兩 = Fraction(實, 法)

# 轉換回斤
a = 生絲數兩 / 16#----- content ends here -----

"""
"""
