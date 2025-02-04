"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves finding the number of acres of good land (`a`) and bad land (`b`) purchased, given the total cost and the prices of each type of land.

Here is the Python code:


"""


from fractions import Fraction

# Given data
price_good_land = 300  # price per acre of good land
price_bad_land = 500 / 7  # price per acre of bad land
total_cost = 10000  # total cost for one qing (100 acres)

# Using the method described in the problem:
# Assume two scenarios:
# 1. Good land = 20 acres, Bad land = 80 acres
# 2. Good land = 10 acres, Bad land = 90 acres

# Calculate the excess and deficit in cost for each scenario
excess = 20 * price_good_land + 80 * price_bad_land - total_cost
deficit = 10 * price_good_land + 90 * price_bad_land - total_cost

# Apply the "盈不足術" (Excess and Deficit Method)
# Let the difference in good land between the two scenarios be the divisor
divisor = 20 - 10  # Difference in good land

# Calculate the total land (100 acres) using the method
a = Fraction(-deficit * divisor, excess - deficit)  # Good land
b = 100 - a  # Bad land

# Output the results
a = a  # Good land in acres
b = b  # Bad land in acres


"""


### Explanation of the Code:
1. **Input Data**:
   - The price of good land is 300 per acre.
   - The price of bad land is \( \frac{500}{7} \) per acre.
   - The total cost for 100 acres (1 qing) is 10,000.

2. **Two Scenarios**:
   - Scenario 1: Assume 20 acres of good land and 80 acres of bad land.
   - Scenario 2: Assume 10 acres of good land and 90 acres of bad land.

3. **Excess and Deficit**:
   - Calculate the excess cost for Scenario 1.
   - Calculate the deficit cost for Scenario 2.

4. **盈不足術 (Excess and Deficit Method)**:
   - Use the difference in good land between the two scenarios as the divisor.
   - Solve for the number of acres of good land (`a`) using the formula:
     \[
     a = \frac{-\text{deficit} \times \text{divisor}}{\text{excess} - \text{deficit}}
     \]
   - Calculate the number of acres of bad land (`b`) as \( b = 100 - a \).

5. **Output**:
   - The values of `a` (good land) and `b` (bad land) are stored in variables.

This code solves the problem using the ancient Chinese mathematical method described in the text.
"""


"""
Code error: both arguments should be Rational instances"""
