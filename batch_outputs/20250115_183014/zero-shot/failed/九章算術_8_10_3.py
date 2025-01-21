"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves two equations:

1. \( 2a + b = 10000 + \frac{a}{2} \)
2. \( a + 2b = 10000 - \frac{b}{2} \)

Here, \( a \) represents the price of a horse in "錢" (money), and \( b \) represents the price of a cow in "錢". We will solve for \( a \) and \( b \) using Python.


"""


from fractions import Fraction

# Define the equations based on the problem
# Equation 1: 2a + b = 10000 + a / 2
# Equation 2: a + 2b = 10000 - b / 2

# Solve for a and b
# Rearrange Equation 1: 2a + b - a / 2 = 10000
# Multiply through by 2 to eliminate fractions: 4a + 2b - a = 20000
# Simplify: 3a + 2b = 20000

# Rearrange Equation 2: a + 2b + b / 2 = 10000
# Multiply through by 2 to eliminate fractions: 2a + 4b + b = 20000
# Simplify: 2a + 5b = 20000

# Now we solve the system of linear equations:
# 3a + 2b = 20000
# 2a + 5b = 20000

# Multiply the first equation by 2 and the second equation by 3 to align coefficients of a:
# 6a + 4b = 40000
# 6a + 15b = 60000

# Subtract the first equation from the second:
# (6a + 15b) - (6a + 4b) = 60000 - 40000
# 11b = 20000
b = Fraction(20000, 11)

# Substitute b back into the first equation:
# 3a + 2b = 20000
# 3a + 2 * (20000 / 11) = 20000
# 3a + 40000 / 11 = 20000
# Multiply through by 11 to eliminate fractions:
# 33a + 40000 = 220000
# 33a = 220000 - 40000
# 33a = 180000
a = Fraction(180000, 33)

# The results
a = float(a)  # Convert to float for readability
b = float(b)  # Convert to float for readability

# Output the results
a, b


"""


This code calculates the price of a horse (\( a \)) and a cow (\( b \)) in "錢". The values are stored in the variables `a` and `b`.
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 5454.545454545455
Variable 'b' has wrong value. Expected: 20000/11, Actual: 1818.1818181818182"""
