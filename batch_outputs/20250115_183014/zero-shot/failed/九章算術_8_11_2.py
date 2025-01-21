"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the pulling power of three types of horses (武馬, 中馬, 下馬) when they cooperate under certain conditions. The solution will use fractions to ensure accuracy.

Here is the Python code:


"""


from fractions import Fraction

# Let the pulling power of 武馬, 中馬, 下馬 be a, b, c respectively (in 石 per horse).

# Given conditions:
# 武馬借中馬一匹, 中馬借下馬一匹, 下馬借武馬一匹, and all can pull 40 石 up the slope.

# Equations based on the problem:
# 武馬 + 中馬 = 40
# 中馬 + 下馬 = 40
# 下馬 + 武馬 = 40

# Solve the system of equations:
# Add all three equations:
# (武馬 + 中馬) + (中馬 + 下馬) + (下馬 + 武馬) = 40 + 40 + 40
# 2(武馬 + 中馬 + 下馬) = 120
# 武馬 + 中馬 + 下馬 = 60

# Subtract individual equations to find each horse's pulling power:
# 武馬 = 60 - (中馬 + 下馬)
# 中馬 = 60 - (下馬 + 武馬)
# 下馬 = 60 - (武馬 + 中馬)

# From the first equation:
a = Fraction(60 - 40)  # 武馬 pulling power
b = Fraction(60 - 40)  # 中馬 pulling power
c = Fraction(60 - 40)  # 下馬 pulling power

# Results:
武馬 = a
中馬 = b
下馬 = c

# Print results:
print(f"武馬 pulling power: {a} 石")
print(f"中馬 pulling power: {b} 石")
print(f"下馬 pulling power: {c} 石")


"""


This code calculates the pulling power of each horse type (武馬, 中馬, 下馬) based on the given conditions. The results are stored in variables `a`, `b`, and `c`, which represent the pulling power of 武馬, 中馬, and 下馬 respectively.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 20
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'c' has wrong value. Expected: 1, Actual: 20
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
