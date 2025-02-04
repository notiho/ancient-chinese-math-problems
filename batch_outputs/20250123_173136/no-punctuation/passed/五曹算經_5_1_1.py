"""
今有五百六十五户共責絲八石五斤三两八銖問户出絲㡬何
術曰列絲八石五斤三两八銖以四乘八石得三十二鈞以三十斤乘之納五斤得九百六十五斤以十六两乘之納三两得一萬五千四百四十三两以二十四銖乘之納八銖得三十七萬六百四十銖以五百六十五户除之得一户六百五十六銖以二十四銖除之得二十七两奇八銖以十六除之即得
答曰 a斤 
"""

"""
Suppose there are 565 households collectively responsible for producing 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

The procedure says: 
List the silk as 8 shi, 5 jin, 3 liang, and 8 zhu.
Multiply the 8 shi by 4 to get 32 jun.
Multiply this by 30 jin and add the 5 jin to get 965 jin.
Multiply this by 16 liang and add the 3 liang to get 15,443 liang.
Multiply this by 24 zhu and add the 8 zhu to get 370,640 zhu.
Divide this by 565 households to get 656 zhu per household.
Divide this by 24 zhu to get 27 liang and 8 zhu remaining.
Divide this by 16 liang to get the final result.

Answer: *a* jin.
"""

from fractions import Fraction

# Total silk: 8 shi, 5 jin, 3 liang, 8 zhu
石 = 8
斤 = 5
两 = 3
銖 = 8

# Convert shi to jin
# 1 石 = 4 鈞, 1 鈞 = 30 斤
鈞 = 4 * 石
斤_total = 30 * 鈞 + 斤

# Convert jin to liang
# 1 斤 = 16 两
两_total = 16 * 斤_total + 两

# Convert liang to zhu
# 1 两 = 24 銖
銖_total = 24 * 两_total + 銖

# Divide by 565 households
銖_per_household = Fraction(銖_total, 565)

# Convert zhu to liang
两_per_household = Fraction(銖_per_household, 24)
銖_remainder = 銖_per_household % 24

# Convert liang to jin
斤_per_household = Fraction(两_per_household, 16)
两_remainder = 两_per_household % 16

# Final answer
a = 斤_per_household

"""
"""
