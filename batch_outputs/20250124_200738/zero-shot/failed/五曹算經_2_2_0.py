"""
今有兵九百七十人，人給米七升。問：計㡬何？
術曰：列兵九百七十人，以七升乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount of rice required for 970 soldiers, where each soldier is given 7 sheng (升) of rice. The answer is expressed in hu (斛), where 1 hu = 10 sheng.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
soldiers = 970  # Number of soldiers
rice_per_soldier = 7  # Rice per soldier in sheng

# Total rice in sheng
total_rice_sheng = soldiers * rice_per_soldier

# Convert sheng to hu (1 hu = 10 sheng)
a = Fraction(total_rice_sheng, 10)

# The answer is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the total amount of rice in hu (斛).
"""


"""
Variable 'a' has wrong value. Expected: 679/10, Actual: 679"""
