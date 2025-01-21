"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
This problem involves solving a system of equations to determine how much money each person,甲 (A) and 乙 (B), holds. The problem is essentially a linear algebra problem, and the solution can be derived using the method described in the "方程術" (method of simultaneous equations). Below is the Python implementation:


"""


from fractions import Fraction

# Problem setup:
# Let A (甲) hold `x` money and B (乙) hold `y` money.
# Equation 1: A gets half of B's money and has 50 in total: x + y/2 = 50
# Equation 2: B gets more than half of A's money and also has 50 in total: y + (3/2)x = 50

# Represent the equations:
# Equation 1: x + y/2 = 50
# Equation 2: y + (3/2)x = 50

# Rewrite the equations in standard form:
# Equation 1: 2x + y = 100
# Equation 2: 3x + 2y = 100

# Solve using the method of elimination (方程術):

# Step 1: Eliminate `y` by making the coefficients of `y` in both equations equal.
# Multiply Equation 1 by 2: 4x + 2y = 200
# Equation 2 remains: 3x + 2y = 100

# Step 2: Subtract Equation 2 from the modified Equation 1 to eliminate `y`.
# (4x + 2y) - (3x + 2y) = 200 - 100
# x = 100

# Step 3: Substitute `x = 100` into one of the original equations to solve for `y`.
# Using Equation 1: 2x + y = 100
# 2(100) + y = 100
# 200 + y = 100
# y = -100

# Final result:
a = 100  # 甲持 a錢
b = -100  # 乙持 b錢

# Answer:
print(f"甲持 {a} 錢，乙持 {b} 錢。")


"""


### Explanation of the Code:
1. The problem is modeled as a system of two linear equations.
2. The equations are rewritten in standard form for easier manipulation.
3. The method of elimination is used to solve for one variable at a time.
4. The solution is then substituted back into one of the original equations to find the other variable.

### Answer:
甲持 `a = 100` 錢，乙持 `b = -100` 錢.
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
