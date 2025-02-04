"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

#----- content starts here -----
"""
Suppose there are three types of horses: a strong horse (武馬), a medium horse (中馬), and a weak horse (下馬). 
- A strong horse alone cannot pull 40 shi of weight up a slope.
- Two medium horses together cannot pull 40 shi up a slope.
- Three weak horses together cannot pull 40 shi up a slope.

However:
- The strong horse borrows one medium horse, and together they can pull 40 shi up the slope.
- The medium horse borrows one weak horse, and together they can pull 40 shi up the slope.
- The weak horse borrows one strong horse, and together they can pull 40 shi up the slope.

Question: How much weight can one strong horse, one medium horse, and one weak horse pull individually?

Answer: A strong horse can pull *a* shi, a medium horse can pull *b* shi, and a weak horse can pull *c* shi.
"""

from fractions import Fraction

# Let the pulling power of one strong horse, one medium horse, and one weak horse be a, b, and c respectively.
# From the problem, we know the following equations:
# 1. a < 40
# 2. 2b < 40
# 3. 3c < 40
# 4. a + b = 40
# 5. b + c = 40
# 6. c + a = 40

# Solve the equations:
# From equation (4): b = 40 - a
# From equation (5): c = 40 - b = 40 - (40 - a) = a
# From equation (6): a + c = 40, so c = 40 - a

# Substituting c = 40 - a into equation (5):
# b + (40 - a) = 40
# b = a

# Thus, a = b = c.

# Since all horses together must satisfy the constraints:
# a + b = 40, b + c = 40, c + a = 40, and a = b = c,
# we find that each horse can pull:

a = Fraction(40, 2)  # Strong horse's pulling power
b = Fraction(40, 2)  # Medium horse's pulling power
c = Fraction(40, 2)  # Weak horse's pulling power

# Final results:
a, b, c  # Each horse can pull 20 shi.#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
