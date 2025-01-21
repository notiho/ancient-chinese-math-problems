"""
今有上禾三秉益實六斗當下禾十秉下禾五秉益實一斗當上禾二秉問上下禾實一秉各幾何
術曰如方程置上禾三秉正下禾一十秉負益實六斗負次置上禾二秉負下禾五秉正益實一斗負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b斗 下禾 c秉 實 d斗 
"""

This is a classic simultaneous equations problem from ancient Chinese mathematics, solved using a method similar to Gaussian elimination. Let's break it down step by step and encode it in Python.

"""
Suppose there are 3 bundles of upper millet, which, when supplemented with 6 dou of grain, are equivalent to 10 bundles of lower millet.
Similarly, 5 bundles of lower millet, when supplemented with 1 dou of grain, are equivalent to 2 bundles of upper millet.
Question: How much grain does one bundle of upper millet and one bundle of lower millet yield?

The procedure says: Arrange the equations as follows:
- Place 3 bundles of upper millet as positive, 10 bundles of lower millet as negative, and 6 dou of grain as negative.
- Place 2 bundles of upper millet as negative, 5 bundles of lower millet as positive, and 1 dou of grain as negative.
Use the positive-negative method to solve.

The procedure for solving simultaneous equations says:
- Place the coefficients of upper millet, middle millet, and lower millet, along with the total grain, on the right side.
- Multiply rows to eliminate variables step by step, dividing by the leading coefficient.
- Solve for each variable by substitution.

Answer: *a* bundles of upper millet yield *b* dou, and *c* bundles of lower millet yield *d* dou.
"""

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 3 bundles of upper millet - 10 bundles of lower millet = -6 dou
上禾1 = 3
下禾1 = -10
實1 = -6

# Equation 2: -2 bundles of upper millet + 5 bundles of lower millet = -1 dou
上禾2 = -2
下禾2 = 5
實2 = -1

# Step 1: Eliminate one variable (e.g., 上禾) using the two equations
# Multiply the first equation by 2 and the second by 3 to align the coefficients of 上禾
上禾1, 下禾1, 實1 = 2 * 上禾1, 2 * 下禾1, 2 * 實1
上禾2, 下禾2, 實2 = 3 * 上禾2, 3 * 下禾2, 3 * 實2

# Subtract the second equation from the first to eliminate 上禾
下禾 = 下禾1 - 下禾2
實 = 實1 - 實2

# Step 2: Solve for 下禾 (lower millet)
下禾實 = Fraction(實, 下禾)

# Step 3: Substitute 下禾實 back into one of the original equations to solve for 上禾 (upper millet)
實1 = Fraction(實1, 2)  # Revert to the original scale of the first equation
上禾實 = Fraction(實1 - 下禾1 * 下禾實, 上禾1)

# Results
a = 1  # One bundle of upper millet
b = 上禾實  # Grain yield per bundle of upper millet
c = 1  # One bundle of lower millet
d = 下禾實  # Grain yield per bundle of lower millet

a, b, c, d
"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
