"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
Suppose there are 5 sparrows and 6 swallows. When placed on a balance, all sparrows weigh the same, and all swallows weigh the same. 
When one sparrow and one swallow are placed on opposite sides of the balance, the balance is level. 
The total weight of all sparrows and swallows together is 1 jin (16 liang).

Question: How much does one sparrow and one swallow weigh respectively?

Answer: A sparrow weighs *a* liang, and a swallow weighs *b* liang.
"""

from fractions import Fraction

# Total weight of all sparrows and swallows
total_weight = 16  # in liang (1 jin = 16 liang)

# Let the weight of one sparrow be x liang, and one swallow be y liang
# Equation 1: 5x + 6y = 16
# Equation 2: x = y (from the balance condition where one sparrow equals one swallow in weight)

# Solving the equations:
# From Equation 2, x = y
# Substitute x = y into Equation 1:
# 5x + 6x = 16
# 11x = 16
# x = 16 / 11

# Therefore:
a = Fraction(16, 11)  # Weight of one sparrow in liang
b = Fraction(16, 11)  # Weight of one swallow in liang

a, b  # Output the weights of one sparrow and one swallow respectively
"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
