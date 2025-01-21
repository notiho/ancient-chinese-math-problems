"""
今有貸人千錢月息三十今有貸人七百五十錢九日歸之問息幾何
術曰以月三十日乘千錢為法以息三十乘今所貸錢數又以九日乘之為實實如法得一錢
荅曰 a錢 
"""

"""
Suppose a person lends out 1000 qian with a monthly interest of 30 qian.
Now, another person borrows 750 qian and returns it after 9 days.
Question: how much interest is owed?

The procedure says: Multiply the 30 days in a month by 1000 qian, obtaining the divisor.
Multiply the interest rate (30 qian) by the amount of money borrowed, and then multiply it by the 9 days, obtaining the dividend.
Divide the dividend by the divisor, obtaining the interest in qian.

Answer: *a* qian.
"""

# 貸人千錢
貸款總額 = 1000

# 月息三十
月息 = 30

# 貸人七百五十錢
貸款金額 = 750

# 九日
天數 = 9

# 以月三十日乘千錢為法
法 = 30 * 貸款總額

# 以息三十乘今所貸錢數
實 = 月息 * 貸款金額

# 又以九日乘之
實 *= 天數

# 實如法得一錢
a = Fraction(實, 法)
"""
"""
