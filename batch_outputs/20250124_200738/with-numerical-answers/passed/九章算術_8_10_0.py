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
Question: what are the prices of a horse and a cow respectively?

The procedure says: Solve this using the method of simultaneous equations ("方程"), employing the method of balancing gains and losses ("損益").

The method of simultaneous equations says: Place the coefficients of the variables (禾) in rows: the top row for the first equation, the middle row for the second equation, and the bottom row for the constants. Perform elimination by multiplying and dividing as described to isolate each variable.

Answer: The price of a horse is *a*(=60000/11) qian, and the price of a cow is *b*(=20000/11) qian.
"""

from fractions import Fraction

# Define the equations:
# 2馬 + 1牛 = 10000 + 1/2馬
# 1馬 + 2牛 = 10000 - 1/2牛

# Let 馬 = x (price of a horse), 牛 = y (price of a cow)
# Rewrite the equations:
# (1) 2x + y = 10000 + (1/2)x
# (2) x + 2y = 10000 - (1/2)y

# Simplify both equations:
# (1) 2x - (1/2)x + y = 10000
#     (4/2)x - (1/2)x + y = 10000
#     (3/2)x + y = 10000
#     Multiply through by 2 to eliminate fractions:
#     3x + 2y = 20000
# (2) x + 2y + (1/2)y = 10000
#     x + (4/2)y + (1/2)y = 10000
#     x + (5/2)y = 10000
#     Multiply through by 2 to eliminate fractions:
#     2x + 5y = 20000

# Now solve the system of equations:
# (1) 3x + 2y = 20000
# (2) 2x + 5y = 20000

# Eliminate one variable (e.g., y) using elimination:
# Multiply (1) by 5 and (2) by 2 to align coefficients of y:
# (1) 15x + 10y = 100000
# (2) 4x + 10y = 40000

# Subtract (2) from (1):
# (15x + 10y) - (4x + 10y) = 100000 - 40000
# 11x = 60000
# Solve for x:
a = Fraction(60000, 11)  # Price of a horse

# Substitute x into one of the original equations to solve for y:
# Use (1): 3x + 2y = 20000
# 3(60000/11) + 2y = 20000
# 180000/11 + 2y = 20000
# 2y = 20000 - 180000/11
# 2y = (220000/11) - (180000/11)
# 2y = 40000/11
# y = (40000/11) / 2
b = Fraction(20000, 11)  # Price of a cow

# Final results:
# 馬價 = a = 60000/11 錢
# 牛價 = b = 20000/11 錢#----- content ends here -----

"""
"""
