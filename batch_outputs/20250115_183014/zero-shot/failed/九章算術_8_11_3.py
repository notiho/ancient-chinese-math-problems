"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the pulling power of three types of horses (武馬, 中馬, 下馬). Here's the Python code:


"""


from fractions import Fraction

# Given conditions
# 武馬 (a匹) 力引 b石
# 中馬 (c匹) 力引 d石
# 下馬 (e匹) 力引 f石

# Let:
# 武馬's pulling power = b
# 中馬's pulling power = d
# 下馬's pulling power = f

# Equations based on the problem:
# 武馬借中馬一匹: b + d = 40
# 中馬借下馬一匹: d + f = 40
# 下馬借武馬一匹: f + b = 40

# Solve the system of equations:
# From b + d = 40, we get b = 40 - d
# From d + f = 40, we get f = 40 - d
# Substitute b and f into f + b = 40:
# (40 - d) + (40 - d) = 40
# 80 - 2d = 40
# 2d = 40
# d = 20

# Now substitute d back to find b and f:
d = Fraction(20)  # 中馬's pulling power
b = Fraction(40) - d  # 武馬's pulling power
f = Fraction(40) - d  # 下馬's pulling power

# Results:
a = Fraction(1)  # 武馬 count
c = Fraction(2)  # 中馬 count
e = Fraction(3)  # 下馬 count

# Output the results
print(f"武馬 a匹 力引 b石: a = {a}, b = {b}")
print(f"中馬 c匹 力引 d石: c = {c}, d = {d}")
print(f"下馬 e匹 力引 f石: e = {e}, f = {f}")


"""


### Explanation:
1. The problem gives three equations based on the pulling power of the horses when they borrow each other's strength.
2. We solve the system of equations to find the pulling power of each horse type.
3. The results are stored in variables `a`, `b`, `c`, `d`, `e`, and `f` as required.

### Output:
```
武馬 a匹 力引 b石: a = 1, b = 20
中馬 c匹 力引 d石: c = 2, d = 20
下馬 e匹 力引 f石: e = 3, f = 20
```
"""


"""
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'c' has wrong value. Expected: 1, Actual: 2
Variable 'd' has wrong value. Expected: 120/7, Actual: 20
Variable 'e' has wrong value. Expected: 1, Actual: 3
Variable 'f' has wrong value. Expected: 40/7, Actual: 20"""
