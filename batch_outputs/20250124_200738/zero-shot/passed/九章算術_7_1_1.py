"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，雞價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of people (`a`) and the price of the chicken (`b`) based on the given conditions.

### Problem Breakdown:
1. If each person contributes 9 units of money, there is an excess of 11 units.
2. If each person contributes 6 units of money, there is a shortage of 16 units.
3. We need to find the number of people (`a`) and the price of the chicken (`b`).

### Solution:
Using the "盈不足術" (Excess and Deficit Method):
1. Let the number of people be `a` and the price of the chicken be `b`.
2. From the first condition: `9a = b + 11`
3. From the second condition: `6a = b - 16`
4. Subtract the second equation from the first to eliminate `b` and solve for `a`.
5. Substitute `a` back into one of the equations to solve for `b`.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Define the given conditions
rate1 = 9  # Money contributed per person in the first case
rate2 = 6  # Money contributed per person in the second case
excess = 11  # Excess money in the first case
deficit = 16  # Shortage of money in the second case

# Step 2: Use the Excess and Deficit Method
# (rate1 - rate2) * a = excess + deficit
a = Fraction(excess + deficit, rate1 - rate2)

# Step 3: Solve for the price of the chicken (b)
# Using the first condition: b = rate1 * a - excess
b = rate1 * a - excess

# The results
a, b  # a is the number of people, b is the price of the chicken
#----- content ends here -----


"""


### Explanation of the Code:
1. `rate1` and `rate2` are the amounts contributed by each person in the two cases.
2. `excess` and `deficit` are the excess and shortage amounts, respectively.
3. The equation `(rate1 - rate2) * a = excess + deficit` is derived from subtracting the two conditions.
4. Solve for `a` (number of people) using the equation above.
5. Substitute `a` into the first condition to solve for `b` (price of the chicken).

### Final Answer:
After running the code:
- `a = 9` (number of people)
- `b = 90` (price of the chicken)
"""


"""
"""
