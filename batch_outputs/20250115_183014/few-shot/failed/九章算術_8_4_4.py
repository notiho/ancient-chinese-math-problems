"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
This problem involves solving a system of equations to determine the yield of one bundle of "upper millet" (上禾) and "lower millet" (下禾). The procedure uses ancient Chinese "fangcheng" (方程) methods, which are equivalent to solving linear equations. Below is the Python implementation of the procedure.


"""


from fractions import Fraction

# Problem setup
# 上禾六秉正，下禾一十秉負，損實一斗八升正
eq1_upper_millet = 6  # Coefficient for 上禾 in the first equation
eq1_lower_millet = -10  # Coefficient for 下禾 in the first equation
eq1_loss = 1 * 10 + 8  # 損實一斗八升正 (convert to 升)

# 上禾五秉負，下禾一十五秉正，損實五升正
eq2_upper_millet = -5  # Coefficient for 上禾 in the second equation
eq2_lower_millet = 15  # Coefficient for 下禾 in the second equation
eq2_loss = 5  # 損實五升正

# Solve using the 方程術 (method of elimination)
# Step 1: Eliminate one variable (上禾 or 下禾)
# Multiply the first equation by 5 and the second equation by 6 to align coefficients for 上禾
eq1_upper_millet *= 5
eq1_lower_millet *= 5
eq1_loss *= 5

eq2_upper_millet *= 6
eq2_lower_millet *= 6
eq2_loss *= 6

# Subtract the second equation from the first to eliminate 上禾
lower_millet_coefficient = eq1_lower_millet - eq2_lower_millet
loss_coefficient = eq1_loss - eq2_loss

# Step 2: Solve for 下禾 (lower millet yield per bundle)
lower_millet_yield = Fraction(loss_coefficient, lower_millet_coefficient)

# Step 3: Substitute 下禾 yield back into one of the original equations to solve for 上禾
upper_millet_yield = Fraction(eq1_loss - (eq1_lower_millet * lower_millet_yield), eq1_upper_millet)

# Convert results to 升
a = 1  # Each 上禾 represents 1 bundle
b = upper_millet_yield  # Yield of one 上禾 in 升
c = 1  # Each 下禾 represents 1 bundle
d = lower_millet_yield  # Yield of one 下禾 in 升

# Final results
print(f"上禾 {a}秉 實 {b}升")
print(f"下禾 {c}秉 實 {d}升")


"""


### Explanation of the Code:
1. **Equation Setup**: The problem provides two equations based on the relationships between the bundles of upper millet (上禾), lower millet (下禾), and their respective losses.
2. **Elimination**: The 方程術 method is used to eliminate one variable (上禾 or 下禾) by aligning coefficients and subtracting equations.
3. **Solve for One Variable**: After elimination, the yield of one bundle of 下禾 is calculated.
4. **Substitution**: The yield of 下禾 is substituted back into one of the original equations to solve for 上禾.
5. **Results**: The yields of one bundle of 上禾 and 下禾 are expressed in 升.

### Answer:
The yields of one bundle of 上禾 and 下禾 are calculated as fractions (升) and displayed as the final result.
"""


"""
Variable 'b' has wrong value. Expected: 8, Actual: 16/7
Variable 'd' has wrong value. Expected: 3, Actual: -3/7"""
