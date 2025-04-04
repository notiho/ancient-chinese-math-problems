"""
今有五百六十五户共責絲八石五斤三两八銖問户出絲㡬何
術曰列絲八石五斤三两八銖以四乘八石得三十二鈞以三十斤乘之納五斤得九百六十五斤以十六两乘之納三两得一萬五千四百四十三两以二十四銖乘之納八銖得三十七萬六百四十銖以五百六十五户除之得一户六百五十六銖以二十四銖除之得二十七两奇八銖以十六除之即得
答曰 a斤 b 两 c銖 
"""

"""
Suppose there are 565 households collectively responsible for 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

The procedure says: Arrange the silk amount as 8 shi, 5 jin, 3 liang, and 8 zhu.
Multiply the 8 shi by 4, obtaining 32 jun.
Multiply this by 30 jin, and add the 5 jin, obtaining 965 jin.
Multiply this by 16 liang, and add the 3 liang, obtaining 15,443 liang.
Multiply this by 24 zhu, and add the 8 zhu, obtaining 376,640 zhu.
Divide this by 565 households, obtaining 656 zhu per household.
Divide this by 24 zhu, obtaining 27 liang and 8 zhu remaining.
Divide this by 16 liang, obtaining the final result.

Answer: *a* jin, *b* liang, *c* zhu.
"""

# Total households
戶數 = 565

# Initial silk amount: 8 shi, 5 jin, 3 liang, 8 zhu
石 = 8
斤 = 5
两 = 3
銖 = 8

# Convert shi to jun (1 shi = 4 jun)
鈞 = 石 * 4

# Convert jun to jin (1 jun = 30 jin), then add the remaining jin
斤總 = 鈞 * 30 + 斤

# Convert jin to liang (1 jin = 16 liang), then add the remaining liang
两總 = 斤總 * 16 + 两

# Convert liang to zhu (1 liang = 24 zhu), then add the remaining zhu
銖總 = 两總 * 24 + 銖

# Divide total zhu by the number of households
每戶銖 = Fraction(銖總, 戶數)

# Convert zhu to liang (1 liang = 24 zhu)
每戶两 = 每戶銖 // 24
剩餘銖 = 每戶銖 % 24

# Convert liang to jin (1 jin = 16 liang)
每戶斤 = 每戶两 // 16
剩餘两 = 每戶两 % 16

# Final result
a = 每戶斤
b = 剩餘两
c = 剩餘銖

# Answer: a斤 b两 c銖
"""
"""
