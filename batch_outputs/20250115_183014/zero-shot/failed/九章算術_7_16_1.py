"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem uses the "盈不足術" (Excess and Deficiency Method) to determine the number of "善田" (good fields) and "惡田" (bad fields) purchased.

Here is the Python code:


"""


from fractions import Fraction

# Given data
price_good_field = 300  # price of 1 畝 of good field
price_bad_field = 500 / 7  # price of 1 畝 of bad field
total_price = 10000  # total price for 1 頃 of land

# Hypotheses
good_field_1 = 20  # first hypothesis for good fields
bad_field_1 = 80  # first hypothesis for bad fields
excess_1 = Fraction(1714, 1) + Fraction(2, 7)  # excess money for first hypothesis

good_field_2 = 10  # second hypothesis for good fields
bad_field_2 = 90  # second hypothesis for bad fields
deficit_2 = Fraction(571, 1) + Fraction(3, 7)  # deficit money for second hypothesis

# Calculate the difference in hypotheses
delta_good_field = good_field_1 - good_field_2
delta_bad_field = bad_field_1 - bad_field_2
delta_excess_deficit = excess_1 + deficit_2

# Solve for the number of good fields (a) and bad fields (b)
a = delta_excess_deficit / (delta_good_field * price_good_field + delta_bad_field * price_bad_field)
b = Fraction(1, 1) - a

# Convert the solution to the actual number of fields
a = good_field_2 + a * delta_good_field
b = bad_field_2 + a * delta_bad_field

# Output the results
a, b


"""


This code calculates the number of "善田" (good fields) and "惡田" (bad fields) purchased, represented by variables `a` and `b`. The solution uses the "盈不足術" method to determine the values based on the given hypotheses and their respective excess/deficit amounts.
"""


"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 20.0
Variable 'b' has wrong value. Expected: 175/2, Actual: -110.0"""
