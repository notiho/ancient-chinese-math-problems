"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. The problem involves a right triangle where the product of the leg (股) and the hypotenuse (弦) is given, and the leg is slightly shorter than the hypotenuse by a fraction. We need to calculate the hypotenuse (弦), represented as `a`.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
product = Fraction(4036, 5)  # 股 and 弦相乘冪四千三十六五分之
difference = Fraction(1, 65)  # 股少於弦六五分之一

# Step 1: 冪自乘，倍少數而一，為實
real_value = product * product * (2 * difference + 1)

# Step 2: 半少，為廉法，從
half_difference = difference / 2

# Step 3: 開立方除之，即股
leg = (real_value ** Fraction(1, 3)) / (1 + half_difference)

# Step 4: 加差，即弦
a = leg + difference

# The value of the hypotenuse (弦) is stored in variable `a`
#----- content ends here -----


"""


The variable `a` will contain the value of the hypotenuse (弦) as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 86.92076019907026"""
