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
Place the equation for the first row (3 upper-grade, 2 middle-grade, 1 lower-grade, total 39 dou) on the right.
For the second row, align the middle-grade grain under the upper-grade grain, and place it as the right-hand side.
Multiply the upper-grade grain in the first row by the upper-grade grain in the second row, and divide by the diagonal.
Then multiply by the next row and divide by the diagonal again.
For the middle-grade grain, multiply the middle-grade grain in the second row by the lower-grade grain in the third row, and divide by the diagonal.
For the lower-grade grain, use the upper-grade grain as the divisor and the lower-grade grain as the dividend.
The result is the yield of the lower-grade grain.
To find the middle-grade grain, multiply the divisor by the middle-grade grain in the second row and divide by the lower-grade grain.
The remainder divided by the middle-grade grain gives the yield of the middle-grade grain.
To find the upper-grade grain, multiply the divisor by the upper-grade grain in the first row and divide by the lower-grade and middle-grade grain.
The remainder divided by the upper-grade grain gives the yield of the upper-grade grain.
The results are obtained according to the procedure, and each yields one dou.

Answer: one bundle of upper-grade grain yields *a* dou, one bundle of middle-grade grain yields *b* dou, and one bundle of lower-grade grain yields *c* dou.
"""

# 上禾、中禾、下禾的秉數和總量
方程1 = [3, 2, 1, 39]  # 上禾3秉, 中禾2秉, 下禾1秉, 總量39斗
方程2 = [2, 3, 1, 34]  # 上禾2秉, 中禾3秉, 下禾1秉, 總量34斗
方程3 = [1, 2, 3, 26]  # 上禾1秉, 中禾2秉, 下禾3秉, 總量26斗

# 消去下禾
法1 = 方程1[0]  # 上禾系數
法2 = 方程2[0]  # 上禾系數
倍數 = Fraction(法2, 法1)
方程2 = [方程2[i] - 倍數 * 方程1[i] for i in range(4)]

法1 = 方程1[0]  # 上禾系數
法3 = 方程3[0]  # 上禾系數
倍數 = Fraction(法3, 法1)
方程3 = [方程3[i] - 倍數 * 方程1[i] for i in range(4)]

# 消去中禾
法2 = 方程2[1]  # 中禾系數
法3 = 方程3[1]  # 中禾系數
倍數 = Fraction(法3, 法2)
方程3 = [方程3[i] - 倍數 * 方程2[i] for i in range(4)]

# 求下禾
c = Fraction(方程3[3], 方程3[2])

# 求中禾
法2 = 方程2[1]  # 中禾系數
實 = 方程2[3] - 方程2[2] * c
b = Fraction(實, 法2)

# 求上禾
法1 = 方程1[0]  # 上禾系數
實 = 方程1[3] - 方程1[1] * b - 方程1[2] * c
a = Fraction(實, 法1)

a, b, c  # 上禾、中禾、下禾每秉的斗數
"""
"""
