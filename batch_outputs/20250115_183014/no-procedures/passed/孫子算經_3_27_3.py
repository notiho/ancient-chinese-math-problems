"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
答曰： a家 。
"""

"""
Suppose there are 100 deer entering the city. Each household takes 1 deer, but not all are taken. Then, 3 households share 1 deer, and all the deer are exactly distributed.
Question: how many households are in the city?

Answer: there are *a* households.
"""

# Total number of deer
total_deer = 100

# Let the number of households be `a`
# Each household takes 1 deer, but not all are taken.
# After distributing 1 deer per household, 3 households share 1 deer.
# This means the total number of households is made up of those that take 1 deer each and those that share.

# Equation:
# a = x (households taking 1 deer each) + y (households sharing 1 deer in groups of 3)
# y = x / 3 (since 3 households share 1 deer)
# total_deer = x + y / 3
# Solve for `a`

# Each household taking 1 deer:
a = Fraction(total_deer * 3, 4)  # Total households in the city

a
"""
"""
