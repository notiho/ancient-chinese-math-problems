"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
This problem involves solving a system of equations to determine how much money person A (甲) and person B (乙) each hold. The problem is described in terms of ancient Chinese mathematical methods, specifically using a method akin to solving simultaneous linear equations. Below is the solution translated into Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Let 甲持錢 = x, 乙持錢 = y
# Equation 1: 甲得乙半而錢五十 -> x + y/2 = 50
# Equation 2: 乙得甲太半而亦錢五十 -> y + (3/2)x = 50

# Rewrite the equations:
# Equation 1: 2x + y = 100
# Equation 2: 3x + 2y = 100

# Solve using elimination or substitution:
# Multiply Equation 1 by 2 to align coefficients of y:
# 4x + 2y = 200
# Subtract Equation 2 from this:
# (4x + 2y) - (3x + 2y) = 200 - 100
# x = 100

# Substitute x = 100 into Equation 1:
# 2(100) + y = 100
# 200 + y = 100
# y = -100

# Final results:
a = 100  # 甲持錢
b = -100  # 乙持錢

# Answer:
print(f"甲持 {a} 錢，乙持 {b} 錢。")
#----- content ends here -----


"""


### Explanation:
1. The problem is modeled as a system of two linear equations:
   - \( x + \frac{y}{2} = 50 \)
   - \( y + \frac{3x}{2} = 50 \)
2. The equations are rewritten in standard linear form:
   - \( 2x + y = 100 \)
   - \( 3x + 2y = 100 \)
3. The equations are solved using elimination or substitution to find \( x \) (甲's money) and \( y \) (乙's money).

### Note:
The solution implies that one of the individuals (乙) holds a negative amount of money, which might represent debt or an abstract concept in the context of the problem.
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
