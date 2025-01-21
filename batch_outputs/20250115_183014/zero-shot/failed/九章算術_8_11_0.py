"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves determining the pulling power of three types of horses (武馬, 中馬, 下馬). Here's the Python code:


"""


from fractions import Fraction

# Let the pulling power of 武馬, 中馬, 下馬 be a, c, and e respectively (in 石).
# The problem states that 武馬借中馬一匹, 中馬借下馬一匹, 下馬借武馬一匹, and all can pull 40 石.

# Equations based on the problem:
# 武馬 + 中馬 = 40
# 中馬 + 下馬 = 40
# 下馬 + 武馬 = 40

# Solving the equations:
# Adding all three equations:
# (武馬 + 中馬) + (中馬 + 下馬) + (下馬 + 武馬) = 120
# 2 * (武馬 + 中馬 + 下馬) = 120
# 武馬 + 中馬 + 下馬 = 60

# Substituting into the first equation:
# 武馬 + 中馬 = 40
# 下馬 = 60 - (武馬 + 中馬) = 60 - 40 = 20

# Substituting into the second equation:
# 中馬 + 下馬 = 40
# 中馬 = 40 - 下馬 = 40 - 20 = 20

# Substituting into the third equation:
# 下馬 + 武馬 = 40
# 武馬 = 40 - 下馬 = 40 - 20 = 20

# Assigning the values:
a = Fraction(20)  # 武馬 pulling power in 石
b = Fraction(20)  # 武馬 pulling power in 石
c = Fraction(20)  # 中馬 pulling power in 石
d = Fraction(20)  # 中馬 pulling power in 石
e = Fraction(20)  # 下馬 pulling power in 石
f = Fraction(20)  # 下馬 pulling power in 石

# Results:
print(f"武馬 a匹 力引 {b}石")
print(f"中馬 c匹 力引 {d}石")
print(f"下馬 e匹 力引 {f}石")


"""


This code calculates the pulling power of each type of horse (武馬, 中馬, 下馬) based on the given problem and equations. The solution uses the `Fraction` class to ensure accuracy when dealing with fractional values.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 20
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'c' has wrong value. Expected: 1, Actual: 20
Variable 'd' has wrong value. Expected: 120/7, Actual: 20
Variable 'e' has wrong value. Expected: 1, Actual: 20
Variable 'f' has wrong value. Expected: 40/7, Actual: 20"""
