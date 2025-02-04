"""
今有百鹿入城家取一鹿不盡又三家共一鹿適盡問城中家幾何
術曰以盈不足取之假令七十二家鹿不盡四令之九十家鹿不足二十置七十二于右上盈四于右下置九十于左上不足二十于左下維乘之所得并為實並盈不足為法除之即得
答曰 a家 
"""

"""
Suppose there are 100 deer entering a city. Each household takes one deer, but there are still some left over.
Then, 3 households share one deer, and it is just enough.
Question: how many households are in the city?

The procedure says: Use the surplus and deficiency to calculate.
Suppose there are 72 households, and there is a surplus of 4 deer.
Suppose there are 90 households, and there is a deficiency of 20 deer.
Place 72 on the top right and the surplus 4 on the bottom right.
Place 90 on the top left and the deficiency 20 on the bottom left.
Cross-multiply these values, and add the results to obtain the dividend.
Add the surplus and deficiency to obtain the divisor.
Divide the dividend by the divisor to get the number of households.

Answer: *a* households.
"""

# 假令七十二家，鹿不盡四
假設1_家數 = 72
盈 = 4

# 令之九十家，鹿不足二十
假設2_家數 = 90
不足 = 20

# 維乘之所得并為實
實 = (假設1_家數 * 不足) + (假設2_家數 * 盈)

# 並盈不足為法
法 = 盈 + 不足

# 除之即得
a = Fraction(實, 法)
"""
"""
