"""
今有生絲三十斤，乾之，耗三斤十二兩。今有乾絲一十二斤，問︰生絲幾何？
術曰：置生絲兩數，除耗數，餘，以為法。三十斤乘乾絲兩數為實。實如法得生絲數。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there are 30 jin of raw silk. After drying, it loses 3 jin and 12 liang.
Now, suppose there are 12 jin of dried silk. 
Question: how much raw silk does it correspond to?

The procedure says: Place the raw silk weight and subtract the weight lost during drying. The remainder is taken as the divisor.
Multiply the 30 jin of raw silk by the weight of the dried silk to obtain the dividend.
Divide the dividend by the divisor to obtain the weight of the raw silk.

Answer: *a* jin.
"""

from fractions import Fraction

# 生絲三十斤
生絲 = 30

# 耗三斤十二兩 (1 jin = 16 liang, so 3 jin 12 liang = 3 * 16 + 12 liang)
耗 = 3 * 16 + 12  # in liang

# 轉換生絲為兩 (1 jin = 16 liang)
生絲兩數 = 生絲 * 16  # in liang

# 餘數為法 (生絲兩數 - 耗數)
法 = 生絲兩數 - 耗

# 乾絲一十二斤 (convert to liang)
乾絲 = 12 * 16  # in liang

# 三十斤乘乾絲兩數為實
實 = 乾絲 * 生絲兩數

# 實如法得生絲數
生絲數 = Fraction(實, 法)  # in liang

# 轉換回斤 (1 jin = 16 liang)
a = 生絲數 / 16  # in jin

a#----- content ends here -----

"""
"""
