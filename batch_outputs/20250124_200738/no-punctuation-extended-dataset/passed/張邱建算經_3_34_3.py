"""
今有三人四日客作得麥五斛今有七人一月日客作問得麥幾何
術曰以七人乘一月三十日又以五斛乘之為實以三人乘四日為法實如法而得一
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there are 3 people working as hired laborers for 4 days, and they earn 5 hu of wheat.
Now, there are 7 people working as hired laborers for 1 month (30 days).
Question: how much wheat will they earn?

The procedure says: Multiply the 7 people by 1 month (30 days), then multiply this by 5 hu to obtain the dividend.
Multiply the 3 people by 4 days to obtain the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* hu.
"""

# 三人四日
人1 = 3
日1 = 4

# 得麥五斛
麥1 = 5

# 七人一月三十日
人2 = 7
日2 = 30

# 以七人乘一月三十日
實 = 人2 * 日2

# 又以五斛乘之，為實
實 = 實 * 麥1

# 以三人乘四日，為法
法 = 人1 * 日1

# 實如法而得一
a = Fraction(實, 法)#----- content ends here -----

"""
"""
