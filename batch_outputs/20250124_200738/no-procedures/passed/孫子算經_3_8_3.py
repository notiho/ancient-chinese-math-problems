"""
今有綿，九萬一千一百三十五觔，給與三萬六千四百五十四戶。問：戶得幾何？
答曰： a觔 。
"""

#----- content starts here -----
"""
Suppose there is 91,135 jin of cotton, to be distributed among 36,454 households.
Question: how much does each household get?

Answer: each household gets *a* jin.
"""

# Total cotton in jin
total_cotton = 91135

# Total households
total_households = 36454

# Divide the total cotton by the total households
a = Fraction(total_cotton, total_households)

# Result
a#----- content ends here -----

"""
"""
