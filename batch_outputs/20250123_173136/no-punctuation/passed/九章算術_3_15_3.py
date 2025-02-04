"""
今有絲一斤耗七兩今有絲二十三斤五兩問耗幾何
術曰以一斤展十六兩為法以七兩乘今有絲兩數為實實如法得耗數
荅曰 a兩 
"""

"""
Suppose there is 1 jin of silk, and 7 liang of it is wasted.
Now, there are 23 jin and 5 liang of silk.
Question: how much is wasted?

The procedure says: Take 1 jin as 16 liang as the divisor.
Multiply 7 liang by the current amount of silk (in liang) to get the dividend.
Divide the dividend by the divisor to obtain the amount of waste.

Answer: *a* liang.
"""

# 絲一斤耗七兩
耗率 = 7

# 一斤展十六兩為法
法 = 16

# 今有絲二十三斤五兩
今有絲 = 23 * 16 + 5  # Convert jin and liang to total liang

# 以七兩乘今有絲兩數為實
實 = 耗率 * 今有絲

# 實如法得耗數
a = Fraction(實, 法)
"""
"""
