"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
術曰：以盈不足取之，假令七十二家鹿不盡四，令之九十家鹿不足二十。置七十二于右上，盈四于右下，置九十于左上，不足二十于左下，維乘之所得并為實，並盈不足為法，除之，即得。
答曰： a家 。
"""

"""
Suppose there are 100 deer entering a city. Each household takes one deer, but there are leftovers. Then, three households share one deer, and it is exactly enough.
Question: how many households are in the city?

The procedure says: Use the surplus and deficiency to calculate.
Suppose there are 72 households, and 4 deer are left over.
Suppose there are 90 households, and 20 deer are insufficient.
Place 72 on the top right, and the surplus 4 on the bottom right.
Place 90 on the top left, and the deficiency 20 on the bottom left.
Cross-multiply the values, sum them to obtain the dividend.
Sum the surplus and deficiency to obtain the divisor.
Divide the dividend by the divisor to get the answer.

Answer: *a* households.
"""

# 假令七十二家鹿不盡四
右上 = 72
右下 = 4

# 令之九十家鹿不足二十
左上 = 90
左下 = 20

# 維乘之所得并為實
實 = (右上 * 左下) + (左上 * 右下)

# 並盈不足為法
法 = 右下 + 左下

# 除之，即得
a = Fraction(實, 法)
"""
"""
