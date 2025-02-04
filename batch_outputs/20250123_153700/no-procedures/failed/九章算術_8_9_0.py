"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
Suppose there are two people, A (甲) and B (乙), holding an unknown amount of money.

- If A takes half of B's money, A will have 50 coins.
- If B takes more than half of A's money (specifically, 1.5 times half of A's money), B will also have 50 coins.

Question: How much money does A and B each have?

Answer: A has *a* coins, and B has *b* coins.
"""

from fractions import Fraction

# Let A's money be `a` and B's money be `b`
# From the problem:
# 1. a + b/2 = 50
# 2. b + (3/2)(a/2) = 50

# Solve the equations step by step:

# Equation 1: a + b/2 = 50
# Multiply through by 2 to eliminate the fraction:
# 2a + b = 100  --> (1)

# Equation 2: b + (3/2)(a/2) = 50
# Simplify (3/2)(a/2) to (3/4)a:
# b + (3/4)a = 50
# Multiply through by 4 to eliminate the fraction:
# 4b + 3a = 200  --> (2)

# Solve the system of equations:
# From (1): b = 100 - 2a
# Substitute b into (2):
# 4(100 - 2a) + 3a = 200
# 400 - 8a + 3a = 200
# 400 - 5a = 200
# -5a = -200
# a = 40

# Substitute a = 40 into (1):
# 2(40) + b = 100
# 80 + b = 100
# b = 20

# Final answer:
a = 40  # A's money
b = 20  # B's money

# Output the results
a, b
"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 40
Variable 'b' has wrong value. Expected: 25, Actual: 20"""
