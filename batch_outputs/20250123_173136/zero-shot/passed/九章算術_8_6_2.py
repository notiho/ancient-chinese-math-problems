"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to determine the value of "a" (the price of one cow in gold) and "b" (the price of one sheep in gold).

The equations are:
1. \( 5a + 2b = 10 \)
2. \( 2a + 5b = 8 \)

We will solve these equations using Python and the `Fraction` class to ensure precision.


"""


from fractions import Fraction

# Define the equations
# 5a + 2b = 10
# 2a + 5b = 8

# Solve for a and b
# Multiply the first equation by 5 and the second equation by 2 to align coefficients of b
# 25a + 10b = 50
# 4a + 10b = 16

# Subtract the second equation from the first to eliminate b
# (25a + 10b) - (4a + 10b) = 50 - 16
# 21a = 34
a = Fraction(34, 21)

# Substitute a back into the first equation to solve for b
# 5a + 2b = 10
# 5(Fraction(34, 21)) + 2b = 10
# Fraction(170, 21) + 2b = 10
# 2b = 10 - Fraction(170, 21)
# 2b = Fraction(210, 21) - Fraction(170, 21)
# 2b = Fraction(40, 21)
# b = Fraction(40, 21) / 2
# b = Fraction(20, 21)
b = Fraction(20, 21)

# The results
a  # Price of one cow in gold
b  # Price of one sheep in gold


"""


The solution is:
- \( a = \frac{34}{21} \) (price of one cow in gold)
- \( b = \frac{20}{21} \) (price of one sheep in gold)
"""


"""
"""
