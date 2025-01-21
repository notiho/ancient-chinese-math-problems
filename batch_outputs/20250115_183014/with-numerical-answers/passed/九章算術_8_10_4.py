"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a(=60000/11)錢 ，牛價 b(=20000/11)錢 。
"""

"""
Suppose the price of two horses and one cow exceeds 10,000 by the price of half a horse.
The price of one horse and two cows is less than 10,000 by the price of half a cow.
Question: what are the prices of a horse and a cow respectively?

The procedure says: Use the method of simultaneous equations and the method of balancing gains and losses.

The method of simultaneous equations says: Place the coefficients of the variables (horses and cows) in rows.
The top row corresponds to the first equation, the middle row to the second equation, and the bottom row to the constants.
Perform elimination by multiplying rows and dividing by the pivot element.
Continue until the solution is obtained.

Answer: the price of a horse is *a*(=60000/11) qian, and the price of a cow is *b*(=20000/11) qian.
"""

from fractions import Fraction

# Define the equations:
# 2馬 + 1牛 = 10000 + 1/2馬
# 1馬 + 2牛 = 10000 - 1/2牛

# Represent the equations in matrix form:
# [ 2   1   | 10000 + 1/2馬 ]
# [ 1   2   | 10000 - 1/2牛 ]

# Rewrite the equations to eliminate the fractions:
# Multiply the first equation by 2 to eliminate the 1/2馬 term:
# 4馬 + 2牛 = 20000 + 1馬
# Simplify:
# 3馬 + 2牛 = 20000  (Equation 1)

# Multiply the second equation by 2 to eliminate the 1/2牛 term:
# 2馬 + 4牛 = 20000 - 1牛
# Simplify:
# 2馬 + 5牛 = 20000  (Equation 2)

# Solve the system of equations:
# Equation 1: 3馬 + 2牛 = 20000
# Equation 2: 2馬 + 5牛 = 20000

# Eliminate one variable (e.g., 馬):
# Multiply Equation 1 by 2: 6馬 + 4牛 = 40000
# Multiply Equation 2 by 3: 6馬 + 15牛 = 60000
# Subtract the first from the second:
# (6馬 + 15牛) - (6馬 + 4牛) = 60000 - 40000
# 11牛 = 20000
牛價 = Fraction(20000, 11)  # b = 20000/11

# Substitute 牛價 into Equation 1 to solve for 馬價:
# 3馬 + 2牛 = 20000
# 3馬 + 2 * (20000/11) = 20000
# 3馬 = 20000 - (40000/11)
# 3馬 = (220000/11) - (40000/11)
# 3馬 = 180000/11
# 馬價 = (180000/11) / 3
馬價 = Fraction(180000, 33)  # a = 60000/11

a = 馬價  # 60000/11
b = 牛價  # 20000/11
"""
"""
