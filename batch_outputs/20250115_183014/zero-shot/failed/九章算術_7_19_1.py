"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：本 a錢 。利 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the principal amount (`a`) and the total interest (`b`) based on the given returns over five periods. We will use the method of excess and deficiency (盈不足術) to solve this.

Here is the Python code:


"""


from fractions import Fraction

# Given data
returns = [14000, 13000, 12000, 11000, 10000]  # Returns over five periods
rate = Fraction(13, 100)  # Interest rate (13%)

# Hypothetical cases
principal1 = 30000  # First hypothetical principal
shortfall1 = Fraction(1738, 2)  # Shortfall for the first case

principal2 = 40000  # Second hypothetical principal
excess2 = Fraction(35390, 8)  # Excess for the second case

# Calculate the difference in principal and the difference in shortfall/excess
principal_diff = principal2 - principal1
shortfall_excess_diff = excess2 + shortfall1

# Using the method of excess and deficiency to find the actual principal
a = principal1 + (shortfall1 * principal_diff) / shortfall_excess_diff

# Calculate the total interest (b)
b = sum(returns) - a

# Output the results
a, b


"""


### Explanation:
1. **Given Data**:
   - The returns over five periods are provided as `[14000, 13000, 12000, 11000, 10000]`.
   - The interest rate is `13%`, which is represented as a fraction (`Fraction(13, 100)`).

2. **Hypothetical Cases**:
   - Two hypothetical principal amounts are given: `30000` and `40000`.
   - For the first case, the shortfall is `1738.5` (represented as `Fraction(1738, 2)`).
   - For the second case, the excess is `35390/8` (represented as `Fraction(35390, 8)`).

3. **Method of Excess and Deficiency**:
   - The difference in principal amounts (`principal_diff`) and the difference in shortfall/excess (`shortfall_excess_diff`) are calculated.
   - Using the formula from the method of excess and deficiency, the actual principal (`a`) is calculated.

4. **Total Interest**:
   - The total interest (`b`) is calculated as the sum of all returns minus the principal (`a`).

### Output:
The variables `a` (principal) and `b` (total interest) will contain the solutions to the problem.
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 669890000/21171
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 600370000/21171"""
