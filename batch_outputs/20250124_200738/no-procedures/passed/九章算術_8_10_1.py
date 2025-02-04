"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
荅曰：馬價 a錢 ，牛價 b錢 。
"""

#----- content starts here -----
"""
Suppose the price of 2 horses and 1 cow exceeds 10,000 qian by the price of half a horse.
The price of 1 horse and 2 cows is less than 10,000 qian by the price of half a cow.
Question: what are the prices of a horse and a cow?

Answer: the price of a horse is *a* qian, and the price of a cow is *b* qian.
"""

# Let the price of a horse be x (in qian)
# Let the price of a cow be y (in qian)

# Equation 1: 2x + y = 10000 + x/2
# Equation 2: x + 2y = 10000 - y/2

# Solve for x and y
from fractions import Fraction

# Rearrange Equation 1: 2x + y - x/2 = 10000
# Multiply through by 2 to eliminate the fraction: 4x + 2y - x = 20000
# Simplify: 3x + 2y = 20000
eq1 = lambda x, y: 3 * x + 2 * y - 20000

# Rearrange Equation 2: x + 2y + y/2 = 10000
# Multiply through by 2 to eliminate the fraction: 2x + 4y + y = 20000
# Simplify: 2x + 5y = 20000
eq2 = lambda x, y: 2 * x + 5 * y - 20000

# Solve the system of equations
# Multiply eq1 by 2: 6x + 4y = 40000
# Multiply eq2 by 3: 6x + 15y = 60000
# Subtract the first from the second: 11y = 20000
# Solve for y: y = 20000 / 11
b = Fraction(20000, 11)

# Substitute y into eq1: 3x + 2(20000 / 11) = 20000
# Simplify: 3x + 40000 / 11 = 20000
# Multiply through by 11: 33x + 40000 = 220000
# Solve for x: 33x = 180000, x = 180000 / 33
a = Fraction(180000, 33)

# Results
a, b  # a is the price of a horse, b is the price of a cow#----- content ends here -----

"""
"""
