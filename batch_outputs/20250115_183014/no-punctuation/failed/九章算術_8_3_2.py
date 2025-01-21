"""
今有上禾五秉損實一斗一升當下禾七秉上禾七秉損實二斗五升當下禾五秉問上下禾實一秉各幾何
術曰如方程置上禾五秉正下禾七秉負損實一斗一升正次置上禾七秉正下禾五秉負損實二斗五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 b升 下禾 c秉 d升 
"""

"""
This problem involves solving a system of linear equations using ancient Chinese "fangcheng" (方程) methods. The problem is to determine the yield per sheaf of "upper millet" (上禾) and "lower millet" (下禾) based on given conditions. Below is the translation of the procedure into Python code:


"""


from fractions import Fraction

# Problem setup
# 上禾五秉正，下禾七秉負，損實一斗一升正
上禾1 = 5
下禾1 = -7
損實1 = Fraction(1 * 10 + 1, 10)  # 1斗1升 converted to total 升

# 上禾七秉正，下禾五秉負，損實二斗五升正
上禾2 = 7
下禾2 = -5
損實2 = Fraction(2 * 10 + 5, 10)  # 2斗5升 converted to total 升

# 方程術 (Fangcheng method)
# Step 1: Eliminate one variable
# Multiply the first equation by 7 (to match the coefficient of 上禾 in the second equation)
# Multiply the second equation by 5 (to match the coefficient of 上禾 in the first equation)
上禾系數1 = 上禾1 * 7
下禾系數1 = 下禾1 * 7
損實系數1 = 損實1 * 7

上禾系數2 = 上禾2 * 5
下禾系數2 = 下禾2 * 5
損實系數2 = 損實2 * 5

# Subtract the two equations to eliminate 上禾
下禾系數 = 下禾系數1 - 下禾系數2
損實系數 = 損實系數1 - 損實系數2

# Solve for 下禾實 (yield per sheaf of lower millet)
下禾實 = Fraction(損實系數, 下禾系數)

# Solve for 上禾實 (yield per sheaf of upper millet)
# Substitute 下禾實 back into the first equation
損實1_adjusted = 損實1 - (下禾1 * 下禾實)
上禾實 = Fraction(損實1_adjusted, 上禾1)

# Convert results to 斗 and 升
# 上禾實
上禾斗 = int(上禾實)  # Whole number part in 斗
上禾升 = (上禾實 - 上禾斗) * 10  # Fractional part converted to 升

# 下禾實
下禾斗 = int(下禾實)  # Whole number part in 斗
下禾升 = (下禾實 - 下禾斗) * 10  # Fractional part converted to 升

# Final answer
a = 上禾斗
b = 上禾升
c = 下禾斗
d = 下禾升

print(f"上禾 {a}斗 {b}升 下禾 {c}斗 {d}升")


"""


### Explanation of the Code:
1. **Input Conversion**: The given yields (損實) are converted into fractions (升) for precise calculations.
2. **Fangcheng Method**:
   - The coefficients of the equations are adjusted to eliminate one variable (上禾).
   - The resulting equation is solved for the remaining variable (下禾).
   - The value of the eliminated variable (上禾) is then calculated using the original equations.
3. **Conversion to 斗 and 升**:
   - The results are converted back from fractions into the traditional units of 斗 and 升.
4. **Output**: The results are printed in the required format.

### Answer:
The code will calculate the yield per sheaf of upper millet (上禾) and lower millet (下禾) in terms of 斗 and 升.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 0"""
