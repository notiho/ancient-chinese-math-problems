"""
今有貸人千錢，月息三十。今有貸人七百五十錢，九日歸之，問︰息幾何？
術曰：以月三十日，乘千錢為法。以息三十乘今所貸錢數，又以九日乘之，為實。實如法得一錢。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose a person lends 1000 qian with a monthly interest of 30 qian.
Now, a person borrows 750 qian and returns it after 9 days.
Question: how much is the interest?

The procedure says: Take 30 days in a month and multiply it by 1000 qian to obtain the divisor.
Take the monthly interest of 30 and multiply it by the amount of money currently borrowed, then multiply it by the number of days borrowed to obtain the dividend.
Divide the dividend by the divisor to obtain the interest.

Answer: *a* qian.
"""

# 貸人千錢
貸款總額 = 1000

# 月息三十
月息 = 30

# 月三十日
月天數 = 30

# 今所貸錢數
今貸款 = 750

# 九日
借款天數 = 9

# 以月三十日，乘千錢為法
法 = 月天數 * 貸款總額

# 以息三十乘今所貸錢數，又以九日乘之，為實
實 = 月息 * 今貸款 * 借款天數

# 實如法得一錢
a = Fraction(實, 法)#----- content ends here -----

"""
"""
