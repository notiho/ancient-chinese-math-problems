"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 ，羊價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of people (`a`) and the price of a sheep (`b`) based on the given conditions.

Here is the Python code:


"""


from fractions import Fraction

# Given conditions:
# If each person pays 5, the total is 45 less than the cost of the sheep.
# If each person pays 7, the total is 3 less than the cost of the sheep.

# Let the number of people be 'a' and the price of a sheep be 'b'.

# Using the method described:
# 1. Place the rates (5 and 7) and the deficits (45 and 3) below them.
# 2. Multiply the rates by the deficits and subtract the smaller product from the larger product to get the "實" (numerator).
# 3. Subtract the smaller rate from the larger rate to get the "法" (denominator).
# 4. Divide the numerator by the denominator to find the number of people ('a').
# 5. Use the number of people ('a') to calculate the price of the sheep ('b').

rate1 = 5
rate2 = 7
deficit1 = 45
deficit2 = 3

# Calculate the numerator ("實") and denominator ("法") for 'a'
numerator = rate2 * deficit1 - rate1 * deficit2
denominator = rate2 - rate1

# Solve for the number of people ('a')
a = Fraction(numerator, denominator)

# Solve for the price of the sheep ('b')
b = rate1 * a + deficit1

# Results
a, b


"""


### Explanation of the Code:
1. The rates (5 and 7) and deficits (45 and 3) are used to calculate the numerator and denominator for the number of people (`a`).
2. The formula for `a` is derived from the ancient method:  
   \( a = \frac{(7 \times 45) - (5 \times 3)}{7 - 5} \)
3. Once `a` is calculated, the price of the sheep (`b`) is calculated using the first condition:  
   \( b = 5 \times a + 45 \)

### Output:
The variables `a` and `b` will contain the solutions:
- `a` is the number of people.
- `b` is the price of the sheep.
"""


"""
Variable 'a' has wrong value. Expected: 21, Actual: 150
Variable 'b' has wrong value. Expected: 150, Actual: 795"""
