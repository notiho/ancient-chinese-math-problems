"""
今有五百六十五户共責絲八石五斤三两八銖問户出絲㡬何
術曰列絲八石五斤三两八銖以四乘八石得三十二鈞以三十斤乘之納五斤得九百六十五斤以十六两乘之納三两得一萬五千四百四十三两以二十四銖乘之納八銖得三十七萬六百四十銖以五百六十五户除之得一户六百五十六銖以二十四銖除之得二十七两奇八銖以十六除之即得
答曰 a斤 
"""

#----- content starts here -----
"""
Suppose there are 565 households collectively responsible for 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

The procedure says: Arrange the silk amount as 8 shi, 5 jin, 3 liang, and 8 zhu.
Multiply the 8 shi by 4, obtaining 32 jun.
Multiply this by 30 jin, adding the 5 jin, obtaining 965 jin.
Multiply this by 16 liang, adding the 3 liang, obtaining 15,443 liang.
Multiply this by 24 zhu, adding the 8 zhu, obtaining 370,640 zhu.
Divide this by 565 households, obtaining 656 zhu per household.
Divide this by 24 zhu, obtaining 27 liang and 8 zhu remaining.
Divide this by 16 liang, obtaining the result.

Answer: *a* jin.
"""

from fractions import Fraction

# Total households
戶數 = 565

# 丝 amount: 8石5斤3两8銖
石 = 8
斤 = 5
两 = 3
銖 = 8

# 石 to 鈞: 以四乘八石得三十二鈞
鈞 = 石 * 4

# 鈞 to 斤: 以三十斤乘之納五斤得九百六十五斤
斤總 = 鈞 * 30 + 斤

# 斤 to 两: 以十六两乘之納三两得一萬五千四百四十三两
两總 = 斤總 * 16 + 两

# 两 to 銖: 以二十四銖乘之納八銖得三十七萬六百四十銖
銖總 = 两總 * 24 + 銖

# Divide by 戶數: 以五百六十五户除之得一户六百五十六銖
每戶銖 = Fraction(銖總, 戶數)

# 銖 to 两: 以二十四銖除之得二十七两奇八銖
每戶两 = 每戶銖 // 24
剩餘銖 = 每戶銖 % 24

# 两 to 斤: 以十六除之即得
每戶斤 = 每戶两 // 16
剩餘两 = 每戶两 % 16

# Final result
a = Fraction(每戶斤) + Fraction(剩餘两, 16) + Fraction(剩餘銖, 16 * 24)#----- content ends here -----

"""
"""
