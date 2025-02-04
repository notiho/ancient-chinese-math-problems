"""
今有兵九百七十人，人給米七升。問：計㡬何？
術曰：列兵九百七十人，以七升乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount of rice required for 970 soldiers, where each soldier is given 7 "升" (a unit of volume). The result will be expressed in "斛" (another unit of volume), where 1 斛 = 10 升.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
soldiers = 970  # Number of soldiers
rice_per_soldier = 7  # Rice per soldier in 升

# Total rice in 升
total_rice_in_sheng = soldiers * rice_per_soldier

# Convert 升 to 斛 (1 斛 = 10 升)
a = Fraction(total_rice_in_sheng, 10)

# Result
a  # Total rice in 斛
#----- content ends here -----


"""


The variable `a` will contain the total amount of rice in 斛.
"""


"""
Variable 'a' has wrong value. Expected: 679/10, Actual: 679"""
