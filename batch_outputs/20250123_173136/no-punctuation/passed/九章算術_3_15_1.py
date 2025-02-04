"""
今有絲一斤耗七兩今有絲二十三斤五兩問耗幾何
術曰以一斤展十六兩為法以七兩乘今有絲兩數為實實如法得耗數
荅曰 a兩 
"""

"""
Suppose there is 1 jin of silk, which loses 7 liang during processing. 
Now there is 23 jin and 5 liang of silk. 
Question: how much is the loss?

The procedure says: Take 1 jin as 16 liang as the divisor.
Multiply 7 liang by the total number of liang in the given silk to obtain the dividend.
Divide the dividend by the divisor to get the amount of loss.

Answer: *a* liang.
"""

# 一斤展十六兩為法
法 = 16

# 耗七兩
耗 = 7

# 今有絲二十三斤五兩
今有絲斤 = 23
今有絲兩 = 5

# 將絲的總量轉換為兩
今有絲總兩 = (今有絲斤 * 法) + 今有絲兩

# 以七兩乘今有絲兩數為實
實 = 耗 * 今有絲總兩

# 實如法得耗數
a = Fraction(實, 法)
"""
"""
