"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：雀重 a(=32/19)兩 ，燕重 b(=24/19)兩 。
"""

"""
Suppose there are 5 sparrows and 6 swallows. When placed on a balance, the sparrows are equally heavy, and the swallows are equally light.
When one sparrow and one swallow are exchanged, the balance is perfectly level.
The combined weight of all the sparrows and swallows is 1 jin.
Question: how much does one sparrow and one swallow weigh respectively?

The procedure says: Treat it as a system of equations. Exchange and balance the weights. Each weighs 8 liang.

The detailed procedure for solving systems of equations (方程術) is described, but for simplicity, we will directly solve the equations:
1. Let the weight of one sparrow be *x* and the weight of one swallow be *y*.
2. From the problem, we know:
   - 5x + 6y = 16 (since 1 jin = 16 liang)
   - x - y = 0 (since exchanging one sparrow and one swallow balances the scale).

Answer: The weight of one sparrow is *a*(=32/19) liang, and the weight of one swallow is *b*(=24/19) liang.
"""

from fractions import Fraction

# Let the weight of one sparrow be x and one swallow be y
# Equation 1: 5x + 6y = 16 (1 jin = 16 liang)
# Equation 2: x - y = 0 (balance when exchanged)

# From Equation 2: x = y
# Substitute x = y into Equation 1
# 5x + 6y = 16 becomes 5x + 6x = 16
# Simplify: 11x = 16
x = Fraction(16, 11)  # Weight of one sparrow

# From Equation 2: x = y
y = x  # Weight of one swallow

# Convert to liang (1 jin = 16 liang)
a = x  # Weight of one sparrow
b = y  # Weight of one swallow

a, b
"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
