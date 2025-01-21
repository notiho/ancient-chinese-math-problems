"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
To solve this problem using the described "方程術" (method of equations), we will translate the problem into a system of equations and solve it step by step in Python. Here's the solution:


"""


from fractions import Fraction

# Let 甲持錢 be x and 乙持錢 be y
# Equation 1: 甲得乙半而錢五十 -> x + y/2 = 50
# Equation 2: 乙得甲太半而亦錢五十 -> y + (3/2)x = 50

# Step 1: Express the equations in terms of x and y
# Equation 1: 2x + y = 100
# Equation 2: 3x + 2y = 100

# Step 2: Solve the system of equations using elimination
# Multiply Equation 1 by 2 to align coefficients of y
# 4x + 2y = 200
# Subtract Equation 2 from this result
# (4x + 2y) - (3x + 2y) = 200 - 100
# x = 100

# Step 3: Substitute x = 100 into Equation 1 to find y
# 2(100) + y = 100
# y = 100 - 200
# y = 0

# Final results
a = 100  # 甲持錢
b = 0    # 乙持錢

# Output the results
print(f"甲持錢: {a}錢")
print(f"乙持錢: {b}錢")


"""


This solution follows the structure of the "方程術" by systematically solving the equations step by step. The final result is:

甲持錢: 100錢  
乙持錢: 0錢
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: 0"""
