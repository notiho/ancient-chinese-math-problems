"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
To solve this problem, we will translate the ancient Chinese method of solving simultaneous linear equations (方程術) into Python code. The problem involves two equations:

1. \( 5x + 2y = 10 \)
2. \( 2x + 5y = 8 \)

Where \( x \) is the price of one cow in gold taels, and \( y \) is the price of one sheep in gold taels.

We will follow the described procedure step by step.


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 5x + 2y = 10
# Equation 2: 2x + 5y = 8
a1, b1, c1 = 5, 2, 10  # Coefficients of the first equation
a2, b2, c2 = 2, 5, 8   # Coefficients of the second equation

# Step 1: Eliminate one variable (y) by multiplying equations and subtracting
# Multiply the first equation by b2 (5) and the second equation by b1 (2)
# This makes the coefficients of y in both equations equal
eq1_mult = b2 * a1, b2 * b1, b2 * c1  # (5*5, 5*2, 5*10) -> (25, 10, 50)
eq2_mult = b1 * a2, b1 * b2, b1 * c2  # (2*2, 2*5, 2*8) -> (4, 10, 16)

# Subtract the second equation from the first to eliminate y
# (25x - 4x) + (10y - 10y) = 50 - 16
x_coeff = eq1_mult[0] - eq2_mult[0]  # 25 - 4 = 21
y_coeff = eq1_mult[1] - eq2_mult[1]  # 10 - 10 = 0 (y eliminated)
const = eq1_mult[2] - eq2_mult[2]    # 50 - 16 = 34

# Now we have a single equation: 21x = 34
# Solve for x
x = Fraction(const, x_coeff)  # x = 34 / 21

# Step 2: Substitute x back into one of the original equations to solve for y
# Using the first equation: 5x + 2y = 10
# 2y = 10 - 5x
# y = (10 - 5x) / 2
y = Fraction(c1 - a1 * x, b1)  # y = (10 - 5*(34/21)) / 2

# Results
a = x  # Price of one cow
b = y  # Price of one sheep

print(f"牛一，直金 {a} 兩，羊一，直金 {b} 兩。")


"""


### Explanation of the Code:
1. **Input Coefficients**: The coefficients of the two equations are defined.
2. **Elimination**: The variable \( y \) is eliminated by multiplying the equations to make the coefficients of \( y \) equal, then subtracting one equation from the other.
3. **Solve for \( x \)**: The resulting equation is solved for \( x \).
4. **Substitute \( x \) into an Original Equation**: The value of \( x \) is substituted back into one of the original equations to solve for \( y \).
5. **Output Results**: The values of \( x \) and \( y \) are printed as the prices of one cow and one sheep, respectively.

### Final Answer:
The prices of one cow and one sheep in gold taels are represented as fractions for exactness:
- \( a = \text{price of one cow} \)
- \( b = \text{price of one sheep} \)
"""


"""
"""
