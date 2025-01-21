"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves determining the number of acres of good fields ("善田") and bad fields ("惡田") purchased, given the total price and some constraints. Here's the Python code:


"""


from fractions import Fraction

# Define the variables and equations based on the problem statement
# Let a = acres of good fields (善田)
# Let b = acres of bad fields (惡田)

# Equation 1: Total price of good and bad fields
# 300a + 500b = 10000

# Equation 2: Excess or deficit conditions
# If a = 20 and b = 80, the price exceeds by 1714 2/7 (1714 + 2/7)
# If a = 10 and b = 90, the price is short by 571 3/7 (571 + 3/7)

# Convert the excess and deficit into fractions
excess = Fraction(1714) + Fraction(2, 7)
deficit = Fraction(571) + Fraction(3, 7)

# Calculate the rates for the excess and deficit conditions
rate_excess = 300 * 20 + 500 * 80 - excess
rate_deficit = 300 * 10 + 500 * 90 + deficit

# Use the "盈不足術" (Excess and Deficit Method) to solve for a and b
# The difference in rates and the difference in acres are used
difference_rate = rate_excess - rate_deficit
difference_acres = 20 - 10  # Difference in good field acres

# Solve for a (善田)
a = difference_rate / (300 * difference_acres)

# Solve for b (惡田) using the total acres equation
b = 100 - a

# Print the results
a = Fraction(a)
b = Fraction(b)

print(f"善田 a = {a} 畝")
print(f"惡田 b = {b} 畝")


"""


This Python code uses the "盈不足術" (Excess and Deficit Method) to solve for the number of acres of good fields (`a`) and bad fields (`b`). The solution is expressed in terms of fractions to maintain precision.
"""


"""
Variable 'a' has wrong value. Expected: 25/2, Actual: -10/7
Variable 'b' has wrong value. Expected: 175/2, Actual: 710/7"""
