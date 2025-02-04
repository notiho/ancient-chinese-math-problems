"""
今有貸人千錢月息三十今有貸人七百五十錢九日歸之問息幾何
術曰以月三十日乘千錢為法以息三十乘今所貸錢數又以九日乘之為實實如法得一錢
荅曰 a錢 
"""

"""
Suppose someone lends out 1000 qian with a monthly interest of 30 qian.
Now, someone borrows 750 qian and returns it after 9 days.
Question: how much is the interest?

The procedure says: Multiply the 30 days in a month by 1000 qian to obtain the divisor.
Multiply the interest rate of 30 by the amount of money borrowed, then multiply it by the 9 days to obtain the dividend.
Divide the dividend by the divisor to obtain the interest.

Answer: *a* qian.
"""

# 貸人千錢
貸款 = 1000

# 月息三十
月息 = 30

# 月三十日
月日 = 30

# 今貸人七百五十錢
今貸款 = 750

# 九日
日數 = 9

# 以月三十日乘千錢為法
法 = 月日 * 貸款

# 以息三十乘今所貸錢數
實 = 月息 * 今貸款

# 又以九日乘之
實 = 實 * 日數

# 實如法得一錢
a = Fraction(實, 法)
"""
"""
