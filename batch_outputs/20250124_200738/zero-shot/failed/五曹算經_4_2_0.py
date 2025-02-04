"""
今有粟七百斛，欲雇車運之每一斛雇七升。問：車主粟主各㡬何？
術曰：列粟七百斛以雇粟七升乘之得四十九斛為車粟以減本粟七百斛餘為主粟。
答曰：車主 a斛 粟主 b斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_grain = 700  # in hu (斛)
grain_per_hire = Fraction(7, 10)  # 7升 = 7/10斛

# Calculations
grain_for_cars = total_grain * grain_per_hire  # 車主粟
grain_for_owner = total_grain - grain_for_cars  # 粟主粟

# Assigning to variables
a = grain_for_cars  # 車主粟
b = grain_for_owner  # 粟主粟
#----- content ends here -----


"""


Now, `a` represents the amount of grain for the car owner, and `b` represents the amount of grain for the grain owner. Both are calculated using the given formula.
"""


"""
Variable 'a' has wrong value. Expected: 49, Actual: 490
Variable 'b' has wrong value. Expected: 651, Actual: 210"""
