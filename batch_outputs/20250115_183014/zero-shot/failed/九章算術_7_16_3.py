"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves finding the number of "善田" (good fields, denoted as `a`) and "惡田" (bad fields, denoted as `b`) such that their combined price equals 10,000. The price per unit area of good fields and bad fields is given, and two scenarios are provided to solve the problem using the method of excess and deficiency (盈不足術).

Here is the Python code:


"""


from fractions import Fraction

# Given data
price_good = 300  # Price per 畝 for good fields
price_bad = 500 / 7  # Price per 畝 for bad fields
total_price = 10000  # Total price for 1 頃 (100 畝)

# Scenario 1: Assume 20 畝 good fields and 80 畝 bad fields
a1 = 20  # Good fields in scenario 1
b1 = 80  # Bad fields in scenario 1
excess = Fraction(1714, 7) + Fraction(2, 7)  # Excess amount in scenario 1

# Scenario 2: Assume 10 畝 good fields and 90 畝 bad fields
a2 = 10  # Good fields in scenario 2
b2 = 90  # Bad fields in scenario 2
deficit = Fraction(571, 7) + Fraction(3, 7)  # Deficit amount in scenario 2

# Method of excess and deficiency (盈不足術)
# Compute the rates (所出率)
rate1 = a1 * price_good + b1 * price_bad - total_price  # Excess rate
rate2 = a2 * price_good + b2 * price_bad - total_price  # Deficit rate

# Combine the rates and solve for the unknowns
combined_rate = rate1 - rate2
combined_excess_deficit = excess + deficit

# Solve for the number of good fields (a)
a = combined_excess_deficit / combined_rate

# Solve for the number of bad fields (b)
b = 100 - a  # Total area is 100 畝

# Output the results
a = Fraction(a)  # Convert to Fraction for exact representation
b = Fraction(b)  # Convert to Fraction for exact representation

# Results
a, b


"""


This code calculates the values of `a` (good fields) and `b` (bad fields) using the method of excess and deficiency. The results are stored in the variables `a` and `b`.
"""


"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 5156621573339217/36028797018963968
Variable 'b' has wrong value. Expected: 175/2, Actual: 1756700722813993/17592186044416"""
