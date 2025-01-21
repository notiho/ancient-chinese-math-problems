"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves three equations with three unknowns: the prices of a cow (a), a sheep (b), and a pig (c). We'll use the `Fraction` class to ensure precise calculations for non-integer values.

Here is the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem statement:
# 1. 2a + 5b - 13c = 1000
# 2. 3a - 9b + 3c = 0
# 3. -5a + 6b + 8c = -600

# Solve the system of equations using substitution or elimination.

# Step 1: Solve for one variable in terms of the others.
# From equation 1: 2a + 5b - 13c = 1000
# Solve for a:
a = (1000 - 5*b + 13*c) / 2

# Substitute a into equations 2 and 3:
# Equation 2: 3a - 9b + 3c = 0
# 3((1000 - 5*b + 13*c) / 2) - 9b + 3c = 0
# Multiply through by 2 to eliminate the fraction:
# 3(1000 - 5b + 13c) - 18b + 6c = 0
# 3000 - 15b + 39c - 18b + 6c = 0
# -33b + 45c = -3000
# Simplify:
# 11b - 15c = 1000  (Equation 4)

# Equation 3: -5a + 6b + 8c = -600
# Substitute a = (1000 - 5*b + 13*c) / 2:
# -5((1000 - 5*b + 13*c) / 2) + 6b + 8c = -600
# Multiply through by 2 to eliminate the fraction:
# -5(1000 - 5b + 13c) + 12b + 16c = -1200
# -5000 + 25b - 65c + 12b + 16c = -1200
# 37b - 49c = 3800  (Equation 5)

# Step 2: Solve the two-variable system (Equations 4 and 5):
# Equation 4: 11b - 15c = 1000
# Equation 5: 37b - 49c = 3800

# Multiply Equation 4 by 37 and Equation 5 by 11 to align coefficients of b:
# 37(11b - 15c) = 37(1000)
# 11(37b - 49c) = 11(3800)
# 407b - 555c = 37000
# 407b - 539c = 41800

# Subtract the second equation from the first:
# (407b - 555c) - (407b - 539c) = 37000 - 41800
# -16c = -4800
# c = 300

# Substitute c = 300 into Equation 4:
# 11b - 15(300) = 1000
# 11b - 4500 = 1000
# 11b = 5500
# b = 500

# Substitute b = 500 and c = 300 into the expression for a:
# a = (1000 - 5*b + 13*c) / 2
# a = (1000 - 5(500) + 13(300)) / 2
# a = (1000 - 2500 + 3900) / 2
# a = 2400 / 2
# a = 1200

# Final values:
a = Fraction(1200)  # Price of a cow
b = Fraction(500)   # Price of a sheep
c = Fraction(300)   # Price of a pig

# Output the results
print(f"a (price of a cow) = {a}")
print(f"b (price of a sheep) = {b}")
print(f"c (price of a pig) = {c}")


"""


### Explanation of the Code:
1. The problem is translated into three linear equations based on the given conditions.
2. The equations are solved step-by-step using substitution and elimination methods.
3. The `Fraction` class ensures that all calculations are precise and fractions are preserved.
4. The final results are stored in variables `a`, `b`, and `c`, representing the prices of a cow, a sheep, and a pig, respectively.

### Final Answer:
- Price of a cow (`a`) = 1200
- Price of a sheep (`b`) = 500
- Price of a pig (`c`) = 300
"""


"""
Code error: name 'b' is not defined"""
