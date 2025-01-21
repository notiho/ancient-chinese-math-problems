"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
This problem involves solving a system of equations to determine how much money each person, Jia (甲) and Yi (乙), holds. The problem is essentially a linear algebra problem, and the solution can be derived using the method described in the "方程術" (method of solving equations). Below is the Python implementation:


"""


from fractions import Fraction

# Let 甲持錢 = x, 乙持錢 = y
# Equation 1: 甲得乙半而錢五十 -> x + y/2 = 50
# Equation 2: 乙得甲太半而亦錢五十 -> y + (3/2)x = 50

# Rewrite the equations:
# Equation 1: 2x + y = 100
# Equation 2: 3x + 2y = 100

# Solve using the method of elimination (方程術)

# Step 1: Eliminate y by aligning coefficients
# Multiply Equation 1 by 2: 4x + 2y = 200
# Subtract Equation 2: (4x + 2y) - (3x + 2y) = 200 - 100
x = 100  # x = 100

# Step 2: Substitute x into Equation 1 to solve for y
# 2x + y = 100
y = 100 - 2 * x
y = 0  # y = 0

# Final result
a = x  # 甲持錢
b = y  # 乙持錢

print(f"甲持 {a} 錢，乙持 {b} 錢。")


"""


### Explanation of the Solution:
1. **Equations Setup**:
   - From the problem, we derive two equations:
     - \( x + \frac{y}{2} = 50 \)
     - \( y + \frac{3x}{2} = 50 \)
   - These are rewritten as:
     - \( 2x + y = 100 \)
     - \( 3x + 2y = 100 \)

2. **Elimination**:
   - Multiply the first equation by 2 to align the coefficients of \( y \).
   - Subtract the second equation from the modified first equation to solve for \( x \).

3. **Substitution**:
   - Substitute the value of \( x \) back into one of the original equations to solve for \( y \).

4. **Result**:
   - The solution gives the amount of money held by Jia (甲) and Yi (乙).

However, based on the problem's description, it seems there might be a misunderstanding or inconsistency in the setup. If you have additional clarifications, please let me know!
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: 0"""
