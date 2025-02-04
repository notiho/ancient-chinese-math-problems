"""
今有黃金九枚，白銀一十一枚，稱之重適等。交易其一，金輕十三兩。問︰金、銀一枚各重幾何？
荅曰：金重 a斤 ，銀重 b斤 。
"""

#----- content starts here -----
"""
Suppose there are 9 pieces of gold and 11 pieces of silver, and their total weight is equal. 
If one piece of gold is exchanged for one piece of silver, the gold becomes lighter by 13 liang.
Question: How much does one piece of gold and one piece of silver weigh?

Answer: One piece of gold weighs *a* jin, and one piece of silver weighs *b* jin.
"""

# Let the weight of one piece of gold be x jin, and one piece of silver be y jin.
# Total weight of gold = 9x
# Total weight of silver = 11y
# Since their total weights are equal:
# 9x = 11y  ---- (1)

# When one piece of gold is exchanged for one piece of silver, the gold becomes lighter by 13 liang (1 jin = 16 liang):
# x - y = 13 / 16  ---- (2)

# Solve the system of equations (1) and (2):
# From (1): x = (11/9)y
# Substitute x into (2): (11/9)y - y = 13/16
# Simplify: (2/9)y = 13/16
# Solve for y: y = (13/16) * (9/2) = 117 / 32

# Substitute y back into x = (11/9)y:
# x = (11/9) * (117/32) = 429 / 96

from fractions import Fraction

# Weight of one piece of silver
b = Fraction(117, 32)  # in jin

# Weight of one piece of gold
a = Fraction(429, 96)  # in jin

a, b  # Output the weights of gold and silver#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 143/64, Actual: 143/32
Variable 'b' has wrong value. Expected: 117/64, Actual: 117/32"""
