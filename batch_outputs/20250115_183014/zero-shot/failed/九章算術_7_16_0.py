"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves finding the number of acres of good land ("善田", denoted as `a`) and poor land ("惡田", denoted as `b`) purchased, given the total cost and the prices of each type of land.

Here is the Python code:


"""


from fractions import Fraction

# Prices per acre
price_good_land = 300  # 善田每畝價錢
price_poor_land = 500 / 7  # 惡田每畝價錢

# Total land purchased
total_land = 100  # 一頃 = 100 畝

# Total cost
total_cost = 10000  # 總價錢

# Using the excess and deficit method (盈不足術)
# Case 1: Assume 20 acres of good land and 80 acres of poor land
excess = 20 * price_good_land + 80 * price_poor_land - total_cost

# Case 2: Assume 10 acres of good land and 90 acres of poor land
deficit = 10 * price_good_land + 90 * price_poor_land - total_cost

# Calculate the difference in land (善田差)
difference_good_land = 20 - 10

# Calculate the total land price difference
difference_cost = excess - deficit

# Solve for the number of good land acres (善田 a)
a = Fraction(deficit * difference_good_land, difference_cost)

# Solve for the number of poor land acres (惡田 b)
b = total_land - a

# Output the results
a, b


"""


### Explanation:
1. **Prices per acre**: The price of good land is 300 per acre, and the price of poor land is \( \frac{500}{7} \) per acre.
2. **Total land**: The total land purchased is 100 acres (1頃 = 100畝).
3. **Total cost**: The total cost of the land is 10,000.
4. **Excess and Deficit**: Two hypothetical cases are given:
   - Case 1: 20 acres of good land and 80 acres of poor land result in an excess of \( 1714 \frac{2}{7} \).
   - Case 2: 10 acres of good land and 90 acres of poor land result in a deficit of \( 571 \frac{3}{7} \).
5. **Difference in land**: The difference in good land between the two cases is \( 20 - 10 = 10 \).
6. **Difference in cost**: The difference in cost between the two cases is the excess minus the deficit.
7. **Solve for `a` and `b`**:
   - Use the formula derived from the excess and deficit method to calculate the number of acres of good land (`a`).
   - Subtract `a` from the total land to get the number of acres of poor land (`b`).

### Solution:
The variables `a` and `b` will contain the number of acres of good land and poor land, respectively.
"""


"""
Code error: both arguments should be Rational instances"""
