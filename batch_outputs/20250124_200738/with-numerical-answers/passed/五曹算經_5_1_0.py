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
Divide this by 16 liang to obtain the final result.

Answer: *a*(=41/24) jin.
"""

from fractions import Fraction

# Total silk owed: 8 shi, 5 jin, 3 liang, 8 zhu
石 = 8
斤 = 5
两 = 3
銖 = 8

# Conversion factors
石_to_鈞 = 4
鈞_to_斤 = 30
斤_to_两 = 16
两_to_銖 = 24

# Convert 石 to 鈞
鈞 = 石 * 石_to_鈞

# Convert 鈞 to 斤 and add the remaining 斤
斤_total = 鈞 * 鈞_to_斤 + 斤

# Convert 斤 to 两 and add the remaining 两
两_total = 斤_total * 斤_to_两 + 两

# Convert 两 to 銖 and add the remaining 銖
銖_total = 两_total * 两_to_銖 + 銖

# Total households
戶 = 565

# Divide total 銖 by households
銖_per_戶 = Fraction(銖_total, 戶)

# Convert 銖 per household to 两 and 銖
两_per_戶 = 銖_per_戶 // 两_to_銖
銖_remainder = 銖_per_戶 % 两_to_銖

# Convert 两 per household to 斤
斤_per_戶 = Fraction(两_per_戶, 斤_to_两) + Fraction(銖_remainder, 斤_to_两 * 两_to_銖)

# Final result
a = 斤_per_戶  # 41/24 斤#----- content ends here -----

"""
"""
