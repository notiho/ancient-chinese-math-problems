"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves finding the number of acres of good land (`a`) and bad land (`b`) purchased, given the total cost and the prices of each type of land.

Here is the Python code:


"""


from fractions import Fraction

# Given data
price_good_land = 300  # price per acre of good land
price_bad_land = 500 / 7  # price per acre of bad land
total_price = 10000  # total price for one qing (100 acres)

# Using the method described in the problem:
# Assume two cases:
# Case 1: 20 acres of good land and 80 acres of bad land
# Case 2: 10 acres of good land and 90 acres of bad land

# Case 1: Excess amount
excess = Fraction(1714, 7) + Fraction(2, 7)  # 1714 2/7

# Case 2: Deficit amount
deficit = Fraction(571, 7) + Fraction(3, 7)  # 571 3/7

# Calculate the difference in the number of acres of good land and bad land
difference_good_land = 20 - 10  # Difference in good land
difference_bad_land = 80 - 90  # Difference in bad land

# Calculate the total price difference for the two cases
price_difference = (difference_good_land * price_good_land +
                    difference_bad_land * price_bad_land)

# Calculate the total amount of excess and deficit
total_difference = excess + deficit

# Solve for the number of acres of good land (a)
a = total_difference / price_difference

# Solve for the number of acres of bad land (b)
b = 100 - a  # Total land is 100 acres (1 qing)

# Print the results
a = float(a)
b = float(b)
print("善田 (good land):", a, "畝")
print("惡田 (bad land):", b, "畝")


"""

"""


"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 0.143125
Variable 'b' has wrong value. Expected: 175/2, Actual: 99.856875"""
