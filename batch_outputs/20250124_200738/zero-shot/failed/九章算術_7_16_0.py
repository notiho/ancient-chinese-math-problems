"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves finding the number of acres of good land ("善田") and bad land ("惡田") purchased, given their respective prices and the total cost. We'll use the method described in the problem (盈不足術, or the "excess and deficiency method") to compute the solution.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Prices per acre
price_good_land = 300  # 善田每畝價錢
price_bad_land = 500 / 7  # 惡田每畝價錢

# Total land purchased
total_land = 100  # 一頃 = 100 畝

# Total cost
total_cost = 10000  # 總價錢

# First assumption: 20 acres of good land, 80 acres of bad land
good_land_1 = 20
bad_land_1 = 80
cost_1 = good_land_1 * price_good_land + bad_land_1 * price_bad_land
excess_1 = cost_1 - total_cost  # 多一千七百一十四錢、七分錢之二
excess_1 = Fraction(1714, 1) + Fraction(2, 7)

# Second assumption: 10 acres of good land, 90 acres of bad land
good_land_2 = 10
bad_land_2 = 90
cost_2 = good_land_2 * price_good_land + bad_land_2 * price_bad_land
deficiency_2 = total_cost - cost_2  # 不足五百七十一錢、七分錢之三
deficiency_2 = Fraction(571, 1) + Fraction(3, 7)

# Using the excess and deficiency method
# Difference in good land between the two assumptions
delta_good_land = good_land_1 - good_land_2

# Total excess and deficiency
total_difference = excess_1 + deficiency_2

# Solve for the number of acres of good land
a = total_difference / delta_good_land

# Solve for the number of acres of bad land
b = total_land - a

# Output the results
a = float(a)  # 善田畝數
b = float(b)  # 惡田畝數
#----- content ends here -----


"""


### Explanation of the Code:
1. **Prices per Acre**: The price of good land is 300 per acre, and the price of bad land is \( \frac{500}{7} \) per acre.
2. **Assumptions**: Two scenarios are given:
   - First assumption: 20 acres of good land and 80 acres of bad land, resulting in an excess cost.
   - Second assumption: 10 acres of good land and 90 acres of bad land, resulting in a deficiency in cost.
3. **Excess and Deficiency**: The excess and deficiency values are calculated based on the total cost and the costs under each assumption.
4. **Excess and Deficiency Method**: Using the difference in the number of acres of good land between the two assumptions and the total excess and deficiency, we solve for the number of acres of good land. The number of acres of bad land is then calculated as the remainder of the total land.

### Final Answer:
The variables `a` and `b` will contain the number of acres of good land and bad land, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 228.57142857142858
Variable 'b' has wrong value. Expected: 175/2, Actual: -128.57142857142858"""
