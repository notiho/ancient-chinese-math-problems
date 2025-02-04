"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
Suppose there are two people, A (甲) and B (乙), holding an unknown amount of money.
If A takes half of B's money, A will have 50 coins.
If B takes more than half of A's money, B will also have 50 coins.
Question: How much money does A and B each have?

Answer: A has *a* coins, and B has *b* coins.
"""

# Let A's money be `a` and B's money be `b`
# From the problem:
# 1. a + b/2 = 50
# 2. b + (3/2)a = 50

from fractions import Fraction

# Solve the equations:
# From equation 1: b = 2 * (50 - a)
b = lambda a: 2 * (50 - a)

# Substitute b into equation 2:
# 2 * (50 - a) + (3/2)a = 50
# Simplify:
# 100 - 2a + (3/2)a = 50
# Combine terms:
# 100 - (4/2)a + (3/2)a = 50
# 100 - (1/2)a = 50
# (1/2)a = 50
# a = 100

a = 100

# Substitute a back into equation for b:
b = b(a)

# Final results:
a = Fraction(a)
b = Fraction(b)

a, b  # A has `a` coins, B has `b` coins
"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
