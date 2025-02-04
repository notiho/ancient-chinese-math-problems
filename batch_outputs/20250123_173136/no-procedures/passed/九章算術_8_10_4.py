"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
Suppose the price of 2 horses and 1 cow exceeds 10,000 qian by the price of half a horse.
The price of 1 horse and 2 cows is less than 10,000 qian by the price of half a cow.
Question: What are the prices of a horse and a cow?

Answer: The price of a horse is *a* qian, and the price of a cow is *b* qian.
"""

# Let the price of a horse be x (in qian)
# Let the price of a cow be y (in qian)

# Equation 1: 2x + y = 10000 + x/2
# Equation 2: x + 2y = 10000 - y/2

# Solve for x and y
from fractions import Fraction

# Simplify Equation 1: 2x + y = 10000 + x/2
# Multiply through by 2 to eliminate the fraction: 4x + 2y = 20000 + x
# Rearrange: 3x + 2y = 20000  (Equation A)

# Simplify Equation 2: x + 2y = 10000 - y/2
# Multiply through by 2 to eliminate the fraction: 2x + 4y = 20000 - y
# Rearrange: 2x + 5y = 20000  (Equation B)

# Solve the system of equations:
# From Equation A: 3x + 2y = 20000
# From Equation B: 2x + 5y = 20000

# Multiply Equation A by 2: 6x + 4y = 40000
# Multiply Equation B by 3: 6x + 15y = 60000
# Subtract the first from the second: 11y = 20000
y = Fraction(20000, 11)  # Price of a cow

# Substitute y back into Equation A: 3x + 2y = 20000
x = Fraction(20000 - 2 * y, 3)  # Price of a horse

# Final answers
a = x  # Price of a horse
b = y  # Price of a cow

a, b  # Output the results
"""
"""
