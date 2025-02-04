"""
今有貸人千錢，月息三十。今有貸人七百五十錢，九日歸之，問︰息幾何？
術曰：以月三十日，乘千錢為法。以息三十乘今所貸錢數，又以九日乘之，為實。實如法得一錢。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose a person lends 1000 qian with a monthly interest of 30 qian.
Now, another person borrows 750 qian and returns it after 9 days.
Question: how much interest is owed?

The procedure says: Take 30 days in a month and multiply it by 1000 qian to obtain the divisor.
Take the monthly interest (30 qian) and multiply it by the amount borrowed (750 qian), then multiply it by the number of days (9 days) to obtain the dividend.
Divide the dividend by the divisor to obtain the interest.

Answer: *a* qian.
"""

from fractions import Fraction

# Given values
貸款總額 = 1000  # 千錢
月息 = 30  # 千錢
貸款天數 = 30  # 一月三十日
今貸款 = 750  # 千錢
歸還天數 = 9  # 九日

# 法：以月三十日乘千錢
法 = 貸款天數 * 貸款總額

# 實：以息三十乘今所貸錢數，又以九日乘之
實 = 月息 * 今貸款 * 歸還天數

# 息：實如法得一錢
a = Fraction(實, 法)

a  # Interest owed in qian#----- content ends here -----

"""
"""
