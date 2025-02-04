"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem uses the "盈不足術" (Excess and Deficiency Method) to determine the number of "善田" (good fields) and "惡田" (bad fields) purchased.

Here is the Python code:


"""


from fractions import Fraction

# Given data
price_good_field = 300  # Price of one 畝 of good field
price_bad_field = 500 / 7  # Price of one 畝 of bad field
total_price = 10000  # Total price for one 頃 (100 畝)

# First assumption: 20 畝 of good field, 80 畝 of bad field
good_field_1 = 20
bad_field_1 = 80
excess_1 = Fraction(1714, 7) + Fraction(2, 7)  # Excess amount in money

# Second assumption: 10 畝 of good field, 90 畝 of bad field
good_field_2 = 10
bad_field_2 = 90
deficit_2 = Fraction(571, 7) + Fraction(3, 7)  # Deficit amount in money

# Calculate the rates (盈、不足)
rate_1 = good_field_1 * price_good_field + bad_field_1 * price_bad_field - total_price
rate_2 = good_field_2 * price_good_field + bad_field_2 * price_bad_field - total_price

# Excess and Deficiency Method
# Difference in rates
difference_rate = rate_1 - rate_2

# Difference in excess and deficit
difference_excess_deficit = excess_1 + deficit_2

# Solve for the number of good fields (a)
a = difference_excess_deficit / difference_rate

# Solve for the number of bad fields (b)
b = 100 - a  # Since the total is 100 畝

# Print the results
a = Fraction(a).limit_denominator()  # Convert to fraction
b = Fraction(b).limit_denominator()  # Convert to fraction
print(f"善田 a = {a} 畝")
print(f"惡田 b = {b} 畝")


"""


This code calculates the number of good fields (`a`) and bad fields (`b`) using the ancient Chinese method of "盈不足術" (Excess and Deficiency Method). The solution is expressed in terms of fractions to maintain precision.
"""


"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 229/1600
Variable 'b' has wrong value. Expected: 175/2, Actual: 159771/1600"""
