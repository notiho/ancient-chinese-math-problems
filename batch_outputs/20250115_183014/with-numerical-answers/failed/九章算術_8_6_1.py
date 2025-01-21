"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a(=1) ，直金 b(=34/21)兩 ，羊 c(=1) ，直金 d(=20/21)兩 。
"""

"""
The problem involves solving a system of linear equations to determine the value of a cow and a sheep in terms of gold taels. The ancient Chinese method of solving such problems is referred to as "fangcheng" (方程), which is essentially an early form of solving simultaneous linear equations.

The problem can be translated into the following equations based on the given information:

1. \( 5x + 2y = 10 \)  (where \(x\) is the value of a cow and \(y\) is the value of a sheep)
2. \( 2x + 5y = 8 \)

We will solve this system of equations step by step using the principles of the "fangcheng" method.


"""


from fractions import Fraction

# 牛五、羊二，直金十兩
# Equation 1: 5x + 2y = 10
eq1_cow_coeff = 5
eq1_sheep_coeff = 2
eq1_constant = 10

# 牛二、羊五，直金八兩
# Equation 2: 2x + 5y = 8
eq2_cow_coeff = 2
eq2_sheep_coeff = 5
eq2_constant = 8

# Step 1: Eliminate one variable (e.g., x) by aligning coefficients
# Multiply Equation 1 by 2 and Equation 2 by 5 to align the coefficients of x
eq1_cow_coeff *= 2
eq1_sheep_coeff *= 2
eq1_constant *= 2

eq2_cow_coeff *= 5
eq2_sheep_coeff *= 5
eq2_constant *= 5

# Equation 1 becomes: 10x + 4y = 20
# Equation 2 becomes: 10x + 25y = 40

# Step 2: Subtract the modified Equation 1 from the modified Equation 2 to eliminate x
sheep_coeff = eq2_sheep_coeff - eq1_sheep_coeff  # 25y - 4y = 21y
constant = eq2_constant - eq1_constant  # 40 - 20 = 20

# The resulting equation is: 21y = 20
# Solve for y
y = Fraction(constant, sheep_coeff)  # y = 20 / 21

# Step 3: Substitute y back into one of the original equations to solve for x
# Using the original Equation 1: 5x + 2y = 10
x = Fraction(eq1_constant - eq1_sheep_coeff * y, eq1_cow_coeff)  # x = (10 - 2 * (20/21)) / 5

# Simplify x
x = Fraction(10, 1) - Fraction(40, 21)
x = Fraction(210, 21) - Fraction(40, 21)
x = Fraction(170, 21)
x = Fraction(x, eq1_cow_coeff)

# Results
a = 1  # Number of cows
b = x  # Value of a cow in gold taels
c = 1  # Number of sheep
d = y  # Value of a sheep in gold taels

print(f"牛 a(={a}) ，直金 b(={b})兩 ，羊 c(={c}) ，直金 d(={d})兩 。")


"""

"""


"""
Variable 'b' has wrong value. Expected: 34/21, Actual: 17/21"""
