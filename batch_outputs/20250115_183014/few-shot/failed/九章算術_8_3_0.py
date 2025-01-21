"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "fangcheng" (方程) method. Below is the solution translated into Python code:


"""


from fractions import Fraction

# 上禾五秉，損實一斗一升，當下禾七秉
上禾1 = 5
下禾1 = -7
損實1 = 1 * 10 + 1  # Convert 1斗1升 to total 升 (1斗 = 10升)

# 上禾七秉，損實二斗五升，當下禾五秉
上禾2 = 7
下禾2 = -5
損實2 = 2 * 10 + 5  # Convert 2斗5升 to total 升

# 方程術: Solve the system of linear equations using elimination
# Equation 1: 5x - 7y = 11
# Equation 2: 7x - 5y = 25

# Step 1: Eliminate one variable (e.g., y)
# Multiply the first equation by 5 and the second equation by 7
eq1_multiplied = [5 * 上禾1, 5 * 下禾1, 5 * 損實1]  # [25x, -35y, 55]
eq2_multiplied = [7 * 上禾2, 7 * 下禾2, 7 * 損實2]  # [49x, -35y, 175]

# Subtract the two equations to eliminate y
eliminated_y = [
    eq1_multiplied[0] - eq2_multiplied[0],  # Coefficient of x
    eq1_multiplied[2] - eq2_multiplied[2],  # Constant term
]  # [-24x, -120]

# Solve for x (上禾實)
上禾實 = Fraction(eliminated_y[1], eliminated_y[0])  # x = -120 / -24 = 5斗

# Step 2: Substitute x back into one of the original equations to solve for y (下禾實)
# Using the first equation: 5x - 7y = 11
下禾實 = Fraction(損實1 - 上禾1 * 上禾實, 下禾1)  # y = (11 - 5*5) / -7 = 2斗

# Convert results to 斗 and 升
a = 上禾實 // 10  # 上禾斗
b = 上禾實 % 10   # 上禾升
c = 下禾實 // 10  # 下禾斗
d = 下禾實 % 10   # 下禾升

# Final answer
print(f"上禾 {a}斗 {b}升, 下禾 {c}斗 {d}升")


"""


### Explanation of the Code:
1. **Input Conversion**: The problem specifies the losses in terms of 斗 and 升. These are converted into total 升 for easier calculations (1斗 = 10升).
2. **System of Equations**: The problem provides two equations:
   - \( 5x - 7y = 11 \) (converted to 升)
   - \( 7x - 5y = 25 \) (converted to 升)
3. **Elimination Method**: The "fangcheng" method is used to eliminate one variable (in this case, \( y \)) by multiplying the equations and subtracting them.
4. **Solve for Variables**: Once \( x \) (上禾實) is found, it is substituted back into one of the original equations to solve for \( y \) (下禾實).
5. **Convert Back to 斗 and 升**: The results are converted back into the original units of 斗 and 升 for the final answer.

### Final Output:
The answer will be printed in the format:
```
上禾 a斗 b升, 下禾 c斗 d升
```
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 0"""
