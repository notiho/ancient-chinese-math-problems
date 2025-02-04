"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the principal amount (`a`) and the total interest (`b`) based on the given returns over five periods. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
returns = [14000, 13000, 12000, 11000, 10000]  # Returns over five periods
rate = Fraction(13, 100)  # Interest rate (13%)

# Step 1: Define the total amount returned (sum of all returns)
total_returned = sum(returns)

# Step 2: Use the "盈不足" (excess and deficiency) method to calculate the principal and interest
# Assume two trial values for the principal
trial1 = 30000  # First trial value
trial2 = 40000  # Second trial value

# Calculate the total amount (principal + interest) for each trial
total1 = trial1 + trial1 * rate * 5  # Total for trial1
total2 = trial2 + trial2 * rate * 5  # Total for trial2

# Calculate the excess and deficiency
excess = total2 - total_returned  # Excess for trial2
deficiency = total_returned - total1  # Deficiency for trial1

# Use the formula to calculate the actual principal
a = (trial1 * excess + trial2 * deficiency) / (excess + deficiency)

# Step 3: Calculate the total interest
b = a * rate * 5

# Output the results
a = Fraction(a).limit_denominator()  # Principal
b = Fraction(b).limit_denominator()  # Total interest

# Results
print(f"Principal (a): {a} 錢")
print(f"Total Interest (b): {b} 錢")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Given Data**: The returns over five periods and the interest rate are provided.
2. **Total Returned**: The sum of all returns is calculated.
3. **Trial Values**: Two trial values for the principal (`trial1` and `trial2`) are assumed.
4. **Excess and Deficiency**: The excess and deficiency are calculated based on the total returned and the total amount for each trial.
5. **Principal Calculation**: The formula for the "盈不足" method is used to calculate the actual principal (`a`).
6. **Interest Calculation**: The total interest (`b`) is calculated based on the principal and the interest rate over five periods.
7. **Output**: The results are displayed as fractions for accuracy.

### Results:
The variables `a` and `b` will contain the principal and total interest, respectively, as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 400000/11
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 260000/11"""
