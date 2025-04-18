"""
今有貸人千錢，月息三十。今有貸人七百五十錢，九日歸之，問︰息幾何？
術曰：以月三十日，乘千錢為法。以息三十乘今所貸錢數，又以九日乘之，為實。實如法得一錢。
荅曰： a(=27/4)錢 。
"""

"""
Suppose a person lends out 1000 qian, with a monthly interest of 30 qian.
Now, suppose a person lends out 750 qian, and it is returned after 9 days.
Question: how much is the interest?

The procedure says: Take 30 days in a month and multiply it by 1000 qian to obtain the divisor.
Take the monthly interest of 30 and multiply it by the amount of money currently lent out, and then multiply it by the number of days, to obtain the dividend.
Divide the dividend by the divisor to obtain the interest.

Answer: *a*(=27/4) qian.
"""

# 貸人千錢
貸款額 = 1000

# 月息三十
月息 = 30

# 月三十日
月日數 = 30

# 今貸人七百五十錢
今貸款額 = 750

# 九日歸之
歸還日數 = 9

# 乘千錢為法
法 = 月日數 * 貸款額

# 以息三十乘今所貸錢數
實 = 月息 * 今貸款額

# 又以九日乘之
實 *= 歸還日數

# 實如法得一錢
a = Fraction(實, 法) # 27/4 qian

"""
"""
