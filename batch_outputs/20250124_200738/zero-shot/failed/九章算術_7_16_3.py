"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves finding the number of "善田" (good fields, denoted as `a`) and "惡田" (bad fields, denoted as `b`) such that their combined price equals 10,000. The price per unit area of good fields and bad fields is given, and two scenarios are provided to solve the problem using the method of excess and deficiency (盈不足術).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
price_good_field = 300  # Price per 畝 for good fields
price_bad_field = 500 / 7  # Price per 畝 for bad fields
total_price = 10000  # Total price for one 頃 (100 畝)

# Scenario 1: Assume 20 畝 of good fields and 80 畝 of bad fields
a1 = 20
b1 = 80
price1 = a1 * price_good_field + b1 * price_bad_field
excess = price1 - total_price  # Excess amount in this scenario

# Scenario 2: Assume 10 畝 of good fields and 90 畝 of bad fields
a2 = 10
b2 = 90
price2 = a2 * price_good_field + b2 * price_bad_field
deficiency = total_price - price2  # Deficiency amount in this scenario

# Using the method of excess and deficiency (盈不足術)
# The difference in the number of good fields between the two scenarios
delta_a = a1 - a2

# The total difference in price between the two scenarios
delta_price = excess + deficiency

# Solve for the number of good fields (a)
a = Fraction(deficiency * delta_a, delta_price)

# Solve for the number of bad fields (b)
b = Fraction(100) - a  # Total area is 100 畝 (1 頃)

# Output the results
a, b
#----- content ends here -----


"""


### Explanation:
1. **Price Calculation**: The price per 畝 for good fields is 300, and for bad fields, it's \( \frac{500}{7} \). The total price for 1 頃 (100 畝) is 10,000.
2. **Scenarios**: Two scenarios are given:
   - Scenario 1: 20 畝 of good fields and 80 畝 of bad fields result in an excess of \( 1714 + \frac{2}{7} \).
   - Scenario 2: 10 畝 of good fields and 90 畝 of bad fields result in a deficiency of \( 571 + \frac{3}{7} \).
3. **Excess and Deficiency Method**: Using the method described, the difference in the number of good fields (\( \Delta a \)) and the total price difference (\( \Delta \text{price} \)) are used to compute the actual number of good fields (\( a \)) and bad fields (\( b \)).

### Solution:
The variables `a` and `b` will contain the number of good fields and bad fields, respectively, as fractions.
"""


"""
Code error: both arguments should be Rational instances"""
