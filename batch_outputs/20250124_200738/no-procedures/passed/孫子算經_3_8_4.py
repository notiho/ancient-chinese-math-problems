"""
今有綿，九萬一千一百三十五觔，給與三萬六千四百五十四戶。問：戶得幾何？
答曰： a觔 。
"""

#----- content starts here -----
"""
Suppose there is 91,135 jin of cotton, to be distributed among 36,454 households.
Question: how much does each household receive?

Answer: each household receives *a* jin.
"""

# Total cotton in jin
綿 = 91135

# Total households
戶 = 36454

# Divide the total cotton by the number of households to get the amount per household
a = Fraction(綿, 戶)

# Result
a#----- content ends here -----

"""
"""
