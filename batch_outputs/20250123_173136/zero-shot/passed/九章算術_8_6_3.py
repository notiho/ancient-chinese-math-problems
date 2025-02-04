"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
To solve this problem, we can translate the ancient Chinese math problem into a system of linear equations and solve it using Python. Here's how we can compute the values of `a` (price of one cow) and `b` (price of one sheep):

The problem gives us the following equations:
1. \( 5a + 2b = 10 \)
2. \( 2a + 5b = 8 \)

We will solve this system of equations using substitution or elimination.

Here is the Python code:


"""


from fractions import Fraction

# Define the equations
# 5a + 2b = 10
# 2a + 5b = 8

# Solve for a and b
# Multiply the first equation by 5 and the second equation by 2 to eliminate b
# 25a + 10b = 50
# 4a + 10b = 16

# Subtract the second equation from the first
# (25a + 10b) - (4a + 10b) = 50 - 16
# 21a = 34
a = Fraction(34, 21)

# Substitute a into the first equation to solve for b
# 5a + 2b = 10
# 5(Fraction(34, 21)) + 2b = 10
# Fraction(170, 21) + 2b = 10
# 2b = 10 - Fraction(170, 21)
# 2b = Fraction(210, 21) - Fraction(170, 21)
# 2b = Fraction(40, 21)
# b = Fraction(40, 21) / 2
b = Fraction(20, 21)

# The results
a  # Price of one cow in gold taels
b  # Price of one sheep in gold taels


"""


### Solution:
- \( a = \frac{34}{21} \) taels (price of one cow)
- \( b = \frac{20}{21} \) taels (price of one sheep)
"""


"""
"""
