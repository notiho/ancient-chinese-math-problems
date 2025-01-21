"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a(=60000/11)錢 ，牛價 b(=20000/11)錢 。
"""

"""
Suppose there are two horses and one ox, and their combined price exceeds 10,000 qian, equal to the price of half a horse.
One horse and two oxen have a combined price less than 10,000 qian, equal to the price of half an ox.
Question: what are the prices of a horse and an ox, respectively?

The procedure says: Use the method of simultaneous equations and the method of balancing losses and gains.

The procedure for simultaneous equations says: Place the upper row with three bundles, the middle row with two bundles, and the lower row with one bundle, with a total of 39 dou on the right side. Arrange the middle and left bundles as on the right side.
Multiply the upper row of the right side by the middle row and divide by the direct divisor. Repeat for the next row, also dividing by the direct divisor.
Then, multiply the middle row by the middle bundle and divide by the direct divisor. For the left side, if the lower bundle is not exact, take the upper as the divisor and the lower as the dividend. The dividend is the actual value of the lower bundle.
To find the middle bundle, multiply the divisor by the middle row and the lower actual value, and divide by the actual value of the lower bundle. The remainder, as the middle bundle count plus one, is the actual value of the middle bundle.
To find the upper bundle, multiply the divisor by the right row and the lower actual value, and divide by the actual values of the lower and middle bundles. The remainder, as the upper bundle count plus one, is the actual value of the upper bundle.
The actual values are obtained as per the divisor, each being one dou.

Answer: the price of a horse is *a*(=60000/11) qian, and the price of an ox is *b*(=20000/11) qian.
"""

from fractions import Fraction

# Define the equations:
# 2馬 + 1牛 = 10000 + 1/2馬
# 1馬 + 2牛 = 10000 - 1/2牛

# Let 馬 = x (price of a horse), 牛 = y (price of an ox)
# Rewrite the equations:
# (1) 2x + y = 10000 + x/2
# (2) x + 2y = 10000 - y/2

# Simplify equation (1):
# Multiply through by 2 to eliminate the fraction:
# 4x + 2y = 20000 + x
# Rearrange:
# 3x + 2y = 20000  ----> (A)

# Simplify equation (2):
# Multiply through by 2 to eliminate the fraction:
# 2x + 4y = 20000 - y
# Rearrange:
# 2x + 5y = 20000  ----> (B)

# Solve the system of equations (A) and (B) using elimination:
# (A) 3x + 2y = 20000
# (B) 2x + 5y = 20000

# Multiply (A) by 5 and (B) by 2 to align coefficients of x:
# 15x + 10y = 100000
#  4x + 10y = 40000

# Subtract the second equation from the first:
# (15x + 10y) - (4x + 10y) = 100000 - 40000
# 11x = 60000
x = Fraction(60000, 11)  # Price of a horse

# Substitute x into (A) to solve for y:
# 3x + 2y = 20000
# 3(60000/11) + 2y = 20000
# 180000/11 + 2y = 20000
# 2y = 20000 - 180000/11
# 2y = (220000 - 180000) / 11
# 2y = 40000 / 11
y = Fraction(20000, 11)  # Price of an ox

# Final answers:
a = x  # 60000/11
b = y  # 20000/11
"""
"""
