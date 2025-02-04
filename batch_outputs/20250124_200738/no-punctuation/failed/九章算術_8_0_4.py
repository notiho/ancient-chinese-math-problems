"""
今有上禾三秉中禾二秉下禾一秉實三十九斗上禾二秉中禾三秉下禾一秉實三十四斗上禾一秉中禾二秉下禾三秉實二十六斗問上中下禾實一秉各幾何
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉 a斗 中禾一秉 b斗 下禾一秉 c斗 
"""

#----- content starts here -----
"""
Suppose there are three bundles of upper millet, two bundles of middle millet, and one bundle of lower millet, yielding 39 dou.
There are two bundles of upper millet, three bundles of middle millet, and one bundle of lower millet, yielding 34 dou.
There is one bundle of upper millet, two bundles of middle millet, and three bundles of lower millet, yielding 26 dou.
Question: how much does one bundle of upper, middle, and lower millet yield respectively?

The procedure for solving systems of equations says:
Place the equation for the upper millet (3 bundles), middle millet (2 bundles), and lower millet (1 bundle) yielding 39 dou on the right side.
On the left side, arrange the coefficients of the millet types as in the right equation.
Using the rightmost row, multiply the upper millet row entirely, and divide by the diagonal coefficient.
Repeat for the next row, dividing by the diagonal coefficient.
For the middle millet, take the middle row and multiply it by the remaining left row, dividing by the diagonal coefficient.
For the lower millet, use the upper row as the divisor and the lower row as the dividend.
The result is the yield of lower millet.
To find the middle millet, multiply the middle row by the lower millet yield and divide by the diagonal coefficient.
To find the upper millet, multiply the upper row by the lower millet yield and divide by the diagonal coefficient.
The results are the yields of one bundle of each type of millet.

Answer: one bundle of upper millet yields *a* dou, one bundle of middle millet yields *b* dou, and one bundle of lower millet yields *c* dou.
"""

# Coefficients and totals from the problem
上禾系數 = [3, 2, 1]
中禾系數 = [2, 3, 1]
下禾系數 = [1, 2, 3]
總量 = [39, 34, 26]

# Step 1: Eliminate the first variable (上禾)
# Multiply the second row by 3 and the first row by 2, then subtract
中禾系數 = [3 * 中禾系數[i] - 2 * 上禾系數[i] for i in range(3)]
總量[1] = 3 * 總量[1] - 2 * 總量[0]

# Multiply the third row by 3 and the first row by 1, then subtract
下禾系數 = [3 * 下禾系數[i] - 1 * 上禾系數[i] for i in range(3)]
總量[2] = 3 * 總量[2] - 1 * 總量[0]

# Step 2: Eliminate the second variable (中禾)
# Multiply the third row by the new middle coefficient of the second row, and subtract
下禾系數 = [中禾系數[1] * 下禾系數[i] - 中禾系數[2] * 中禾系數[i] for i in range(3)]
總量[2] = 中禾系數[1] * 総量[2] - 中禾系數[2] * 總量[1]

# Step 3: Solve for 下禾
c = Fraction(總量[2], 下禾系數[2])

# Step 4: Solve for 中禾
b = Fraction(總量[1] - 中禾系數[2] * c, 中禾系數[1])

# Step 5: Solve for 上禾
a = Fraction(總量[0] - 上禾系數[1] * b - 上禾系數[2] * c, 上禾系數[0])

# Results
a, b, c#----- content ends here -----

"""
Code error: name '総量' is not defined"""
