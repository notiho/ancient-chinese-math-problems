"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "fangcheng" (方程) method. Below is the Python implementation of the procedure.


"""

#----- content starts here -----

from fractions import Fraction

# 武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上
武馬 = 1
中馬 = 2
下馬 = 3
載重 = 40

# 借力關係
# 武馬借中馬一匹
武借中 = 1
# 中馬借下馬一匹
中借下 = 1
# 下馬借武馬一匹
下借武 = 1

# 方程術：設置方程
# Let 武馬力 = x, 中馬力 = y, 下馬力 = z
# Equation 1: 武馬 + 中馬借力 = 40
# Equation 2: 中馬 + 下馬借力 = 40
# Equation 3: 下馬 + 武馬借力 = 40

# 方程表示：
# x + y = 40
# y + z = 40
# z + x = 40

# Step 1: Solve for x, y, z using substitution/elimination
# From Equation 1: x = 40 - y
# From Equation 2: y = 40 - z
# From Equation 3: z = 40 - x

# Substitute y = 40 - z into x = 40 - y
# x = 40 - (40 - z) = z
# Substitute z = 40 - x into y = 40 - z
# y = 40 - (40 - x) = x

# Therefore, x = y = z = 20

# 武馬一匹力引 a石
a = 20
# 中馬一匹力引 b石
b = 20
# 下馬一匹力引 c石
c = 20

# Output the results
print(f"武馬一匹力引 {a} 石")
print(f"中馬一匹力引 {b} 石")
print(f"下馬一匹力引 {c} 石")
#----- content ends here -----


"""


### Explanation:
1. The problem is translated into a system of linear equations based on the relationships between the horses' strengths and the loads they carry.
2. Using substitution and elimination, we solve for the strength of each horse (武馬, 中馬, 下馬).
3. The solution shows that each horse has the same pulling strength of 20 石.

### Answer:
- 武馬一匹力引 **20** 石
- 中馬一匹力引 **20** 石
- 下馬一匹力引 **20** 石
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
