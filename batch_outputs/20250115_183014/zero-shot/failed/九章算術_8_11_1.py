"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves determining the pulling power of three types of horses (武馬, 中馬, 下馬) when they cooperate under certain conditions. We'll use the `Fraction` class to handle the calculations.

Here is the Python code:


"""


from fractions import Fraction

# Let the pulling power of 武馬, 中馬, and 下馬 be a, b, and c respectively (in 石).
# The equations are derived from the problem statement:
# 武馬借中馬一匹, 中馬借下馬一匹, 下馬借武馬一匹, 皆能上阪.

# Equation 1: 武馬 + 中馬 = 40
# Equation 2: 中馬 + 下馬 = 40
# Equation 3: 下馬 + 武馬 = 40

# Solving the system of equations:
# From Equation 1: 武馬 = 40 - 中馬
# Substitute into Equation 3: 下馬 + (40 - 中馬) = 40
# Simplify: 下馬 = 中馬
# Substitute 下馬 = 中馬 into Equation 2: 中馬 + 中馬 = 40
# Simplify: 2 * 中馬 = 40
# Solve for 中馬: 中馬 = 20

# Now that we know 中馬 = 20, substitute back to find 武馬 and 下馬:
c = Fraction(20)  # 中馬 pulling power
e = c             # 下馬 pulling power (same as 中馬)
a = Fraction(40) - c  # 武馬 pulling power

# Assign the results to variables with the appropriate names:
b = a  # 武馬 pulling power
d = c  # 中馬 pulling power
f = e  # 下馬 pulling power

# Results:
print(f"武馬 pulling power (a): {b} 石")
print(f"中馬 pulling power (c): {d} 石")
print(f"下馬 pulling power (e): {f} 石")


"""


### Explanation:
1. The problem is translated into a system of linear equations based on the conditions described.
2. The equations are solved step-by-step using substitution and simplification.
3. The `Fraction` class ensures that all calculations are precise and can handle non-integer results if necessary.
4. The results are stored in variables `a`, `b`, `c`, `d`, `e`, and `f` as required.

### Output:
```
武馬 pulling power (a): 20 石
中馬 pulling power (c): 20 石
下馬 pulling power (e): 20 石
```
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 20
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'c' has wrong value. Expected: 1, Actual: 20
Variable 'd' has wrong value. Expected: 120/7, Actual: 20
Variable 'e' has wrong value. Expected: 1, Actual: 20
Variable 'f' has wrong value. Expected: 40/7, Actual: 20"""
