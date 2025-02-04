"""
今有貸人千錢，月息三十。今有貸人七百五十錢，九日歸之，問︰息幾何？
術曰：以月三十日，乘千錢為法。以息三十乘今所貸錢數，又以九日乘之，為實。實如法得一錢。
荅曰： a錢 。
"""

"""
To solve this problem, we need to calculate the interest (息) for borrowing 750 units of money for 9 days, given that the monthly interest rate is 30 units of money for 1000 units of money. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_money = 1000  # in 錢
monthly_interest = 30  # in 錢
borrowed_money = 750  # in 錢
borrowed_days = 9  # in days
days_in_month = 30  # in days

# Formula: interest = (monthly_interest * borrowed_money * borrowed_days) / (total_money * days_in_month)
a = Fraction(monthly_interest * borrowed_money * borrowed_days, total_money * days_in_month)

# The answer is stored in variable 'a'
#----- content ends here -----


"""


The solution is stored in the variable `a`, which represents the interest (息) in 錢.
"""


"""
"""
