"""
今有負籠重一石一十七斤，行七十六步，五十返。今負籠重一石，行百步，問︰返幾何？
術曰：以今所行步數乘今籠重斤數為法，故籠重斤數乘故步，又以返數乘之，為實。實如法得一返。
荅曰： a返 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
current_basket_weight = 1 * 16 + 17  # 1石1十7斤 converted to斤 (1石 = 16斤)
current_steps = 76
current_returns = 50

new_basket_weight = 1 * 16  # 1石 converted to斤
new_steps = 100

# Calculation
# Using the formula: (current_steps * current_basket_weight) = (new_steps * new_basket_weight * a)
# Solve for a (number of returns)
a = Fraction(current_steps * current_basket_weight, new_steps * new_basket_weight)

# Result
a  # a is the number of returns
#----- content ends here -----


"""


The variable `a` will hold the solution in terms of the number of returns.
"""


"""
Variable 'a' has wrong value. Expected: 150000/2603, Actual: 627/400"""
