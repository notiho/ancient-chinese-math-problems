"""
今有五雀六燕集稱之衡雀俱重燕俱輕一雀一燕交而處衡適平并燕雀重一斤問燕雀一枚各重幾何
術曰如方程交易質之各重八兩
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰雀重 a兩 燕重 b兩 
"""

"""
Suppose there are 5 sparrows and 6 swallows gathered on a balance. The sparrows are all equally heavy, and the swallows are all equally light.
When one sparrow and one swallow are exchanged on the balance, the balance remains level.
The combined weight of all the sparrows and swallows is 1 jin (16 liang).
Question: how much does one sparrow weigh, and how much does one swallow weigh?

The procedure says: Treat this as a system of equations. Exchange and balance them, and each weighs 8 liang.

The answer says: a sparrow weighs *a* liang, and a swallow weighs *b* liang.
"""

# Total weight of all sparrows and swallows
總重 = 16  # 1 jin = 16 liang

# Number of sparrows and swallows
雀數 = 5
燕數 = 6

# When one sparrow is exchanged for one swallow, the balance remains level
# This implies that the weight of one sparrow equals the weight of one swallow.

# Let the weight of one sparrow be x liang and one swallow be y liang.
# From the problem, we have:
# 1. 5x + 6y = 16
# 2. x = y (from the balance condition)

# Substitute x = y into the first equation
# 5x + 6x = 16
# 11x = 16
# x = 16 / 11

a = Fraction(16, 11)  # Weight of one sparrow
b = Fraction(16, 11)  # Weight of one swallow
"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
