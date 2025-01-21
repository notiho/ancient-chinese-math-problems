"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
To solve this problem using the described ancient Chinese method (方程術), we need to translate the procedure into Python code step by step. The problem involves solving a system of linear equations:

1. \( 5x + 2y = 10 \) (where \( x \) is the price of a cow, and \( y \) is the price of a sheep).
2. \( 2x + 5y = 8 \).

The procedure involves using elimination and substitution to solve for \( x \) and \( y \). Below is the Python implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# 5x + 2y = 10
# 2x + 5y = 8
a1, b1, c1 = 5, 2, 10  # Coefficients of the first equation
a2, b2, c2 = 2, 5, 8   # Coefficients of the second equation

# Step 1: Eliminate one variable (y) by multiplying the equations
# Multiply the first equation by b2 and the second equation by b1
eq1 = [a1 * b2, b1 * b2, c1 * b2]  # [5*5, 2*5, 10*5]
eq2 = [a2 * b1, b2 * b1, c2 * b1]  # [2*2, 5*2, 8*2]

# Subtract the second equation from the first to eliminate y
# (a1*b2)x - (a2*b1)x = (c1*b2) - (c2*b1)
x_numerator = eq1[2] - eq2[2]  # Numerator for x
x_denominator = eq1[0] - eq2[0]  # Denominator for x
x = Fraction(x_numerator, x_denominator)  # Value of x (price of a cow)

# Step 2: Substitute x back into one of the original equations to solve for y
# Using the first equation: a1*x + b1*y = c1
y_numerator = c1 - a1 * x  # Numerator for y
y_denominator = b1  # Denominator for y
y = Fraction(y_numerator, y_denominator)  # Value of y (price of a sheep)

# Results
a = 1  # Number of cows
b = x  # Price of a cow in gold
c = 1  # Number of sheep
d = y  # Price of a sheep in gold

# Output
print(f"牛 {a} ，直金 {b}兩 ，羊 {c} ，直金 {d}兩 。")


"""


### Explanation of the Code:
1. **Elimination**: The first step eliminates one variable (in this case, \( y \)) by multiplying the equations to align the coefficients of \( y \), then subtracting one equation from the other.
2. **Substitution**: After finding \( x \) (price of a cow), substitute it back into one of the original equations to solve for \( y \) (price of a sheep).
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as the problem involves ratios and might not result in integers.

### Output:
The program will calculate and output the values of \( x \) (price of a cow) and \( y \) (price of a sheep) in terms of gold.
"""


"""
"""
