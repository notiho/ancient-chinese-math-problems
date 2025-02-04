"""
今有貸人千錢月息三十今有貸人七百五十錢九日歸之問息幾何
術曰以月三十日乘千錢為法以息三十乘今所貸錢數又以九日乘之為實實如法得一錢
荅曰 a錢 
"""

#----- content starts here -----
"""
Suppose someone lends out 1000 qian with a monthly interest of 30 qian. 
Now, someone borrows 750 qian and returns it after 9 days.
Question: how much interest is owed?

The procedure says: Multiply the 30 days in a month by 1000 qian to get the divisor.
Multiply the interest rate (30) by the amount of money borrowed, and then multiply it by the 9 days to get the dividend.
Divide the dividend by the divisor to get the interest.

Answer: *a* qian.
"""

# 貸人千錢
貸款總額 = 1000

# 月息三十
月息 = 30

# 月三十日
月日數 = 30

# 今所貸七百五十錢
貸款金額 = 750

# 九日
借款天數 = 9

# 以月三十日乘千錢為法
法 = 月日數 * 貸款總額

# 以息三十乘今所貸錢數
實 = 月息 * 貸款金額

# 又以九日乘之
實 = 實 * 借款天數

# 實如法得一錢
a = Fraction(實, 法)#----- content ends here -----

"""
"""
