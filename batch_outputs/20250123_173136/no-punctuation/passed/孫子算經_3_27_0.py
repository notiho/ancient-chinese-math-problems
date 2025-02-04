"""
今有百鹿入城家取一鹿不盡又三家共一鹿適盡問城中家幾何
術曰以盈不足取之假令七十二家鹿不盡四令之九十家鹿不足二十置七十二于右上盈四于右下置九十于左上不足二十于左下維乘之所得并為實並盈不足為法除之即得
答曰 a家 
"""

"""
Suppose there are 100 deer entering the city. Each household takes 1 deer, but there are leftovers.
Then, 3 households share 1 deer, and it is just enough.
Question: how many households are in the city?

The procedure says: Use the surplus and deficiency to calculate.
Suppose there are 72 households, and there is a surplus of 4 deer.
Suppose there are 90 households, and there is a deficiency of 20 deer.
Place 72 on the upper right and the surplus 4 on the lower right.
Place 90 on the upper left and the deficiency 20 on the lower left.
Cross-multiply them, and add the results to obtain the dividend.
Add the surplus and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain the number of households.

Answer: *a* households.
"""

# 假令七十二家，鹿不盡四
右上 = 72
右下 = 4

# 令之九十家，鹿不足二十
左上 = 90
左下 = 20

# 維乘之所得并為實
實 = (左上 * 右下) + (右上 * 左下)

# 並盈不足為法
法 = 右下 + 左下

# 除之即得
a = Fraction(實, 法)
"""
"""
