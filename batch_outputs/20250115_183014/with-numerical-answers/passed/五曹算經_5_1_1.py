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
Divide this by 16 liang, obtaining the final result.

Answer: *a*(=1) jin, *b*(=11) liang, *c*(=8) zhu.
"""

# Total silk owed: 8石5斤3两8銖
石 = 8
斤 = 5
两 = 3
銖 = 8

# Convert 石 to 鈞 (1石 = 4鈞)
鈞 = 4 * 石

# Convert 鈞 to 斤 (1鈞 = 30斤)
斤_total = 30 * 鈞 + 斤

# Convert 斤 to 两 (1斤 = 16两)
两_total = 16 * 斤_total + 两

# Convert 两 to 銖 (1两 = 24銖)
銖_total = 24 * 两_total + 銖

# Divide by 565 households
銖_per_household = Fraction(銖_total, 565)

# Convert 銖 back to 两 and 銖 (1两 = 24銖)
两_per_household =銖_per_household // 24
銖_remaining =銖_per_household % 24

# Convert 两 to 斤 and 两 (1斤 = 16两)
斤_per_household = 两_per_household // 16
两_remaining = 两_per_household % 16

# Final result
a = 斤_per_household  # 1
b = 两_remaining       # 11
c = 銖_remaining       # 8
"""
"""
