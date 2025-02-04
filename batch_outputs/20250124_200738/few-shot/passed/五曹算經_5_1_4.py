"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
術曰：列絲八石五斤三两八銖，以四乘八石得三十二鈞；以三十斤乘之、納五斤，得九百六十五斤；以十六两乘之、納三两，得一萬五千四百四十三两；以二十四銖乘之、納八銖，得三十七萬六百四十銖。以五百六十五户除之，得一户六百五十六銖；以二十四銖除之，得二十七两奇八銖；以十六除之即得。
答曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there are 565 households, and they are collectively responsible for 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

The procedure says: 
List the silk amount as 8 shi, 5 jin, 3 liang, and 8 zhu.
Multiply 8 shi by 4 to get 32 jun.
Multiply this by 30 jin and add 5 jin, obtaining 965 jin.
Multiply this by 16 liang and add 3 liang, obtaining 15,443 liang.
Multiply this by 24 zhu and add 8 zhu, obtaining 370,640 zhu.
Divide this by 565 households, obtaining 656 zhu per household.
Divide this by 24 zhu, obtaining 27 liang and 8 zhu remaining.
Divide this by 16 liang to get the final result.

Answer: *a* jin.
"""

from fractions import Fraction

# Total households
戶數 = 565

# Total silk: 8 shi, 5 jin, 3 liang, 8 zhu
石 = 8
斤 = 5
两 = 3
銖 = 8

# Step 1: Convert shi to jun (1 shi = 4 jun)
鈞 = 石 * 4

# Step 2: Convert jun to jin (1 jun = 30 jin)
斤總 = 鈞 * 30 + 斤

# Step 3: Convert jin to liang (1 jin = 16 liang)
两總 = 斤總 * 16 + 两

# Step 4: Convert liang to zhu (1 liang = 24 zhu)
銖總 = 两總 * 24 + 銖

# Step 5: Divide total zhu by the number of households
每戶銖 = Fraction(銖總, 戶數)

# Step 6: Convert zhu back to liang (1 liang = 24 zhu)
每戶两 = 每戶銖 // 24
剩餘銖 = 每戶銖 % 24

# Step 7: Convert liang to jin (1 jin = 16 liang)
每戶斤 = 每戶两 // 16
剩餘两 = 每戶两 % 16

# Final result
a = 每戶斤 + Fraction(剩餘两, 16) + Fraction(剩餘銖, 16 * 24)#----- content ends here -----

"""
"""
