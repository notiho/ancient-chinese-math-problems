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
List the silk as 8 shi, 5 jin, 3 liang, and 8 zhu.
- Multiply 8 shi by 4 to get 32 jun.
- Multiply this by 30 jin per jun, and add 5 jin, obtaining 965 jin.
- Multiply this by 16 liang per jin, and add 3 liang, obtaining 15,443 liang.
- Multiply this by 24 zhu per liang, and add 8 zhu, obtaining 370,640 zhu.
Divide this by 565 households, obtaining 656 zhu per household.
- Divide this by 24 zhu per liang, obtaining 27 liang and 8 zhu remaining.
- Divide this by 16 liang per jin to get the final result.

Answer: *a* jin.
"""

from fractions import Fraction

# Total silk owed: 8 shi, 5 jin, 3 liang, 8 zhu
shi = 8
jin = 5
liang = 3
zhu = 8

# Conversion factors
shi_to_jun = 4
jun_to_jin = 30
jin_to_liang = 16
liang_to_zhu = 24

# Step 1: Convert shi to jun
jun = shi * shi_to_jun

# Step 2: Convert jun to jin and add the remaining jin
total_jin = jun * jun_to_jin + jin

# Step 3: Convert jin to liang and add the remaining liang
total_liang = total_jin * jin_to_liang + liang

# Step 4: Convert liang to zhu and add the remaining zhu
total_zhu = total_liang * liang_to_zhu + zhu

# Step 5: Divide total zhu by the number of households
households = 565
zhu_per_household = Fraction(total_zhu, households)

# Step 6: Convert zhu per household to liang and zhu
liang_per_household = zhu_per_household // liang_to_zhu
remaining_zhu = zhu_per_household % liang_to_zhu

# Step 7: Convert liang per household to jin and liang
jin_per_household = liang_per_household // jin_to_liang
remaining_liang = liang_per_household % jin_to_liang

# Final result
a = f"{jin_per_household}斤 {remaining_liang}两 {remaining_zhu}銖"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 41/24, Actual: 1斤 11两 8銖"""
