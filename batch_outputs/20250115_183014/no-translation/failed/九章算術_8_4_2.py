"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
To solve this problem, we will follow the ancient Chinese mathematical procedure ("方程術") step by step. Here's the Python implementation:


"""


from fractions import Fraction

# Problem setup
# 上禾六秉正，下禾一十秉負，損實一斗八升正
eq1 = [6, -10, Fraction(1 * 10 + 8, 10)]  # Convert 1斗8升 to 升 (1斗 = 10升)

# 上禾五秉負，下禾一十五秉正，損實五升正
eq2 = [-5, 15, Fraction(5, 10)]  # Convert 5升 to 升

# Solve using 方程術
# Step 1: Normalize the equations
# Multiply eq1 by 5 (to eliminate fractions) and eq2 by 6
eq1 = [6 * 5, -10 * 5, Fraction(1 * 10 + 8, 10) * 5]
eq2 = [-5 * 6, 15 * 6, Fraction(5, 10) * 6]

# Step 2: Eliminate one variable (下禾)
# Multiply eq1 by 15 and eq2 by 10, then add them to eliminate 下禾
eq1 = [6 * 5 * 15, -10 * 5 * 15, Fraction(1 * 10 + 8, 10) * 5 * 15]
eq2 = [-5 * 6 * 10, 15 * 6 * 10, Fraction(5, 10) * 6 * 10]

# Add the equations
combined = [
    eq1[0] + eq2[0],  # 上禾 coefficient
    eq1[1] + eq2[1],  # 下禾 coefficient (should be 0)
    eq1[2] + eq2[2],  # Constant term
]

# Solve for 上禾 (one 秉 of 上禾)
上禾實 = combined[2] / combined[0]

# Step 3: Solve for 下禾
# Substitute 上禾實 back into one of the original equations
下禾實 = (eq1[2] - eq1[0] * 上禾實) / eq1[1]

# Convert results to 升
a = 1  # 上禾秉
b = 上禾實 * 10  # Convert to 升
c = 1  # 下禾秉
d = 下禾實 * 10  # Convert to 升

# Results
print(f"上禾 {a}秉 實 {b}升")
print(f"下禾 {c}秉 實 {d}升")


"""


### Explanation of the Code:
1. **Equation Setup**: The problem is represented as two equations:
   - `6上禾 - 10下禾 = 1斗8升`
   - `-5上禾 + 15下禾 = 5升`
   These are converted into fractions for precise calculations.

2. **Normalization**: The equations are scaled to eliminate fractions.

3. **Elimination**: Using the method of elimination, one variable (下禾) is removed to solve for the other (上禾).

4. **Back-Substitution**: The value of 上禾 is substituted back into one of the original equations to solve for 下禾.

5. **Conversion**: The results are converted to 升 for the final answer.

### Final Answer:
The results `a`, `b`, `c`, and `d` represent the values for 上禾 and 下禾 in terms of 秉 and 升, respectively.
"""


"""
Variable 'b' has wrong value. Expected: 8, Actual: 11
Variable 'd' has wrong value. Expected: 3, Actual: 24/5"""
