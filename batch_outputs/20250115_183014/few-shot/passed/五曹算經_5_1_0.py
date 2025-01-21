"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
術曰：列絲八石五斤三两八銖，以四乘八石得三十二鈞；以三十斤乘之、納五斤，得九百六十五斤；以十六两乘之、納三两，得一萬五千四百四十三两；以二十四銖乘之、納八銖，得三十七萬六百四十銖。以五百六十五户除之，得一户六百五十六銖；以二十四銖除之，得二十七两奇八銖；以十六除之即得。
答曰： a斤 b 两 c銖 。
"""

"""
Suppose there are 565 households, and together they owe 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household owe?

The procedure says: 
List the silk as 8 shi, 5 jin, 3 liang, and 8 zhu.
Multiply the 8 shi by 4, obtaining 32 jun.
Multiply this by 30 jin, and add 5 jin, obtaining 965 jin.
Multiply this by 16 liang, and add 3 liang, obtaining 15,443 liang.
Multiply this by 24 zhu, and add 8 zhu, obtaining 370,640 zhu.
Divide this by 565 households, obtaining 656 zhu per household.
Divide this by 24 zhu, obtaining 27 liang and 8 zhu remaining.
Divide this by 16 liang, obtaining the final result.

Answer: *a* jin, *b* liang, *c* zhu.
"""

from fractions import Fraction

# Total silk owed: 8 shi, 5 jin, 3 liang, 8 zhu
石 = 8
斤 = 5
两 = 3
銖 = 8

# Convert 8 shi to jun (1 shi = 4 jun)
鈞 = 4 * 石

# Convert jun to jin (1 jun = 30 jin) and add 5 jin
斤 = 30 * 鈞 + 斤

# Convert jin to liang (1 jin = 16 liang) and add 3 liang
两 = 16 * 斤 + 两

# Convert liang to zhu (1 liang = 24 zhu) and add 8 zhu
銖 = 24 * 两 + 銖

# Total households
戶 = 565

# Divide total zhu by households to get zhu per household
每戶銖 = Fraction(銖, 戶)

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

a, b, c  # Output the result as a斤 b两 c銖
"""
"""
