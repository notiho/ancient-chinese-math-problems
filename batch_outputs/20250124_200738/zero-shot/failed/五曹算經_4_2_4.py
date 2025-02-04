"""
今有粟七百斛，欲雇車運之每一斛雇七升。問：車主粟主各㡬何？
術曰：列粟七百斛以雇粟七升乘之得四十九斛為車粟以減本粟七百斛餘為主粟。
答曰：車主 a斛 粟主 b斛 。
"""

"""
Here is the Python code that computes the values of the unknowns "a" (車主) and "b" (粟主) based on the problem:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_grain = 700  # 粟七百斛
grain_per_hire = Fraction(7, 1)  # 每一斛雇七升 (7升 = 7/10斛)

# Calculate the grain paid to the car owner (車主)
a = total_grain * grain_per_hire / 10  # Convert 7升 to 7/10斛
# Calculate the grain remaining for the grain owner (粟主)
b = total_grain - a

# Results
a, b
#----- content ends here -----


"""


This will compute the values of `a` (車主) and `b` (粟主) in units of 斛.
"""


"""
Variable 'a' has wrong value. Expected: 49, Actual: 490
Variable 'b' has wrong value. Expected: 651, Actual: 210"""
