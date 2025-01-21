"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾 a秉 ， b斗 ，中禾 c秉 ， d斗 ，下禾 e秉 ， f斗 。
"""

"""
This problem involves solving a system of linear equations to determine the yield of one bundle of upper, middle, and lower grain. Below is the translation of the procedure into Python code:


"""


from fractions import Fraction

# Given equations:
# 3上禾 + 2中禾 + 1下禾 = 39斗
# 2上禾 + 3中禾 + 1下禾 = 34斗
# 1上禾 + 2中禾 + 3下禾 = 26斗

# Coefficients of the equations
coefficients = [
    [3, 2, 1],  # Coefficients of 上禾, 中禾, 下禾 in the first equation
    [2, 3, 1],  # Coefficients of 上禾, 中禾, 下禾 in the second equation
    [1, 2, 3]   # Coefficients of 上禾, 中禾, 下禾 in the third equation
]

# Constants on the right-hand side of the equations
constants = [39, 34, 26]

# Step 1: Eliminate 上禾 from the second and third equations
factor1 = Fraction(coefficients[1][0], coefficients[0][0])  # Factor to eliminate 上禾 from the second equation
factor2 = Fraction(coefficients[2][0], coefficients[0][0])  # Factor to eliminate 上禾 from the third equation

# Update the second equation
coefficients[1] = [
    coefficients[1][i] - factor1 * coefficients[0][i]
    for i in range(3)
]
constants[1] -= factor1 * constants[0]

# Update the third equation
coefficients[2] = [
    coefficients[2][i] - factor2 * coefficients[0][i]
    for i in range(3)
]
constants[2] -= factor2 * constants[0]

# Step 2: Eliminate 中禾 from the third equation
factor3 = Fraction(coefficients[2][1], coefficients[1][1])  # Factor to eliminate 中禾 from the third equation

coefficients[2] = [
    coefficients[2][i] - factor3 * coefficients[1][i]
    for i in range(3)
]
constants[2] -= factor3 * constants[1]

# Step 3: Solve for 下禾
下禾 = Fraction(constants[2], coefficients[2][2])

# Step 4: Solve for 中禾
中禾 = Fraction(constants[1] - coefficients[1][2] * 下禾, coefficients[1][1])

# Step 5: Solve for 上禾
上禾 = Fraction(constants[0] - coefficients[0][2] * 下禾 - coefficients[0][1] * 中禾, coefficients[0][0])

# Results
a, b = 上禾.numerator, 上禾.denominator
c, d = 中禾.numerator, 中禾.denominator
e, f = 下禾.numerator, 下禾.denominator

print(f"上禾 {a}秉 ， {b}斗 ，中禾 {c}秉 ， {d}斗 ，下禾 {e}秉 ， {f}斗 。")


"""


### Explanation of the Code:
1. **Input the equations**: The coefficients of the equations and the constants on the right-hand side are stored in lists.
2. **Gaussian elimination**: The procedure eliminates variables step by step:
   - Eliminate `上禾` from the second and third equations.
   - Eliminate `中禾` from the third equation.
3. **Back substitution**: Solve for `下禾`, then `中禾`, and finally `上禾`.
4. **Output the results**: The results are expressed as fractions to ensure accuracy.

### Final Answer:
The values of `a`, `b`, `c`, `d`, `e`, and `f` will be computed and displayed as the solution to the problem.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 37
Variable 'b' has wrong value. Expected: 37/4, Actual: 4
Variable 'c' has wrong value. Expected: 1, Actual: 17
Variable 'd' has wrong value. Expected: 17/4, Actual: 4
Variable 'e' has wrong value. Expected: 1, Actual: 11
Variable 'f' has wrong value. Expected: 11/4, Actual: 4"""
