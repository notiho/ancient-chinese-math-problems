"""
今有百鹿入城家取一鹿不盡又三家共一鹿適盡問城中家幾何
術曰以盈不足取之假令七十二家鹿不盡四令之九十家鹿不足二十置七十二于右上盈四于右下置九十于左上不足二十于左下維乘之所得并為實並盈不足為法除之即得
答曰 a家 
"""

#----- content starts here -----
"""
Suppose there are 100 deer entering the city. Each household takes one deer, but there are still some left over. 
Then, three households share one deer, and it is just enough.
Question: how many households are in the city?

The procedure says: Use the surplus and deficit to calculate.
Suppose there are 72 households, and 4 deer are left over.
Suppose there are 90 households, and 20 deer are lacking.
Place 72 on the upper right and the surplus 4 on the lower right.
Place 90 on the upper left and the deficit 20 on the lower left.
Cross-multiply them, add the results to obtain the dividend.
Add the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* households.
"""

# 假令七十二家，鹿不盡四
盈家 = 72
盈 = 4

# 令之九十家，鹿不足二十
不足家 = 90
不足 = 20

# 維乘之所得并為實
實 = (盈家 * 不足) + (不足家 * 盈)

# 並盈不足為法
法 = 盈 + 不足

# 除之即得
a = Fraction(實, 法)#----- content ends here -----

"""
"""
