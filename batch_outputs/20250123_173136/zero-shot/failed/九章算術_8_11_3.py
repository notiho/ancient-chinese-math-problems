"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the pulling power of three types of horses: 武馬 (a), 中馬 (b), and 下馬 (c). Each horse's pulling power is represented in terms of "石" (a unit of weight). The solution will use the `Fraction` class to handle any fractional results.

Here is the Python code:


"""


from fractions import Fraction

# Given equations based on the problem:
# 武馬 (a), 中馬 (b), 下馬 (c)
# 1. a + b = 40
# 2. b + c = 40
# 3. c + a = 40

# Solve the system of equations:
# Adding all three equations:
# (a + b) + (b + c) + (c + a) = 40 + 40 + 40
# 2a + 2b + 2c = 120
# a + b + c = 60

# Substituting back to find individual values:
# From a + b = 40, we get c = 60 - 40 = 20
# From b + c = 40, we get a = 60 - 40 = 20
# From c + a = 40, we get b = 60 - 40 = 20

a = Fraction(20)  # 武馬 pulling power
b = Fraction(20)  # 中馬 pulling power
c = Fraction(20)  # 下馬 pulling power

# Results
print(f"武馬 (a) pulling power: {a} 石")
print(f"中馬 (b) pulling power: {b} 石")
print(f"下馬 (c) pulling power: {c} 石")


"""


### Explanation:
1. The problem provides three equations:
   - \( a + b = 40 \)
   - \( b + c = 40 \)
   - \( c + a = 40 \)

2. Adding all three equations together gives:
   - \( 2a + 2b + 2c = 120 \)
   - Simplify to \( a + b + c = 60 \).

3. Using the total \( a + b + c = 60 \), we substitute back into the original equations to find each variable:
   - \( c = 60 - (a + b) = 60 - 40 = 20 \)
   - \( a = 60 - (b + c) = 60 - 40 = 20 \)
   - \( b = 60 - (c + a) = 60 - 40 = 20 \)

4. The solution is \( a = 20 \), \( b = 20 \), \( c = 20 \).

### Output:
```
武馬 (a) pulling power: 20 石
中馬 (b) pulling power: 20 石
下馬 (c) pulling power: 20 石
```
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
