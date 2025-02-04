"""
假令有股弦相乘冪四千七百三十九五分之三，句少於弦五十四五分之二。問：股多少？
答曰： a 。
"""

"""
This problem involves solving a right triangle relationship using the Pythagorean theorem. Here's the breakdown:

- The product of the leg (股) and hypotenuse (弦) is given as \( 4739 \frac{3}{5} \).
- The other leg (句) is shorter than the hypotenuse by \( 54 \frac{2}{5} \).
- We are tasked to find the length of the leg (股).

Let's translate this into Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
product_of_leg_and_hypotenuse = Fraction(4739 * 5 + 3, 5)  # 4739 3/5
difference_between_hypotenuse_and_other_leg = Fraction(54 * 5 + 2, 5)  # 54 2/5

# Let 股 = x, 弦 = y, and 句 = z
# From the problem:
# x * y = product_of_leg_and_hypotenuse
# z = y - difference_between_hypotenuse_and_other_leg
# Using the Pythagorean theorem: x^2 + z^2 = y^2

# Solve for 股 (x)
# Substitute z = y - difference_between_hypotenuse_and_other_leg into the Pythagorean theorem:
# x^2 + (y - difference_between_hypotenuse_and_other_leg)^2 = y^2
# Expand and simplify:
# x^2 + y^2 - 2 * y * difference_between_hypotenuse_and_other_leg + difference_between_hypotenuse_and_other_leg^2 = y^2
# x^2 = 2 * y * difference_between_hypotenuse_and_other_leg - difference_between_hypotenuse_and_other_leg^2
# Also, from x * y = product_of_leg_and_hypotenuse, we have y = product_of_leg_and_hypotenuse / x
# Substitute y into the equation for x^2 and solve.

# Iterative solution to find x
for 股 in range(1, 10000):  # Arbitrary range to search for the solution
    股 = Fraction(股)
    弦 = product_of_leg_and_hypotenuse / 股
    句 = 弦 - difference_between_hypotenuse_and_other_leg
    if 股**2 + 句**2 == 弦**2:
        a = 股
        break

# Output the result
a
#----- content ends here -----


"""


This code systematically solves for the length of the leg (股) using the given conditions and the Pythagorean theorem. The result will be stored in `a`.
"""


"""
"""
