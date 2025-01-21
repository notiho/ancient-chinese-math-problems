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
Multiply the 8 shi by 4 to obtain 32 jun.
Multiply this by 30 jin and add 5 jin to obtain 965 jin.
Multiply this by 16 liang and add 3 liang to obtain 15,443 liang.
Multiply this by 24 zhu and add 8 zhu to obtain 376,640 zhu.
Divide this by 565 households to obtain 656 zhu per household.
Divide this by 24 zhu to obtain 27 liang and 8 zhu remaining.
Divide this by 16 liang to obtain the final result.

Answer: *a* jin, *b* liang, *c* zhu.
"""

# Total silk: 8 shi, 5 jin, 3 liang, 8 zhu
石 = 8
斤 = 5
两 = 3
銖 = 8

# Convert shi to jin
# Multiply 8 shi by 4 to get 32 jun
鈞 = 石 * 4

# Multiply 32 jun by 30 jin and add 5 jin
斤總 = 鈞 * 30 + 斤

# Convert jin to liang
# Multiply 965 jin by 16 liang and add 3 liang
两總 = 斤總 * 16 + 两

# Convert liang to zhu
# Multiply 15,443 liang by 24 zhu and add 8 zhu
銖總 = 两總 * 24 + 銖

# Divide total zhu by 565 households
銖每戶 = Fraction(銖總, 565)

# Convert zhu to liang
两每戶 =銖每戶 // 24
銖剩餘 =銖每戶 % 24

# Convert liang to jin
斤每戶 = 两每戶 // 16
两剩餘 = 两每戶 % 16

# Final result
a = 斤每戶
b = 两剩餘
c = 銖剩餘
"""
"""
