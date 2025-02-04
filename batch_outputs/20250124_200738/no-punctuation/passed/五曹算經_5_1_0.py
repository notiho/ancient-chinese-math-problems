"""
今有五百六十五户共責絲八石五斤三两八銖問户出絲㡬何
術曰列絲八石五斤三两八銖以四乘八石得三十二鈞以三十斤乘之納五斤得九百六十五斤以十六两乘之納三两得一萬五千四百四十三两以二十四銖乘之納八銖得三十七萬六百四十銖以五百六十五户除之得一户六百五十六銖以二十四銖除之得二十七两奇八銖以十六除之即得
答曰 a斤 
"""

#----- content starts here -----
"""
Suppose there are 565 households collectively responsible for producing 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household need to produce?

The procedure says:
List the silk amount as 8 shi, 5 jin, 3 liang, and 8 zhu.
Multiply 8 shi by 4 to get 32 jun.
Multiply this by 30 jin and add 5 jin to get 965 jin.
Multiply this by 16 liang and add 3 liang to get 15,443 liang.
Multiply this by 24 zhu and add 8 zhu to get 376,640 zhu.
Divide this by 565 households to get 656 zhu per household.
Divide this by 24 zhu to get 27 liang and 8 zhu remaining.
Divide this by 16 liang to get the final result.

Answer: *a* jin.
"""

from fractions import Fraction

# Total households
戶數 = 565

# Initial silk amount: 8 shi, 5 jin, 3 liang, 8 zhu
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
斤 = 鈞 * 鈞_to_斤 + 斤

# Convert 斤 to 两 and add the remaining 两
两 = 斤 * 斤_to_两 + 两

# Convert 两 to 銖 and add the remaining 銖
銖 = 两 * 两_to_銖 + 銖

# Divide total 銖 by the number of households
戶出銖 = Fraction(銖, 戶數)

# Convert 銖 to 两 (24 銖 = 1 两)
戶出两 = 戶出銖 // 两_to_銖
剩餘銖 = 戶出銖 % 两_to_銖

# Convert 两 to 斤 (16 两 = 1 斤)
戶出斤 = 戶出两 // 斤_to_两
剩餘两 = 戶出两 % 斤_to_两

# Final result
a = Fraction(戶出斤) + Fraction(剩餘两, 斤_to_两) + Fraction(剩餘銖, 斤_to_两 * 两_to_銖)#----- content ends here -----

"""
"""
