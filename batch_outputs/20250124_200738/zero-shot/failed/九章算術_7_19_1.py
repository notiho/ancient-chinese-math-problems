"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the principal amount (`a`) and the total interest (`b`) based on the given returns over five periods. We will use the method of excess and deficiency (盈不足術) to solve this.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
returns = [14000, 13000, 12000, 11000, 10000]  # Returns over five periods
rate = Fraction(13, 10)  # Interest rate (13%)

# Step 1: Assume two trial principal amounts
trial1 = 30000  # First trial principal
trial2 = 40000  # Second trial principal

# Step 2: Calculate the total repayment (principal + interest) for each trial
total1 = sum(trial1 * rate**i for i in range(5))  # Total repayment for trial1
total2 = sum(trial2 * rate**i for i in range(5))  # Total repayment for trial2

# Step 3: Calculate the excess and deficiency
excess = total2 - sum(returns)  # Excess for trial2
deficiency = sum(returns) - total1  # Deficiency for trial1

# Step 4: Use the method of excess and deficiency to find the true principal
a = (trial1 * excess + trial2 * deficiency) / (excess + deficiency)

# Step 5: Calculate the total interest
b = sum(returns) - a

# Output the results
a = Fraction(a).limit_denominator()  # Principal amount
b = Fraction(b).limit_denominator()  # Total interest

# Results
a, b
#----- content ends here -----


"""


### Explanation:
1. **Input Data**: The returns over five periods and the interest rate are given.
2. **Trial Values**: Two trial principal amounts (`trial1` and `trial2`) are assumed.
3. **Excess and Deficiency**: Calculate the excess and deficiency based on the total repayment for each trial and the actual total returns.
4. **Principal Calculation**: Use the method of excess and deficiency to compute the true principal (`a`).
5. **Interest Calculation**: Subtract the principal from the total returns to find the total interest (`b`).

### Output:
The variables `a` and `b` will contain the principal amount and total interest, respectively, as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 600000000/90431
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 4825860000/90431"""
