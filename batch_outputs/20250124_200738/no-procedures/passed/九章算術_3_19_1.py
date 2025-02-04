"""
今有貸人千錢，月息三十。今有貸人七百五十錢，九日歸之，問︰息幾何？
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose someone lends 1000 qian with a monthly interest of 30 qian.
Now, someone borrows 750 qian and returns it after 9 days.
Question: how much interest is owed?

Answer: *a* qian.
"""

from fractions import Fraction

#貸人千錢，月息三十
本金 = 1000
月息 = 30

#貸人七百五十錢，九日歸之
借款 = 750
天數 = 9

# Calculate daily interest rate
日息 = Fraction(月息, 30)  # 30 days in a month

# Calculate interest owed
a = Fraction(借款, 本金) * 日息 * 天數

a  # The interest owed in qian#----- content ends here -----

"""
"""
