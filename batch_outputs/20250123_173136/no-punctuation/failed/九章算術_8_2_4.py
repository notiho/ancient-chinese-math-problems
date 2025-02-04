"""
今有上禾二秉中禾三秉下禾四秉實皆不滿斗上取中中取下下取上各一秉而實滿斗問上中下禾實一秉各幾何
術曰如方程各置所取以正負術入之正負術曰同名相除異名相益正無入負之負無入正之其異名相除同名相益正無入正之負無入負之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a斗 中禾一秉實 b斗 下禾一秉實 c斗 
"""

"""
This problem involves solving a system of equations to determine the actual volume of grain in one sheaf of upper, middle, and lower grains. The procedure uses ancient Chinese methods for solving simultaneous equations, which are described in the problem statement. Below is the Python implementation:


"""


from fractions import Fraction

# 上禾二秉，中禾三秉，下禾四秉
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 實皆不滿斗，上取中，中取下，下取上，各一秉而實滿斗
# This gives the equations:
# 上禾 + 中禾 = 1
# 中禾 + 下禾 = 1
# 下禾 + 上禾 = 1

# 方程術解法
# Using the equations:
# 上禾 + 中禾 = 1
# 中禾 + 下禾 = 1
# 下禾 + 上禾 = 1

# Step 1: Express the equations in terms of coefficients and constants
# Coefficients matrix:
# [1, 1, 0] [上禾]
# [0, 1, 1] [中禾]
# [1, 0, 1] [下禾]
# Constants vector: [1, 1, 1]

# Step 2: Solve using elimination or substitution
# Add the three equations:
# (上禾 + 中禾) + (中禾 + 下禾) + (下禾 + 上禾) = 1 + 1 + 1
# 2上禾 + 2中禾 + 2下禾 = 3
# 上禾 + 中禾 + 下禾 = 3/2

# Substitute 上禾 + 中禾 = 1 into 上禾 + 中禾 + 下禾 = 3/2:
# 1 + 下禾 = 3/2
# 下禾 = 3/2 - 1 = 1/2

# Substitute 下禾 = 1/2 into 中禾 + 下禾 = 1:
# 中禾 + 1/2 = 1
# 中禾 = 1 - 1/2 = 1/2

# Substitute 中禾 = 1/2 into 上禾 + 中禾 = 1:
# 上禾 + 1/2 = 1
# 上禾 = 1 - 1/2 = 1/2

# Results
a = Fraction(1, 2)  # 上禾一秉實
b = Fraction(1, 2)  # 中禾一秉實
c = Fraction(1, 2)  # 下禾一秉實

# Output the results
print(f"上禾一秉實 {a}斗")
print(f"中禾一秉實 {b}斗")
print(f"下禾一秉實 {c}斗")


"""


### Explanation:
1. The problem is translated into a system of three linear equations.
2. The equations are solved step by step using substitution and elimination, as described in the ancient Chinese procedure.
3. The solution is expressed in terms of fractions to maintain precision, as required by the problem.

### Answer:
- 上禾一秉實: 1/2斗
- 中禾一秉實: 1/2斗
- 下禾一秉實: 1/2斗
"""


"""
Variable 'a' has wrong value. Expected: 9/25, Actual: 1/2
Variable 'b' has wrong value. Expected: 7/25, Actual: 1/2
Variable 'c' has wrong value. Expected: 4/25, Actual: 1/2"""
