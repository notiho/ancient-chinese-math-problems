"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
術曰：列絲八石五斤三两八銖，以四乘八石得三十二鈞；以三十斤乘之、納五斤，得九百六十五斤；以十六两乘之、納三两，得一萬五千四百四十三两；以二十四銖乘之、納八銖，得三十七萬六百四十銖。以五百六十五户除之，得一户六百五十六銖；以二十四銖除之，得二十七两奇八銖；以十六除之即得。
答曰： a(=41/24)斤 。
"""

#----- content starts here -----
"""
Suppose there are 565 households, and together they owe 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household owe?

The procedure says: 
List the silk amount as 8 shi, 5 jin, 3 liang, and 8 zhu. 
Multiply the 8 shi by 4, obtaining 32 jun. 
Multiply this by 30 jin, adding 5 jin, obtaining 965 jin. 
Multiply this by 16 liang, adding 3 liang, obtaining 15,443 liang. 
Multiply this by 24 zhu, adding 8 zhu, obtaining 370,640 zhu. 
Divide this by 565 households, obtaining 656 zhu per household. 
Divide this by 24 zhu, obtaining 27 liang and 8 zhu remaining. 
Divide this by 16 liang to obtain the final result.

Answer: *a*(=41/24) jin.
"""

from fractions import Fraction

# Total silk owed: 8 shi, 5 jin, 3 liang, 8 zhu
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
鈞 = 石 * 石_to_鈞  # 8 * 4 = 32

# Step 2: Convert 鈞 to 斤 and add 5 斤
斤_total = 鈞 * 鈞_to_斤 + 斤  # 32 * 30 + 5 = 965

# Step 3: Convert 斤 to 两 and add 3 两
两_total = 斤_total * 斤_to_两 + 两  # 965 * 16 + 3 = 15,443

# Step 4: Convert 两 to 銖 and add 8 銖
銖_total = 两_total * 两_to_銖 + 銖  # 15,443 * 24 + 8 = 370,640

# Step 5: Divide total 銖 by 565 households
銖_per_household = Fraction(銖_total, 565)  # 370,640 / 565 = 656 zhu

# Step 6: Convert 銖 to 两 (24 銖 = 1 两)
两_per_household = Fraction(銖_per_household, 两_to_銖)  # 656 / 24 = 27 liang and 8 zhu

# Step 7: Convert 两 to 斤 (16 两 = 1 斤)
斤_per_household = Fraction(两_per_household, 斤_to_两)  # 27/16 + 8/(16*24) = 41/24

a = 斤_per_household  # 41/24
#----- content ends here -----

"""
"""
