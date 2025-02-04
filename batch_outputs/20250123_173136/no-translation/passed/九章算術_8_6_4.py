"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
To solve this problem, we will translate the ancient Chinese method of solving simultaneous linear equations (方程術) into Python code. The problem involves two equations:

1. \( 5x + 2y = 10 \) (where \( x \) is the price of one cow and \( y \) is the price of one sheep).
2. \( 2x + 5y = 8 \).

Here is the Python code:


"""


from fractions import Fraction

# Coefficients of the equations
# 5x + 2y = 10
# 2x + 5y = 8
a1, b1, c1 = 5, 2, 10  # Coefficients for the first equation
a2, b2, c2 = 2, 5, 8   # Coefficients for the second equation

# Step 1: Eliminate one variable (using 方程術)
# Multiply the first equation by b2 and the second equation by b1 to align the coefficients of y
eq1 = [a1 * b2, b1 * b2, c1 * b2]  # [5*5, 2*5, 10*5] -> [25, 10, 50]
eq2 = [a2 * b1, b2 * b1, c2 * b1]  # [2*2, 5*2, 8*2] -> [4, 10, 16]

# Subtract the second equation from the first to eliminate y
# (25x + 10y - 4x - 10y = 50 - 16)
x_coeff = eq1[0] - eq2[0]  # 25 - 4 = 21
x_const = eq1[2] - eq2[2]  # 50 - 16 = 34

# Solve for x
x = Fraction(x_const, x_coeff)  # x = 34 / 21

# Step 2: Substitute x back into one of the original equations to solve for y
# Using the first equation: 5x + 2y = 10
y_const = c1 - a1 * x  # 10 - 5 * (34 / 21)
y = Fraction(y_const, b1)  # y = (10 - 170 / 21) / 2

# Simplify y
y = Fraction(y_const, b1)

# Results
a = x  # Price of one cow
b = y  # Price of one sheep

# Output
a, b


"""


### Explanation of the Code:
1. **Aligning Coefficients**: The first step is to align the coefficients of \( y \) in both equations by multiplying each equation by the coefficient of \( y \) from the other equation.
2. **Elimination**: Subtract one equation from the other to eliminate \( y \), leaving an equation with only \( x \).
3. **Solve for \( x \)**: Solve the resulting equation for \( x \).
4. **Substitute \( x \)**: Substitute the value of \( x \) back into one of the original equations to solve for \( y \).
5. **Fraction Representation**: Use the `Fraction` class to ensure precise arithmetic with fractions.

### Final Answer:
- \( a \): Price of one cow in gold (in taels).
- \( b \): Price of one sheep in gold (in taels).
"""


"""
"""
