"""
今有五雀六燕集稱之衡雀俱重燕俱輕一雀一燕交而處衡適平并燕雀重一斤問燕雀一枚各重幾何
術曰如方程交易質之各重八兩
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰雀重 a兩 燕重 b兩 
"""

#----- content starts here -----
"""
Suppose there are 5 sparrows and 6 swallows placed on a balance. The sparrows are all equally heavy, and the swallows are all equally light.
When one sparrow and one swallow are exchanged on the balance, it becomes perfectly balanced.
The combined weight of all the sparrows and swallows is 1 jin (16 liang).
Question: how much does one sparrow and one swallow weigh respectively?

The procedure says: Treat it as a system of equations. Exchange and balance the weights. Each weighs 8 liang.

The answer says: the sparrow weighs *a* liang, and the swallow weighs *b* liang.
"""

# Total weight of 5 sparrows and 6 swallows
total_weight = 16  # in liang

# Let the weight of one sparrow be x liang and one swallow be y liang
# Equation 1: 5x + 6y = 16
# Equation 2: x = y (from the balance when one sparrow and one swallow are exchanged)

# From Equation 2, x = y
x = Fraction(total_weight, 2) / (5 + 6)

# Sparrow weight (a)
a = x

# Swallow weight (b)
b = x#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 8/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 8/11"""
