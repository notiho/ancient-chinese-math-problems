"""
今有五百六十五户共責絲八石五斤三两八銖問户出絲㡬何
術曰列絲八石五斤三两八銖以四乘八石得三十二鈞以三十斤乘之納五斤得九百六十五斤以十六两乘之納三两得一萬五千四百四十三两以二十四銖乘之納八銖得三十七萬六百四十銖以五百六十五户除之得一户六百五十六銖以二十四銖除之得二十七两奇八銖以十六除之即得
答曰 a斤 b 两 c銖 
"""

"""
Suppose there are 565 households collectively responsible for 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

The procedure says:
- Multiply 8 shi by 4 to convert to 32 jun.
- Multiply by 30 to convert to 960 jin, then add 5 jin to get 965 jin.
- Multiply by 16 to convert to 15,440 liang, then add 3 liang to get 15,443 liang.
- Multiply by 24 to convert to 370,640 zhu, then add 8 zhu to get 370,648 zhu.
- Divide by 565 households to get 656 zhu per household.
- Divide by 24 zhu to get 27 liang and 8 zhu remaining.
- Divide the remaining liang by 16 to get the final result.

Answer: Each household contributes *a* jin, *b* liang, and *c* zhu.
"""

from fractions import Fraction

# Total silk: 8 shi, 5 jin, 3 liang, 8 zhu
石 = 8
斤 = 5
两 = 3
銖 = 8

# Convert 8 shi to jun: 1 shi = 4 jun
鈞 = 石 * 4

# Convert jun to jin: 1 jun = 30 jin
斤 = 鈞 * 30 + 斤

# Convert jin to liang: 1 jin = 16 liang
两 = 斤 * 16 + 两

# Convert liang to zhu: 1 liang = 24 zhu
銖 = 两 * 24 + 銖

# Divide total zhu by 565 households
每戶銖 = Fraction(銖, 565)

# Convert zhu to liang: 1 liang = 24 zhu
每戶两 = 每戶銖 // 24
剩餘銖 = 每戶銖 % 24

# Convert liang to jin: 1 jin = 16 liang
每戶斤 = 每戶两 // 16
剩餘两 = 每戶两 % 16

# Final result
a = 每戶斤
b = 剩餘两
c = 剩餘銖

a, b, c  # Output the results
"""
"""
