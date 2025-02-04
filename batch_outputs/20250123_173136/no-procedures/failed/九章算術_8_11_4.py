"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
Suppose there are three types of horses: a Wu horse (武馬), a Zhong horse (中馬), and a Xia horse (下馬). 
- A Wu horse has 1 horse.
- A Zhong horse has 2 horses.
- A Xia horse has 3 horses.
Each horse is tasked with pulling 40 shi (石) up a slope but cannot do so individually.

To solve this, the Wu horse borrows 1 Zhong horse, the Zhong horse borrows 1 Xia horse, and the Xia horse borrows 1 Wu horse. 
With this arrangement, all groups can successfully pull the load up the slope.

Question: What is the pulling power of each horse type (in shi)?
Answer: The Wu horse pulls *a* shi, the Zhong horse pulls *b* shi, and the Xia horse pulls *c* shi.
"""

from fractions import Fraction

# Let the pulling power of each type of horse be:
# 武馬 = a, 中馬 = b, 下馬 = c

# Given conditions:
# 1. 武馬 + 中馬 = 40
# 2. 中馬 + 下馬 = 40
# 3. 下馬 + 武馬 = 40

# Solve the system of equations:
# Add all three equations:
# (武馬 + 中馬) + (中馬 + 下馬) + (下馬 + 武馬) = 120
# 2 * (武馬 + 中馬 + 下馬) = 120
# 武馬 + 中馬 + 下馬 = 60

# Subtract each pair of equations to isolate variables:
# 武馬 = 60 - 2 * 中馬
# 中馬 = 60 - 2 * 下馬
# 下馬 = 60 - 2 * 武馬

# Substitute into the equations to solve:
# From 武馬 + 中馬 = 40:
# (60 - 2 * 中馬) + 中馬 = 40
# 60 - 中馬 = 40
# 中馬 = 20

# From 中馬 + 下馬 = 40:
# 20 + 下馬 = 40
# 下馬 = 20

# From 下馬 + 武馬 = 40:
# 20 + 武馬 = 40
# 武馬 = 20

# Final pulling power:
a = 20  # 武馬 pulling power
b = 20  # 中馬 pulling power
c = 20  # 下馬 pulling power

# Results:
a, b, c
"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
