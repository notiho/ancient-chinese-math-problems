"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
To solve this problem using the ancient Chinese "方程術" (method of simultaneous equations), we will translate the procedure into Python code step by step. The problem involves solving a system of two linear equations:

1. \( 5x + 2y = 10 \) (where \( x \) is the price of a cow and \( y \) is the price of a sheep in gold taels).
2. \( 2x + 5y = 8 \).

Here is the Python implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 5x + 2y = 10
a1, b1, c1 = 5, 2, 10

# Equation 2: 2x + 5y = 8
a2, b2, c2 = 2, 5, 8

# Step 1: Eliminate one variable (y) using the "方程術"
# Multiply the first equation by b2 (5) and the second equation by b1 (2)
# This aligns the coefficients of y for elimination
eq1_mult = b2 * a1, b2 * b1, b2 * c1  # (5*5, 5*2, 5*10)
eq2_mult = b1 * a2, b1 * b2, b1 * c2  # (2*2, 2*5, 2*8)

# Subtract the two equations to eliminate y
# (5*5)x - (2*2)x = (5*10) - (2*8)
x_coeff = eq1_mult[0] - eq2_mult[0]
constant = eq1_mult[2] - eq2_mult[2]

# Solve for x
x = Fraction(constant, x_coeff)

# Step 2: Substitute x back into one of the original equations to solve for y
# Using the first equation: 5x + 2y = 10
y = Fraction(c1 - a1 * x, b1)

# Results
a = "牛"
b = x  # Price of a cow in gold taels
c = "羊"
d = y  # Price of a sheep in gold taels

print(f"{a}直金 {b}兩")
print(f"{c}直金 {d}兩")


"""


### Explanation of the Code:
1. The coefficients of the two equations are extracted and aligned for elimination.
2. The "方程術" method is applied to eliminate one variable (in this case, \( y \)).
3. The resulting equation is solved for \( x \) (price of a cow).
4. The value of \( x \) is substituted back into one of the original equations to solve for \( y \) (price of a sheep).
5. The results are printed as the price of a cow and a sheep in gold taels.

### Final Answer:
- \( 牛 \) (cow) is worth \( b \) taels of gold.
- \( 羊 \) (sheep) is worth \( d \) taels of gold.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 牛
Variable 'c' has wrong value. Expected: 1, Actual: 羊"""
