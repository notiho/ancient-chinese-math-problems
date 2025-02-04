"""
今有上禾三秉益實六斗當下禾十秉下禾五秉益實一斗當上禾二秉問上下禾實一秉各幾何
術曰如方程置上禾三秉正下禾一十秉負益實六斗負次置上禾二秉負下禾五秉正益實一斗負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a斗 下禾一秉實 b斗 
"""

"""
Suppose there are three bundles of upper millet, which yield an additional 6 dou of grain, equivalent to ten bundles of lower millet.
Additionally, five bundles of lower millet yield an additional 1 dou of grain, equivalent to two bundles of upper millet.
Question: how much grain does one bundle of upper millet and one bundle of lower millet yield?

The procedure says: Treat this as a system of linear equations.
Place 3 bundles of upper millet as positive, 10 bundles of lower millet as negative, and 6 dou of grain as negative.
Next, place 2 bundles of upper millet as negative, 5 bundles of lower millet as positive, and 1 dou of grain as negative.
Use the method of solving systems of equations.

The method for solving systems of equations says: Arrange the coefficients of the equations, with the right-hand side values (grain) placed on the right.
The left-hand side coefficients (millet bundles) are arranged in rows.
Multiply the first row by the coefficient of the second row's leading term, and divide by the diagonal term.
Repeat for the second row, and so on.
For the middle row, if it does not divide evenly, multiply it by the left row's leading term and divide by the diagonal term.
The remaining terms are used to calculate the grain yield per bundle.
Finally, calculate the yield for the upper millet and lower millet using the derived values.

The answer says: one bundle of upper millet yields *a* dou, and one bundle of lower millet yields *b* dou.
"""

from fractions import Fraction

# Equation 1: 3 bundles of upper millet - 10 bundles of lower millet = -6 dou
# Equation 2: -2 bundles of upper millet + 5 bundles of lower millet = -1 dou

# Coefficients for the equations
上禾系數1 = 3
下禾系數1 = -10
實1 = -6

上禾系數2 = -2
下禾系數2 = 5
實2 = -1

# Step 1: Eliminate one variable (e.g., 下禾)
# Multiply the first equation by 5 and the second equation by 10 to align 下禾 coefficients
上禾系數1 *= 5
下禾系數1 *= 5
實1 *= 5

上禾系數2 *= 10
下禾系數2 *= 10
實2 *= 10

# Subtract the second equation from the first to eliminate 下禾
上禾系數 = 上禾系數1 - 上禾系數2
實 = 實1 - 实2

# Solve for 上禾
上禾實 = Fraction(實, 上禾系數)

# Step 2: Solve for 下禾 using the first equation
下禾實 = Fraction(實1 - 上禾系數1 * 上禾實, 下禾系數1)

# Results
a = 上禾實
b = 下禾實
"""
Code error: name '实2' is not defined"""
