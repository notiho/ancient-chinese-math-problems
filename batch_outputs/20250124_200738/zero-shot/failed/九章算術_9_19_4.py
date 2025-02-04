"""
今有邑方不知大小，各中開門。出北門二十步有木。出南門十四步，折而西行一千七百七十五步見木。問︰邑方幾何？
術曰：以出北門步數乘西行步數，倍之，為實。并出南門步數為從法，開方除之，即邑方。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
north_steps = 20  # 出北門步數
south_steps = 14  # 出南門步數
west_steps = 1775  # 西行步數

# Calculation
product = north_steps * west_steps  # 出北門步數乘西行步數
double_product = 2 * product  # 倍之
total = double_product + south_steps  # 并出南門步數為從法
a = math.sqrt(total)  # 開方除之，即邑方

# Result
a = Fraction(a).limit_denominator()  # Represent as a fraction
#----- content ends here -----


"""


The variable `a` will contain the solution in steps (`步`).
"""


"""
Variable 'a' has wrong value. Expected: 250, Actual: 101212953/379808"""
