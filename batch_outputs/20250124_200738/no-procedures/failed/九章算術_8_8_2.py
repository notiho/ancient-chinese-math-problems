"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
荅曰：雀重 a兩 ，燕重 b兩 。
"""

#----- content starts here -----
"""
Suppose there are 5 sparrows and 6 swallows. When placed on a balance, the sparrows are heavier, and the swallows are lighter. 
When one sparrow and one swallow are exchanged, the balance becomes even. 
The total weight of all the sparrows and swallows together is 1 jin (16 liang).

Question: How much does one sparrow and one swallow weigh respectively?

Answer: A sparrow weighs *a* liang, and a swallow weighs *b* liang.
"""

from fractions import Fraction

# Total weight of all sparrows and swallows
total_weight = 16  # 1 jin = 16 liang

# Let the weight of one sparrow be x liang, and the weight of one swallow be y liang.
# There are 5 sparrows and 6 swallows, so:
# 5x + 6y = 16  (Equation 1)

# When one sparrow and one swallow are exchanged, the balance becomes even.
# This means the difference in weight between one sparrow and one swallow is equal to the difference in the total number of sparrows and swallows:
# x - y = (6 - 5) = 1  (Equation 2)

# Solve the system of equations:
# From Equation 2: x = y + 1
# Substitute x into Equation 1:
# 5(y + 1) + 6y = 16
# 5y + 5 + 6y = 16
# 11y + 5 = 16
# 11y = 11
# y = 1

# Substitute y = 1 into x = y + 1:
# x = 1 + 1 = 2

# Results:
a = Fraction(2)  # Weight of one sparrow
b = Fraction(1)  # Weight of one swallow

# Output:
a, b  # (Sparrow weight, Swallow weight)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 2
Variable 'b' has wrong value. Expected: 24/19, Actual: 1"""
