"""
今有取保一歲，價錢二千五百。今先取一千二百，問︰當作日幾何？
術曰：以價錢為法，以一歲三百五十四日乘先取錢數為實，實如法得日數。
荅曰： a日 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
price = 2500  # Total price in monetary units
days_in_year = 354  # Days in one year
partial_payment = 1200  # Partial payment in monetary units

# Calculation
a = Fraction(partial_payment * days_in_year, price)

# Result
a  # This represents the number of days
#----- content ends here -----


"""


The variable `a` will store the number of days corresponding to the partial payment.
"""


"""
"""
