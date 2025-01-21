"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
Suppose there are 5 sparrows and 6 swallows. Together, they balance a scale. Each sparrow has the same weight, and each swallow has the same weight. 
When one sparrow and one swallow are exchanged, the scale remains balanced. 
The combined weight of all sparrows and swallows is 1 jin (16 liang). 
Question: how much does each sparrow and each swallow weigh?

The procedure says: Treat it as a system of equations. Exchange and balance them. Each weighs 8 liang.

The answer says: Each sparrow weighs *a* liang, and each swallow weighs *b* liang.
"""

# Total weight in jin (converted to liang)
總重 = 16  # 1 jin = 16 liang

# Number of sparrows and swallows
雀數 = 5
燕數 = 6

# Let each sparrow weigh `雀重` liang and each swallow weigh `燕重` liang.
# Equation 1: 5 * 雀重 + 6 * 燕重 = 16
# Equation 2: 雀重 = 燕重 (from the balance condition)

# Solving the equations:
# Substitute 雀重 = 燕重 into Equation 1:
# 5 * 燕重 + 6 * 燕重 = 16
# 11 * 燕重 = 16
燕重 = Fraction(16, 11)

# Substitute 燕重 back into 雀重 = 燕重
雀重 = 燕重

# Results
a = 雀重
b = 燕重
"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
