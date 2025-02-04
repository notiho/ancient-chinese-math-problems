"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
術曰：以盈不足取之，假令七十二家鹿不盡四，令之九十家鹿不足二十。置七十二于右上，盈四于右下，置九十于左上，不足二十于左下，維乘之所得并為實，並盈不足為法，除之，即得。
答曰： a家 。
"""

#----- content starts here -----
"""
Suppose there are 100 deer brought into a city. Each household takes one deer, but there are leftovers. Then, three households share one deer, and it is exactly used up.
Question: How many households are in the city?

The procedure says: Use the surplus and deficit to calculate. Assume there are 72 households, and 4 deer are left over. Then assume there are 90 households, and 20 deer are lacking.
Place 72 on the top right, the surplus 4 on the bottom right, 90 on the top left, and the deficit 20 on the bottom left.
Cross-multiply the values, sum them to obtain the dividend. Add the surplus and deficit to obtain the divisor. Divide the dividend by the divisor to get the result.

Answer: *a* households.
"""

from fractions import Fraction

# Problem setup
總鹿數 = 100  # Total number of deer

# Assumptions
假設1_家數 = 72  # First assumption: 72 households
假設1_盈 = 4     # Surplus: 4 deer left over

假設2_家數 = 90  # Second assumption: 90 households
假設2_不足 = 20  # Deficit: 20 deer lacking

# Cross-multiply and sum to get the dividend (實)
實 = (假設1_家數 * 假設2_不足) + (假設2_家數 * 假設1_盈)

# Add surplus and deficit to get the divisor (法)
法 = 假設1_盈 + 假設2_不足

# Calculate the number of households
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
