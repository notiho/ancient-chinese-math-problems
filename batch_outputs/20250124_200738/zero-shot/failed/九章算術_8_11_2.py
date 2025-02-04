"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves determining the pulling power of three types of horses (武馬, 中馬, 下馬) represented as `a`, `b`, and `c`, respectively. The relationships between their pulling powers are described in the problem.

Here is the Python code to compute the values of `a`, `b`, and `c`:


"""

#----- content starts here -----

from fractions import Fraction

# Given equations based on the problem:
# 1. 武馬 (a) + 中馬 (b) = 40
# 2. 中馬 (b) + 下馬 (c) = 40
# 3. 下馬 (c) + 武馬 (a) = 40

# Solve the system of equations:
# Add all three equations:
# (a + b) + (b + c) + (c + a) = 40 + 40 + 40
# 2a + 2b + 2c = 120
# Simplify:
a_plus_b_plus_c = Fraction(120, 2)  # a + b + c = 60

# From the first equation: a + b = 40
# Substitute into a + b + c = 60:
c = a_plus_b_plus_c - Fraction(40)  # c = 60 - 40 = 20

# From the second equation: b + c = 40
# Substitute c = 20:
b = Fraction(40) - c  # b = 40 - 20 = 20

# From the third equation: c + a = 40
# Substitute c = 20:
a = Fraction(40) - c  # a = 40 - 20 = 20

# Results:
a = Fraction(20)  # 武馬 pulling power
b = Fraction(20)  # 中馬 pulling power
c = Fraction(20)  # 下馬 pulling power

# The pulling power of each horse:
# 武馬 (a): 20 石
# 中馬 (b): 20 石
# 下馬 (c): 20 石
#----- content ends here -----


"""


### Explanation:
1. We start with the three equations derived from the problem:
   - \( a + b = 40 \)
   - \( b + c = 40 \)
   - \( c + a = 40 \)

2. Adding all three equations gives:
   - \( 2a + 2b + 2c = 120 \)
   - Simplify to \( a + b + c = 60 \).

3. Using substitution, we solve for \( c \), \( b \), and \( a \) step by step.

4. The final results are:
   - \( a = 20 \) 石 (武馬 pulling power)
   - \( b = 20 \) 石 (中馬 pulling power)
   - \( c = 20 \) 石 (下馬 pulling power)
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
