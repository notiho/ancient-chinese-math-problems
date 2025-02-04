"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
Suppose the price of 2 horses and 1 cow exceeds 10,000 qian by the price of half a horse.
And the price of 1 horse and 2 cows is less than 10,000 qian by the price of half a cow.
Question: what are the prices of a horse and a cow?

Answer: the price of a horse is *a* qian, and the price of a cow is *b* qian.
"""

# Let the price of a horse be x (馬價)
# Let the price of a cow be y (牛價)

# Equation 1: 2x + y = 10000 + x/2
# Equation 2: x + 2y = 10000 - y/2

# Solve for x and y step by step

from fractions import Fraction

# Simplify Equation 1: 2x + y = 10000 + x/2
# Multiply through by 2 to eliminate the fraction
# 4x + 2y = 20000 + x
# Rearrange: 3x + 2y = 20000  (Equation A)

# Simplify Equation 2: x + 2y = 10000 - y/2
# Multiply through by 2 to eliminate the fraction
# 2x + 4y = 20000 - y
# Rearrange: 2x + 5y = 20000  (Equation B)

# Solve the system of equations (Equation A and Equation B)
# Equation A: 3x + 2y = 20000
# Equation B: 2x + 5y = 20000

# Multiply Equation A by 2 and Equation B by 3 to align coefficients of x
# 6x + 4y = 40000  (Equation A * 2)
# 6x + 15y = 60000 (Equation B * 3)

# Subtract the first from the second to eliminate x
# (6x + 15y) - (6x + 4y) = 60000 - 40000
# 11y = 20000
y = Fraction(20000, 11)  # 牛價 (price of a cow)

# Substitute y back into Equation A to solve for x
# 3x + 2y = 20000
# 3x + 2(20000 / 11) = 20000
# 3x + 40000 / 11 = 20000
# 3x = 20000 - 40000 / 11
# 3x = (220000 - 40000) / 11
# 3x = 180000 / 11
x = Fraction(180000, 33)  # 馬價 (price of a horse)

# Final answers
a = x  # 馬價
b = y  # 牛價

# Output results
a, b
"""
"""
