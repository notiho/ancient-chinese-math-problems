"""
今有三人四日客作得麥五斛今有七人一月日客作問得麥幾何
術曰以七人乘一月三十日又以五斛乘之為實以三人乘四日為法實如法而得一
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there are 3 people working as hired laborers for 4 days, and they earn 5 hu of wheat.
Now, there are 7 people working as hired laborers for 1 month (30 days).
Question: how much wheat do they earn?

The procedure says: Multiply the 7 people by 1 month (30 days), and also multiply the 5 hu by this, obtaining the dividend.
Multiply the 3 people by 4 days, obtaining the divisor.
Divide the dividend by the divisor, obtaining the result.

Answer: *a* hu.
"""

# 三人四日
人數_1 = 3
日數_1 = 4

# 得麥五斛
麥_1 = 5

# 七人一月三十日
人數_2 = 7
日數_2 = 30

# 以七人乘一月三十日
實_2 = 人數_2 * 日數_2

# 又以五斛乘之，為實
實 = 麥_1 * 實_2

# 以三人乘四日，為法
法 = 人數_1 * 日數_1

# 實如法而得一
a = Fraction(實, 法)#----- content ends here -----

"""
"""
