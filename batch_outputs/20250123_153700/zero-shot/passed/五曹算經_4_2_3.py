"""
今有粟七百斛，欲雇車運之每一斛雇七升。問：車主粟主各㡬何？
術曰：列粟七百斛以雇粟七升乘之得四十九斛為車粟以減本粟七百斛餘為主粟。
答曰：車主 a斛 粟主 b斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
total_grain = 700  # Total grain in hu
grain_per_hu_for_hiring = Fraction(7, 1)  # Grain per hu for hiring in sheng

# Convert grain per hu for hiring to hu (1 hu = 10 dou = 100 sheng)
grain_per_hu_for_hiring_in_hu = grain_per_hu_for_hiring / 100

# Calculate the grain for the car owner (a) and the grain for the grain owner (b)
a = total_grain * grain_per_hu_for_hiring_in_hu  # Grain for the car owner
b = total_grain - a  # Grain for the grain owner

# Results
a, b


"""


This code calculates the grain for the car owner (`a`) and the grain for the grain owner (`b`) using the given information. The units are properly converted, and the solution uses the `Fraction` class to ensure precision.
"""


"""
"""
