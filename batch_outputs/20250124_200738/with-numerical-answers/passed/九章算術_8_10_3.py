"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a(=60000/11)錢 ，牛價 b(=20000/11)錢 。
"""

#----- content starts here -----
"""
Suppose there are two horses and one cow, and their combined price exceeds 10,000 qian, equal to the price of half a horse.
One horse and two cows have a combined price less than 10,000 qian, equal to the price of half a cow.
Question: what are the prices of a horse and a cow?

The procedure says: Use the method of simultaneous equations and the method of balancing losses and gains.

The method of simultaneous equations says:
1. Place the coefficients of the variables (horses and cows) in rows, with the total values on the right-hand side.
2. Perform row operations to eliminate variables systematically, reducing the system to simpler equations.
3. Solve for each variable by back-substitution.

Answer: The price of a horse is *a*(=60000/11) qian, and the price of a cow is *b*(=20000/11) qian.
"""

from fractions import Fraction

# Equations:
# 2馬 + 1牛 = 10000 + 1/2馬
# 1馬 + 2牛 = 10000 - 1/2牛

# Let 馬 = x (price of a horse), 牛 = y (price of a cow)
# Rewrite the equations:
# (1) 2x + y = 10000 + x/2
# (2) x + 2y = 10000 - y/2

# Simplify equation (1):
# Multiply through by 2 to eliminate the fraction:
# 4x + 2y = 20000 + x
# Rearrange:
# 3x + 2y = 20000  ----> (3)

# Simplify equation (2):
# Multiply through by 2 to eliminate the fraction:
# 2x + 4y = 20000 - y
# Rearrange:
# 2x + 5y = 20000  ----> (4)

# Solve the system of equations (3) and (4):
# (3) 3x + 2y = 20000
# (4) 2x + 5y = 20000

# Eliminate x by multiplying (3) by 2 and (4) by 3:
eq1 = [6, 4, 40000]  # 6x + 4y = 40000
eq2 = [6, 15, 60000] # 6x + 15y = 60000

# Subtract eq1 from eq2:
# (6x + 15y) - (6x + 4y) = 60000 - 40000
# 11y = 20000
y = Fraction(20000, 11)  # 牛價 (price of a cow)

# Substitute y into (3) to solve for x:
# 3x + 2y = 20000
x = Fraction(20000 - 2 * y, 3)  # 馬價 (price of a horse)

a = x  # 馬價 = 60000/11
b = y  # 牛價 = 20000/11#----- content ends here -----

"""
"""
