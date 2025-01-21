"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
To solve this problem, we need to follow the ancient Chinese method of solving simultaneous linear equations, as described in the problem. Here's the Python implementation:


"""


from fractions import Fraction

# Problem setup
# First equation: 6上禾 - 10下禾 = 1斗8升 (convert to 升: 1斗 = 10升)
eq1_upper = 6  # Coefficient of 上禾
eq1_lower = -10  # Coefficient of 下禾
eq1_constant = 1 * 10 + 8  # Convert 1斗8升 to 升

# Second equation: -5上禾 + 15下禾 = 5升
eq2_upper = -5  # Coefficient of 上禾
eq2_lower = 15  # Coefficient of 下禾
eq2_constant = 5  # Already in 升

# Solve using elimination method
# Multiply equations to align coefficients for elimination
eq1_upper_scaled = eq1_upper * 5  # Scale first equation by 5
eq1_lower_scaled = eq1_lower * 5
eq1_constant_scaled = eq1_constant * 5

eq2_upper_scaled = eq2_upper * 6  # Scale second equation by 6
eq2_lower_scaled = eq2_lower * 6
eq2_constant_scaled = eq2_constant * 6

# Eliminate 上禾 (upper variable)
lower_coefficient = eq1_lower_scaled + eq2_lower_scaled
lower_constant = eq1_constant_scaled + eq2_constant_scaled

# Solve for 下禾 (lower variable)
下禾實 = Fraction(lower_constant, lower_coefficient)

# Substitute back to solve for 上禾 (upper variable)
upper_constant = eq1_constant - eq1_lower * 下禾實
上禾實 = Fraction(upper_constant, eq1_upper)

# Convert results to 秉 and 升
a = 1  # 上禾 per 秉
b = 上禾實  # 上禾實 in 升
c = 1  # 下禾 per 秉
d = 下禾實  # 下禾實 in 升

# Output results
print(f"上禾 {a}秉 實 {b}升")
print(f"下禾 {c}秉 實 {d}升")


"""


### Explanation:
1. **Setup the equations**: The problem gives two equations relating the quantities of 上禾 and 下禾. These are converted into coefficients and constants.
2. **Elimination method**: The equations are scaled to align coefficients for one variable (上禾) and eliminate it, solving for the other variable (下禾).
3. **Back substitution**: The value of 下禾 is substituted back into one of the original equations to solve for 上禾.
4. **Conversion**: The results are expressed in terms of 秉 and 升.

This code will calculate the values of 上禾 and 下禾 per 秉 in 升.
"""


"""
"""
