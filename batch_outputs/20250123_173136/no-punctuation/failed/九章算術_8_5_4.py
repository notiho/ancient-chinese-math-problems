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
Set up the equations as follows:
- 3 bundles of upper millet (positive), 10 bundles of lower millet (negative), and 6 dou of grain (negative).
- 2 bundles of upper millet (negative), 5 bundles of lower millet (positive), and 1 dou of grain (negative).
Use the method of solving linear equations to find the solution.

The procedure for solving linear equations says:
1. Place the coefficients of the upper millet, middle millet (if any), lower millet, and the grain on the right-hand side.
2. Arrange the coefficients in rows, with the right-hand side values in the last column.
3. Use elimination to solve for the unknowns:
   - Multiply rows to align coefficients and eliminate variables step by step.
   - Solve for the remaining variables using substitution or back-substitution.
4. The results for each variable correspond to the grain yield per bundle.

Answer: one bundle of upper millet yields *a* dou, and one bundle of lower millet yields *b* dou.
"""

# Coefficients for the first equation: 3上禾 - 10下禾 = -6斗
上禾1 = 3
下禾1 = -10
實1 = -6

# Coefficients for the second equation: -2上禾 + 5下禾 = -1斗
上禾2 = -2
下禾2 = 5
實2 = -1

# Eliminate one variable (下禾) using the two equations
# Multiply the first equation by 5 and the second equation by 10 to align 下禾 coefficients
上禾1 *= 5
下禾1 *= 5
實1 *= 5

上禾2 *= 10
下禾2 *= 10
實2 *= 10

# Subtract the second equation from the first to eliminate 下禾
上禾 = 上禾1 - 上禾2
實 = 實1 - 实2

# Solve for 上禾 (grain yield per bundle of upper millet)
a = Fraction(實, 上禾)

# Substitute a back into one of the original equations to solve for 下禾
實1 = Fraction(實1, 5)  # Restore original scaling
下禾 = (實1 - 上禾1 * a) / 下禾1

b = 下禾
"""
Code error: name '实2' is not defined"""
