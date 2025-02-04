"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
Suppose there are 5 sparrows and 6 swallows. When placed on a balance, the sparrows are heavier, and the swallows are lighter. 
If one sparrow and one swallow are placed together, the balance is even. 
The total weight of all sparrows and swallows together is 1 jin (16 liang).

Question: How much does one sparrow and one swallow weigh?

Answer: A sparrow weighs *a* liang, and a swallow weighs *b* liang.
"""

from fractions import Fraction

# Total weight of all sparrows and swallows
total_weight = 16  # in liang (1 jin = 16 liang)

# Let the weight of one sparrow be x (in liang)
# Let the weight of one swallow be y (in liang)

# Equation 1: 5x + 6y = 16
# Equation 2: x + y = 2 (since one sparrow and one swallow balance the scale)

# Solve for x and y
x_plus_y = 2
x = Fraction(x_plus_y * 6 - total_weight, 1)

"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
