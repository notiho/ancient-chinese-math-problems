"""
今有百鹿入城，家取一鹿，不盡，又三家共一鹿，適盡。問：城中家幾何？
術曰：以盈不足取之，假令七十二家鹿不盡四，令之九十家鹿不足二十。置七十二于右上，盈四于右下，置九十于左上，不足二十于左下，維乘之所得并為實，並盈不足為法，除之，即得。
答曰： a(=75)家 。
"""

#----- content starts here -----
"""
Suppose there are 100 deer brought into a city. Each household takes one deer, but there are not enough, and 3 households share 1 deer, making it exactly sufficient.
Question: how many households are in the city?

The procedure says: Use the surplus and deficiency to calculate.
Suppose there are 72 households, and the deer are 4 short.
Suppose there are 90 households, and the deer are 20 short.
Place 72 on the top right, and the surplus 4 on the bottom right.
Place 90 on the top left, and the deficiency 20 on the bottom left.
Cross-multiply these, and add the results to obtain the dividend.
Add the surplus and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a*(=75) households.
"""

# 假令七十二家鹿不盡四
假家1 = 72
盈1 = 4

# 令之九十家鹿不足二十
假家2 = 90
不足2 = 20

# 維乘之所得并為實
實 = (假家1 * 不足2) + (假家2 * 盈1)

# 並盈不足為法
法 = 盈1 + 不足2

# 除之，即得
a = Fraction(實, 法)  # 75 households#----- content ends here -----

"""
"""
