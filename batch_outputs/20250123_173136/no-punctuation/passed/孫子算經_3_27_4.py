"""
今有百鹿入城家取一鹿不盡又三家共一鹿適盡問城中家幾何
術曰以盈不足取之假令七十二家鹿不盡四令之九十家鹿不足二十置七十二于右上盈四于右下置九十于左上不足二十于左下維乘之所得并為實並盈不足為法除之即得
答曰 a家 
"""

"""
Suppose there are 100 deer entering a city. Each household takes one deer, but there are not enough deer. Additionally, 3 households share one deer, and it is just enough.
Question: how many households are in the city?

The procedure says: Use the excess and deficiency to calculate.
Suppose there are 72 households, and 4 deer are left over.
Suppose there are 90 households, and 20 deer are lacking.
Place 72 on the top right, and 4 on the bottom right.
Place 90 on the top left, and 20 on the bottom left.
Cross-multiply these, and add the results to obtain the dividend.
Add the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* households.
"""

# 假令七十二家，鹿不盡四
假設1_家數 = 72
假設1_盈 = 4

# 令之九十家，鹿不足二十
假設2_家數 = 90
假設2_不足 = 20

# 維乘之所得并為實
實 = (假設1_家數 * 假設2_不足) + (假設2_家數 * 假設1_盈)

# 並盈不足為法
法 = 假設1_盈 + 假設2_不足

# 除之即得
a = Fraction(實, 法)
"""
"""
