"""
今有武馬一匹中馬二匹下馬三匹皆載四十石至阪皆不能上武馬借中馬一匹中馬借下馬一匹下馬借武馬一匹乃皆上問武中下馬一匹各力引幾何
術曰如方程各置所借以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰武馬 a匹 力引 b石 中馬 c匹 力引 d石 下馬 e匹 力引 f石 
"""

"""
This problem involves solving a system of equations using the ancient Chinese "fangcheng" (方程) method, which is equivalent to solving simultaneous linear equations. The problem describes three types of horses (武馬, 中馬, 下馬) and their respective capacities to pull loads. The solution involves determining the pulling capacity of each type of horse.

Here is the solution encoded in Python:


"""


from fractions import Fraction

# Problem setup
# 武馬 (Wuma), 中馬 (Zhongma), 下馬 (Xiama)
# Each type of horse borrows another to successfully pull the load.
# The total load is 40 石 (shi).

# Define the equations based on the problem:
# Let 武馬 = a, 中馬 = b, 下馬 = c (their pulling capacities in 石)
# Equation 1: 武馬 + 中馬 = 40
# Equation 2: 中馬 + 下馬 = 40
# Equation 3: 下馬 + 武馬 = 40

# Step 1: Represent the equations in matrix form
# Coefficients matrix:
# [ 1  1  0 ]   [ a ]   [ 40 ]
# [ 0  1  1 ] * [ b ] = [ 40 ]
# [ 1  0  1 ]   [ c ]   [ 40 ]

# Step 2: Solve using fangcheng (elimination method)
# Add all three equations to find the total:
total = 40 + 40 + 40  # Sum of all right-hand sides
# Total pulling capacity of all horses (武馬 + 中馬 + 下馬):
total_capacity = total / 2  # Each pair is counted twice
# 武馬 + 中馬 + 下馬 = total_capacity
# a + b + c = total_capacity

# Step 3: Solve for each variable
# From Equation 1: a + b = 40
# Subtract Equation 2: (a + b) - (b + c) = 40 - 40
# a - c = 0 => a = c

# From Equation 2: b + c = 40
# Subtract Equation 3: (b + c) - (c + a) = 40 - 40
# b - a = 0 => b = a

# Since a = b = c, divide total_capacity by 3 to find each:
a = Fraction(total_capacity, 3)
b = a
c = a

# Step 4: Calculate pulling capacity of each horse
武馬_力引 = a
中馬_力引 = b
下馬_力引 = c

# Output the results
print(f"武馬: {1}匹, 力引: {武馬_力引}石")
print(f"中馬: {1}匹, 力引: {中馬_力引}石")
print(f"下馬: {1}匹, 力引: {下馬_力引}石")


"""


### Explanation:
1. The problem is reduced to a system of three linear equations.
2. Using the "fangcheng" method, we solve for the pulling capacity of each type of horse.
3. The solution shows that all three types of horses have equal pulling capacities, which is `40/3` 石 per horse.

### Answer:
- 武馬: 1匹, 力引: \( \frac{40}{3} \) 石
- 中馬: 1匹, 力引: \( \frac{40}{3} \) 石
- 下馬: 1匹, 力引: \( \frac{40}{3} \) 石
"""


"""
Code error: both arguments should be Rational instances"""
