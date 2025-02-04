"""
今有五雀六燕集稱之衡雀俱重燕俱輕一雀一燕交而處衡適平并燕雀重一斤問燕雀一枚各重幾何
術曰如方程交易質之各重八兩
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰雀重 a兩 燕重 b兩 
"""

"""
Suppose there are 5 sparrows and 6 swallows gathered on a balance scale. The sparrows are all equally heavy, and the swallows are all equally light. 
When one sparrow and one swallow are exchanged on the scale, the balance is perfectly level. 
The combined weight of all the sparrows and swallows is 1 jin (16 liang). 
Question: How much does one sparrow and one swallow weigh respectively?

The procedure says: Using the method of equations, exchange and balance the weights. Each weighs 8 liang.

The method of equations (方程術) is described in detail, but for this problem, the solution is straightforward.

Answer: A sparrow weighs *a* liang, and a swallow weighs *b* liang.
"""

# Total weight of all sparrows and swallows
總重 = 16  # 1 jin = 16 liang

# Number of sparrows and swallows
雀數 = 5
燕數 = 6

# When one sparrow is exchanged with one swallow, the balance is level
# This implies the difference in weight between a sparrow and a swallow is zero.

# Let the weight of one sparrow be x liang, and the weight of one swallow be y liang.
# We have the following equations:
# 1. 5x + 6y = 16  (total weight)
# 2. x = y          (balance condition)

# Solving the equations:
# From equation 2, substitute x = y into equation 1:
# 5x + 6x = 16
# 11x = 16
# x = 16 / 11

# But this contradicts the balance condition. Correcting interpretation:
# Both are equal directly.

a = Fraction(總重, (雀數 + 燕數))  # Weight of one sparrow
b = a  # Weight of one swallow
"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
