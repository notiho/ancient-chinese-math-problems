"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the principal amount (`a`) and the total interest (`b`) based on the given returns over five periods.


"""


from fractions import Fraction

# Given data
returns = [14000, 13000, 12000, 11000, 10000]  # Returns over five periods
rate = Fraction(13, 100)  # Interest rate (13%)

# Let the principal amount be `a` and the total interest be `b`
# The total amount returned is the sum of the returns
total_returned = sum(returns)

# The total amount returned is equal to the principal plus the total interest
# Total interest is calculated as the principal multiplied by the interest rate over five periods
# total_returned = a + b
# b = a * rate * 5

# Substituting b into the equation:
# total_returned = a + a * rate * 5
# total_returned = a * (1 + rate * 5)

# Solve for `a`:
a = Fraction(total_returned) / (1 + rate * 5)

# Calculate `b`:
b = a * rate * 5

# Results
a = float(a)  # Convert to float for readability
b = float(b)  # Convert to float for readability

a, b


"""


This code calculates the principal amount (`a`) and the total interest (`b`) based on the given returns and the interest rate. The results are stored in the variables `a` and `b`.
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 36363.63636363636
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 23636.363636363636"""
