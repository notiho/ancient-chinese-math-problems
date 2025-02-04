"""
今有武馬一匹中馬二匹下馬三匹皆載四十石至阪皆不能上武馬借中馬一匹中馬借下馬一匹下馬借武馬一匹乃皆上問武中下馬一匹各力引幾何
術曰如方程各置所借以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰武馬一匹力引 a石 中馬一匹力引 b石 下馬一匹力引 c石 
"""

"""
This is a classic problem involving a system of linear equations, solved using the ancient Chinese "fangcheng" (方程) method. The problem describes three types of horses (武馬, 中馬, 下馬) and their respective contributions to carrying loads. Let's translate the procedure into Python code step by step.

### Problem Description:
- A 武馬 (strong horse) can carry 40 shi but cannot climb a slope alone.
- A 中馬 (medium horse) and a 下馬 (weak horse) also cannot climb the slope alone.
- To solve the problem, the horses borrow strength from each other:
  - 武馬 borrows a 中馬.
  - 中馬 borrows a 下馬.
  - 下馬 borrows a 武馬.
- The goal is to determine the carrying capacity (力引) of each horse type.

### Procedure:
The procedure uses the fangcheng method (similar to solving a system of linear equations). Each horse's contribution is represented as a variable, and the relationships are encoded into equations.


"""

#----- content starts here -----

from fractions import Fraction

# Define the total load and borrowing relationships
total_load = 40  # Each horse is expected to carry 40 shi

# Step 1: Set up the equations
# Let:
# a = 武馬's carrying capacity (力引)
# b = 中馬's carrying capacity (力引)
# c = 下馬's carrying capacity (力引)

# The equations based on the problem are:
# 武馬 + 中馬 = 40
# 中馬 + 下馬 = 40
# 下馬 + 武馬 = 40

# Step 2: Solve the equations using the fangcheng method
# Add all three equations:
# (武馬 + 中馬) + (中馬 + 下馬) + (下馬 + 武馬) = 40 + 40 + 40
# 2 * (武馬 + 中馬 + 下馬) = 120
# 武馬 + 中馬 + 下馬 = 60

# Now solve for each variable:
# 武馬 = (武馬 + 中馬 + 下馬) - (中馬 + 下馬)
# 中馬 = (武馬 + 中馬 + 下馬) - (下馬 + 武馬)
# 下馬 = (武馬 + 中馬 + 下馬) - (武馬 + 中馬)

# Step 3: Calculate the results
武馬 = Fraction(60 - 40)
中馬 = Fraction(60 - 40)
下馬 = Fraction(60 - 40)

# Output the results
a = 武馬
b = 中馬
c = 下馬

print(f"武馬一匹力引 {a} 石")
print(f"中馬一匹力引 {b} 石")
print(f"下馬一匹力引 {c} 石")
#----- content ends here -----


"""


### Explanation:
1. The equations are derived from the borrowing relationships.
2. The sum of all horses' capacities is calculated first.
3. Each horse's capacity is determined by subtracting the capacities of the other two horses from the total.

### Answer:
武馬一匹力引 `a` 石  
中馬一匹力引 `b` 石  
下馬一匹力引 `c` 石
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
