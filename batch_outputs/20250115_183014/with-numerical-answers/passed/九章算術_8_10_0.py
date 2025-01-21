"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a(=60000/11)錢 ，牛價 b(=20000/11)錢 。
"""

"""
Suppose the price of two horses and one cow exceeds 10,000 by the price of half a horse.
The price of one horse and two cows is less than 10,000 by the price of half a cow.
Question: what are the prices of a horse and a cow?

The procedure says: Use the method of simultaneous equations and the method of balancing gains and losses.

The procedure for simultaneous equations says:
Place the upper row with three bundles of grain, the middle row with two bundles, and the lower row with one bundle, with the total being 39 dou on the right side.
The middle and left bundles are arranged like the right side.
Multiply the upper row of the right side by the middle row and divide by the direct value.
Then multiply by the next row and divide by the direct value again.
For the middle row, multiply the middle row's bundles by the left row and divide by the direct value.
For the left row, if the lower bundles are not exact, use the upper as the divisor and the lower as the dividend.
The dividend is the actual value of the lower bundles.
To find the middle bundles, multiply the divisor by the middle row's lower actual value and divide by the lower bundles' actual value.
The remainder, as the middle bundles' count plus one, is the middle bundles' actual value.
To find the upper bundles, multiply the divisor by the right row's lower actual value and divide by the lower and middle bundles' actual values.
The remainder, as the upper bundles' count plus one, is the upper bundles' actual value.
The actual values are all determined by the divisor, and each gets one dou.

Answer: the price of a horse is *a*(=60000/11) qian, and the price of a cow is *b*(=20000/11) qian.
"""

from fractions import Fraction

# Equation 1: 2馬 + 1牛 = 10000 + 1/2馬
# Equation 2: 1馬 + 2牛 = 10000 - 1/2牛

# Let 馬 = x (price of a horse), 牛 = y (price of a cow)
# Rewrite equations:
# 2x + y = 10000 + 1/2x  -> Multiply through by 2 to eliminate fraction:
# 4x + 2y = 20000 + x    -> Simplify:
# 3x + 2y = 20000        -> (1)

# x + 2y = 10000 - 1/2y  -> Multiply through by 2 to eliminate fraction:
# 2x + 4y = 20000 - y    -> Simplify:
# 2x + 5y = 20000        -> (2)

# Solve the system of equations:
# From (1): 3x + 2y = 20000
# From (2): 2x + 5y = 20000

# Multiply (1) by 5 and (2) by 2 to align coefficients of y:
# 15x + 10y = 100000      -> (3)
#  4x + 10y = 40000       -> (4)

# Subtract (4) from (3):
# (15x + 10y) - (4x + 10y) = 100000 - 40000
# 11x = 60000
x = Fraction(60000, 11)  # Price of a horse

# Substitute x into (1): 3x + 2y = 20000
# 3(60000/11) + 2y = 20000
# 180000/11 + 2y = 20000
# 2y = 20000 - 180000/11
# 2y = (220000 - 180000) / 11
# 2y = 40000 / 11
y = Fraction(20000, 11)  # Price of a cow

# Final results:
a = x  # 60000/11
b = y  # 20000/11
"""
"""
