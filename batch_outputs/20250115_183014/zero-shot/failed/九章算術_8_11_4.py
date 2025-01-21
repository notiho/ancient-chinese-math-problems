"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves determining the pulling power of three types of horses (武馬, 中馬, 下馬) when they borrow each other's strength to pull a load.

Here is the Python code:


"""


from fractions import Fraction

# Let the pulling power of 武馬, 中馬, 下馬 be a, c, and e respectively (in 石 per horse).
# The total load is 40 石, and the borrowing relationships are described in the problem.

# Equations derived from the problem:
# 武馬借中馬一匹: a + c = 40
# 中馬借下馬一匹: c + e = 40
# 下馬借武馬一匹: e + a = 40

# Solve the system of equations:
# From the first equation: a = 40 - c
# Substitute into the third equation: e + (40 - c) = 40 -> e = c
# Substitute e = c into the second equation: c + c = 40 -> c = 20
# Substitute c = 20 into e = c: e = 20
# Substitute c = 20 into a = 40 - c: a = 20

# Assign the results to variables:
a = Fraction(20)  # 武馬 pulling power in 石
c = Fraction(20)  # 中馬 pulling power in 石
e = Fraction(20)  # 下馬 pulling power in 石

# Output the results:
b = a  # 武馬 pulling power in 石
d = c  # 中馬 pulling power in 石
f = e  # 下馬 pulling power in 石

# The pulling powers are:
# 武馬 a匹 力引 b石
# 中馬 c匹 力引 d石
# 下馬 e匹 力引 f石


"""


### Explanation:
1. The problem describes a scenario where three types of horses (武馬, 中馬, 下馬) each try to pull a load of 40 石 but fail individually.
2. By borrowing strength from one another, they succeed. This leads to three equations:
   - 武馬借中馬一匹: \( a + c = 40 \)
   - 中馬借下馬一匹: \( c + e = 40 \)
   - 下馬借武馬一匹: \( e + a = 40 \)
3. Solving this system of equations gives \( a = 20 \), \( c = 20 \), and \( e = 20 \).
4. The pulling power of each horse is 20 石.

The solution is implemented in Python using the `Fraction` class to ensure exact arithmetic.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 20
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'c' has wrong value. Expected: 1, Actual: 20
Variable 'd' has wrong value. Expected: 120/7, Actual: 20
Variable 'e' has wrong value. Expected: 1, Actual: 20
Variable 'f' has wrong value. Expected: 40/7, Actual: 20"""
