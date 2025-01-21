"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
To solve this problem, we will follow the ancient Chinese procedure for solving simultaneous linear equations, as described in the problem. Here's the Python implementation:


"""


from fractions import Fraction

# Step 1: Represent the equations
# Equation 1: 3上禾 - 10下禾 = -6 (converted to standard form)
# Equation 2: -2上禾 + 5下禾 = -1 (converted to standard form)

# Coefficients for the equations
# [上禾, 下禾, constant]
eq1 = [3, -10, -6]
eq2 = [-2, 5, -1]

# Step 2: Eliminate one variable (use 上禾 as the pivot)
# Multiply eq1 by 2 and eq2 by 3 to align coefficients of 上禾
eq1_scaled = [2 * x for x in eq1]  # [6, -20, -12]
eq2_scaled = [3 * x for x in eq2]  # [-6, 15, -3]

# Add the scaled equations to eliminate 上禾
combined_eq = [
    eq1_scaled[0] + eq2_scaled[0],  # 上禾 coefficient (should be 0)
    eq1_scaled[1] + eq2_scaled[1],  # 下禾 coefficient
    eq1_scaled[2] + eq2_scaled[2],  # constant
]  # Result: [0, -5, -15]

# Simplify the combined equation
# -5下禾 = -15
下禾實 = Fraction(-15, -5)  # 下禾實 = 3斗

# Step 3: Solve for 上禾實 using 下禾實 in one of the original equations
# Substitute 下禾實 into eq1: 3上禾 - 10下禾 = -6
# 3上禾 - 10(3) = -6
# 3上禾 - 30 = -6
# 3上禾 = 24
上禾實 = Fraction(24, 3)  # 上禾實 = 8斗

# Step 4: Output the results
a = 1  # 上禾秉
b = 上禾實  # 上禾實
c = 1  # 下禾秉
d = 下禾實  # 下禾實

# Final Answer
print(f"上禾 {a}秉 實 {b}斗 ，下禾 {c}秉 實 {d}斗 。")


"""


### Explanation of the Code:
1. **Equation Representation**: The two equations are represented in standard form with coefficients for `上禾`, `下禾`, and the constant term.
2. **Elimination**: The variable `上禾` is eliminated by scaling and combining the equations.
3. **Solving for 下禾實**: After elimination, the value of `下禾實` is calculated.
4. **Substitution**: The value of `下禾實` is substituted back into one of the original equations to solve for `上禾實`.
5. **Output**: The results are displayed as per the problem's requirements.

### Final Answer:
```
上禾 1秉 實 8斗 ，下禾 1秉 實 3斗 。
```
"""


"""
"""
