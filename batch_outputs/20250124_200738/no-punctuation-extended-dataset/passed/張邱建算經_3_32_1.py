"""
今有亭一區五十人七日築訖今有三十人問幾何日築訖
術曰以本人數乘築訖日數為實以今有人數為法實如法得一
答曰 a日
"""

#----- content starts here -----
"""
Suppose there is one group of 50 people who completed construction in 7 days.
Now there is a group of 30 people. 
Question: how many days will it take to complete the construction?

The procedure says: Multiply the number of original people by the number of days they took to complete the construction, obtaining the dividend.
Take the number of current people as the divisor.
Divide the dividend by the divisor to obtain the number of days.

Answer: *a* days.
"""

# 本人數
本人數 = 50

# 築訖日數
築訖日數 = 7

# 今有人數
今有人數 = 30

# 以本人數乘築訖日數，為實
實 = 本人數 * 築訖日數

# 以今有人數為法
法 = 今有人數

# 實如法得一
a = Fraction(實, 法)#----- content ends here -----

"""
"""
