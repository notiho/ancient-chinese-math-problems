"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
This problem involves solving a system of linear equations to determine the pulling power of three types of horses: 武馬 (strong horse), 中馬 (medium horse), and 下馬 (weak horse). The solution follows the ancient Chinese method of solving simultaneous equations, as described in the problem.

Here is the Python implementation:


"""


from fractions import Fraction

# 武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。
# 武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。

# Let:
# x = pulling power of 武馬 (strong horse)
# y = pulling power of 中馬 (medium horse)
# z = pulling power of 下馬 (weak horse)

# Formulate the equations based on the problem:
# 武馬借中馬一匹: x + y = 40
# 中馬借下馬一匹: y + z = 40
# 下馬借武馬一匹: z + x = 40

# Step 1: Represent the equations
# x + y = 40
# y + z = 40
# z + x = 40

# Step 2: Solve the equations using elimination (as described in the 方程術)

# Add all three equations:
# (x + y) + (y + z) + (z + x) = 40 + 40 + 40
# 2x + 2y + 2z = 120
# Divide through by 2:
x_plus_y_plus_z = 60  # x + y + z = 60

# Use x + y = 40 to find z:
z = x_plus_y_plus_z - 40  # z = (x + y + z) - (x + y)
z = 20

# Use y + z = 40 to find x:
x = x_plus_y_plus_z - 40  # x = (x + y + z) - (y + z)
x = 20

# Use z + x = 40 to find y:
y = x_plus_y_plus_z - 40  # y = (x + y + z) - (z + x)
y = 20

# Step 3: Output the results
a, b = 1, x  # 武馬 (strong horse): 1匹, pulling power b石
c, d = 1, y  # 中馬 (medium horse): 1匹, pulling power d石
e, f = 1, z  # 下馬 (weak horse): 1匹, pulling power f石

# Final answer:
print(f"武馬 {a}匹 力引 {b}石")
print(f"中馬 {c}匹 力引 {d}石")
print(f"下馬 {e}匹 力引 {f}石")


"""


### Explanation:
1. The problem is translated into three linear equations based on the borrowing and pulling conditions.
2. The equations are solved using elimination, as described in the ancient Chinese method.
3. The results are presented as the pulling power of each type of horse.

### Answer:
```
武馬 1匹 力引 20石
中馬 1匹 力引 20石
下馬 1匹 力引 20石
```
"""


"""
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'd' has wrong value. Expected: 120/7, Actual: 20
Variable 'f' has wrong value. Expected: 40/7, Actual: 20"""
