"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
答曰： a家 。
"""

"""
Suppose there are 100 deer entering a city. Each household takes 1 deer, but it is not enough. Then, 3 households share 1 deer, and it is exactly enough.
Question: how many households are in the city?

Answer: *a* households.
"""

# Total deer
total_deer = 100

# Let the number of households be `a`
# Each household initially takes 1 deer, but there are not enough.
# Then, 3 households share 1 deer, and it is exactly enough.

# Equation:
# a = total_deer + (2/3) * a
# Simplify:
# (1 - 2/3) * a = total_deer
# (1/3) * a = total_deer
# a = 3 * total_deer

a = 3 * total_deer  # Number of households

a  # Output the result
"""
Variable 'a' has wrong value. Expected: 75, Actual: 300"""
