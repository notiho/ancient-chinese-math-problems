"""
今有上禾五秉損實一斗一升當下禾七秉上禾七秉損實二斗五升當下禾五秉問上下禾實一秉各幾何
術曰如方程置上禾五秉正下禾七秉負損實一斗一升正次置上禾七秉正下禾五秉負損實二斗五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉 a升 下禾一秉 b升 
"""

"""
Suppose there are 5 bundles of superior grain, which lose 1 dou and 1 sheng in weight, and correspond to 7 bundles of inferior grain.
Similarly, 7 bundles of superior grain lose 2 dou and 5 sheng in weight, and correspond to 5 bundles of inferior grain.
Question: how much does one bundle of superior grain and one bundle of inferior grain weigh?

The procedure says: Treat it as a system of linear equations. 
Set 5 bundles of superior grain as positive, 7 bundles of inferior grain as negative, and the loss of 1 dou and 1 sheng as positive.
Next, set 7 bundles of superior grain as positive, 5 bundles of inferior grain as negative, and the loss of 2 dou and 5 sheng as positive.
Use the positive-negative method to solve.

The procedure for solving linear equations says:
Place the coefficients of the superior grain, middle grain, and inferior grain, along with the total weight, on the right side.
Align the coefficients of the grains on the left side as they appear on the right.
Multiply the first row's superior grain coefficient by the second row's inferior grain coefficient, and divide by the diagonal coefficient.
Repeat for the second row.
For the middle grain, multiply the middle row's coefficient by the left row's inferior grain coefficient, and divide by the diagonal coefficient.
For the inferior grain, divide the remaining coefficients as described.
Finally, calculate the weight of each grain type.

Answer: one bundle of superior grain weighs *a* sheng, and one bundle of inferior grain weighs *b* sheng.
"""

from fractions import Fraction

# 上禾五秉損實一斗一升
上禾1 = 5
下禾1 = -7
損實1 = 10 + 1  # 1斗1升 = 10升 + 1升

# 上禾七秉損實二斗五升
上禾2 = 7
下禾2 = -5
損實2 = 20 + 5  # 2斗5升 = 20升 + 5升

# 方程術解法
# Step 1: Eliminate one variable (下禾)
# Multiply the first equation by 下禾2 and the second equation by 下禾1
eq1_mult = 上禾1 * 下禾2
eq2_mult = 上禾2 * 下禾1
損實1_mult = 損實1 * 下禾2
損實2_mult = 損實2 * 下禾1

# Subtract the equations to eliminate 下禾
上禾系數 = eq1_mult - eq2_mult
損實系數 = 損實1_mult - 損實2_mult

# Solve for 上禾 (weight of one superior grain bundle)
a = Fraction(損實系數, 上禾系數)

# Step 2: Solve for 下禾 (weight of one inferior grain bundle)
# Substitute a back into the first equation
b = Fraction(損實1 - (上禾1 * a), 下禾1)

# Final answer
a = a  # Weight of one superior grain bundle in 升
b = b  # Weight of one inferior grain bundle in 升
"""
"""
