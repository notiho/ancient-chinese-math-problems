"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves two equations based on the price of horses and cows. Using the given information, we will solve for the price of a horse (`a`) and the price of a cow (`b`) using the `Fraction` class.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Let the price of a horse be 'a' (in qian) and the price of a cow be 'b' (in qian).
# The problem gives us the following equations:
# 1. 2a + b = 10000 + a/2
# 2. a + 2b = 10000 - b/2

# Rewrite the equations:
# From equation 1: 2a + b = 10000 + a/2
# Multiply through by 2 to eliminate the fraction:
# 4a + 2b = 20000 + a
# Simplify:
# 3a + 2b = 20000  (Equation 1)

# From equation 2: a + 2b = 10000 - b/2
# Multiply through by 2 to eliminate the fraction:
# 2a + 4b = 20000 - b
# Simplify:
# 2a + 5b = 20000  (Equation 2)

# Solve the system of equations:
# 3a + 2b = 20000  (Equation 1)
# 2a + 5b = 20000  (Equation 2)

# Multiply Equation 1 by 2 and Equation 2 by 3 to align coefficients of 'a':
# 6a + 4b = 40000  (Modified Equation 1)
# 6a + 15b = 60000  (Modified Equation 2)

# Subtract Modified Equation 1 from Modified Equation 2:
# (6a + 15b) - (6a + 4b) = 60000 - 40000
# 11b = 20000
# Solve for b:
b = Fraction(20000, 11)

# Substitute b back into Equation 1 to solve for a:
# 3a + 2b = 20000
# 3a + 2(Fraction(20000, 11)) = 20000
# 3a = 20000 - 2(Fraction(20000, 11))
# 3a = Fraction(220000, 11) - Fraction(40000, 11)
# 3a = Fraction(180000, 11)
# a = Fraction(180000, 33)

a = Fraction(180000, 33)
b = Fraction(20000, 11)

# The price of a horse (a) and a cow (b) are:
# a (horse price) = 5454 6/11 qian
# b (cow price) = 1818 2/11 qian
#----- content ends here -----


"""


### Final Values:
- `a = Fraction(180000, 33)` (price of a horse in qian)
- `b = Fraction(20000, 11)` (price of a cow in qian)
"""


"""
"""
