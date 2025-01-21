"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
術曰：列絲八石五斤三两八銖，以四乘八石得三十二鈞；以三十斤乘之、納五斤，得九百六十五斤；以十六两乘之、納三两，得一萬五千四百四十三两；以二十四銖乘之、納八銖，得三十七萬六百四十銖。以五百六十五户除之，得一户六百五十六銖；以二十四銖除之，得二十七两奇八銖；以十六除之即得。
答曰： a(=1)斤 b(=11) 两 c(=8)銖 。
"""

"""
Suppose there are 565 households, and together they owe 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household owe?

The procedure says: Arrange the silk amount as 8 shi, 5 jin, 3 liang, and 8 zhu.
Multiply 8 shi by 4 to get 32 jun.
Multiply this by 30 jin per jun, and add 5 jin, obtaining 965 jin.
Multiply this by 16 liang per jin, and add 3 liang, obtaining 15443 liang.
Multiply this by 24 zhu per liang, and add 8 zhu, obtaining 370640 zhu.
Divide this by 565 households, obtaining 656 zhu per household.
Divide this by 24 zhu per liang, obtaining 27 liang and 8 zhu remaining.
Divide this by 16 liang per jin to get the final result.

Answer: *a*(=1) jin, *b*(=11) liang, *c*(=8) zhu.
"""

# Total silk owed: 8 shi, 5 jin, 3 liang, 8 zhu
絲_石 = 8
絲_斤 = 5
絲_两 = 3
絲_銖 = 8

# Conversion factors
石_to_鈞 = 4
鈞_to_斤 = 30
斤_to_两 = 16
两_to_銖 = 24

# Households
戶數 = 565

# Step 1: Convert 8 shi to jun
絲_鈞 = 石_to_鈞 * 絲_石  # 32 jun

# Step 2: Convert jun to jin and add 5 jin
絲_斤 = 絲_鈞 * 鈞_to_斤 + 絲_斤  # 965 jin

# Step 3: Convert jin to liang and add 3 liang
絲_两 = 絲_斤 * 斤_to_两 + 絲_两  # 15443 liang

# Step 4: Convert liang to zhu and add 8 zhu
絲_銖 = 絲_两 * 两_to_銖 + 絲_銖  # 370640 zhu

# Step 5: Divide total zhu by the number of households
戶_銖 = 絲_銖 // 戶數  # 656 zhu per household
剩餘銖 = 絲_銖 % 戶數  # Remaining zhu (not used here)

# Step 6: Convert zhu to liang
戶_两 = 戶_銖 // 两_to_銖  # 27 liang
戶_銖 = 戶_銖 % 两_to_銖  # 8 zhu remaining

# Step 7: Convert liang to jin
戶_斤 = 戶_两 // 斤_to_两  # 1 jin
戶_两 = 戶_两 % 斤_to_两  # 11 liang remaining

# Final answer
a = 戶_斤  # 1 jin
b = 戶_两  # 11 liang
c = 戶_銖  # 8 zhu
"""
"""
