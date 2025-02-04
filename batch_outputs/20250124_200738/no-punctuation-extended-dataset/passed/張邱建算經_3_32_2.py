"""
今有亭一區五十人七日築訖今有三十人問幾何日築訖
術曰以本人數乘築訖日數為實以今有人數為法實如法得一
答曰 a日
"""

#----- content starts here -----
"""
Suppose there is a pavilion, and 50 people complete its construction in 7 days.
Now, with 30 people, how many days will it take to complete the construction?

The procedure says: Multiply the original number of people by the number of days it took to complete the construction, obtaining the dividend.
Use the current number of people as the divisor.
Divide the dividend by the divisor to obtain the number of days.

Answer: *a* days.
"""

# 本人數
本人數 = 50

# 築訖日數
築訖日數 = 7

# 今有人數
今有人數 = 30

# 以本人數乘築訖日數為實
實 = 本人數 * 築訖日數

# 以今有人數為法
法 = 今有人數

# 實如法得一
a = Fraction(實, 法)#----- content ends here -----

"""
"""
