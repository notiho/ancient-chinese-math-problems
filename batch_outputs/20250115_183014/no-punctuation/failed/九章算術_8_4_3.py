"""
今有上禾六秉損實一斗八升當下禾一十秉下禾十五秉損實五升當上禾五秉問上下禾實一秉各幾何
術曰如方程置上禾六秉正下禾一十秉負損實一斗八升正次置上禾五秉負下禾一十五秉正損實五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b升 下禾 c秉 實 d升 
"""

"""
This is a complex problem involving a system of linear equations, solved using ancient Chinese "fangcheng" (matrix-like) methods. Below is the Python implementation of the procedure described in the problem:


"""


from fractions import Fraction

# Problem setup
# 上禾六秉損實一斗八升
上禾_1 = 6
下禾_1 = 10
損實_1 = 1 * 10 + 8  # Convert 1斗8升 to total 升

# 下禾十五秉損實五升
上禾_2 = 5
下禾_2 = 15
損實_2 = 5  # Already in 升

# 方程術
# Step 1: Normalize the equations
# Equation 1: 6上禾 - 10下禾 = 1斗8升 (損實_1)
# Equation 2: -5上禾 + 15下禾 = 5升 (損實_2)

# Step 2: Eliminate one variable (use 上禾 as the pivot)
# Multiply Equation 1 by 5 and Equation 2 by 6 to align coefficients of 上禾
eq1_mult = 5
eq2_mult = 6

上禾_elim = eq1_mult * 上禾_1 + eq2_mult * 上禾_2  # This should cancel out 上禾
下禾_elim = eq1_mult * 下禾_1 + eq2_mult * 下禾_2
損實_elim = eq1_mult * 損實_1 + eq2_mult * 損實_2

# Step 3: Solve for 下禾
下禾實 = Fraction(損實_elim, 下禾_elim)

# Step 4: Back-substitute to find 上禾
上禾實 = Fraction(損實_1 - 下禾_1 * 下禾實, 上禾_1)

# Convert results to appropriate units
a = 上禾實.numerator // 10  # 上禾斗
b = 上禾實.numerator % 10  # 上禾升
c = 下禾實.numerator // 10  # 下禾斗
d = 下禾實.numerator % 10  # 下禾升

# Answer
print(f"上禾 {a}斗 {b}升")
print(f"下禾 {c}斗 {d}升")


"""


### Explanation of the Code:
1. **Input Setup**: The problem provides two equations involving the number of bundles of 上禾 (upper millet) and 下禾 (lower millet), along with their respective losses in volume.
2. **Normalization**: The equations are normalized to align the coefficients of 上禾 for elimination.
3. **Elimination**: The 上禾 variable is eliminated by multiplying the equations by appropriate factors and adding them.
4. **Solve for 下禾**: After elimination, the remaining equation is solved for 下禾.
5. **Back-substitution**: The value of 下禾 is substituted back into one of the original equations to solve for 上禾.
6. **Unit Conversion**: The results are converted into the appropriate units of 斗 (dou) and 升 (sheng).

### Note:
This implementation assumes the procedure described in the problem is followed exactly. If there are any ambiguities or additional constraints, adjustments may be needed.
"""


"""
Variable 'b' has wrong value. Expected: 8, Actual: 1
Variable 'c' has wrong value. Expected: 1, Actual: 0
Variable 'd' has wrong value. Expected: 3, Actual: 6"""
