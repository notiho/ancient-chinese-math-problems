"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves solving a system of linear equations to find the prices of a cow (`a`), a sheep (`b`), and a pig (`c`). Here's the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem:
# 2a + 5b - 13c = 1000
# 3a - 9b + 3c = 0
# -5a + 6b + 8c = -600

# Solve the system of equations using substitution/elimination:
# Coefficients matrix:
# |  2   5  -13 |   | a |   =   |  1000 |
# |  3  -9    3 | * | b |   =   |     0 |
# | -5   6    8 |   | c |   =   |  -600 |

# Step 1: Eliminate one variable (e.g., `a`) using the first two equations.
# Multiply the first equation by 3 and the second equation by 2 to align coefficients of `a`:
# 6a + 15b - 39c = 3000
# 6a - 18b + 6c = 0

# Subtract the second equation from the first:
# (6a + 15b - 39c) - (6a - 18b + 6c) = 3000 - 0
# 33b - 45c = 3000
# Simplify:
# 11b - 15c = 1000  (Equation 4)

# Step 2: Eliminate `a` using the first and third equations.
# Multiply the first equation by 5 and the third equation by 2:
# 10a + 25b - 65c = 5000
# -10a + 12b + 16c = -1200

# Add the two equations:
# (10a + 25b - 65c) + (-10a + 12b + 16c) = 5000 - 1200
# 37b - 49c = 3800
# Simplify:
# 37b - 49c = 3800  (Equation 5)

# Step 3: Solve the system of two equations (Equation 4 and Equation 5) for `b` and `c`.
# 11b - 15c = 1000
# 37b - 49c = 3800

# Multiply the first equation by 37 and the second equation by 11 to align coefficients of `b`:
# 407b - 555c = 37000
# 407b - 539c = 41800

# Subtract the second equation from the first:
# (407b - 555c) - (407b - 539c) = 37000 - 41800
# -16c = -4800
# Solve for `c`:
c = Fraction(-4800, -16)
c = Fraction(300)  # Price of a pig

# Substitute `c` back into Equation 4 to solve for `b`:
# 11b - 15c = 1000
# 11b - 15(300) = 1000
# 11b - 4500 = 1000
# 11b = 5500
b = Fraction(5500, 11)
b = Fraction(500)  # Price of a sheep

# Substitute `b` and `c` back into the first original equation to solve for `a`:
# 2a + 5b - 13c = 1000
# 2a + 5(500) - 13(300) = 1000
# 2a + 2500 - 3900 = 1000
# 2a - 1400 = 1000
# 2a = 2400
a = Fraction(2400, 2)
a = Fraction(1200)  # Price of a cow

# Final results:
a = Fraction(1200)  # Price of a cow
b = Fraction(500)   # Price of a sheep
c = Fraction(300)   # Price of a pig


"""


### Solution:
- The price of a cow (`a`) is **1200**.
- The price of a sheep (`b`) is **500**.
- The price of a pig (`c`) is **300**.
"""


"""
"""
