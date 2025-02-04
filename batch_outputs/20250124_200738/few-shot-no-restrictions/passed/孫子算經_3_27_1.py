"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
術曰：以盈不足取之，假令七十二家鹿不盡四，令之九十家鹿不足二十。置七十二于右上，盈四于右下，置九十于左上，不足二十于左下，維乘之所得并為實，並盈不足為法，除之，即得。
答曰： a家 。
"""

#----- content starts here -----
"""
Suppose there are 100 deer entering the city. Each household takes one deer, but there are leftovers. Then, three households share one deer, and it is exactly used up.
Question: How many households are in the city?

The procedure says: Use the surplus and deficit to calculate. Suppose there are 72 households, and the deer are 4 in surplus. Suppose there are 90 households, and the deer are 20 in deficit.
Place 72 on the top right, and the surplus 4 on the bottom right. Place 90 on the top left, and the deficit 20 on the bottom left.
Cross-multiply, sum the results to obtain the dividend. Sum the surplus and deficit to obtain the divisor. Divide, and the result is the number of households.

Answer: *a* households.
"""

# Known values
deer = 100  # Total number of deer

# Hypotheses
households_1 = 72  # First hypothesis: 72 households
surplus_1 = 4      # Surplus of 4 deer

households_2 = 90  # Second hypothesis: 90 households
deficit_2 = 20     # Deficit of 20 deer

# Cross-multiply and sum to obtain the dividend (實)
實 = (households_1 * deficit_2) + (households_2 * surplus_1)

# Sum the surplus and deficit to obtain the divisor (法)
法 = surplus_1 + deficit_2

# Divide to find the number of households
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
