"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
This problem is a classic simultaneous equations problem, which can be solved using the method of elimination or substitution. The description provided in the "術" corresponds to solving a system of linear equations. Let's translate this into Python code step by step.

The problem can be expressed as:
1. \( 5x + 2y = 10 \) (where \( x \) is the price of a cow and \( y \) is the price of a sheep)
2. \( 2x + 5y = 8 \)

We will solve this system of equations using the described method.


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 5x + 2y = 10
a1, b1, c1 = 5, 2, 10

# Equation 2: 2x + 5y = 8
a2, b2, c2 = 2, 5, 8

# Step 1: Eliminate one variable (y) by multiplying equations
# Multiply equation 1 by b2 and equation 2 by b1
eq1_mult = [a1 * b2, b1 * b2, c1 * b2]
eq2_mult = [a2 * b1, b2 * b1, c2 * b1]

# Subtract the equations to eliminate y
x_coeff = eq1_mult[0] - eq2_mult[0]
constant = eq1_mult[2] - eq2_mult[2]

# Solve for x
x = Fraction(constant, x_coeff)

# Step 2: Substitute x back into one of the original equations to solve for y
# Using equation 1: 5x + 2y = 10
y = Fraction(c1 - a1 * x, b1)

# Results
a = "牛"
b = x  # Price of a cow
c = "羊"
d = y  # Price of a sheep

print(f"{a} {b}兩, {c} {d}兩")


"""


### Explanation of the Code:
1. The coefficients of the two equations are extracted.
2. The first step eliminates one variable (in this case, \( y \)) by multiplying the equations to align the coefficients of \( y \), then subtracting one equation from the other.
3. The resulting equation is solved for \( x \) (price of a cow).
4. The value of \( x \) is substituted back into one of the original equations to solve for \( y \) (price of a sheep).
5. The results are printed.

### Final Answer:
- \( 牛 \): \( b \)兩 (price of a cow)
- \( 羊 \): \( d \)兩 (price of a sheep)
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 牛
Variable 'c' has wrong value. Expected: 1, Actual: 羊"""
