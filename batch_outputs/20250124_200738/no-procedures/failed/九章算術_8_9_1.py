"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
荅曰：甲持 a錢 ，乙持 b錢 。
"""

#----- content starts here -----
"""
Suppose there are two people, A (甲) and B (乙), holding an unknown amount of money.
If A takes half of B's money, A will have 50 coins.
If B takes more than half of A's money (3/2 of half of A's money), B will also have 50 coins.
Question: how much money does A and B each have?

Answer: A has *a* coins, and B has *b* coins.
"""

from fractions import Fraction

# Let A's money be `a` and B's money be `b`
# From the problem:
# 1. a + (1/2)b = 50
# 2. b + (3/2)(1/2)a = 50

# Rewrite the equations:
# Equation 1: a + (1/2)b = 50
# Equation 2: b + (3/4)a = 50

# Solve for `a` and `b` using substitution:
# From Equation 1: (1/2)b = 50 - a
# b = 2(50 - a) = 100 - 2a

# Substitute `b` into Equation 2:
# (100 - 2a) + (3/4)a = 50
# 100 - 2a + (3/4)a = 50
# Combine terms:
# 100 - (8/4)a + (3/4)a = 50
# 100 - (5/4)a = 50
# (5/4)a = 100 - 50
# (5/4)a = 50
# a = 50 * (4/5)
# a = 40

# Substitute `a = 40` into Equation 1:
# 40 + (1/2)b = 50
# (1/2)b = 50 - 40
# (1/2)b = 10
# b = 10 * 2
# b = 20

# Final result:
a = 40  # A's money
b = 20  # B's money

# Output the results
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 40
Variable 'b' has wrong value. Expected: 25, Actual: 20"""
