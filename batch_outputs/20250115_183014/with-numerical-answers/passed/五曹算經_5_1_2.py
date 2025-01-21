"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
術曰：列絲八石五斤三两八銖，以四乘八石得三十二鈞；以三十斤乘之、納五斤，得九百六十五斤；以十六两乘之、納三两，得一萬五千四百四十三两；以二十四銖乘之、納八銖，得三十七萬六百四十銖。以五百六十五户除之，得一户六百五十六銖；以二十四銖除之，得二十七两奇八銖；以十六除之即得。
答曰： a(=1)斤 b(=11) 两 c(=8)銖 。
"""

"""
Suppose there are 565 households, and together they owe 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household owe?

The procedure says: Arrange the silk amount as 8 shi, 5 jin, 3 liang, and 8 zhu.
Multiply the 8 shi by 4, obtaining 32 jun.
Multiply this by 30 jin, and add 5 jin, obtaining 965 jin.
Multiply this by 16 liang, and add 3 liang, obtaining 15,443 liang.
Multiply this by 24 zhu, and add 8 zhu, obtaining 370,640 zhu.
Divide this by 565 households, obtaining 656 zhu per household.
Divide this by 24 zhu, obtaining 27 liang and 8 zhu remaining.
Divide this by 16 liang to obtain the final result.

Answer: *a*(=1) jin, *b*(=11) liang, *c*(=8) zhu.
"""

# Total silk owed: 8 shi, 5 jin, 3 liang, 8 zhu
絲_石 = 8
絲_斤 = 5
絲_两 = 3
絲_銖 = 8

# Convert 8 shi to jun (1 shi = 4 jun)
絲_鈞 = 4 * 絲_石

# Convert jun to jin (1 jun = 30 jin)
絲_斤_total = 30 * 絲_鈞 + 絲_斤

# Convert jin to liang (1 jin = 16 liang)
絲_两_total = 16 * 絲_斤_total + 絲_两

# Convert liang to zhu (1 liang = 24 zhu)
絲_銖_total = 24 * 絲_两_total + 絲_銖

# Total households
戶數 = 565

# Divide total zhu by households
戶_銖 = 絲_銖_total // 戶數
戶_銖_餘 = 絲_銖_total % 戶數

# Convert zhu to liang (1 liang = 24 zhu)
戶_两 = 戶_銖 // 24
戶_銖_餘 = 戶_銖 % 24

# Convert liang to jin (1 jin = 16 liang)
戶_斤 = 戶_两 // 16
戶_两_餘 = 戶_两 % 16

# Final result
a = 戶_斤  # 1 jin
b = 戶_两_餘  # 11 liang
c = 戶_銖_餘  # 8 zhu
"""
"""
