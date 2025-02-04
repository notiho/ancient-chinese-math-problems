"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
This problem is a classic system of linear equations problem from ancient Chinese mathematics. It involves determining the pulling power of three types of horses (武馬, 中馬, 下馬) based on their interactions and borrowing of power. Below is the solution translated into Python code, following the procedure described.


"""


from fractions import Fraction

# 武馬一匹, 中馬二匹, 下馬三匹, 各載四十石至阪
武馬 = 1
中馬 = 2
下馬 = 3
載重 = 40

# 借力的方程
# 武馬借中馬一匹, 中馬借下馬一匹, 下馬借武馬一匹
# 方程表示：
# 武馬 + 中馬 = 40
# 中馬 + 下馬 = 40
# 下馬 + 武馬 = 40

# 置上禾三秉, 中禾二秉, 下禾一秉
# Translate the equations into a system of linear equations:
# Let 武馬 = x, 中馬 = y, 下馬 = z
# x + y = 40
# y + z = 40
# z + x = 40

# Solve using substitution and elimination:
# Step 1: Express x, y, z in terms of each other
# From x + y = 40, we get x = 40 - y
# From y + z = 40, we get z = 40 - y
# Substitute z = 40 - y into z + x = 40:
# (40 - y) + x = 40
# x = y

# Step 2: Substitute x = y into x + y = 40:
# y + y = 40
# 2y = 40
# y = 20
# x = y = 20
# z = 40 - y = 20

# Results:
a = 20  # 武馬一匹力引 20 石
b = 20  # 中馬一匹力引 20 石
c = 20  # 下馬一匹力引 20 石

# Output the results
print(f"武馬一匹力引 {a} 石，中馬一匹力引 {b} 石，下馬一匹力引 {c} 石。")


"""


### Explanation:
1. The problem is modeled as a system of three linear equations based on the borrowing of power between the horses.
2. The equations are solved step-by-step using substitution and elimination, following the ancient Chinese method described in the procedure.
3. The solution shows that each horse (武馬, 中馬, 下馬) has the same pulling power of 20 石.

### Answer:
武馬一匹力引 **20 石**，中馬一匹力引 **20 石**，下馬一匹力引 **20 石**.
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
