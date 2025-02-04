"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
答曰： a家 。
"""

#----- content starts here -----
"""
Suppose there are 100 deer entering a city. Each household takes 1 deer, but not all are taken. Then, 3 households share 1 deer, and it is exactly finished.
Question: how many households are in the city?

Answer: *a* households.
"""

from fractions import Fraction

# Total number of deer
total_deer = 100

# Let the number of households be `x`
# Each household takes 1 deer, but not all are taken, so `x` households take 1 deer each.
# The remaining deer are shared by groups of 3 households, and it is exactly finished.

# Equation:
# x + (x / 3) = total_deer
# Solve for x.

# Solve for x
a = Fraction(3 * total_deer, 4)

# The number of households is:
a#----- content ends here -----

"""
"""
