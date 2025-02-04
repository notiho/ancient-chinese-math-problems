"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""
Suppose there are three types of grain: upper grain (shanghe), middle grain (zhonghe), and lower grain (xiahe). 
The quantities of grain bundles and their total yields are as follows:
- 3 bundles of upper grain, 2 bundles of middle grain, and 1 bundle of lower grain yield 39 dou.
- 2 bundles of upper grain, 3 bundles of middle grain, and 1 bundle of lower grain yield 34 dou.
- 1 bundle of upper grain, 2 bundles of middle grain, and 3 bundles of lower grain yield 26 dou.

Question: How much does one bundle of upper grain, middle grain, and lower grain yield respectively?

The procedure for solving equations says:
1. Arrange the equations such that the coefficients of the grains and their total yields are aligned.
2. Use elimination to simplify the equations:
   - Multiply the first equation by the coefficient of the upper grain in the second equation, and subtract.
   - Repeat for the third equation.
3. Use the resulting equations to solve for the lower grain yield.
4. Substitute the lower grain yield into the simplified equations to solve for the middle grain yield.
5. Substitute both the lower and middle grain yields into the original equations to solve for the upper grain yield.

Answer: One bundle of upper grain yields *a* dou, one bundle of middle grain yields *b* dou, and one bundle of lower grain yields *c* dou.
"""

# Coefficients and total yields from the problem
上禾1, 中禾1, 下禾1, 總1 = 3, 2, 1, 39
上禾2, 中禾2, 下禾2, 總2 = 2, 3, 1, 34
上禾3, 中禾3, 下禾3, 總3 = 1, 2, 3, 26

# Step 1: Eliminate 上禾 (upper grain) from the second and third equations
# Multiply the first equation by 上禾2 and subtract from the second equation
中禾_新2 = 中禾2 * 上禾1 - 中禾1 * 上禾2
下禾_新2 = 下禾2 * 上禾1 - 下禾1 * 上禾2
總_新2 = 總2 * 上禾1 - 總1 * 上禾2

# Multiply the first equation by 上禾3 and subtract from the third equation
中禾_新3 = 中禾3 * 上禾1 - 中禾1 * 上禾3
下禾_新3 = 下禾3 * 上禾1 - 下禾1 * 上禾3
總_新3 = 總3 * 上禾1 - 總1 * 上禾3

# Step 2: Eliminate 中禾 (middle grain) from the third equation
# Multiply the new second equation by 中禾_新3 and subtract from the new third equation
下禾_最終 = 下禾_新3 * 中禾_新2 - 下禾_新2 * 中禾_新3
總_最終 = 總_新3 * 中禾_新2 - 總_新2 * 中禾_新3

# Solve for 下禾 (lower grain)
c = Fraction(總_最終, 下禾_最終)

# Step 3: Solve for 中禾 (middle grain) using the new second equation
總_新2 -= 下禾_新2 * c
b = Fraction(總_新2, 中禾_新2)

# Step 4: Solve for 上禾 (upper grain) using the first equation
總1 -= 中禾1 * b + 下禾1 * c
a = Fraction(總1, 上禾1)

# Final results
a, b, c  # 上禾一秉 yields a斗, 中禾一秉 yields b斗, 下禾一秉 yields c斗
"""
"""
