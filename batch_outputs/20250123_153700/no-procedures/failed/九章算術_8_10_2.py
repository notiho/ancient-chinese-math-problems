"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
Suppose there are two horses and one cow, and their total value exceeds 10,000 qian by the value of half a horse.
Also, one horse and two cows together are worth less than 10,000 qian by the value of half a cow.
Question: what are the values of a horse and a cow?

Answer: the value of a horse is *a* qian, and the value of a cow is *b* qian.
"""

# Let the value of a horse be `馬價 = x` and the value of a cow be `牛價 = y`.

# Equations:
# 2x + y = 10000 + x / 2  (from the first condition)
# x + 2y = 10000 - y / 2  (from the second condition)

# Solve for x and y step by step.

from fractions import Fraction

# First equation: 2x + y = 10000 + x / 2
# Multiply through by 2 to eliminate the fraction:
# 4x + 2y = 20000 + x
# Rearrange:
# 3x + 2y = 20000  (Equation 1)

# Second equation: x + 2y = 10000 - y / 2
# Multiply through by 2 to eliminate the fraction:
# 2x + 4y = 20000 - y
# Rearrange:
# 2x + 5y = 20000  (Equation 2)

# Solve the system of equations:
# From Equation 1: 3x + 2y = 20000
# From Equation 2: 2x + 5y = 20000

# Multiply Equation 1 by 5 and Equation 2 by 2 to align coefficients of x:
# 15x + 10y = 100000  (Equation 3)
#  4x + 10y = 40000   (Equation 4)

# Subtract Equation 4 from Equation 3:
# (15x - 4x) + (10y - 10y) = 100000 - 40000
# 11x = 60000
x = Fraction(60000, 11)  # Value of a horse

# Substitute x into Equation 1 to solve for y:
# 3x + 2y = 20000
# 3(60000 / 11) + 2y = 20000
# 180000 / 11 + 2y = 20000
# 2y = 20000 - 180000 / 11
# 2y = (220000 - 180000) / 11
# 2y = 40000 / 11
y = Fraction(40000, 22)  # Value of a cow

# Final answers:
馬價 = x
牛價 = y

馬價, 牛價
"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
