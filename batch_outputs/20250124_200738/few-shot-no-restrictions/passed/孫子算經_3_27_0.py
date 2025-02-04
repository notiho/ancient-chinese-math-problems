"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
術曰：以盈不足取之，假令七十二家鹿不盡四，令之九十家鹿不足二十。置七十二于右上，盈四于右下，置九十于左上，不足二十于左下，維乘之所得并為實，並盈不足為法，除之，即得。
答曰： a家 。
"""

#----- content starts here -----
"""
Suppose there are 100 deer entering the city. Each household takes 1 deer, but there are leftovers.
Then, 3 households share 1 deer, and it is exactly enough.
Question: how many households are in the city?

The procedure says: Use the surplus and deficit to calculate.
Suppose there are 72 households, and there are 4 deer left over.
Suppose there are 90 households, and there is a deficit of 20 deer.
Place 72 in the top right, and the surplus 4 in the bottom right.
Place 90 in the top left, and the deficit 20 in the bottom left.
Cross-multiply the values, sum them to obtain the dividend.
Sum the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* households.
"""

from fractions import Fraction

# Problem setup
鹿總數 = 100  # Total number of deer

# 假設 72 家，盈 4 鹿
右上 = 72
右下 = 4

# 假設 90 家，不足 20 鹿
左上 = 90
左下 = 20

# 維乘之所得并為實
實 = (右上 * 左下) + (左上 * 右下)

# 並盈不足為法
法 = 右下 + 左下

# 除之，即得
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
