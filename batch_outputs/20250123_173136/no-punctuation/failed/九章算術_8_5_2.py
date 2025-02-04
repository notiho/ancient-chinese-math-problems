"""
今有上禾三秉益實六斗當下禾十秉下禾五秉益實一斗當上禾二秉問上下禾實一秉各幾何
術曰如方程置上禾三秉正下禾一十秉負益實六斗負次置上禾二秉負下禾五秉正益實一斗負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a斗 下禾一秉實 b斗 
"""

"""
Suppose there are 3 bundles of upper millet, which add 6 dou of grain, equivalent to 10 bundles of lower millet.
Additionally, 5 bundles of lower millet add 1 dou of grain, equivalent to 2 bundles of upper millet.
Question: how much grain does one bundle of upper millet and one bundle of lower millet yield?

The procedure says: Treat this as a system of linear equations.
Place 3 bundles of upper millet as positive, 10 bundles of lower millet as negative, and 6 dou of grain as negative.
Next, place 2 bundles of upper millet as negative, 5 bundles of lower millet as positive, and 1 dou of grain as negative.
Use the positive-negative procedure to solve.

The system of equations procedure says:
1. Place the coefficients of upper millet, middle millet (if any), lower millet, and the total grain on the right side.
2. Arrange the rows such that the leftmost non-zero coefficient in each row aligns vertically.
3. Use the first row to eliminate the upper millet term in the second row by multiplying and subtracting.
4. Use the resulting second row to eliminate the lower millet term in the first row.
5. Solve for the lower millet's grain yield by dividing the total grain by its coefficient.
6. Substitute back to solve for the upper millet's grain yield.

Answer: one bundle of upper millet yields *a* dou, and one bundle of lower millet yields *b* dou.
"""

# Define the coefficients of the equations
# Equation 1: 3上禾 - 10下禾 = -6
上禾1 = 3
下禾1 = -10
實1 = -6

# Equation 2: -2上禾 + 5下禾 = -1
上禾2 = -2
下禾2 = 5
實2 = -1

# Step 1: Eliminate the 上禾 term from the second equation
# Multiply the first equation by 2 and the second equation by 3 (to align 上禾 coefficients)
上禾1, 下禾1, 實1 = 2 * 上禾1, 2 * 下禾1, 2 * 實1
上禾2, 下禾2, 實2 = 3 * 上禾2, 3 * 下禾2, 3 * 實2

# Subtract the second equation from the first
下禾 = 下禾1 - 下禾2
實 = 實1 - 實2

# Step 2: Solve for 下禾 (grain yield per bundle of lower millet)
b = Fraction(實, 下禾)

# Step 3: Substitute b into the first equation to solve for 上禾
實1 = -6  # Reset the original value of 實1
實_upper = 實1 - (-10 * b)  # Substitute b into the first equation
a = Fraction(實_upper, 3)

# Results
a, b  # a is the grain yield per bundle of upper millet, b is the grain yield per bundle of lower millet
"""
Variable 'a' has wrong value. Expected: 8, Actual: -8/7
Variable 'b' has wrong value. Expected: 3, Actual: 9/35"""
