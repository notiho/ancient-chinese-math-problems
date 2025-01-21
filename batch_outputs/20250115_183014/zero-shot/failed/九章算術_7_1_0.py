"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，雞價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
rate1 = 9  # rate per person in the first case
excess = 11  # excess amount in the first case
rate2 = 6  # rate per person in the second case
shortage = 16  # shortage amount in the second case

# Step 1: Compute the numerator (實)
numerator = rate1 * rate2 * (excess + shortage)

# Step 2: Compute the denominator (法)
denominator = rate1 * shortage + rate2 * excess

# Step 3: Compute the number of people (a)
a = Fraction(numerator, denominator)

# Step 4: Compute the price of the chicken (b)
b = Fraction(rate1 * rate2 * (excess + shortage), denominator)

# Results
a, b


"""


### Explanation:
1. **Given Data**:
   - `rate1` is the amount each person contributes in the first case.
   - `excess` is the leftover amount in the first case.
   - `rate2` is the amount each person contributes in the second case.
   - `shortage` is the deficit amount in the second case.

2. **Formulas**:
   - The numerator (實) is calculated as the product of the rates and the sum of the excess and shortage.
   - The denominator (法) is calculated as the sum of the products of the rates with the shortage and excess, respectively.
   - The number of people (`a`) is the fraction of the numerator divided by the denominator.
   - The price of the chicken (`b`) is calculated similarly.

### Output:
The variables `a` (number of people) and `b` (price of the chicken) will contain the solutions as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 9, Actual: 243/35
Variable 'b' has wrong value. Expected: 70, Actual: 243/35"""
