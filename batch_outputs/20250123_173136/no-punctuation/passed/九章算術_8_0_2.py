"""
今有上禾三秉中禾二秉下禾一秉實三十九斗上禾二秉中禾三秉下禾一秉實三十四斗上禾一秉中禾二秉下禾三秉實二十六斗問上中下禾實一秉各幾何
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉 a斗 中禾一秉 b斗 下禾一秉 c斗 
"""

"""
Suppose there are three bundles of upper-grade grain, two bundles of middle-grade grain, and one bundle of lower-grade grain, yielding a total of 39 dou.
There are two bundles of upper-grade grain, three bundles of middle-grade grain, and one bundle of lower-grade grain, yielding a total of 34 dou.
There is one bundle of upper-grade grain, two bundles of middle-grade grain, and three bundles of lower-grade grain, yielding a total of 26 dou.
Question: how much does one bundle of upper-grade, middle-grade, and lower-grade grain yield respectively?

The procedure for solving systems of equations says:
Place the first equation (three bundles of upper-grade grain, two bundles of middle-grade grain, one bundle of lower-grade grain, yielding 39 dou) on the right side.
On the left side, arrange the coefficients of the middle-grade grain and lower-grade grain as in the right side.
Using the first row, multiply the upper-grade grain coefficient across the second row, then divide by the diagonal coefficient.
Repeat this for the third row.
For the middle-grade grain, multiply the middle-grade coefficient across the third row and divide by the diagonal coefficient.
For the lower-grade grain, use the remaining coefficients to solve for the lower-grade grain yield.
Finally, back-substitute to solve for the middle-grade and upper-grade grain yields.

Answer: one bundle of upper-grade grain yields *a* dou, one bundle of middle-grade grain yields *b* dou, and one bundle of lower-grade grain yields *c* dou.
"""

# Coefficients of the equations
# 3 bundles of upper-grade, 2 bundles of middle-grade, 1 bundle of lower-grade = 39 dou
# 2 bundles of upper-grade, 3 bundles of middle-grade, 1 bundle of lower-grade = 34 dou
# 1 bundle of upper-grade, 2 bundles of middle-grade, 3 bundles of lower-grade = 26 dou

# Equation coefficients
上禾系數 = [3, 2, 1]
中禾系數 = [2, 3, 2]
下禾系數 = [1, 1, 3]
實 = [39, 34, 26]

# Elimination process
# Step 1: Eliminate the upper-grade grain coefficient from the second and third rows
中禾系數[1] = 中禾系數[1] * 上禾系數[0] - 上禾系數[1] * 中禾系數[0]
下禾系數[1] = 下禾系數[1] * 上禾系數[0] - 上禾系數[1] * 下禾系數[0]
實[1] = 實[1] * 上禾系數[0] - 上禾系數[1] * 實[0]

中禾系數[2] = 中禾系數[2] * 上禾系數[0] - 上禾系數[2] * 中禾系數[0]
下禾系數[2] = 下禾系數[2] * 上禾系數[0] - 上禾系數[2] * 下禾系數[0]
實[2] = 實[2] * 上禾系數[0] - 上禾系數[2] * 實[0]

# Step 2: Eliminate the middle-grade grain coefficient from the third row
下禾系數[2] = 下禾系數[2] * 中禾系數[1] - 中禾系數[2] * 下禾系數[1]
實[2] = 實[2] * 中禾系數[1] - 中禾系數[2] * 實[1]

# Step 3: Solve for the lower-grade grain yield
c = Fraction(實[2], 下禾系數[2])

# Step 4: Back-substitute to solve for the middle-grade grain yield
b = Fraction(實[1] - 下禾系數[1] * c, 中禾系數[1])

# Step 5: Back-substitute to solve for the upper-grade grain yield
a = Fraction(實[0] - 中禾系數[0] * b - 下禾系數[0] * c, 上禾系數[0])

# Results
a, b, c  # Upper-grade, middle-grade, and lower-grade grain yields per bundle
"""
"""
