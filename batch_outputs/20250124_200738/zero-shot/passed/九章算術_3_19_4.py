"""
今有貸人千錢，月息三十。今有貸人七百五十錢，九日歸之，問︰息幾何？
術曰：以月三十日，乘千錢為法。以息三十乘今所貸錢數，又以九日乘之，為實。實如法得一錢。
荅曰： a錢 。
"""

"""
To solve this problem, we need to calculate the interest (息) for a loan of 750 coins (錢) over 9 days, given that the monthly interest rate is 30 coins for a loan of 1000 coins. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
loan_total = 1000  # in coins
monthly_interest = 30  # in coins
loan_amount = 750  # in coins
days = 9  # in days
days_in_month = 30  # days in a month

# Calculation
# Formula: (monthly_interest * loan_amount * days) / (loan_total * days_in_month)
a = Fraction(monthly_interest * loan_amount * days, loan_total * days_in_month)

# Result
a  # Interest in coins
#----- content ends here -----


"""


The variable `a` will contain the interest in coins as a `Fraction`.
"""


"""
"""
