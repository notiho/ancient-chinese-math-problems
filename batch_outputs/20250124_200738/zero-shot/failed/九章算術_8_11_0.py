"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the pulling power of three types of horses: 武馬 (a), 中馬 (b), and 下馬 (c). The solution will use the `Fraction` class to handle fractional results.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem description
# Let a, b, c represent the pulling power of 武馬, 中馬, and 下馬 respectively.

# Equation 1: 武馬借中馬一匹 (武馬 + 中馬 = 40)
# Equation 2: 中馬借下馬一匹 (中馬 + 下馬 = 40)
# Equation 3: 下馬借武馬一匹 (下馬 + 武馬 = 40)

# Solve the system of equations
# From Equation 1: a + b = 40
# From Equation 2: b + c = 40
# From Equation 3: c + a = 40

# Rearrange the equations to express a, b, and c in terms of each other:
# a = 40 - b
# b = 40 - c
# c = 40 - a

# Substitute these into one another to solve for a, b, and c:
# Substitute b = 40 - c into a = 40 - b:
# a = 40 - (40 - c)
# a = c

# Substitute c = 40 - a into b = 40 - c:
# b = 40 - (40 - a)
# b = a

# Since a = b = c, substitute into any equation, e.g., a + b = 40:
# a + a = 40
# 2a = 40
# a = 20

# Therefore, a = 20, b = 20, c = 20

# Assign the results to variables
a = Fraction(20)  # 武馬 pulling power
b = Fraction(20)  # 中馬 pulling power
c = Fraction(20)  # 下馬 pulling power

# Results
print(f"武馬 pulling power (a): {a} 石")
print(f"中馬 pulling power (b): {b} 石")
print(f"下馬 pulling power (c): {c} 石")
#----- content ends here -----


"""


### Explanation:
1. The problem provides three equations based on the pulling power of the horses when they borrow power from each other.
2. By solving the system of equations, we find that all three types of horses have the same pulling power.
3. The solution is expressed using the `Fraction` class to ensure accuracy and clarity.

### Output:
```
武馬 pulling power (a): 20 石
中馬 pulling power (b): 20 石
下馬 pulling power (c): 20 石
```
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
