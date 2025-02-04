"""
今有絲一斤耗七兩今有絲二十三斤五兩問耗幾何
術曰以一斤展十六兩為法以七兩乘今有絲兩數為實實如法得耗數
荅曰 a兩 
"""

"""
Suppose there is 1 jin of silk, and 7 liang are wasted. 
Now there are 23 jin and 5 liang of silk.
Question: how much is wasted?

The procedure says: Take 1 jin expanded into 16 liang as the divisor.
Multiply 7 liang by the total number of liang in the given silk, obtaining the dividend.
Divide the dividend by the divisor to get the amount of waste.

Answer: *a* liang.
"""

# 一斤展十六兩為法
法 = 16

# 耗七兩
耗 = 7

# 今有絲二十三斤五兩
絲斤 = 23
絲兩 = 5

# 將絲轉換為總兩數
絲總兩 = (絲斤 * 16) + 絲兩

# 以七兩乘今有絲兩數，為實
實 = 耗 * 絲總兩

# 實如法得耗數
a = Fraction(實, 法)
"""
"""
