"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 ，羊價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of people (`a`) and the price of a sheep (`b`) based on the given conditions.

### Problem Breakdown:
1. If each person contributes 5 units, the total is 45 units short of the required amount.
2. If each person contributes 7 units, the total is 3 units short of the required amount.

We will use the method described in the problem to solve for `a` (number of people) and `b` (price of a sheep).

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Given data
rate1 = 5  # Contribution rate in the first case
short1 = 45  # Shortfall in the first case
rate2 = 7  # Contribution rate in the second case
short2 = 3  # Shortfall in the second case

# Step 1: Calculate the "實" (numerator)
numerator = (rate2 * short1) - (rate1 * short2)

# Step 2: Calculate the "法" (denominator)
denominator = (rate2 - rate1)

# Step 3: Solve for the number of people (a)
a = Fraction(numerator, denominator)

# Step 4: Solve for the price of a sheep (b)
b = Fraction(rate1 * a + short1)

# Results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Numerator Calculation (`實`)**:
   - Multiply the second rate (`rate2`) by the first shortfall (`short1`).
   - Multiply the first rate (`rate1`) by the second shortfall (`short2`).
   - Subtract the two results.

2. **Denominator Calculation (`法`)**:
   - Subtract the first rate (`rate1`) from the second rate (`rate2`).

3. **Solve for `a` (number of people)**:
   - Divide the numerator by the denominator to get the number of people.

4. **Solve for `b` (price of a sheep)**:
   - Use the first condition to calculate the total price of the sheep.

### Output:
The variables `a` and `b` will contain the solutions:
- `a`: Number of people.
- `b`: Price of a sheep.
"""


"""
Variable 'a' has wrong value. Expected: 21, Actual: 150
Variable 'b' has wrong value. Expected: 150, Actual: 795"""
