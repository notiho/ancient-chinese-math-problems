"""
今有武馬一匹中馬二匹下馬三匹皆載四十石至阪皆不能上武馬借中馬一匹中馬借下馬一匹下馬借武馬一匹乃皆上問武中下馬一匹各力引幾何
術曰如方程各置所借以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰武馬一匹力引 a石 中馬一匹力引 b石 下馬一匹力引 c石 
"""

"""
This problem involves solving a system of equations using the ancient Chinese method of "fangcheng" (方程), which is an early form of linear algebra. The problem describes three types of horses (武馬, 中馬, 下馬) and their respective contributions to carrying loads. Let's translate the procedure into Python code step by step.

### Problem Setup
- 武馬 (Wuma) = 1 horse
- 中馬 (Zhongma) = 2 horses
- 下馬 (Xiama) = 3 horses
- Each horse carries 40 shi (石), but they cannot ascend the slope alone.
- Borrowing occurs between the horses, and we need to calculate the pulling force (力引) of each type of horse.

The procedure involves setting up equations based on the borrowing and solving them using the described method.

### Procedure
The procedure describes how to solve the equations step by step using elimination and substitution. Below is the Python implementation:


"""


from fractions import Fraction

# Define the total load and borrowing relationships
# 武馬借中馬1匹, 中馬借下馬1匹, 下馬借武馬1匹
# Let the pulling force of 武馬 = a, 中馬 = b, 下馬 = c

# Step 1: Set up the equations based on the problem description
# 武馬借中馬: a + b = 40
# 中馬借下馬: b + c = 40
# 下馬借武馬: c + a = 40

# Step 2: Solve the system of equations using the described method
# Add all three equations:
# (a + b) + (b + c) + (c + a) = 40 + 40 + 40
# 2a + 2b + 2c = 120
# Simplify:
a_plus_b_plus_c = Fraction(120, 2)  # a + b + c = 60

# From the first equation: a + b = 40
# Substitute into a + b + c = 60:
c = a_plus_b_plus_c - 40  # c = 60 - 40 = 20

# From the second equation: b + c = 40
# Substitute c = 20:
b = 40 - c  # b = 40 - 20 = 20

# From the third equation: c + a = 40
# Substitute c = 20:
a = 40 - c  # a = 40 - 20 = 20

# Step 3: Output the results
a = Fraction(a)  # 武馬 pulling force
b = Fraction(b)  # 中馬 pulling force
c = Fraction(c)  # 下馬 pulling force

# Final Answer
print(f"武馬一匹力引 {a} 石")
print(f"中馬一匹力引 {b} 石")
print(f"下馬一匹力引 {c} 石")


"""


### Explanation of the Code
1. **Equations Setup**: The problem gives three equations based on the borrowing relationships between the horses.
2. **Summation**: Adding all three equations simplifies the system and allows us to solve for the sum of the pulling forces.
3. **Substitution**: Using the simplified equations, we substitute values to solve for each variable step by step.
4. **Output**: The pulling force for each type of horse is calculated and displayed.

### Final Answer
武馬一匹力引 `20` 石  
中馬一匹力引 `20` 石  
下馬一匹力引 `20` 石
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
