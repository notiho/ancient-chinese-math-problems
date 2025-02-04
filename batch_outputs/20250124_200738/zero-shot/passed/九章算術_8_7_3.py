"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves three equations with three unknowns: the prices of a cow (a), a sheep (b), and a pig (c). We'll use the `Fraction` class to ensure precise calculations for non-integer values.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem statement:
# 1. 2a + 5b - 13c = 1000
# 2. 3a - 9b + 3c = 0
# 3. -5a + 6b + 8c = -600

# Solve the system of linear equations using substitution or elimination.

# Step 1: Solve for one variable in terms of the others.
# From equation 2: 3a - 9b + 3c = 0
# Divide through by 3: a - 3b + c = 0
# Rearrange: a = 3b - c

# Step 2: Substitute a = 3b - c into equations 1 and 3.

# Substituting into equation 1: 2a + 5b - 13c = 1000
# 2(3b - c) + 5b - 13c = 1000
# 6b - 2c + 5b - 13c = 1000
# 11b - 15c = 1000  (Equation 4)

# Substituting into equation 3: -5a + 6b + 8c = -600
# -5(3b - c) + 6b + 8c = -600
# -15b + 5c + 6b + 8c = -600
# -9b + 13c = -600  (Equation 5)

# Step 3: Solve the two-variable system (Equations 4 and 5).
# 11b - 15c = 1000
# -9b + 13c = -600

# Multiply equation 4 by 9 and equation 5 by 11 to eliminate b:
# 99b - 135c = 9000
# -99b + 143c = -6600

# Add the two equations:
# 8c = 2400
# c = 300

# Substitute c = 300 into equation 4:
# 11b - 15(300) = 1000
# 11b - 4500 = 1000
# 11b = 5500
# b = 500

# Substitute b = 500 and c = 300 into a = 3b - c:
# a = 3(500) - 300
# a = 1500 - 300
# a = 1200

# Final results:
a = Fraction(1200)  # Price of a cow
b = Fraction(500)   # Price of a sheep
c = Fraction(300)   # Price of a pig

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. The problem is translated into three linear equations based on the given conditions.
2. We solve the system of equations step by step using substitution and elimination.
3. The `Fraction` class is used to ensure precise arithmetic for non-integer results.
4. The final values of `a`, `b`, and `c` represent the prices of a cow, a sheep, and a pig, respectively.

### Solution:
- Price of a cow (`a`): 1200
- Price of a sheep (`b`): 500
- Price of a pig (`c`): 300
"""


"""
"""
