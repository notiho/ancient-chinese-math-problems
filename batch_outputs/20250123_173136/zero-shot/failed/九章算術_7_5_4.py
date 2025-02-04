"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 ，羊價 b 。
"""

"""
To solve this problem, let's translate it into Python code. The problem involves finding the number of people (`a`) and the price of a sheep (`b`) based on the given conditions.

### Problem Breakdown:
1. If each person contributes 5 units of money, the total is 45 units short of the required amount.
2. If each person contributes 7 units of money, the total is 3 units short of the required amount.

We will use the method described in the problem to solve for `a` (number of people) and `b` (price of a sheep).

### Python Code:

"""


from fractions import Fraction

# Given data
rate1 = 5  # First contribution rate
rate2 = 7  # Second contribution rate
short1 = 45  # Shortfall for the first rate
short2 = 3   # Shortfall for the second rate

# Calculate the "實" (numerator of the solution)
numerator = (rate2 * short1) - (rate1 * short2)

# Calculate the "法" (denominator of the solution)
denominator = (rate2 - rate1)

# Number of people (a)
a = Fraction(numerator, denominator)

# Price of a sheep (b)
b = rate1 * a + short1

# Results
a, b


"""


### Explanation:
1. The "實" (numerator) is calculated as `(rate2 * short1) - (rate1 * short2)`.
2. The "法" (denominator) is calculated as `(rate2 - rate1)`.
3. The number of people (`a`) is the fraction `實 / 法`.
4. The price of a sheep (`b`) is calculated using the first condition: `rate1 * a + short1`.

### Solution:
After running the code, the values of `a` and `b` will be computed as fractions or integers, depending on the inputs.
"""


"""
Variable 'a' has wrong value. Expected: 21, Actual: 150
Variable 'b' has wrong value. Expected: 150, Actual: 795"""
