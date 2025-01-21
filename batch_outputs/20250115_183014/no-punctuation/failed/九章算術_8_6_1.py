"""
今有牛五羊二直金十兩牛二羊五直金八兩問牛羊各直金幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰牛 a 直金 b兩 羊 c 直金 d兩 
"""

"""
Suppose there are 5 oxen and 2 sheep worth 10 liang of gold, and 2 oxen and 5 sheep worth 8 liang of gold.
Question: how much is each ox and each sheep worth in gold?

The procedure says: This is like a system of linear equations.

The procedure for solving systems of linear equations says: Place the coefficients of the first equation (upper row) as 3 bundles, the second equation (middle row) as 2 bundles, and the third equation (lower row) as 1 bundle.
Place the total values (right-hand side) as 39 dou on the right side.
For the middle row, place the coefficients as on the right side.
For the upper row, multiply the coefficients of the upper row by the middle row, dividing by the diagonal coefficient, and repeat for the next row, also dividing by the diagonal coefficient.
For the middle row, if the middle coefficient is not exact, multiply by the lower row and divide by the diagonal coefficient.
For the lower row, if the lower coefficient is not exact, take the upper row as the divisor and the lower row as the dividend.
The result is the value of the lower row.
To find the middle row, multiply the diagonal coefficient by the middle row and divide by the lower row's result.
To find the upper row, multiply the diagonal coefficient by the upper row and divide by the middle and lower row results.
The results are the values of each variable.

Answer: Each ox is worth *a* liang of gold, and each sheep is worth *b* liang of gold.
"""

# 牛五羊二直金十兩
牛1 = 5
羊1 = 2
金1 = 10

# 牛二羊五直金八兩
牛2 = 2
羊2 = 5
金2 = 8

# 方程術解法
# Step 1: Eliminate one variable (羊) using the two equations
# Multiply the first equation by 5 (coefficient of 羊 in the second equation)
# Multiply the second equation by 2 (coefficient of 羊 in the first equation)
eq1_multiplied = (5 * 牛1, 5 * 羊1, 5 * 金1)  # (25牛, 10羊, 50金)
eq2_multiplied = (2 * 牛2, 2 * 羊2, 2 * 金2)  # (4牛, 10羊, 16金)

# Subtract the second equation from the first to eliminate 羊
牛_diff = eq1_multiplied[0] - eq2_multiplied[0]  # 25牛 - 4牛 = 21牛
金_diff = eq1_multiplied[2] - eq2_multiplied[2]  # 50金 - 16金 = 34金

# Step 2: Solve for 牛
牛_value = Fraction(金_diff, 牛_diff)  # 牛 = 34金 / 21

# Step 3: Substitute 牛_value back into one of the original equations to solve for 羊
# Using the first equation: 5牛 + 2羊 = 10金
羊_value = Fraction(金1 - (牛1 * 牛_value), 羊1)  # 羊 = (10金 - 5牛) / 2

# Final results
a = 牛_value  # 牛直金 a兩
b = 羊_value  # 羊直金 b兩
"""
Variable 'a' has wrong value. Expected: 1, Actual: 34/21
Variable 'b' has wrong value. Expected: 34/21, Actual: 20/21
Missing variable in output: 'c'
Missing variable in output: 'd'"""
