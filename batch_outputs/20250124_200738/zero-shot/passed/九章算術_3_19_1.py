"""
今有貸人千錢，月息三十。今有貸人七百五十錢，九日歸之，問︰息幾何？
術曰：以月三十日，乘千錢為法。以息三十乘今所貸錢數，又以九日乘之，為實。實如法得一錢。
荅曰： a錢 。
"""

"""
To solve this problem, we need to compute the interest (息) for a loan of 750 coins over 9 days, given that the monthly interest rate is 30 coins for a loan of 1000 coins. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
loan_amount = 750  # in coins
days = 9  # in days
monthly_interest_rate = 30  # in coins
standard_loan = 1000  # in coins
standard_days = 30  # in days

# Calculate the interest
a = Fraction(monthly_interest_rate * loan_amount * days, standard_loan * standard_days)

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the interest in coins.
"""


"""
"""
