"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
術曰：以盈不足取之，假令七十二家鹿不盡四，令之九十家鹿不足二十。置七十二于右上，盈四于右下，置九十于左上，不足二十于左下，維乘之所得并為實，並盈不足為法，除之，即得。
答曰： a家 。
"""

#----- content starts here -----
"""
Suppose there are 100 deer brought into a city. Each household takes one deer, but there are leftovers.
Then, three households share one deer, and it is exactly enough.
Question: how many households are in the city?

The procedure says: Use the surplus and deficit to calculate.
Suppose there are 72 households, and there are 4 deer left over.
Suppose there are 90 households, and there is a deficit of 20 deer.
Place 72 in the top right, and the surplus 4 in the bottom right.
Place 90 in the top left, and the deficit 20 in the bottom left.
Cross-multiply and sum the results to obtain the dividend.
Add the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to get the answer.

Answer: *a* households.
"""

from fractions import Fraction

# Known values
鹿總數 = 100  # Total number of deer
盈 = 4  # Surplus when there are 72 households
不足 = 20  # Deficit when there are 90 households
右上 = 72  # Households when surplus occurs
左上 = 90  # Households when deficit occurs

# Cross-multiply and sum to get the dividend (實)
實 = (右上 * 不足) + (左上 * 盈)

# Add surplus and deficit to get the divisor (法)
法 = 盈 + 不足

# Divide to get the number of households
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
