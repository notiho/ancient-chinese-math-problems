"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "方程術" (method of solving simultaneous equations). Let's translate the problem into Python code step by step.

The problem can be expressed as two equations:
1. \( 2M + B = 10000 + \frac{1}{2}M \)
2. \( M + 2B = 10000 - \frac{1}{2}B \)

Where \( M \) is the price of a horse (馬價), and \( B \) is the price of a cow (牛價).

We will solve this using the described method.


"""


from fractions import Fraction

# Define the equations
# Equation 1: 2M + B = 10000 + (1/2)M
# Rearrange: (2 - 1/2)M + B = 10000
eq1_M_coeff = Fraction(2) - Fraction(1, 2)  # Coefficient of M in equation 1
eq1_B_coeff = Fraction(1)                  # Coefficient of B in equation 1
eq1_const = Fraction(10000)                # Constant term in equation 1

# Equation 2: M + 2B = 10000 - (1/2)B
# Rearrange: M + (2 + 1/2)B = 10000
eq2_M_coeff = Fraction(1)                  # Coefficient of M in equation 2
eq2_B_coeff = Fraction(2) + Fraction(1, 2) # Coefficient of B in equation 2
eq2_const = Fraction(10000)                # Constant term in equation 2

# Solve using elimination
# Multiply eq1 by eq2_B_coeff and eq2 by eq1_B_coeff to align B coefficients
eq1_scaled_M_coeff = eq1_M_coeff * eq2_B_coeff
eq1_scaled_const = eq1_const * eq2_B_coeff

eq2_scaled_M_coeff = eq2_M_coeff * eq1_B_coeff
eq2_scaled_const = eq2_const * eq1_B_coeff

# Subtract the scaled equations to eliminate B
M_coeff = eq1_scaled_M_coeff - eq2_scaled_M_coeff
const = eq1_scaled_const - eq2_scaled_const

# Solve for M
M = const / M_coeff

# Substitute M back into one of the original equations to solve for B
B = (eq1_const - eq1_M_coeff * M) / eq1_B_coeff

# Results
a = M  # 馬價
b = B  # 牛價

# Output the results
a, b


"""


### Explanation of the Code:
1. The equations are rearranged to isolate the coefficients of \( M \) and \( B \), as well as the constant terms.
2. The elimination method is used to eliminate \( B \) by scaling the equations appropriately.
3. After eliminating \( B \), the value of \( M \) (馬價) is calculated.
4. The value of \( M \) is substituted back into one of the original equations to solve for \( B \) (牛價).
5. The results are stored in variables `a` and `b`.

### Final Answer:
- \( a \): 馬價 (price of a horse)
- \( b \): 牛價 (price of a cow)
"""


"""
"""
