"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese "方程術" (method of solving simultaneous equations). Let's translate the problem into Python code step by step.

The problem can be expressed as two equations:
1. \( 2M + B = 10000 + \frac{1}{2}M \)
2. \( M + 2B = 10000 - \frac{1}{2}B \)

Where \( M \) is the price of a horse, and \( B \) is the price of a cow. We'll solve this using the described procedure.


"""


from fractions import Fraction

# Define the equations
# Equation 1: 2M + B = 10000 + (1/2)M
# Rearrange: (2 - 1/2)M + B = 10000
# Simplify: (3/2)M + B = 10000
eq1_coeff_M = Fraction(3, 2)
eq1_coeff_B = 1
eq1_const = 10000

# Equation 2: M + 2B = 10000 - (1/2)B
# Rearrange: M + (2 + 1/2)B = 10000
# Simplify: M + (5/2)B = 10000
eq2_coeff_M = 1
eq2_coeff_B = Fraction(5, 2)
eq2_const = 10000

# Solve using the described method
# Step 1: Eliminate M by multiplying equations appropriately
# Multiply eq1 by 1 (coefficient of M in eq2) and eq2 by (3/2) (coefficient of M in eq1)
multiplier_eq1 = eq2_coeff_M
multiplier_eq2 = eq1_coeff_M

new_eq1_coeff_B = multiplier_eq1 * eq1_coeff_B
new_eq1_const = multiplier_eq1 * eq1_const

new_eq2_coeff_B = multiplier_eq2 * eq2_coeff_B
new_eq2_const = multiplier_eq2 * eq2_const

# Subtract the two equations to eliminate M
final_coeff_B = new_eq2_coeff_B - new_eq1_coeff_B
final_const = new_eq2_const - new_eq1_const

# Solve for B
b = final_const / final_coeff_B

# Substitute B back into one of the original equations to solve for M
# Using the first equation: (3/2)M + B = 10000
a = (eq1_const - eq1_coeff_B * b) / eq1_coeff_M

# Output the results
a = float(a)
b = float(b)


"""

"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 5454.545454545455
Variable 'b' has wrong value. Expected: 20000/11, Actual: 1818.1818181818182"""
