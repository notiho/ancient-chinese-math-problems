"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，雞價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of people (`a`) and the price of a chicken (`b`) based on the given conditions.

Here is the Python code:


"""


from fractions import Fraction

# Given data
rate1 = 9  # Amount each person contributes in the first scenario
excess = 11  # Excess amount in the first scenario
rate2 = 6  # Amount each person contributes in the second scenario
deficit = 16  # Deficit amount in the second scenario

# Step 1: Compute the total amount in each scenario
total1 = rate1 * (rate2 - rate1)  # Total amount in the first scenario
total2 = rate2 * (rate2 - rate1)  # Total amount in the second scenario

# Step 2: Compute the difference between excess and deficit
difference = excess + deficit

# Step 3: Solve for the number of people (a)
a = Fraction(total1 + total2, difference)

# Step 4: Solve for the price of a chicken (b)
b = Fraction(rate1 * a - excess)

# Results
a, b


"""


### Explanation:
1. **Input Data**:
   - `rate1` and `rate2` are the amounts each person contributes in the two scenarios.
   - `excess` and `deficit` are the excess and deficit amounts in the two scenarios.

2. **Formulas**:
   - The total amount contributed by all people in each scenario is calculated using the rates and differences.
   - The difference between the excess and deficit is used to compute the number of people (`a`).
   - The price of a chicken (`b`) is derived from the total contribution in one scenario.

3. **Output**:
   - The solution gives the number of people (`a`) and the price of a chicken (`b`) as fractions.

Let me know if you need further clarification!
"""


"""
Variable 'a' has wrong value. Expected: 9, Actual: -5/3
Variable 'b' has wrong value. Expected: 70, Actual: -26"""
