"""
今有上禾三秉中禾二秉下禾一秉實三十九斗上禾二秉中禾三秉下禾一秉實三十四斗上禾一秉中禾二秉下禾三秉實二十六斗問上中下禾實一秉各幾何
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉 a斗 中禾一秉 b斗 下禾一秉 c斗 
"""

#----- content starts here -----
"""
Suppose there are three bundles of upper-grade grain, two bundles of middle-grade grain, and one bundle of lower-grade grain, yielding a total of 39 dou.
There are two bundles of upper-grade grain, three bundles of middle-grade grain, and one bundle of lower-grade grain, yielding a total of 34 dou.
There is one bundle of upper-grade grain, two bundles of middle-grade grain, and three bundles of lower-grade grain, yielding a total of 26 dou.
Question: how much does one bundle of upper-grade, middle-grade, and lower-grade grain yield respectively?

The procedure for solving systems of equations says: Place the equation with three bundles of upper-grade grain, two bundles of middle-grade grain, and one bundle of lower-grade grain yielding 39 dou on the right side.
On the left side, arrange the coefficients of the grains as on the right side.
Using the top row, multiply all rows below it by the coefficient of the upper-grade grain in the top row, and divide by the diagonal coefficient.
Repeat this for the middle-grade grain and lower-grade grain.
For the middle-grade grain, use the middle row to eliminate the coefficients below it.
For the lower-grade grain, use the bottom row to eliminate the coefficients above it.
Finally, solve for the lower-grade grain, then substitute back to solve for the middle-grade grain, and finally for the upper-grade grain.

Answer: one bundle of upper-grade grain yields *a* dou, one bundle of middle-grade grain yields *b* dou, and one bundle of lower-grade grain yields *c* dou.
"""

# Coefficients and constants from the problem
上禾系數 = [3, 2, 1]
中禾系數 = [2, 3, 1]
下禾系數 = [1, 2, 3]
常數 = [39, 34, 26]

# Step 1: Eliminate the upper-grade grain coefficient from the second and third equations
中禾系數 = [中禾系數[i] * 上禾系數[0] - 上禾系數[i] * 中禾系數[0] for i in range(3)]
下禾系數 = [下禾系數[i] * 上禾系數[0] - 上禾系數[i] * 下禾系數[0] for i in range(3)]
常數 = [常數[i] * 上禾系數[0] - 上禾系數[i] * 常數[0] for i in range(3)]

# Step 2: Eliminate the middle-grade grain coefficient from the third equation
下禾系數[2] = 下禾系數[2] * 中禾系數[1] - 中禾系數[2] * 下禾系數[1]
常數[2] = 常數[2] * 中禾系數[1] - 中禾系數[2] * 常數[1]

# Step 3: Solve for the lower-grade grain
c = Fraction(常數[2], 下禾系數[2])

# Step 4: Solve for the middle-grade grain
b = Fraction(常數[1] - 下禾系數[1] * c, 中禾系數[1])

# Step 5: Solve for the upper-grade grain
a = Fraction(常數[0] - 中禾系數[0] * b - 下禾系數[0] * c, 上禾系數[0])

# Results
a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 37/4, Actual: 0
Variable 'b' has wrong value. Expected: 17/4, Actual: 1
Variable 'c' has wrong value. Expected: 11/4, Actual: 19/4"""
