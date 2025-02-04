"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
術曰：列絲八石五斤三两八銖，以四乘八石得三十二鈞；以三十斤乘之、納五斤，得九百六十五斤；以十六两乘之、納三两，得一萬五千四百四十三两；以二十四銖乘之、納八銖，得三十七萬六百四十銖。以五百六十五户除之，得一户六百五十六銖；以二十四銖除之，得二十七两奇八銖；以十六除之即得。
答曰： a(=41/24)斤 。
"""

#----- content starts here -----
"""
Suppose there are 565 households, and together they owe 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household owe?

The procedure says: Arrange the silk amount as 8 shi, 5 jin, 3 liang, and 8 zhu.
Multiply the 8 shi by 4, obtaining 32 jun.
Multiply this by 30 jin, and add 5 jin, obtaining 965 jin.
Multiply this by 16 liang, and add 3 liang, obtaining 15,443 liang.
Multiply this by 24 zhu, and add 8 zhu, obtaining 370,640 zhu.
Divide this by 565 households, obtaining 656 zhu per household.
Divide this by 24 zhu, obtaining 27 liang and 8 zhu remaining.
Divide this by 16 liang to obtain the result.

Answer: *a*(=41/24) jin.
"""

from fractions import Fraction

# Total silk owed: 8 shi, 5 jin, 3 liang, 8 zhu
石 = 8
斤 = 5
两 = 3
銖 = 8

# Convert shi to jin
石_to_斤 = 4 * 30  # 1 shi = 4 jun, 1 jun = 30 jin
total_斤 = 石 * 石_to_斤 + 斤  # 8 shi * 120 jin/shi + 5 jin = 965 jin

# Convert jin to liang
斤_to_两 = 16  # 1 jin = 16 liang
total_两 = total_斤 * 斤_to_两 + 两  # 965 jin * 16 liang/jin + 3 liang = 15,443 liang

# Convert liang to zhu
两_to_銖 = 24  # 1 liang = 24 zhu
total_銖 = total_两 * 两_to_銖 + 銖  # 15,443 liang * 24 zhu/liang + 8 zhu = 370,640 zhu

# Divide by the number of households
戶數 = 565
銖_per_戶 = Fraction(total_銖, 戶數)  # 370,640 zhu / 565 households = 656 zhu/household

# Convert zhu back to liang
两_per_戶 = Fraction(銖_per_戶, 两_to_銖)  # 656 zhu / 24 zhu/liang = 27 liang and 8 zhu remaining

# Convert liang back to jin
斤_per_戶 = Fraction(两_per_戶, 斤_to_两)  # 27 liang / 16 liang/jin = 41/24 jin

a = 斤_per_戶  # 41/24 jin#----- content ends here -----

"""
"""
