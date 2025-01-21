"""
今有五百六十五户共責絲八石五斤三两八銖問户出絲㡬何
術曰列絲八石五斤三两八銖以四乘八石得三十二鈞以三十斤乘之納五斤得九百六十五斤以十六两乘之納三两得一萬五千四百四十三两以二十四銖乘之納八銖得三十七萬六百四十銖以五百六十五户除之得一户六百五十六銖以二十四銖除之得二十七两奇八銖以十六除之即得
答曰 a斤 b 两 c銖 
"""

"""
Suppose there are 565 households collectively responsible for 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

The procedure says:
List the silk amount as 8 shi, 5 jin, 3 liang, and 8 zhu.
Multiply the 8 shi by 4 to get 32 jun.
Multiply this by 30 jin and add the 5 jin to get 965 jin.
Multiply this by 16 liang and add the 3 liang to get 15,443 liang.
Multiply this by 24 zhu and add the 8 zhu to get 376,640 zhu.
Divide this by 565 households to get 656 zhu per household.
Divide 656 zhu by 24 to get 27 liang and 8 zhu remaining.
Divide 27 liang by 16 to get the final result.

Answer: *a* jin, *b* liang, *c* zhu.
"""

# Total silk: 8 shi, 5 jin, 3 liang, 8 zhu
石 = 8
斤 = 5
两 = 3
銖 = 8

# Convert 8 shi to jun (1 shi = 4 jun)
鈞 = 4 * 石

# Convert jun to jin (1 jun = 30 jin) and add the remaining 5 jin
斤 = 30 * 鈞 + 斤

# Convert jin to liang (1 jin = 16 liang) and add the remaining 3 liang
两 = 16 * 斤 + 两

# Convert liang to zhu (1 liang = 24 zhu) and add the remaining 8 zhu
銖 = 24 * 两 + 銖

# Divide total zhu by 565 households
戶出銖 = Fraction(銖, 565)

# Convert zhu to liang (1 liang = 24 zhu)
戶出两 = 戶出銖 // 24
剩餘銖 = 戶出銖 % 24

# Convert liang to jin (1 jin = 16 liang)
戶出斤 = 戶出两 // 16
剩餘两 = 戶出两 % 16

# Final result
a = 戶出斤
b = 剩餘两
c = 剩餘銖

# Answer: a jin, b liang, c zhu
"""
"""
