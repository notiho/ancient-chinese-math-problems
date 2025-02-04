"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：雀重 a(=32/19)兩 ，燕重 b(=24/19)兩 。
"""

"""
Suppose there are 5 sparrows and 6 swallows, and they are placed on a balance. The sparrows all weigh the same, and the swallows all weigh the same. 
When one sparrow and one swallow are exchanged, the balance is perfectly level. 
The combined weight of all the sparrows and swallows is 1 jin. 
Question: how much does each sparrow and each swallow weigh?

The procedure says: Treat it as a system of linear equations. Solve by substitution and balancing. Each weighs 8 liang.

The answer says: Each sparrow weighs *a*(=32/19) liang, and each swallow weighs *b*(=24/19) liang.
"""

from fractions import Fraction

# Total weight of all sparrows and swallows
total_weight = 16  # 1 jin = 16 liang

# Number of sparrows and swallows
sparrows = 5
swallows = 6

# Let the weight of one sparrow be x and one swallow be y
# Equation 1: 5x + 6y = 16
# Equation 2: x - y = 0 (balance condition when one sparrow is exchanged with one swallow)

# Solve for x and y
# From Equation 2: x = y + Fraction(8, 19) (balance condition)
# Substitute into Equation 1
# 5x + 6y = 16
# 5(y + Fraction(8, 19)) + 6y = 16
# Expand and solve for y
# 5y + Fraction(40, 19) + 6y = 16
# 11y = 16 - Fraction(40, 19)
# 11y = Fraction(304, 19) - Fraction(40, 19)
# 11y = Fraction(264, 19)
# y = Fraction(24, 19)

# Substitute y back into Equation 2 to solve for x
# x = y + Fraction(8, 19)
# x = Fraction(24, 19) + Fraction(8, 19)
# x = Fraction(32, 19)

# Results
a = Fraction(32, 19)  # Weight of one sparrow in liang
b = Fraction(24, 19)  # Weight of one swallow in liang
"""
"""
