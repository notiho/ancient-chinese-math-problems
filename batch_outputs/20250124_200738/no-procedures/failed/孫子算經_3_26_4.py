"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
答曰：甲持錢 a ，乙持錢 b 。
"""

#----- content starts here -----
"""
Suppose there are two people, A (甲) and B (乙), each holding an unknown amount of money.
If A takes half of B's money, A will have 48.  
If B takes more than half of A's money, B will also have 48.  
Question: How much money did A and B originally have?

Answer: A originally had *a*, and B originally had *b*.
"""

# Let A's money be `a` and B's money be `b`
from fractions import Fraction

# Equation 1: A + (1/2)B = 48
# Equation 2: B + (3/4)A = 48

# Solve for `a` and `b`
# From Equation 1: (1/2)B = 48 - A
# B = 2 * (48 - A)

# Substitute B into Equation 2:
# 2 * (48 - A) + (3/4)A = 48
# Expand:
# 96 - 2A + (3/4)A = 48
# Combine terms:
# 96 - 48 = 2A - (3/4)A
# 48 = (8/4)A - (3/4)A
# 48 = (5/4)A
# A = 48 * (4/5)
a = Fraction(48 * 4, 5)

# Substitute A back into Equation 1 to find B:
# B = 2 * (48 - A)
b = 2 * (48 - a)

# Results
a, b  # A's money and B's money#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36, Actual: 192/5
Variable 'b' has wrong value. Expected: 24, Actual: 96/5"""
