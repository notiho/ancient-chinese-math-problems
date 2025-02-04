"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
術曰：列絲八石五斤三两八銖，以四乘八石得三十二鈞；以三十斤乘之、納五斤，得九百六十五斤；以十六两乘之、納三两，得一萬五千四百四十三两；以二十四銖乘之、納八銖，得三十七萬六百四十銖。以五百六十五户除之，得一户六百五十六銖；以二十四銖除之，得二十七两奇八銖；以十六除之即得。
答曰： a(=41/24)斤 。
"""

#----- content starts here -----
"""
Suppose there are 565 households, collectively responsible for 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

The procedure says: Arrange the silk amount as 8 shi, 5 jin, 3 liang, and 8 zhu.
Multiply the 8 shi by 4 to obtain 32 jun.
Multiply this by 30 jin and add 5 jin, obtaining 965 jin.
Multiply this by 16 liang and add 3 liang, obtaining 15,443 liang.
Multiply this by 24 zhu and add 8 zhu, obtaining 370,640 zhu.
Divide this by 565 households, obtaining 656 zhu per household.
Divide this by 24 zhu, obtaining 27 liang and 8 zhu remaining.
Divide this by 16 liang to obtain the final result.

Answer: *a*(=41/24) jin.
"""

from fractions import Fraction

# Total silk: 8 shi, 5 jin, 3 liang, 8 zhu
石 = 8
斤 = 5
两 = 3
銖 = 8

# Convert shi to jin
# 1 shi = 4 jun, 1 jun = 30 jin
石_to_斤 = (石 * 4) * 30 + 斤  # 965 jin

# Convert jin to liang
# 1 jin = 16 liang
斤_to_两 = (石_to_斤 * 16) + 两  # 15,443 liang

# Convert liang to zhu
# 1 liang = 24 zhu
两_to_銖 = (斤_to_两 * 24) + 銖  # 370,640 zhu

# Divide by the number of households
户數 = 565
每户銖 = Fraction(两_to_銖, 户數)  # 656 zhu per household

# Convert zhu back to liang
每户两 = Fraction(每户銖, 24)  # 27 liang and 8 zhu remaining

# Convert liang back to jin
每户斤 = Fraction(每户两, 16)  # 41/24 jin

a = 每户斤  # 41/24 jin#----- content ends here -----

"""
"""
