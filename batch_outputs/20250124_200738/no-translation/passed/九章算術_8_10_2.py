"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "方程術" (method of solving simultaneous equations). Let's translate the problem into Python code step by step.

The problem can be expressed as two equations:
1. \( 2M + B = 10000 + \frac{1}{2}M \)
2. \( M + 2B = 10000 - \frac{1}{2}B \)

Where \( M \) is the price of a horse (馬價), and \( B \) is the price of a cow (牛價).

We will solve this using the described method.


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations in terms of coefficients and constants
# Equation 1: 2M + B = 10000 + (1/2)M
# Rearrange: (2 - 1/2)M + B = 10000
coeff1_M = 2 - Fraction(1, 2)  # Coefficient of M in the first equation
coeff1_B = 1                  # Coefficient of B in the first equation
const1 = 10000                # Constant term in the first equation

# Equation 2: M + 2B = 10000 - (1/2)B
# Rearrange: M + (2 + 1/2)B = 10000
coeff2_M = 1                  # Coefficient of M in the second equation
coeff2_B = 2 + Fraction(1, 2) # Coefficient of B in the second equation
const2 = 10000                # Constant term in the second equation

# Use elimination to solve for M and B
# Multiply the first equation by coeff2_B and the second equation by coeff1_B
# This eliminates B when subtracting the equations
factor1 = coeff2_B
factor2 = coeff1_B

new_coeff1_M = factor1 * coeff1_M
new_const1 = factor1 * const1

new_coeff2_M = factor2 * coeff2_M
new_const2 = factor2 * const2

# Subtract the equations to eliminate B
final_coeff_M = new_coeff1_M - new_coeff2_M
final_const = new_const1 - new_const2

# Solve for M
M = Fraction(final_const, final_coeff_M)

# Substitute M back into one of the original equations to solve for B
# Using the first equation: (2 - 1/2)M + B = 10000
B = Fraction(const1 - coeff1_M * M, coeff1_B)

# Results
a = M  # 馬價
b = B  # 牛價

# Output the results
a, b
#----- content ends here -----


"""


This code solves the problem using the described ancient Chinese method of elimination and substitution. The results are expressed as fractions for precision.
"""


"""
"""
