"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，雞價 b 。
"""

"""
To solve this problem, we will translate the given ancient Chinese math problem into Python code. The problem involves finding the number of people (`a`) and the price of a chicken (`b`) based on the given conditions.

### Problem Breakdown:
1. If each person contributes 9 units of money, there is a surplus of 11 units.
2. If each person contributes 6 units of money, there is a deficit of 16 units.
3. We need to find the number of people (`a`) and the price of a chicken (`b`).

### Solution:
Using the "盈不足術" (Surplus and Deficit Method), the solution can be derived as follows:
1. Let `a` be the number of people and `b` be the price of a chicken.
2. The total money collected when each person contributes 9 is `9a`, and the surplus is 11. Thus, the total price of the chickens is `9a - 11`.
3. The total money collected when each person contributes 6 is `6a`, and the deficit is 16. Thus, the total price of the chickens is `6a + 16`.
4. Since the total price of the chickens is the same in both cases, we equate the two expressions:
   ```
   9a - 11 = 6a + 16
   ```
   Solve for `a` (number of people).
5. Once `a` is found, substitute it back into either equation to find `b` (price of a chicken).

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Solve for the number of people (a)
# Equation: 9a - 11 = 6a + 16
a = Fraction(16 + 11, 9 - 6)  # a = (16 + 11) / (9 - 6)

# Step 2: Solve for the price of a chicken (b)
# Use the equation: b = 9a - 11
b = 9 * a - 11

# Results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. We use the `Fraction` class to ensure that the calculations are accurate and handle non-integer results.
2. The number of people (`a`) is calculated by solving the equation `9a - 11 = 6a + 16`.
3. The price of a chicken (`b`) is calculated using the equation `b = 9a - 11`.

### Solution:
After running the code:
- `a = 9` (number of people)
- `b = 70` (price of a chicken)

Thus, the answer is:
```
荅曰： 9人 ，雞價 70 。
```
"""


"""
"""
