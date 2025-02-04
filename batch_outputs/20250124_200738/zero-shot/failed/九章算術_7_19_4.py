"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the principal amount (`a`) and the total interest (`b`) based on the given returns and the rate of interest.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
returns = [14000, 13000, 12000, 11000, 10000]  # Returns in each period
rate = Fraction(13, 100)  # Interest rate (13%)

# Step 1: Set up the equations
# Let the principal amount be `a` and the total interest be `b`.
# The total amount returned is the sum of the returns.
total_returned = sum(returns)

# The total amount returned is equal to the principal plus the total interest.
# total_returned = a + b

# The total interest `b` is calculated based on the principal `a` and the rate of interest.
# b = a * rate * 5 (since there are 5 periods)

# Step 2: Solve for `a` and `b`
# Substitute b = a * rate * 5 into the total_returned equation:
# total_returned = a + a * rate * 5
# total_returned = a * (1 + rate * 5)

a = Fraction(total_returned, 1 + rate * 5)
b = a * rate * 5

# The results
a = float(a)  # Principal amount in money
b = float(b)  # Total interest in money

# Output the results
print("Principal (a):", a, "錢")
print("Total Interest (b):", b, "錢")
#----- content ends here -----


"""


### Explanation:
1. The total amount returned is the sum of the five returns: `14000 + 13000 + 12000 + 11000 + 10000`.
2. The total amount returned is equal to the principal (`a`) plus the total interest (`b`).
3. The total interest is calculated as `b = a * rate * 5`, where the rate is 13% (or `13/100` as a fraction) and there are 5 periods.
4. Substitute `b` into the total returned equation to solve for `a`.
5. Once `a` is found, calculate `b` using the formula `b = a * rate * 5`.

This code computes the values of `a` (principal) and `b` (total interest).
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 36363.63636363636
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 23636.363636363636"""
