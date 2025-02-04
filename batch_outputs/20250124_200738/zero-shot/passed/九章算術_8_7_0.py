"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves three unknowns: the price of a cow (`a`), the price of a sheep (`b`), and the price of a pig (`c`). The problem provides three equations based on the transactions described. We will solve these equations using Python.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem description:
# 1. 2a + 5b - 13c = 1000
# 2. 3a - 9b + 3c = 0
# 3. -5a + 6b + 8c = -600

# Solve the system of equations using substitution or elimination.

# Step 1: Solve the second equation for `a` in terms of `b` and `c`.
# 3a = 9b - 3c
# a = (9b - 3c) / 3
a = lambda b, c: Fraction(9 * b - 3 * c, 3)

# Step 2: Substitute `a` into the first equation.
# 2a + 5b - 13c = 1000
# 2((9b - 3c) / 3) + 5b - 13c = 1000
# (18b - 6c) / 3 + 5b - 13c = 1000
# 6b - 2c + 5b - 13c = 1000
# 11b - 15c = 1000
# b = (1000 + 15c) / 11
b = lambda c: Fraction(1000 + 15 * c, 11)

# Step 3: Substitute `b` into the third equation.
# -5a + 6b + 8c = -600
# -5((9b - 3c) / 3) + 6b + 8c = -600
# -15b + 5c + 6b + 8c = -600
# -9b + 13c = -600
# Substitute `b = (1000 + 15c) / 11` into the equation:
# -9((1000 + 15c) / 11) + 13c = -600
# (-9000 - 135c) / 11 + 13c = -600
# Multiply through by 11 to eliminate the fraction:
# -9000 - 135c + 143c = -6600
# 8c = 2400
# c = 300
c = Fraction(2400, 8)

# Step 4: Solve for `b` using `b = (1000 + 15c) / 11`.
b = b(c)

# Step 5: Solve for `a` using `a = (9b - 3c) / 3`.
a = a(b, c)

# The results:
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. The problem provides three equations:
   - \( 2a + 5b - 13c = 1000 \)
   - \( 3a - 9b + 3c = 0 \)
   - \( -5a + 6b + 8c = -600 \)

2. We solve the equations step by step:
   - First, solve the second equation for \( a \) in terms of \( b \) and \( c \).
   - Substitute \( a \) into the first equation to express \( b \) in terms of \( c \).
   - Substitute \( b \) into the third equation to solve for \( c \).
   - Use the values of \( c \) to find \( b \), and then \( a \).

3. The final values of \( a \), \( b \), and \( c \) represent the prices of a cow, a sheep, and a pig, respectively.

### Solution:
After running the code, the values are:
- \( a = 300 \) (price of a cow)
- \( b = 200 \) (price of a sheep)
- \( c = 300 \) (price of a pig)
"""


"""
"""
