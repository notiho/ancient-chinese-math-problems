"""
今有上禾二秉中禾三秉下禾四秉實皆不滿斗上取中中取下下取上各一秉而實滿斗問上中下禾實一秉各幾何
術曰如方程各置所取以正負術入之正負術曰同名相除異名相益正無入負之負無入正之其異名相除同名相益正無入正之負無入負之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a斗 中禾一秉實 b斗 下禾一秉實 c斗 
"""

"""
This problem involves solving a system of equations using ancient Chinese mathematical methods, specifically the "正負術" (positive and negative method) and "方程術" (method of equations). Below is the Python implementation of the procedure described:


"""


from fractions import Fraction

# 上禾二秉, 中禾三秉, 下禾四秉
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 實皆不滿斗, 上取中, 中取下, 下取上, 各一秉而實滿斗
# Let 上禾一秉實 = a斗, 中禾一秉實 = b斗, 下禾一秉實 = c斗
# The equations are:
# 1. 上禾 + 中禾 = 1斗
# 2. 中禾 + 下禾 = 1斗
# 3. 下禾 + 上禾 = 1斗

# 方程術: Solve the system of equations
# Rewrite the equations:
# a + b = 1
# b + c = 1
# c + a = 1

# Step 1: Express one variable in terms of the others
# From the first equation: a = 1 - b
# Substitute into the third equation: c + (1 - b) = 1 -> c = b

# Step 2: Substitute c = b into the second equation
# b + b = 1 -> 2b = 1 -> b = 1/2

# Step 3: Solve for a and c
a = 1 - Fraction(1, 2)  # a = 1 - b
c = Fraction(1, 2)      # c = b

# The results:
b = Fraction(1, 2)  # 中禾一秉實
a = Fraction(1, 2)  # 上禾一秉實
c = Fraction(1, 2)  # 下禾一秉實

# Output the results
print(f"上禾一秉實 a = {a}斗")
print(f"中禾一秉實 b = {b}斗")
print(f"下禾一秉實 c = {c}斗")


"""


### Explanation of the Solution:
1. The problem describes a system of three equations based on the relationships between the contributions of the three types of grain (上禾, 中禾, 下禾) to a full dou.
2. Using substitution and elimination (as described in the 方程術), we solve for the amount of grain contributed by each type.
3. The solution shows that each type of grain contributes **1/2 dou** per秉.

### Answer:
- 上禾一秉實 a = 1/2斗
- 中禾一秉實 b = 1/2斗
- 下禾一秉實 c = 1/2斗
"""


"""
Variable 'a' has wrong value. Expected: 9/25, Actual: 1/2
Variable 'b' has wrong value. Expected: 7/25, Actual: 1/2
Variable 'c' has wrong value. Expected: 4/25, Actual: 1/2"""
