"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
答曰： a家 。
"""

#----- content starts here -----
"""
Suppose there are 100 deer entering a city. Each household takes 1 deer, but it is not enough. Then, 3 households share 1 deer, and it is just enough.
Question: how many households are in the city?

Answer: *a* households.
"""

from fractions import Fraction

# Total number of deer
total_deer = 100

# Let the number of households be `a`
# Each household takes 1 deer, but when 3 households share 1 deer, it is just enough.
# This means the total number of deer is equal to the number of households divided by 3.

# Equation: total_deer = a / 3
a = total_deer * 3

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 75, Actual: 300"""
