"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves finding the number of acres of good land (`a`) and bad land (`b`) purchased, given the total cost and the price per acre of each type of land.

Here is the Python code:


"""


from fractions import Fraction

# Prices per acre
price_good_land = 300  # in money units
price_bad_land = 500 / 7  # in money units

# Total land purchased
total_land = 100  # in acres (1 "頃" = 100 畝)

# Total cost
total_cost = 10000  # in money units

# Using the excess and deficit method described in the problem:
# Assume 20 acres of good land and 80 acres of bad land:
excess = 20 * price_good_land + 80 * price_bad_land - total_cost

# Assume 10 acres of good land and 90 acres of bad land:
deficit = 10 * price_good_land + 90 * price_bad_land - total_cost

# Solve for the number of good land (a) and bad land (b):
# Using the formula:
# a = (excess * total_land - deficit * total_land) / (excess - deficit)
a = Fraction(excess * total_land - deficit * total_land, excess - deficit)

# b = total_land - a
b = total_land - a

# Results
a = float(a)  # Convert to float for clarity
b = float(b)  # Convert to float for clarity


"""


The variables `a` and `b` will contain the number of acres of good land and bad land, respectively.
"""


"""
Code error: both arguments should be Rational instances"""
