"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
Suppose there are 5 sparrows and 6 swallows. When placed on a balance, the sparrows are all equally heavy, and the swallows are all equally light.
When one sparrow and one swallow are exchanged, the balance becomes even.
The combined weight of all the sparrows and swallows is 1 jin.
Question: how much does each sparrow and each swallow weigh?

The procedure says: Treat it as a system of equations. Exchange and balance the weights. Each weighs 8 liang.

The answer says: each sparrow weighs *a* liang, and each swallow weighs *b* liang.
"""

# Total weight of all sparrows and swallows
總重 = 16  # 1斤 = 16兩

# Number of sparrows and swallows
雀數 = 5
燕數 = 6

# Let the weight of one sparrow be x liang, and one swallow be y liang
# Equation 1: 5x + 6y = 16
# Equation 2: x - y = 0 (from the balance condition when one sparrow and one swallow are exchanged)

# Solving the equations:
# From Equation 2: x = y
x = Fraction(總重, (雀數 + 燕數))  # x = y = total weight divided by total number of birds
y = x

# Results
a = x  # Weight of one sparrow
b = y  # Weight of one swallow
"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
