"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：本 a錢 。利 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the principal amount (`a`) and the total interest (`b`) based on the given returns over five periods.

Here is the Python code:


"""


from fractions import Fraction

# Given data
returns = [14000, 13000, 12000, 11000, 10000]  # Returns over five periods
rate = Fraction(13, 100)  # Interest rate (13%)

# Step 1: Assume a principal amount (e.g., 30000 and 40000) to calculate discrepancies
principal1 = 30000
principal2 = 40000

# Calculate discrepancies for the assumed principals
discrepancy1 = sum(principal1 * (1 + rate) ** i for i in range(1, 6)) - sum(returns)
discrepancy2 = sum(principal2 * (1 + rate) ** i for i in range(1, 6)) - sum(returns)

# Step 2: Use the "盈不足術" (excess and deficiency method) to find the actual principal
a = (discrepancy2 * principal1 - discrepancy1 * principal2) / (discrepancy2 - discrepancy1)

# Step 3: Calculate the total interest
b = sum(returns) - a

# Output the results
a = Fraction(a).limit_denominator()  # Convert to Fraction for exact representation
b = Fraction(b).limit_denominator()  # Convert to Fraction for exact representation

# Results
print(f"Principal (a): {a} 錢")
print(f"Total Interest (b): {b} 錢")


"""


This code calculates the principal (`a`) and total interest (`b`) using the excess and deficiency method described in the problem. The results are represented as fractions for accuracy.
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 7468665487/911514
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 47222174513/911514"""
