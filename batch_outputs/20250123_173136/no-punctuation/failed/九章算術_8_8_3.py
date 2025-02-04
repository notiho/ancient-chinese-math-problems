"""
今有五雀六燕集稱之衡雀俱重燕俱輕一雀一燕交而處衡適平并燕雀重一斤問燕雀一枚各重幾何
術曰如方程交易質之各重八兩
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰雀重 a兩 燕重 b兩 
"""

"""
Suppose there are 5 sparrows and 6 swallows gathered on a balance. The sparrows are all equally heavy, and the swallows are all equally light.
When one sparrow and one swallow are exchanged, the balance is perfectly level.
The combined weight of the sparrows and swallows is 1 jin (16 liang).
Question: how much does one sparrow and one swallow weigh respectively?

The procedure says: Treat this as a system of equations. Exchange and balance the weights to solve.
Each weighs 8 liang.

The method for solving systems of equations says: Place the coefficients of the variables (weights of sparrows and swallows) in rows, and the total weight on the right-hand side.
Use elimination to simplify the system by multiplying rows and dividing by the coefficients, reducing the system step by step.
The solution is obtained when the coefficients are reduced to 1 for each variable.

Answer: the sparrow weighs *a* liang, and the swallow weighs *b* liang.
"""

# Total weight of sparrows and swallows
total_weight = 16  # 1 jin = 16 liang

# Number of sparrows and swallows
sparrows = 5
swallows = 6

# Equation 1: 5 * sparrow_weight + 6 * swallow_weight = 16
# Equation 2: sparrow_weight = swallow_weight (from balance exchange)

# Let sparrow_weight = x, swallow_weight = y
# From Equation 2: x = y
# Substitute x = y into Equation 1:
# 5x + 6x = 16
# 11x = 16
# x = 16 / 11

# Sparrow weight
a = Fraction(total_weight, sparrows + swallows)

# Swallow weight (equal to sparrow weight)
b = a
"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
