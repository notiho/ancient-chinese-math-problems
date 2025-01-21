"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code. The problem involves solving a system of linear equations using elimination methods, as described in the "方程術" (method of equations). Let's proceed step by step.


"""


from fractions import Fraction

# 武馬 (x), 中馬 (y), 下馬 (z)
# Equations based on the problem:
# 1. 武馬借中馬一匹: x + y = 40
# 2. 中馬借下馬一匹: y + z = 40
# 3. 下馬借武馬一匹: z + x = 40

# Step 1: Represent the equations
# x + y = 40
# y + z = 40
# z + x = 40

# Step 2: Eliminate variables using the 方程術
# Add all three equations to find the total:
# (x + y) + (y + z) + (z + x) = 40 + 40 + 40
# 2x + 2y + 2z = 120
# Divide by 2:
x_plus_y_plus_z = 60

# Step 3: Solve for each variable
# From x + y + z = 60 and x + y = 40:
z = x_plus_y_plus_z - 40  # z = 60 - 40 = 20

# From x + y + z = 60 and y + z = 40:
x = x_plus_y_plus_z - 40  # x = 60 - 40 = 20

# From x + y + z = 60 and z + x = 40:
y = x_plus_y_plus_z - 40  # y = 60 - 40 = 20

# Step 4: Assign results
a = 1  # 武馬 1 匹
b = x  # 武馬力引 b 石

c = 1  # 中馬 1 匹
d = y  # 中馬力引 d 石

e = 1  # 下馬 1 匹
f = z  # 下馬力引 f 石

# Results
print(f"武馬 {a}匹 力引 {b}石")
print(f"中馬 {c}匹 力引 {d}石")
print(f"下馬 {e}匹 力引 {f}石")


"""


### Explanation:
1. We start by setting up the equations based on the problem description.
2. Using the method of elimination (as described in the "方程術"), we solve for the sum of all variables and then isolate each variable.
3. The results are assigned to the respective variables for 武馬, 中馬, and 下馬.

### Final Answer:
武馬 1匹 力引 20石  
中馬 1匹 力引 20石  
下馬 1匹 力引 20石
"""


"""
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'd' has wrong value. Expected: 120/7, Actual: 20
Variable 'f' has wrong value. Expected: 40/7, Actual: 20"""
