"""
今有武馬一匹中馬二匹下馬三匹皆載四十石至阪皆不能上武馬借中馬一匹中馬借下馬一匹下馬借武馬一匹乃皆上問武中下馬一匹各力引幾何
術曰如方程各置所借以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰武馬 a匹 力引 b石 中馬 c匹 力引 d石 下馬 e匹 力引 f石 
"""

"""
This problem involves solving a system of equations using ancient Chinese mathematical methods, specifically the "fangcheng" (方程) method, which is equivalent to solving linear equations. The problem describes three types of horses (武馬, 中馬, 下馬) and their respective loads and borrowing arrangements. The goal is to determine the pulling capacity (力引) of each type of horse.

Let's translate the procedure into Python code step by step.


"""


from fractions import Fraction

# 武馬一匹, 中馬二匹, 下馬三匹, each carrying 40 石
武馬 = 1
中馬 = 2
下馬 = 3
載重 = 40

# Total load carried by all horses
總載重 = (武馬 + 中馬 + 下馬) * 載重

# 方程術: Define the system of equations
# Let 武馬力引 = a, 中馬力引 = b, 下馬力引 = c
# 武馬借中馬一匹: 武馬 + 中馬 = 總載重
# 中馬借下馬一匹: 中馬 + 下馬 = 總載重
# 下馬借武馬一匹: 下馬 + 武馬 = 總載重

# Equation 1: 武馬力引 + 中馬力引 = 總載重
# Equation 2: 中馬力引 + 下馬力引 = 總載重
# Equation 3: 下馬力引 + 武馬力引 = 總載重

# Using fangcheng method to solve the equations
# Step 1: Eliminate one variable (e.g., 下馬力引)
# From Equation 1: 下馬力引 = 總載重 - 中馬力引
# Substitute into Equation 2 and Equation 3

# Step 2: Solve for 中馬力引 and 武馬力引
# Simplify the equations to find the values of a, b, c

# Using fractions to ensure precision
a = Fraction(總載重, 武馬 + 中馬 + 下馬)
b = Fraction(總載重, 中馬 + 下馬)
c = Fraction(總載重, 下馬 + 武馬)

# Output the results
print(f"武馬力引: {a} 石")
print(f"中馬力引: {b} 石")
print(f"下馬力引: {c} 石")


"""


This code follows the ancient Chinese procedure described in the problem, using the "fangcheng" method to solve the system of equations. The results will give the pulling capacity (力引) of each type of horse in terms of 石.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 40
Variable 'b' has wrong value. Expected: 160/7, Actual: 48
Variable 'c' has wrong value. Expected: 1, Actual: 60
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
