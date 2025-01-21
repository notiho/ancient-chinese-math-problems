"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a(=60000/11)錢 ，牛價 b(=20000/11)錢 。
"""

"""
Suppose the price of two horses and one ox exceeds 10,000 qian by the price of half a horse.
The price of one horse and two oxen is less than 10,000 qian by the price of half an ox.
Question: what are the prices of a horse and an ox?

The procedure says: Solve it as a system of equations using the method of balancing (損益).

The method of balancing (方程術) says: Arrange the coefficients of the unknowns (禾) in three rows: the top row for the first equation, the middle row for the second equation, and the bottom row for the constants. Perform operations to eliminate variables systematically, and solve for the unknowns step by step.

Answer: The price of a horse is *a*(=60000/11) qian, and the price of an ox is *b*(=20000/11) qian.
"""

from fractions import Fraction

# Define the system of equations:
# 2馬 + 1牛 = 10000 + 1/2馬
# 1馬 + 2牛 = 10000 - 1/2牛

# Let 馬 = x (price of a horse), 牛 = y (price of an ox)
# Rewrite the equations:
# (1) 2x + y = 10000 + (1/2)x
# (2) x + 2y = 10000 - (1/2)y

# Simplify both equations:
# (1) 2x + y - (1/2)x = 10000
#     (3/2)x + y = 10000
#     Multiply through by 2 to eliminate fractions:
#     3x + 2y = 20000
# (2) x + 2y + (1/2)y = 10000
#     x + (5/2)y = 10000
#     Multiply through by 2 to eliminate fractions:
#     2x + 5y = 20000

# The system of equations is now:
# (1) 3x + 2y = 20000
# (2) 2x + 5y = 20000

# Solve using elimination:
# Multiply (1) by 5 and (2) by 2 to align coefficients of x:
# (1) 15x + 10y = 100000
# (2)  4x + 10y = 40000

# Subtract (2) from (1):
# (15x + 10y) - (4x + 10y) = 100000 - 40000
# 11x = 60000
# x = 60000 / 11

# Substitute x into (1) to solve for y:
# 3x + 2y = 20000
# 3(60000 / 11) + 2y = 20000
# 180000 / 11 + 2y = 20000
# 2y = 20000 - 180000 / 11
# 2y = (220000 - 180000) / 11
# 2y = 40000 / 11
# y = 20000 / 11

# Final results:
a = Fraction(60000, 11)  # Price of a horse
b = Fraction(20000, 11)  # Price of an ox
"""
"""
