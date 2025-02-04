"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

#----- content starts here -----
"""
Suppose there are three types of grain: upper grain (shanghe), middle grain (zhonghe), and lower grain (xiahe). 
The quantities and total yields are as follows:
- 3 bundles of upper grain, 2 bundles of middle grain, and 1 bundle of lower grain yield 39 dou.
- 2 bundles of upper grain, 3 bundles of middle grain, and 1 bundle of lower grain yield 34 dou.
- 1 bundle of upper grain, 2 bundles of middle grain, and 3 bundles of lower grain yield 26 dou.

Question: How much does one bundle of each type of grain yield?

The procedure for solving simultaneous equations says:
1. Place the equations for the upper, middle, and lower grains on the right-hand side.
2. Multiply the upper grain coefficients in the first equation by the coefficients in the second equation, then divide directly.
3. Repeat for the next equation, dividing directly again.
4. For the middle grain, multiply the coefficients of the middle grain in the second equation by the coefficients in the third equation, then divide directly.
5. For the lower grain, use the upper coefficients as the divisor and the lower coefficients as the dividend. The result is the yield of the lower grain.
6. To find the yield of the middle grain, multiply the divisor by the coefficients of the middle grain in the second equation, then divide by the coefficients of the lower grain.
7. To find the yield of the upper grain, multiply the divisor by the coefficients of the upper grain in the first equation, then divide by the coefficients of the lower and middle grains.

The answer says: one bundle of upper grain yields *a* dou, one bundle of middle grain yields *b* dou, and one bundle of lower grain yields *c* dou.
"""

from fractions import Fraction

# Coefficients of the equations
# 3上禾 + 2中禾 + 1下禾 = 39
# 2上禾 + 3中禾 + 1下禾 = 34
# 1上禾 + 2中禾 + 3下禾 = 26

# Step 1: Define the coefficients and results
上禾1, 中禾1, 下禾1, 實1 = 3, 2, 1, 39
上禾2, 中禾2, 下禾2, 實2 = 2, 3, 1, 34
上禾3, 中禾3, 下禾3, 實3 = 1, 2, 3, 26

# Step 2: Eliminate 上禾 to solve for 中禾 and 下禾
# Multiply the first equation by 2 (coeff of 上禾 in the second equation)
# Multiply the second equation by 3 (coeff of 上禾 in the first equation)
# Subtract the two equations
中禾_new1 = 中禾1 * 上禾2 - 中禾2 * 上禾1
下禾_new1 = 下禾1 * 上禾2 - 下禾2 * 上禾1
實_new1 = 實1 * 上禾2 - 實2 * 上禾1

# Multiply the second equation by 1 (coeff of 上禾 in the third equation)
# Multiply the third equation by 2 (coeff of 上禾 in the second equation)
# Subtract the two equations
中禾_new2 = 中禾2 * 上禾3 - 中禾3 * 上禾2
下禾_new2 = 下禾2 * 上禾3 - 下禾3 * 上禾2
實_new2 = 實2 * 上禾3 - 實3 * 上禾2

# Step 3: Eliminate 中禾 to solve for 下禾
# Multiply the first reduced equation by 中禾_new2
# Multiply the second reduced equation by 中禾_new1
# Subtract the two equations
下禾_final = Fraction(實_new1 * 中禾_new2 - 實_new2 * 中禾_new1, 下禾_new1 * 中禾_new2 - 下禾_new2 * 中禾_new1)

# Step 4: Solve for 中禾
中禾_final = Fraction(實_new1 - 下禾_new1 * 下禾_final, 中禾_new1)

# Step 5: Solve for 上禾
上禾_final = Fraction(實1 - 中禾1 * 中禾_final - 下禾1 * 下禾_final, 上禾1)

# Results
a = 上禾_final
b = 中禾_final
c = 下禾_final#----- content ends here -----

"""
"""
