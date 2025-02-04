"""
今有糲飯七斗六升、七分升之四，欲為飧。問︰得幾何？
術曰：以糲飯求飧，六之，五而一。
荅曰：為飧 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem states that we have a certain amount of 糲飯 (coarse rice) and we want to calculate how much 飧 (cooked rice) it can produce. The method provided says to multiply the amount of 糲飯 by 6 and then divide by 5.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given 糲飯 (coarse rice) amount
糲飯 = Fraction(7, 1) + Fraction(6, 10) + Fraction(4, 70)  # 7斗6升7分升之4

# Calculation for 飧 (cooked rice)
a = 糲飯 * 6 / 5  # Multiply by 6 and divide by 5

# Result
a  # a斗
#----- content ends here -----


"""


The variable `a` will hold the result in terms of 斗 (a unit of volume).
"""


"""
"""
