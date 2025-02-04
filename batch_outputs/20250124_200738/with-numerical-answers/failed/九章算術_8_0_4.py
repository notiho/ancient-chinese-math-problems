"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a(=37/4)斗 ，中禾一秉， b(=17/4)斗 ，下禾一秉， c(=11/4)斗 。
"""

#----- content starts here -----
"""
Suppose there are three types of grain: upper grain (shanghe), middle grain (zhonghe), and lower grain (xiahe).
The problem provides the following information:
- 3 bundles of upper grain, 2 bundles of middle grain, and 1 bundle of lower grain yield 39 dou.
- 2 bundles of upper grain, 3 bundles of middle grain, and 1 bundle of lower grain yield 34 dou.
- 1 bundle of upper grain, 2 bundles of middle grain, and 3 bundles of lower grain yield 26 dou.

Question: How much does one bundle of each type of grain yield?

The procedure for solving systems of equations says:
1. Arrange the equations with the coefficients of the grains on the left and the total dou on the right.
2. Use elimination to simplify the equations:
   - Multiply the rows as needed and subtract to eliminate variables.
   - Continue until only one variable remains in the last row.
3. Solve for the remaining variable in the last row.
4. Substitute back to solve for the other variables.

Answer: One bundle of upper grain yields *a*(=37/4) dou, one bundle of middle grain yields *b*(=17/4) dou, and one bundle of lower grain yields *c*(=11/4) dou.
"""

# Coefficients and totals from the problem
# 3上 + 2中 + 1下 = 39
# 2上 + 3中 + 1下 = 34
# 1上 + 2中 + 3下 = 26

# Step 1: Represent the equations
上禾1, 上禾2, 上禾3 = 3, 2, 1
中禾1, 中禾2, 中禾3 = 2, 3, 2
下禾1, 下禾2, 下禾3 = 1, 1, 3
實1, 實2, 實3 = 39, 34, 26

# Step 2: Eliminate 上禾 (upper grain)
# Multiply the first equation by 2 and the second equation by 3, then subtract
中禾_1 = 2 * 中禾1 - 3 * 中禾2
下禾_1 = 2 * 下禾1 - 3 * 下禾2
實_1 = 2 * 實1 - 3 * 實2

# Multiply the second equation by 1 and the third equation by 2, then subtract
中禾_2 = 中禾2 - 2 * 中禾3
下禾_2 = 下禾2 - 2 * 下禾3
實_2 = 實2 - 2 * 實3

# Step 3: Eliminate 中禾 (middle grain)
# Multiply the first reduced equation by 下禾_2 and the second reduced equation by 下禾_1, then subtract
法 = 下禾_1 * 中禾_2 - 下禾_2 * 中禾_1
實 = 下禾_1 * 實_2 - 下禾_2 * 實_1

# Solve for 下禾 (lower grain)
下禾 = Fraction(實, 法)

# Step 4: Solve for 中禾 (middle grain)
實 = 中禾_1 * 下禾 - 實_1
中禾 = Fraction(實, -下禾_1)

# Step 5: Solve for 上禾 (upper grain)
實 = 上禾1 * 下禾 + 中禾1 * 中禾 - 實1
上禾 = Fraction(實, -上禾1)

# Final results
a = 上禾  # 37/4
b = 中禾  # 17/4
c = 下禾  # 11/4#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 37/4, Actual: 83/12
Variable 'b' has wrong value. Expected: 17/4, Actual: 11/4
Variable 'c' has wrong value. Expected: 11/4, Actual: 17/4"""
