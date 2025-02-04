"""
今有甲乙二人持錢不知其數甲得乙半而錢五十乙得甲太半而亦錢五十問甲乙持錢各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰甲持 a錢 乙持 b錢 
"""

"""
This problem involves solving a system of equations based on the given relationships between the amounts of money held by two individuals, A (甲) and B (乙). The solution can be derived using the ancient Chinese "fangcheng" (方程) method, which is an early form of solving simultaneous linear equations. Below is the Python implementation of the procedure:


"""

#----- content starts here -----

from fractions import Fraction

# Problem setup:
# Let 甲持錢 = x (money held by A)
# Let 乙持錢 = y (money held by B)
# Equations:
# 1. x = y / 2 + 50
# 2. y = x * 3 / 2 + 50

# Step 1: Express the equations in terms of a system of linear equations.
# Rewrite the equations:
# x - y / 2 = 50  --> Multiply through by 2 to eliminate the fraction: 2x - y = 100
# y - 3x / 2 = 50 --> Multiply through by 2 to eliminate the fraction: 2y - 3x = 100

# Step 2: Solve the system of equations using the fangcheng method.

# Coefficients of the equations:
# Equation 1: 2x - y = 100
# Equation 2: -3x + 2y = 100

# Representing the system in matrix form:
# |  2  -1 |   | x |   = | 100 |
# | -3   2 | * | y |   = | 100 |

# Step 3: Use fangcheng (elimination) to solve for x and y.

# Multiply the first equation by 2 (to align coefficients of y):
# 4x - 2y = 200
# -3x + 2y = 100

# Add the two equations to eliminate y:
# (4x - 2y) + (-3x + 2y) = 200 + 100
# x = 300

# Substitute x = 300 into the first equation to solve for y:
# 2x - y = 100
# 2(300) - y = 100
# 600 - y = 100
# y = 500

# Final result:
a = 300  # 甲持錢
b = 500  # 乙持錢

# Output the results:
print(f"甲持 {a} 錢")
print(f"乙持 {b} 錢")
#----- content ends here -----


"""


### Explanation of the Solution:
1. The problem is modeled as a system of two linear equations based on the relationships described:
   - A (甲) has half of B's (乙) money plus 50.
   - B (乙) has 1.5 times A's (甲) money plus 50.
2. The equations are rewritten to eliminate fractions and represented in matrix form.
3. The fangcheng method (elimination) is applied to solve for the unknowns `x` (A's money) and `y` (B's money).
4. The solution is found to be:
   - A (甲) holds 300 units of money.
   - B (乙) holds 500 units of money.

### Answer:
甲持 a = 300 錢  
乙持 b = 500 錢
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 300
Variable 'b' has wrong value. Expected: 25, Actual: 500"""
