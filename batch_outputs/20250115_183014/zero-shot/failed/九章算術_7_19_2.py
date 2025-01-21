"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：本 a錢 。利 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the principal amount (`a`) and the total interest (`b`) based on the given returns over five periods. Here's the Python code:


"""


from fractions import Fraction

# Given data
returns = [14000, 13000, 12000, 11000, 10000]  # Returns over five periods
rate = Fraction(13, 100)  # Interest rate (13%)

# Using the "盈不足術" (Excess and Deficiency Method)
# Assume two trial values for the principal amount
trial1 = 30000  # First trial value for the principal
trial2 = 40000  # Second trial value for the principal

# Calculate the total repayment for each trial value
repayment1 = sum(trial1 * (1 + rate)**i for i in range(1, 6)) - sum(returns)
repayment2 = sum(trial2 * (1 + rate)**i for i in range(1, 6)) - sum(returns)

# Calculate the principal amount (a) using the excess and deficiency method
a = trial1 + (trial2 - trial1) * (-repayment1) / (repayment2 - repayment1)

# Calculate the total interest (b)
b = a * rate * 5  # Total interest over five periods

# Output the results
a = Fraction(a).limit_denominator()  # Represent as a fraction
b = Fraction(b).limit_denominator()  # Represent as a fraction


"""


After running this code, the variables `a` and `b` will contain the principal amount and total interest, respectively, as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 7468665487/911514
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 3547555473/666095"""
