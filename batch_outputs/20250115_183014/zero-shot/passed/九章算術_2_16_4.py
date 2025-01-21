"""
今有粟五斗五升，欲為飧。問︰得幾何？
術曰：以粟求飧，九之，五而一。
荅曰：為飧 a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
粟 = Fraction(5, 1) + Fraction(5, 10)  # 5斗5升 = 5斗 + 5/10斗 = 5.5斗

# Calculation
飧 = 粟 * Fraction(9, 5)  # Multiply 粟 by 9/5 to calculate 飧

# Result
a = 飧  # Assign the result to variable 'a'


"""


The variable `a` will hold the value of 飧 in terms of "斗".
"""


"""
"""
