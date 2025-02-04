"""
今有生絲三十斤乾之耗三斤十二兩今有乾絲一十二斤問生絲幾何
術曰置生絲兩數除耗數餘以為法三十斤乘乾絲兩數為實實如法得生絲數
荅曰 a斤 
"""

"""
Suppose there are 30 jin of raw silk, and drying it results in a loss of 3 jin and 12 liang.
Now, there are 12 jin of dried silk.
Question: how much raw silk does it correspond to?

The procedure says: Place the number of liang in the raw silk and subtract the loss to obtain the divisor.
Multiply 30 jin by the number of liang in the dried silk to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of raw silk.

The answer says: *a* jin.
"""

# 生絲三十斤
生絲 = 30

# 耗三斤十二兩
耗斤 = 3
耗兩 = 12
耗數 = 耗斤 * 16 + 耗兩  # Convert to liang (1 jin = 16 liang)

# 乾絲一十二斤
乾絲 = 12
乾絲兩數 = 乾絲 * 16  # Convert to liang

# 置生絲兩數除耗數餘，以為法
生絲兩數 = 生絲 * 16  # Convert to liang
法 = 生絲兩數 - 耗數

# 三十斤乘乾絲兩數，為實
實 = 生絲兩數 * 乾絲兩數

# 實如法得生絲數
生絲數 = Fraction(實, 法)

# Convert back to jin
a = 生絲數 / 16
"""
"""
