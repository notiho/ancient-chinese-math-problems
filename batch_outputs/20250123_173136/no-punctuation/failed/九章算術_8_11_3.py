"""
今有武馬一匹中馬二匹下馬三匹皆載四十石至阪皆不能上武馬借中馬一匹中馬借下馬一匹下馬借武馬一匹乃皆上問武中下馬一匹各力引幾何
術曰如方程各置所借以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰武馬一匹力引 a石 中馬一匹力引 b石 下馬一匹力引 c石 
"""

"""
This is a classic problem involving a system of linear equations, where the strength of each type of horse (武馬, 中馬, 下馬) is determined based on the loads they can carry and the borrowing arrangement described. The solution involves setting up and solving the equations using the method described in the "方程術" (method of solving equations). Let's translate this into Python code:


"""


from fractions import Fraction

# Problem setup
# 武馬 (x), 中馬 (y), 下馬 (z)
# Each horse carries 40 石, but they cannot ascend the slope alone.
# Borrowing arrangement:
# 武馬 borrows 1 中馬
# 中馬 borrows 1 下馬
# 下馬 borrows 1 武馬

# Equation setup based on the problem description:
# 武馬 + 中馬 = 40 (武馬 borrows 1 中馬)
# 中馬 + 下馬 = 40 (中馬 borrows 1 下馬)
# 下馬 + 武馬 = 40 (下馬 borrows 1 武馬)

# Representing the equations:
# x + y = 40
# y + z = 40
# z + x = 40

# Solving the equations:
# From the first equation: y = 40 - x
# Substitute y into the second equation: (40 - x) + z = 40
# Simplify: z = x
# Substitute z = x into the third equation: x + x = 40
# Simplify: 2x = 40
# Solve for x: x = 20
# Substitute x = 20 into z = x: z = 20
# Substitute x = 20 into y = 40 - x: y = 20

# Results:
a = Fraction(20)  # 武馬 (x)
b = Fraction(20)  # 中馬 (y)
c = Fraction(20)  # 下馬 (z)

# Output the results
print(f"武馬一匹力引 {a} 石")
print(f"中馬一匹力引 {b} 石")
print(f"下馬一匹力引 {c} 石")


"""


### Explanation:
1. The problem describes a system of linear equations based on the borrowing arrangement of the horses.
2. Using substitution and elimination, the equations are solved step by step.
3. The solution shows that each type of horse (武馬, 中馬, 下馬) has the same pulling strength of 20 石.

### Answer:
武馬一匹力引 20 石  
中馬一匹力引 20 石  
下馬一匹力引 20 石
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
