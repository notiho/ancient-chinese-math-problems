"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves three equations with three unknowns: the price of a cow (`a`), the price of a sheep (`b`), and the price of a pig (`c`). We will use the `Fraction` class to ensure precise calculations.

Here is the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem statement:
# 1. 2a + 5b - 13c = 1000
# 2. 3a - 9b + 3c = 0
# 3. -5a + 6b + 8c = -600

# Solve the system of equations using substitution or elimination.

# Step 1: Express the equations in matrix form:
# Coefficients matrix:
# [  2   5 -13 ]
# [  3  -9   3 ]
# [ -5   6   8 ]
# Constants vector:
# [ 1000 ]
# [    0 ]
# [ -600 ]

# Step 2: Solve using elimination.

# Multiply the first equation by 3 and the second equation by 2 to eliminate `a`:
# 6a + 15b - 39c = 3000
# 6a - 18b + 6c = 0
# Subtract the second from the first:
# 33b - 45c = 3000  --> Equation (4)

# Multiply the first equation by 5 and the third equation by 2 to eliminate `a`:
# 10a + 25b - 65c = 5000
# -10a + 12b + 16c = -1200
# Add the two equations:
# 37b - 49c = 3800  --> Equation (5)

# Step 3: Solve for `b` and `c` using equations (4) and (5).

# Multiply equation (4) by 37 and equation (5) by 33 to eliminate `b`:
# 1221b - 1665c = 111000
# 1221b - 1617c = 125400
# Subtract the second from the first:
# -48c = -14400
# c = 300

# Substitute `c = 300` into equation (4):
# 33b - 45(300) = 3000
# 33b - 13500 = 3000
# 33b = 16500
# b = 500

# Substitute `b = 500` and `c = 300` into the first equation:
# 2a + 5(500) - 13(300) = 1000
# 2a + 2500 - 3900 = 1000
# 2a - 1400 = 1000
# 2a = 2400
# a = 1200

# Final results:
a = Fraction(1200)  # Price of a cow
b = Fraction(500)   # Price of a sheep
c = Fraction(300)   # Price of a pig

# Output the results
a, b, c


"""


### Explanation of the Code:
1. The problem is translated into three linear equations based on the given conditions.
2. The equations are solved step by step using elimination to reduce the system to two equations with two unknowns, and then to one equation with one unknown.
3. The `Fraction` class is used to ensure precise arithmetic without floating-point errors.
4. The final values of `a`, `b`, and `c` represent the prices of a cow, a sheep, and a pig, respectively.

### Solution:
- Price of a cow (`a`): 1200
- Price of a sheep (`b`): 500
- Price of a pig (`c`): 300
"""


"""
"""
