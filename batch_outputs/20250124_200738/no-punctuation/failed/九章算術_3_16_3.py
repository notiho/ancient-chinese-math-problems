"""
今有生絲三十斤乾之耗三斤十二兩今有乾絲一十二斤問生絲幾何
術曰置生絲兩數除耗數餘以為法三十斤乘乾絲兩數為實實如法得生絲數
荅曰 a斤 
"""

#----- content starts here -----
"""
Suppose there are 30 jin of raw silk, and drying it results in a loss of 3 jin and 12 liang.
Now, suppose there are 12 jin of dried silk.
Question: how much raw silk does it correspond to?

The procedure says: Place the raw silk's total weight in liang and subtract the loss in liang. The remainder becomes the divisor.
Multiply 30 jin by the dried silk's total weight in liang to obtain the dividend.
Divide the dividend by the divisor to obtain the raw silk's weight.

Answer: *a* jin.
"""

# 生絲三十斤
生絲 = 30

# 耗三斤十二兩
耗斤 = 3
耗兩 = 12
耗總兩 = 耗斤 * 16 + 耗兩  # 1 斤 = 16 兩

# 乾絲一十二斤
乾絲 = 12

# 置生絲兩數
生絲總兩 = 生絲 * 16  # 1 斤 = 16 兩

# 除耗數餘以為法
法 = 生絲總兩 - 耗總兩

# 三十斤乘乾絲兩數為實
實 = 生絲 * (乾絲 * 16)

# 實如法得生絲數
生絲數總兩 = Fraction(實, 法)

# 換算回斤
a = 生絲數總兩 / 16  # 1 斤 = 16 兩#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 96/7, Actual: 6/7"""
