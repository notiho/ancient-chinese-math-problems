"""
今有五百六十五户共責絲八石五斤三两八銖問户出絲㡬何
術曰列絲八石五斤三两八銖以四乘八石得三十二鈞以三十斤乘之納五斤得九百六十五斤以十六两乘之納三两得一萬五千四百四十三两以二十四銖乘之納八銖得三十七萬六百四十銖以五百六十五户除之得一户六百五十六銖以二十四銖除之得二十七两奇八銖以十六除之即得
答曰 a斤 
"""

"""
Suppose there are 565 households collectively responsible for 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

The procedure says: 
List the silk as 8 shi, 5 jin, 3 liang, and 8 zhu.
Multiply 8 shi by 4 to get 32 jun.
Multiply this by 30 jin and add 5 jin to get 965 jin.
Multiply this by 16 liang and add 3 liang to get 15,443 liang.
Multiply this by 24 zhu and add 8 zhu to get 370,640 zhu.
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

# Conversion factors
石_to_鈞 = 4
鈞_to_斤 = 30
斤_to_两 = 16
两_to_銖 = 24

# Step 1: Convert 石 to 鈞
鈞 = 石 * 石_to_鈞

# Step 2: Convert 鈞 to 斤 and add 5 斤
斤 = 鈞 * 鈞_to_斤 + 斤

# Step 3: Convert 斤 to 两 and add 3 两
两 = 斤 * 斤_to_两 + 两

# Step 4: Convert 两 to 銖 and add 8 銖
銖 = 两 * 两_to_銖 + 銖

# Step 5: Divide total 銖 by 565 households
戶銖 = Fraction(銖, 565)

# Step 6: Convert 銖 to 两 and find remainder
戶两 = 戶銖 // 两_to_銖
剩餘銖 = 戶銖 % 两_to_銖

# Step 7: Convert 戶两 to 斤 and find remainder
戶斤 = 戶两 // 斤_to_两
剩餘两 = 戶两 % 斤_to_两

# Final result
a = Fraction(戶斤) + Fraction(剩餘两, 斤_to_两) + Fraction(剩餘銖, 斤_to_两 * 两_to_銖)
"""
"""
