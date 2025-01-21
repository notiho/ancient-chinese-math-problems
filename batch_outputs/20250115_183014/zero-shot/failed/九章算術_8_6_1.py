"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
To solve the problem, we need to translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations. The equations are:

1. \( 5a + 2c = 10 \) (where \( a \) is the price of a cow in gold taels, and \( c \) is the price of a sheep in gold taels)
2. \( 2a + 5c = 8 \)

We will solve for \( a \) and \( c \) using Python. Here's the code:


"""


from fractions import Fraction

# Define the coefficients of the equations
# 5a + 2c = 10
# 2a + 5c = 8

# Solve for a and c using substitution or elimination
# Multiply the first equation by 5 and the second equation by 2 to align coefficients of c
# 25a + 10c = 50
# 4a + 10c = 16

# Subtract the second equation from the first
# (25a + 10c) - (4a + 10c) = 50 - 16
# 21a = 34
a = Fraction(34, 21)

# Substitute a back into the first equation to solve for c
# 5a + 2c = 10
# 2c = 10 - 5a
# c = (10 - 5a) / 2
c = (Fraction(10) - 5 * a) / 2

# Output the results
a = float(a)
c = float(c)


"""


The solution is:
- \( a \): The price of a cow in gold taels
- \( c \): The price of a sheep in gold taels
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 1.619047619047619
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 1, Actual: 0.9523809523809523
Missing variable in output: 'd'"""
