"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
答曰：甲持錢 a ，乙持錢 b 。
"""

"""
Suppose there are two people, A (甲) and B (乙), each holding an unknown amount of money.  
If A takes half of B's money, A will have 48.  
If B takes more than half of A's money, B will also have 48.  

Question: How much money did A and B originally have?

Answer: A has *a*, and B has *b*.
"""

from fractions import Fraction

# Let A's money be `a` and B's money be `b`
# According to the problem:
# 1. a + b/2 = 48
# 2. b + (a * 3/4) = 48

# Solve the equations step by step:

# From equation 1: a + b/2 = 48
# Rearrange to express `a` in terms of `b`:
a = 48 - Fraction(b, 2)

# Substitute `a` into equation 2: b + (a * 3/4) = 48
# b + (3/4 * (48 - b/2)) = 48
# Expand:
# b + (3/4 * 48) - (3/4 * b/2) = 48
# b + 36 - (3/8 * b) = 48
# Combine terms:
# b - (3/8 * b) = 48 - 36
# (8/8 * b - 3/8 * b) = 12
# (5/8 * b) = 12
# Solve for `b`:
b = Fraction(12 * 8, 5)

# Now substitute `b` back into the equation for `a`:
a = 48 - Fraction(b, 2)

# Final results:
a = Fraction(a)
b = Fraction(b)

# Output the results
a, b
"""
Code error: name 'b' is not defined"""
