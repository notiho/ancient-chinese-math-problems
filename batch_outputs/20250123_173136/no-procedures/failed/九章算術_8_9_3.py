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

# Let A's money be x and B's money be y
# Equation 1: x + y/2 = 50
# Equation 2: y + (3/2) * (x/2) = 50

# Solve for x and y
# From Equation 1: y = 2 * (50 - x)
# Substitute y into Equation 2:
# 2 * (50 - x) + (3/2) * (x/2) = 50
# Simplify:
# 100 - 2x + (3/4)x = 50
# Combine terms:
# -2x + (3/4)x = -50
# (-8x + 3x) / 4 = -50
# -5x / 4 = -50
# x = 40

# Substitute x = 40 into Equation 1:
# 40 + y/2 = 50
# y/2 = 10
# y = 20

# Final result
a = 40  # A's money
b = 20  # B's money

a, b  # Output the result
"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 40
Variable 'b' has wrong value. Expected: 25, Actual: 20"""
