"""
今有五百六十五户共責絲八石五斤三两八銖問户出絲㡬何
術曰列絲八石五斤三两八銖以四乘八石得三十二鈞以三十斤乘之納五斤得九百六十五斤以十六两乘之納三两得一萬五千四百四十三两以二十四銖乘之納八銖得三十七萬六百四十銖以五百六十五户除之得一户六百五十六銖以二十四銖除之得二十七两奇八銖以十六除之即得
答曰 a斤 b 两 c銖 
"""

"""
Suppose there are 565 households collectively responsible for 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

The procedure says:
List the silk as 8 shi, 5 jin, 3 liang, and 8 zhu.
Multiply the 8 shi by 4, obtaining 32 jun.
Multiply this by 30 jin, adding the 5 jin, obtaining 965 jin.
Multiply this by 16 liang, adding the 3 liang, obtaining 15,443 liang.
Multiply this by 24 zhu, adding the 8 zhu, obtaining 376,640 zhu.
Divide this by 565 households, obtaining 656 zhu per household.
Divide this by 24 zhu, obtaining 27 liang and a remainder of 8 zhu.
Divide this remainder by 16, obtaining the final result.

Answer: *a* jin, *b* liang, *c* zhu.
"""

# Total silk: 8石5斤3两8銖
石 = 8
斤 = 5
两 = 3
銖 = 8

# Convert 石 to 鈞
鈞 = 石 * 4

# Convert 鈞 to 斤
斤_total = 鈞 * 30 + 斤

# Convert 斤 to 两
两_total = 斤_total * 16 + 两

# Convert 两 to 銖
銖_total = 两_total * 24 + 銖

# Divide by 565 households
銖_per_household = Fraction(銖_total, 565)

# Convert 銖 to 两
两_per_household = Fraction(銖_per_household, 24)
remaining_銖 = 銖_per_household % 24

# Convert 两 to 斤
斤_per_household = Fraction(两_per_household, 16)
remaining_两 = 两_per_household % 16

# Final results
a = int(斤_per_household)
b = int(remaining_两)
c = int(remaining_銖)
"""
"""
