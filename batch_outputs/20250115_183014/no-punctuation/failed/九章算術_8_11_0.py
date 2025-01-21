"""
今有武馬一匹中馬二匹下馬三匹皆載四十石至阪皆不能上武馬借中馬一匹中馬借下馬一匹下馬借武馬一匹乃皆上問武中下馬一匹各力引幾何
術曰如方程各置所借以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰武馬 a匹 力引 b石 中馬 c匹 力引 d石 下馬 e匹 力引 f石 
"""

"""
This is a complex problem involving a system of equations to determine the pulling strength of each type of horse (武馬, 中馬, 下馬). The procedure uses a method akin to solving simultaneous equations, referred to as "方程術" (method of equations). Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# Problem setup
# 武馬 (W), 中馬 (M), 下馬 (L)
# 武馬借中馬一匹, 中馬借下馬一匹, 下馬借武馬一匹
# Each horse carries 40 石, and the total load is 39 石 (or 390 斗, as 1 石 = 10 斗).

# Define the system of equations based on the problem:
# Let W, M, L represent the pulling strength of 武馬, 中馬, 下馬 respectively.
# Equation 1: 武馬借中馬 => W + M = 40
# Equation 2: 中馬借下馬 => M + L = 40
# Equation 3: 下馬借武馬 => L + W = 40

# Step 1: Solve for W, M, L using the equations
# From Equation 1: W = 40 - M
# From Equation 2: L = 40 - M
# Substitute into Equation 3: (40 - M) + (40 - M) = 40
# Simplify: 80 - 2M = 40
# Solve for M: M = 20
M = 20

# Step 2: Solve for W using Equation 1
W = 40 - M  # W = 40 - 20
W = 20

# Step 3: Solve for L using Equation 2
L = 40 - M  # L = 40 - 20
L = 20

# Step 4: Calculate the pulling strength in 石 for each horse
# 武馬 (W), 中馬 (M), 下馬 (L)
a = 1  # 武馬 1 匹
b = W  # 武馬 pulling strength in 石
c = 1  # 中馬 1 匹
d = M  # 中馬 pulling strength in 石
e = 1  # 下馬 1 匹
f = L  # 下馬 pulling strength in 石

# Final results
print(f"武馬 {a} 匹 力引 {b} 石")
print(f"中馬 {c} 匹 力引 {d} 石")
print(f"下馬 {e} 匹 力引 {f} 石")


"""


### Explanation of the Code:
1. The problem is translated into a system of linear equations:
   - \( W + M = 40 \)
   - \( M + L = 40 \)
   - \( L + W = 40 \)
2. The equations are solved step by step to find the values of \( W \), \( M \), and \( L \).
3. The results are presented as the pulling strength (in 石) for each type of horse.

### Answer:
- 武馬 \( a = 1 \) 匹, 力引 \( b = 20 \) 石
- 中馬 \( c = 1 \) 匹, 力引 \( d = 20 \) 石
- 下馬 \( e = 1 \) 匹, 力引 \( f = 20 \) 石
"""


"""
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'd' has wrong value. Expected: 120/7, Actual: 20
Variable 'f' has wrong value. Expected: 40/7, Actual: 20"""
