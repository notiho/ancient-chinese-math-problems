"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 ，羊價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given:
# When each person contributes 5, the total is 45 short.
# When each person contributes 7, the total is 3 short.

# Let the number of people be "a" and the price of the sheep be "b".

# Using the method described:
# Rate of contribution: 5 and 7
# Shortfall: 45 and 3

# Step 1: Calculate the "實" (numerator)
numerator = (7 * 45) - (5 * 3)

# Step 2: Calculate the "法" (denominator)
denominator = (7 - 5)

# Step 3: Solve for the number of people (a)
a = numerator // denominator

# Step 4: Solve for the price of the sheep (b)
b = Fraction(5 * a + 45)

# Results:
a  # Number of people
b  # Price of the sheep


"""


### Explanation:
1. The problem involves two scenarios:
   - When each person contributes 5, the total is 45 short.
   - When each person contributes 7, the total is 3 short.

2. Using the ancient method:
   - Multiply the shortfall by the opposite rate of contribution.
   - Subtract the results to get the numerator ("實").
   - Subtract the rates of contribution to get the denominator ("法").
   - Divide the numerator by the denominator to find the number of people ("a").

3. Once the number of people is determined, calculate the total price of the sheep ("b") using one of the scenarios.

### Final Answer:
- `a` is the number of people.
- `b` is the price of the sheep.
"""


"""
Variable 'a' has wrong value. Expected: 21, Actual: 150
Variable 'b' has wrong value. Expected: 150, Actual: 795"""
