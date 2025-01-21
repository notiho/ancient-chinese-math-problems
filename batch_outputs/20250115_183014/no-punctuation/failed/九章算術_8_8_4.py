"""
今有五雀六燕集稱之衡雀俱重燕俱輕一雀一燕交而處衡適平并燕雀重一斤問燕雀一枚各重幾何
術曰如方程交易質之各重八兩
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰雀重 a兩 燕重 b兩 
"""

"""
Suppose there are 5 sparrows and 6 swallows placed on a balance. The sparrows are all equally heavy, and the swallows are all equally light.
When one sparrow and one swallow are exchanged, the balance remains level.
The combined weight of all the sparrows and swallows is 1 jin.
Question: how much does one sparrow and one swallow weigh respectively?

The procedure says: Treat this as a system of equations. Exchange and balance them. Each weighs 8 liang.

The procedure for solving systems of equations says:
1. Place the coefficients of the unknowns (sparrows and swallows) in rows, with the total weight on the right-hand side.
2. Use the first row to eliminate the coefficients in the second and third rows.
3. Use the second row to eliminate the coefficient in the third row.
4. Solve for the unknowns by back-substitution.

Answer: the sparrow weighs *a* liang, and the swallow weighs *b* liang.
"""

# Total weight of all sparrows and swallows
total_weight_jin = 1  # 1 jin
total_weight_liang = total_weight_jin * 16  # Convert to liang (1 jin = 16 liang)

# Equation 1: 5 sparrows + 6 swallows = total weight
sparrows_coeff = 5
swallows_coeff = 6
total_weight = total_weight_liang

# Equation 2: 1 sparrow = 1 swallow (balance remains level when exchanged)
# This implies the weights of sparrows and swallows are equal.

# Solving:
# Since sparrows and swallows are equal in weight, we can divide the total weight equally among all 11 birds (5 sparrows + 6 swallows).
total_birds = sparrows_coeff + swallows_coeff
weight_per_bird = Fraction(total_weight, total_birds)

# Assigning weights
a = weight_per_bird  # Weight of one sparrow
b = weight_per_bird  # Weight of one swallow

# Final result
a, b  # a = sparrow weight in liang, b = swallow weight in liang
"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
