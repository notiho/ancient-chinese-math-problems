"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾 a(=1)秉 ， b(=37/4)斗 ，中禾 c(=1)秉 ， d(=17/4)斗 ，下禾 e(=1)秉 ， f(=11/4)斗 。
"""

"""
The problem describes a system of linear equations involving three types of grain bundles (上禾, 中禾, 下禾) and their respective contributions to the total volume of grain in dou. The procedure ("方程術") outlines a method for solving this system of equations step by step.

Here is the Python implementation of the procedure:


"""


from fractions import Fraction

# Given equations:
# 3上禾 + 2中禾 + 1下禾 = 39斗
# 2上禾 + 3中禾 + 1下禾 = 34斗
# 1上禾 + 2中禾 + 3下禾 = 26斗

# Step 1: Represent the equations as coefficients and constants
coefficients = [
    [3, 2, 1],  # Coefficients of 上禾, 中禾, 下禾 in the first equation
    [2, 3, 1],  # Coefficients of 上禾, 中禾, 下禾 in the second equation
    [1, 2, 3]   # Coefficients of 上禾, 中禾, 下禾 in the third equation
]
constants = [39, 34, 26]  # Right-hand side constants

# Step 2: Eliminate 下禾 (third variable) from the first two equations
# Multiply the first equation by 1 (coefficients[2][2]) and the third equation by 1 (coefficients[0][2])
factor1 = coefficients[2][2]
factor2 = coefficients[0][2]
row1 = [coefficients[0][i] * factor1 - coefficients[2][i] * factor2 for i in range(3)]
constant1 = constants[0] * factor1 - constants[2] * factor2

# Multiply the second equation by 1 (coefficients[2][2]) and the third equation by 1 (coefficients[1][2])
factor3 = coefficients[2][2]
factor4 = coefficients[1][2]
row2 = [coefficients[1][i] * factor3 - coefficients[2][i] * factor4 for i in range(3)]
constant2 = constants[1] * factor3 - constants[2] * factor4

# Step 3: Eliminate 中禾 (second variable) from the resulting equations
# Multiply the first resulting equation by 3 (row2[1]) and the second resulting equation by 2 (row1[1])
factor5 = row2[1]
factor6 = row1[1]
row3 = [row1[i] * factor5 - row2[i] * factor6 for i in range(3)]
constant3 = constant1 * factor5 - constant2 * factor6

# Step 4: Solve for 上禾 (first variable)
上禾 = Fraction(constant3, row3[0])

# Step 5: Solve for 中禾 (second variable) using the second resulting equation
中禾 = Fraction(constant2 - row2[0] * 上禾, row2[1])

# Step 6: Solve for 下禾 (third variable) using the first equation
下禾 = Fraction(constants[0] - coefficients[0][0] * 上禾 - coefficients[0][1] * 中禾, coefficients[0][2])

# Results
a = Fraction(1)  # 上禾秉數
b = 上禾  # 上禾實
c = Fraction(1)  # 中禾秉數
d = 中禾  # 中禾實
e = Fraction(1)  # 下禾秉數
f = 下禾  # 下禾實

# Output
print(f"上禾 a(={a})秉 ， b(={b})斗 ，中禾 c(={c})秉 ， d(={d})斗 ，下禾 e(={e})秉 ， f(={f})斗 。")


"""


### Explanation of Results:
- **上禾**: *a* = 1 bundle, *b* = 37/4 dou
- **中禾**: *c* = 1 bundle, *d* = 17/4 dou
- **下禾**: *e* = 1 bundle, *f* = 11/4 dou
"""


"""
"""
