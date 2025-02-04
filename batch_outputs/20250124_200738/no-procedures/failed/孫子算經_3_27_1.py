"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
答曰： a家 。
"""

#----- content starts here -----
"""
Suppose there are 100 deer entering a city. Each household takes 1 deer, but not all are taken. Then, 3 households share 1 deer, and all the deer are exactly distributed.
Question: how many households are in the city?

Answer: there are *a* households.
"""

from fractions import Fraction

# Total number of deer
total_deer = 100

# Let the number of households be x
# Each household takes 1 deer, but not all are taken. Then 3 households share 1 deer.
# Equation: x = number of households = deer taken individually + deer shared by 3 households
# x = (total_deer - remaining_deer) + (remaining_deer * 3)

# Solve for x
# remaining_deer = total_deer % 3
remaining_deer = total_deer % 3

# Total households
a = total_deer - remaining_deer + (remaining_deer * 3)

a  # Number of households#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 75, Actual: 102"""
