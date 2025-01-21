"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
To solve this problem, we will translate the ancient Chinese "方程術" (method of simultaneous equations) into Python code. Here's the step-by-step implementation:


"""


from fractions import Fraction

# Problem setup
# First equation: 5上禾 - 7下禾 = 1斗1升
# Second equation: 7上禾 - 5下禾 = 2斗5升

# Convert all units to 升 (1斗 = 10升)
eq1_constant = 1 * 10 + 1  # 1斗1升 = 11升
eq2_constant = 2 * 10 + 5  # 2斗5升 = 25升

# Coefficients of the equations
# Equation 1: 5上禾 - 7下禾 = 11升
# Equation 2: 7上禾 - 5下禾 = 25升
coefficients = [
    [5, -7, eq1_constant],  # First equation
    [7, -5, eq2_constant],  # Second equation
]

# Solve using elimination (正負術)
# Multiply the first equation by 7 (coefficient of 上禾 in the second equation)
# Multiply the second equation by 5 (coefficient of 上禾 in the first equation)
# This eliminates 上禾 when we subtract the equations
multiplier1 = coefficients[1][0]  # 7
multiplier2 = coefficients[0][0]  # 5

# Scale the equations
scaled_eq1 = [coeff * multiplier1 for coeff in coefficients[0]]
scaled_eq2 = [coeff * multiplier2 for coeff in coefficients[1]]

# Subtract the equations to eliminate 上禾
eliminated_eq = [
    scaled_eq1[1] - scaled_eq2[1],  # Coefficient of 下禾
    scaled_eq1[2] - scaled_eq2[2],  # Constant term
]

# Solve for 下禾
下禾 = Fraction(eliminated_eq[1], eliminated_eq[0])

# Substitute 下禾 back into the first equation to solve for 上禾
上禾 = Fraction(
    coefficients[0][2] - coefficients[0][1] * 下禾,
    coefficients[0][0],
)

# Convert results to 斗 and 升
上禾_斗 = 上禾 // 10
上禾_升 = 上禾 % 10

下禾_斗 = 下禾 // 10
下禾_升 = 下禾 % 10

# Final results
a = 上禾_斗
b = 上禾_升
c = 下禾_斗
d = 下禾_升

# Output
print(f"上禾: {a}斗 {b}升")
print(f"下禾: {c}斗 {d}升")


"""


### Explanation of the Code:
1. **Setup the equations**: The problem gives two equations based on the relationship between 上禾 and 下禾. These are converted into a system of linear equations.
2. **Elimination method**: The "正負術" (elimination method) is used to solve the system of equations. This involves scaling and subtracting equations to eliminate one variable.
3. **Solve for one variable**: After eliminating one variable, the remaining equation is solved for 下禾.
4. **Back-substitution**: The value of 下禾 is substituted back into one of the original equations to solve for 上禾.
5. **Convert units**: The results are converted from 升 to 斗 and 升 for the final answer.

### Final Answer:
The values of `a`, `b`, `c`, and `d` represent the quantities of 上禾 and 下禾 in 斗 and 升, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 0"""
