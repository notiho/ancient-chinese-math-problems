"""
今有上禾六秉損實一斗八升當下禾一十秉下禾十五秉損實五升當上禾五秉問上下禾實一秉各幾何
術曰如方程置上禾六秉正下禾一十秉負損實一斗八升正次置上禾五秉負下禾一十五秉正損實五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a升 下禾一秉實 b升 
"""

"""
Suppose there are 6 bundles of superior millet (上禾), with a loss of 1 dou and 8 sheng in total. 
There are 10 bundles of inferior millet (下禾). 
Additionally, there are 15 bundles of inferior millet (下禾) with a loss of 5 sheng in total, corresponding to 5 bundles of superior millet (上禾). 
Question: How much grain does each bundle of superior millet and inferior millet yield?

The procedure says: Treat this as a system of linear equations.
Place 6 bundles of superior millet as positive, 10 bundles of inferior millet as negative, and the loss of 1 dou and 8 sheng as positive.
Next, place 5 bundles of superior millet as negative, 15 bundles of inferior millet as positive, and the loss of 5 sheng as positive.
Use the method of solving linear equations to find the result.

The method of solving linear equations says:
1. Place the coefficients of superior millet, middle millet, and inferior millet on the left, and the total yield on the right.
2. Multiply the rows and divide directly to eliminate variables, proceeding step by step.
3. Solve for the remaining variables by substitution.

The answer says: Each bundle of superior millet yields *a* sheng, and each bundle of inferior millet yields *b* sheng.
"""

from fractions import Fraction

# Convert all units to sheng (1 dou = 10 sheng)
損實1 = 1 * 10 + 8  # 1 dou 8 sheng = 18 sheng
損實2 = 5  # 5 sheng

# Coefficients for the equations
# Equation 1: 6上禾 - 10下禾 = 18
# Equation 2: -5上禾 + 15下禾 = 5
上禾1 = 6
下禾1 = -10
常數1 = 18

上禾2 = -5
下禾2 = 15
常數2 = 5

# Step 1: Eliminate one variable (e.g., 上禾)
# Multiply the first equation by 5 and the second equation by 6 to align 上禾 coefficients
eq1_上禾 = 5 * 上禾1
eq1_下禾 = 5 * 下禾1
eq1_常數 = 5 * 常數1

eq2_上禾 = 6 * 上禾2
eq2_下禾 = 6 * 下禾2
eq2_常數 = 6 * 常數2

# Add the two equations to eliminate 上禾
下禾系數 = eq1_下禾 + eq2_下禾
常數和 = eq1_常數 + eq2_常數

# Solve for 下禾 (1 bundle of inferior millet)
下禾實 = Fraction(常數和, 下禾系數)

# Step 2: Substitute 下禾實 back into one of the original equations to solve for 上禾
# Use the first equation: 6上禾 - 10下禾 = 18
上禾實 = Fraction(常數1 - 下禾1 * 下禾實, 上禾1)

# Convert results to sheng
a = 上禾實  # Each bundle of superior millet
b = 下禾實  # Each bundle of inferior millet
"""
"""
