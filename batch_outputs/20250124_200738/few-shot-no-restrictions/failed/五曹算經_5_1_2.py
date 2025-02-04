"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
術曰：列絲八石五斤三两八銖，以四乘八石得三十二鈞；以三十斤乘之、納五斤，得九百六十五斤；以十六两乘之、納三两，得一萬五千四百四十三两；以二十四銖乘之、納八銖，得三十七萬六百四十銖。以五百六十五户除之，得一户六百五十六銖；以二十四銖除之，得二十七两奇八銖；以十六除之即得。
答曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there are 565 households, and they are collectively responsible for producing 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household produce?

The procedure says:
- Represent the silk amount as 8 shi, 5 jin, 3 liang, and 8 zhu.
- Multiply 8 shi by 4 to convert it to 32 jun.
- Multiply 32 jun by 30 to convert it to 960 jin, then add 5 jin, resulting in 965 jin.
- Multiply 965 jin by 16 to convert it to 15,440 liang, then add 3 liang, resulting in 15,443 liang.
- Multiply 15,443 liang by 24 to convert it to 370,640 zhu, then add 8 zhu, resulting in 370,648 zhu.
- Divide 370,648 zhu by 565 households, resulting in 656 zhu per household.
- Divide 656 zhu by 24 to convert it to 27 liang and 8 zhu.
- Divide 27 liang by 16 to convert it to jin.

Answer: Each household produces *a* jin.
"""

from fractions import Fraction

# Total silk responsibility
石 = 8  # shi
斤 = 5  # jin
两 = 3  # liang
銖 = 8  # zhu

# Convert everything to zhu
# 1 石 = 4 鈞, 1 鈞 = 30 斤, 1 斤 = 16 两, 1 两 = 24 銖
鈞 = 石 * 4
斤_total = 鈞 * 30 + 斤
两_total = 斤_total * 16 + 两
銖_total = 两_total * 24 + 銖

# Total households
戶 = 565

# Divide total zhu by households
銖_per_household = Fraction(銖_total, 戶)

# Convert zhu to liang
两_per_household =銖_per_household#----- content ends here -----

"""
Missing variable in output: 'a'"""
