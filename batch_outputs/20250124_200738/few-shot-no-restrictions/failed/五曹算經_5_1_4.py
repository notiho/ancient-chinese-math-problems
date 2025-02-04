"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
術曰：列絲八石五斤三两八銖，以四乘八石得三十二鈞；以三十斤乘之、納五斤，得九百六十五斤；以十六两乘之、納三两，得一萬五千四百四十三两；以二十四銖乘之、納八銖，得三十七萬六百四十銖。以五百六十五户除之，得一户六百五十六銖；以二十四銖除之，得二十七两奇八銖；以十六除之即得。
答曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there are 565 households, and together they owe 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household owe?

The procedure says:
- Write the silk amount as 8 shi, 5 jin, 3 liang, and 8 zhu.
- Multiply 8 shi by 4 to get 32 jun.
- Multiply 32 jun by 30 jin and add 5 jin to get 965 jin.
- Multiply 965 jin by 16 liang and add 3 liang to get 15,443 liang.
- Multiply 15,443 liang by 24 zhu and add 8 zhu to get 370,640 zhu.
- Divide 370,640 zhu by 565 households to get 656 zhu per household.
- Divide 656 zhu by 24 zhu to get 27 liang and 8 zhu.
- Finally, divide 27 liang by 16 to get the amount in jin.

Answer: *a* jin.
"""

from fractions import Fraction

# Total silk owed
石 = 8  # shi
斤 = 5  # jin
两 = 3  # liang
銖 = 8  # zhu

# Convert all units to zhu
# 1 石 = 4 鈞, 1 鈞 = 30 斤, 1 斤 = 16 两, 1 两 = 24 銖
# Step 1: Convert 石 to 鈞
鈞 = 石 * 4

# Step 2: Convert 鈞 to 斤 and add the remaining 斤
斤_total = 鈞 * 30 + 斤

# Step 3: Convert 斤 to 两 and add the remaining 两
两_total = 斤_total * 16 + 两

# Step 4: Convert 两 to 銖 and add the remaining 銖
銖_total = 两_total * 24 + 銖

# Divide total 銖 by the number of households
户數 = 565
銖_per_household = Fraction(銖_total, 戶數)

# Convert 銖 back to 两 and 銖
两_per_household =銖_per_household // 24
銖_remainder =銖_per_household % 24

# Convert 两 to 斤
斤_per_household = 两_per_household // 16
两_remainder = 两_per_household % 16

# Final answer
a = float(斤_per_household) + Fraction(两_remainder, 16)
print(f"Each household owes: {a} 斤 ({斤_per_household} 斤, {两_remainder} 两, {銖_remainder} 銖).")#----- content ends here -----

"""
Code error: name '戶數' is not defined"""
