"""
今有上禾三秉中禾二秉下禾一秉實三十九斗上禾二秉中禾三秉下禾一秉實三十四斗上禾一秉中禾二秉下禾三秉實二十六斗問上中下禾實一秉各幾何
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾 a秉  b斗 中禾 c秉  d斗 下禾 e秉  f斗 
"""

"""
This problem involves solving a system of linear equations to determine the yield of each type of grain (upper, middle, and lower) per bundle. The ancient Chinese method described here corresponds to solving simultaneous equations using elimination and substitution. Let's translate this into Python code.


"""


from fractions import Fraction

# Given data
# Equation 1: 3 bundles of upper grain, 2 bundles of middle grain, 1 bundle of lower grain yield 39 dou
# Equation 2: 2 bundles of upper grain, 3 bundles of middle grain, 1 bundle of lower grain yield 34 dou
# Equation 3: 1 bundle of upper grain, 2 bundles of middle grain, 3 bundles of lower grain yield 26 dou

# Coefficients of the equations
A = [[3, 2, 1],  # Coefficients for upper, middle, lower in equation 1
     [2, 3, 1],  # Coefficients for upper, middle, lower in equation 2
     [1, 2, 3]]  # Coefficients for upper, middle, lower in equation 3

# Results of the equations
B = [39, 34, 26]

# Step 1: Eliminate the first variable (upper grain) from the second and third equations
# Multiply the first row by 2 and subtract from the second row
A[1] = [A[1][i] - Fraction(2, 3) * A[0][i] for i in range(3)]
B[1] = B[1] - Fraction(2, 3) * B[0]

# Multiply the first row by 1 and subtract from the third row
A[2] = [A[2][i] - Fraction(1, 3) * A[0][i] for i in range(3)]
B[2] = B[2] - Fraction(1, 3) * B[0]

# Step 2: Eliminate the second variable (middle grain) from the third equation
# Multiply the second row by 3 and subtract from the third row
A[2] = [A[2][i] - Fraction(3, 5) * A[1][i] for i in range(3)]
B[2] = B[2] - Fraction(3, 5) * B[1]

# Step 3: Solve for the third variable (lower grain)
lower_grain = B[2] / A[2][2]

# Step 4: Solve for the second variable (middle grain)
middle_grain = (B[1] - A[1][2] * lower_grain) / A[1][1]

# Step 5: Solve for the first variable (upper grain)
upper_grain = (B[0] - A[0][1] * middle_grain - A[0][2] * lower_grain) / A[0][0]

# Results
a, b = 1, upper_grain  # Upper grain: 1 bundle, b dou
c, d = 1, middle_grain  # Middle grain: 1 bundle, d dou
e, f = 1, lower_grain  # Lower grain: 1 bundle, f dou

print(f"上禾 {a}秉 {b}斗 中禾 {c}秉 {d}斗 下禾 {e}秉 {f}斗")


"""


This Python code follows the ancient Chinese procedure step by step, using fractions to ensure precision and solving the system of equations to find the yield per bundle for each type of grain.
"""


"""
Variable 'b' has wrong value. Expected: 37/4, Actual: 338/37
Variable 'd' has wrong value. Expected: 17/4, Actual: 153/37
Variable 'f' has wrong value. Expected: 11/4, Actual: 123/37"""
