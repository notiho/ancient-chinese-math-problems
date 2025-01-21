"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
To solve this problem using the described ancient Chinese method (方程術), we will translate the procedure into Python code step by step. The problem involves solving a system of linear equations to find the "實" (yield per unit) of 上禾 (upper grain) and 下禾 (lower grain).

The equations are:
1. \( 5x - 7y = 1斗1升 \) (convert to total 升: \( 5x - 7y = 101 \))
2. \( 7x - 5y = 2斗5升 \) (convert to total 升: \( 7x - 5y = 205 \))

Here is the Python implementation:


"""


from fractions import Fraction

# Convert the given values into total 升 (1斗 = 10升)
eq1_constant = 1 * 10 + 1  # 1斗1升 = 10 + 1 = 11升
eq2_constant = 2 * 10 + 5  # 2斗5升 = 20 + 5 = 25升

# Coefficients of the equations
# Equation 1: 5x - 7y = 11
# Equation 2: 7x - 5y = 25
a1, b1, c1 = 5, -7, eq1_constant
a2, b2, c2 = 7, -5, eq2_constant

# Solve using elimination method
# Multiply equations to align coefficients for elimination
# Multiply eq1 by 7 and eq2 by 5
eq1_multiplied = [a1 * 7, b1 * 7, c1 * 7]
eq2_multiplied = [a2 * 5, b2 * 5, c2 * 5]

# Subtract the equations to eliminate y
x_coefficient = eq1_multiplied[0] - eq2_multiplied[0]
constant = eq1_multiplied[2] - eq2_multiplied[2]

# Solve for x (實 of 上禾)
x = Fraction(constant, x_coefficient)

# Substitute x back into one of the original equations to solve for y
# Using Equation 1: 5x - 7y = 11
y = Fraction(a1 * x - c1, -b1)

# Convert x and y back to 斗 and 升
x_dou = x // 10  # Whole 斗
x_sheng = x % 10  # Remaining 升

y_dou = y // 10  # Whole 斗
y_sheng = y % 10  # Remaining 升

# Results
a, b = x_dou, x_sheng  # 上禾實 per 秉
c, d = y_dou, y_sheng  # 下禾實 per 秉

# Output
print(f"上禾 {a}斗 {b}升")
print(f"下禾 {c}斗 {d}升")


"""


### Explanation of the Code:
1. **Convert to 升**: Since the problem uses 斗 and 升, we first convert all values to 升 for easier calculation.
2. **Set up equations**: The two equations are set up based on the problem description.
3. **Elimination method**: We eliminate one variable (y) by aligning coefficients and subtracting the equations.
4. **Solve for x and y**: After eliminating y, we solve for x (實 of 上禾) and substitute it back to find y (實 of 下禾).
5. **Convert back to 斗 and 升**: The results are converted back to 斗 and 升 for the final answer.

### Answer:
The final output will give the yield per 秉 for both 上禾 and 下禾 in terms of 斗 and 升.
"""


"""
Code error: Fraction(-48, 0)"""
