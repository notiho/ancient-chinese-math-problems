"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：本 a錢 。利 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the principal amount (`a`) and the total interest (`b`) based on the given returns over five periods. We will use the "盈不足術" (excess and deficiency method) to solve the problem.

Here is the Python code:


"""


from fractions import Fraction

# Given data
returns = [14000, 13000, 12000, 11000, 10000]  # Returns over five periods
rate = Fraction(13, 100)  # Interest rate (13%)

# Hypothetical cases
principal1 = 30000  # Hypothetical principal 1
principal2 = 40000  # Hypothetical principal 2

# Calculate the total repayment for each hypothetical principal
total_repayment1 = sum(principal1 * (1 + rate)**i for i in range(1, 6))
total_repayment2 = sum(principal2 * (1 + rate)**i for i in range(1, 6))

# Calculate the excess and deficiency
excess = total_repayment2 - sum(returns)
deficiency = sum(returns) - total_repayment1

# Use the excess and deficiency method to find the actual principal
a = (principal1 * excess + principal2 * deficiency) / (excess + deficiency)

# Calculate the total interest
b = a * rate * 5  # Total interest over five periods

# Output the results
a = Fraction(a).limit_denominator()  # Principal
b = Fraction(b).limit_denominator()  # Total interest

# Results
a, b


"""


### Explanation:
1. **Inputs**:
   - `returns`: The amounts returned over five periods.
   - `rate`: The interest rate (13% or 13/100).

2. **Hypothetical Principals**:
   - Two hypothetical principals (`principal1` and `principal2`) are chosen to calculate the excess and deficiency.

3. **Excess and Deficiency**:
   - The total repayment for each hypothetical principal is calculated using the formula for compound interest.
   - The excess and deficiency are calculated by comparing the total repayments to the sum of the given returns.

4. **Actual Principal (`a`)**:
   - The actual principal is calculated using the excess and deficiency method.

5. **Total Interest (`b`)**:
   - The total interest is calculated based on the principal, rate, and number of periods.

6. **Output**:
   - The principal (`a`) and total interest (`b`) are represented as fractions for precision.

This code solves the problem and computes the values of `a` (principal) and `b` (total interest).
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 7468665487/911514
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 3547555473/666095"""
