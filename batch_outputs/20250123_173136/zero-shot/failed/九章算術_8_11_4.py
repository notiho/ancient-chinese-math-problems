"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. We will use the `Fraction` class to handle numbers that might not be integers. Here's the solution:


"""


from fractions import Fraction

# Let the pulling power of 武馬 (a), 中馬 (b), and 下馬 (c) be unknowns.
# Given conditions:
# 武馬 (a) + 中馬 (b) = 40
# 中馬 (b) + 下馬 (c) = 40
# 下馬 (c) + 武馬 (a) = 40

# Solve the system of equations:
# 1. a + b = 40
# 2. b + c = 40
# 3. c + a = 40

# From equation 1: b = 40 - a
# Substitute b into equation 2: (40 - a) + c = 40
# Simplify: c = a
# Substitute c into equation 3: a + a = 40
# Simplify: 2a = 40
a = Fraction(40, 2)  # a = 20

# Substitute a into b = 40 - a
b = 40 - a  # b = 20

# Substitute a into c = a
c = a  # c = 20

# Results:
# 武馬 (a) = 20 石
# 中馬 (b) = 20 石
# 下馬 (c) = 20 石


"""


The values of the unknowns are:
- 武馬 (a) = 20 石
- 中馬 (b) = 20 石
- 下馬 (c) = 20 石
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
