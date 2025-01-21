"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：本 a錢 。利 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the principal amount (`a`) and the total interest (`b`) based on the given conditions. Here's the Python code:


"""


from fractions import Fraction

# Given conditions
returns = [14000, 13000, 12000, 11000, 10000]  # The amounts returned in each of the five repayments
rate = Fraction(13, 100)  # The interest rate (13%)

# Assume the principal amount is `a` and the total interest is `b`
# The total amount returned is the sum of all repayments
total_returned = sum(returns)

# The total amount returned is equal to the principal plus the total interest
# b = a * rate
# total_returned = a + b
# total_returned = a + a * rate
# total_returned = a * (1 + rate)

a = Fraction(total_returned, 1 + rate)  # Calculate the principal amount
b = a * rate  # Calculate the total interest

# Output the results
a, b


"""


### Explanation:
1. The total amount returned (`total_returned`) is the sum of all repayments: `14000 + 13000 + 12000 + 11000 + 10000`.
2. The total amount returned is equal to the principal (`a`) plus the total interest (`b`).
3. The total interest (`b`) is calculated as `a * rate`, where the rate is 13%.
4. Substitute `b` into the equation: `total_returned = a + a * rate`.
5. Solve for `a`: `a = total_returned / (1 + rate)`.
6. Calculate `b` using `b = a * rate`.

### Solution:
The variables `a` and `b` will contain the principal amount and the total interest, respectively, represented as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 6000000/113
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 780000/113"""
