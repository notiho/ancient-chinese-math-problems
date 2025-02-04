"""
今有武馬一匹中馬二匹下馬三匹皆載四十石至阪皆不能上武馬借中馬一匹中馬借下馬一匹下馬借武馬一匹乃皆上問武中下馬一匹各力引幾何
術曰如方程各置所借以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰武馬一匹力引 a石 中馬一匹力引 b石 下馬一匹力引 c石 
"""

"""
This problem involves solving a system of equations using the ancient Chinese "fangcheng" (方程) method, which is an early form of linear algebra. The problem describes three types of horses (武馬, 中馬, 下馬) and their respective contributions to carrying loads up a slope. The solution involves setting up equations based on the borrowing and sharing of loads and solving for the individual carrying capacities of each type of horse.

Here is the solution translated into Python code:


"""


from fractions import Fraction

# 武馬一匹, 中馬二匹, 下馬三匹, each carrying 40 石
武馬 = 1
中馬 = 2
下馬 = 3
載重 = 40

# Total load carried by all horses
總載重 = 武馬 * 載重 + 中馬 * 載重 + 下馬 * 載重

# Step 1: Set up the equations
# 武馬借中馬一匹, 中馬借下馬一匹, 下馬借武馬一匹
# Let a = 武馬's carrying capacity, b = 中馬's carrying capacity, c = 下馬's carrying capacity
# The equations are:
# 1. 武馬 + 中馬 = 40
# 2. 中馬 + 下馬 = 40
# 3. 下馬 + 武馬 = 40

# Step 2: Solve the equations using the fangcheng method
# Rewrite the equations:
# a + b = 40
# b + c = 40
# c + a = 40

# Express b in terms of a: b = 40 - a
# Substitute b into the second equation: (40 - a) + c = 40
# Simplify: c = a
# Substitute c into the third equation: a + (40 - a) = 40
# Simplify: a = 20, b = 20, c = 20

# Step 3: Assign the results
a = Fraction(20)  # 武馬's carrying capacity
b = Fraction(20)  # 中馬's carrying capacity
c = Fraction(20)  # 下馬's carrying capacity

# Output the results
print(f"武馬一匹力引 {a} 石")
print(f"中馬一匹力引 {b} 石")
print(f"下馬一匹力引 {c} 石")


"""


### Explanation of the Code:
1. **Setup**: The problem is translated into three equations based on the borrowing and sharing of loads.
2. **Fangcheng Method**: The equations are solved step by step, substituting variables and simplifying until the values of `a`, `b`, and `c` are determined.
3. **Results**: The carrying capacities of 武馬, 中馬, and 下馬 are calculated and displayed.

### Answer:
- 武馬一匹力引 `20` 石
- 中馬一匹力引 `20` 石
- 下馬一匹力引 `20` 石
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
