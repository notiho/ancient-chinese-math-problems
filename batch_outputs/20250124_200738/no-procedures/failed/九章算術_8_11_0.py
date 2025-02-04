"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

#----- content starts here -----
"""
Suppose there is one strong horse (武馬), two medium horses (中馬), and three weak horses (下馬). Each is tasked with carrying 40 shi (石) up a slope, but none can do it alone. 

To solve the problem:
- The strong horse borrows one medium horse.
- The medium horses borrow one weak horse.
- The weak horses borrow one strong horse.

After borrowing, all groups are able to carry the load up the slope. 

Question: What is the pulling capacity of one strong horse (武馬), one medium horse (中馬), and one weak horse (下馬)?

Answer: The pulling capacity of one strong horse is *a* shi, one medium horse is *b* shi, and one weak horse is *c* shi.
"""

# Let the pulling capacities of one strong horse, one medium horse, and one weak horse be a, b, and c respectively.
# Each group must pull 40 shi up the slope.

from fractions import Fraction

# Equations based on the problem:
# 1. 武馬 + 中馬 = 40
# 2. 中馬 + 下馬 = 40
# 3. 下馬 + 武馬 = 40

# Solve the system of equations:
# From equation 1: 中馬 = 40 - 武馬
# Substitute 中馬 into equation 2: (40 - 武馬) + 下馬 = 40
# Simplify: 下馬 = 武馬
# Substitute 下馬 = 武馬 into equation 3: 武馬 + 武馬 = 40
# Simplify: 2 * 武馬 = 40
# Solve for 武馬: 武馬 = 20

# Substitute 武馬 = 20 into 下馬 = 武馬: 下馬 = 20
# Substitute 武馬 = 20 into equation 1: 20 + 中馬 = 40
# Solve for 中馬: 中馬 = 20

# Results:
a = Fraction(20)  # Pulling capacity of one strong horse
b = Fraction(20)  # Pulling capacity of one medium horse
c = Fraction(20)  # Pulling capacity of one weak horse

# Final results:
a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
