"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the principal amount (`a`) and the total interest (`b`) based on the given returns over five periods. The solution uses the "盈不足術" (Excess and Deficiency Method).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
returns = [14000, 13000, 12000, 11000, 10000]  # Returns over five periods
rate = Fraction(13, 100)  # Interest rate (13%)

# Hypothetical cases
principal_case1 = 30000  # Hypothetical principal for case 1
shortfall_case1 = Fraction(1738, 2)  # Shortfall in case 1

principal_case2 = 40000  # Hypothetical principal for case 2
excess_case2 = Fraction(35390, 8)  # Excess in case 2

# Excess and Deficiency Method
# Calculate the difference in principal and the total difference (excess + shortfall)
principal_difference = principal_case2 - principal_case1
total_difference = excess_case2 + shortfall_case1

# Calculate the actual principal (a)
a = principal_case1 + (shortfall_case1 * principal_difference) / total_difference

# Calculate the total interest (b)
b = sum(returns) - a

# Output the results
a, b
#----- content ends here -----


"""


### Explanation:
1. **Given Data**:
   - The returns over five periods are `[14000, 13000, 12000, 11000, 10000]`.
   - The interest rate is `13%`, represented as `Fraction(13, 100)`.

2. **Hypothetical Cases**:
   - Case 1 assumes a principal of `30000`, which results in a shortfall of `1738.5` (or `Fraction(1738, 2)`).
   - Case 2 assumes a principal of `40000`, which results in an excess of `35390/8`.

3. **Excess and Deficiency Method**:
   - The difference in principal between the two cases is `40000 - 30000 = 10000`.
   - The total difference (excess + shortfall) is `35390/8 + 1738/2`.

4. **Calculate the Actual Principal (`a`)**:
   - Using the formula from the "盈不足術", the actual principal is calculated as:
     ```
     a = principal_case1 + (shortfall_case1 * principal_difference) / total_difference
     ```

5. **Calculate the Total Interest (`b`)**:
   - The total interest is the sum of all returns minus the principal:
     ```
     b = sum(returns) - a
     ```

### Output:
The variables `a` and `b` will contain the principal and total interest, respectively, as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 669890000/21171
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 600370000/21171"""
