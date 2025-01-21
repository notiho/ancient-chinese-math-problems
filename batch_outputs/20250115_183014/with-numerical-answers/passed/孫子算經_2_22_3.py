"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a(=22) ，三分人得錢 b(=33) ，四分人得錢 c(=44) 。
"""

"""
Suppose there are 6930 qian to be distributed among 216 people, divided into three groups:
- 81 people, each receiving 2 shares,
- 72 people, each receiving 3 shares,
- 63 people, each receiving 4 shares.

Question: how much does each person in the three groups receive?

The procedure says:
First, place 81 people at the top, 72 people in the middle, and 63 people at the bottom.
Multiply the top position by 2, obtaining 162.
Multiply the middle position by 3, obtaining 216.
Multiply the bottom position by 4, obtaining 252.
Add these three positions together, obtaining 630 as the divisor.

Next, place the total amount of money, 6930 qian, at the top position.
Multiply it by 162, obtaining 1122660.
Multiply it by 216 for the middle position, obtaining 1496880.
Multiply it by 252 for the bottom position, obtaining 1746360.
Each of these is a dividend.

Divide each dividend by the divisor, 630:
- The top position gives 1782,
- The middle position gives 2376,
- The bottom position gives 2772.

Finally, divide each result by the number of people in the respective group to find the amount each person receives.

Answer: Each person in the 2-share group receives *a*(=22) qian, each person in the 3-share group receives *b*(=33) qian, and each person in the 4-share group receives *c*(=44) qian.
"""

# Total money
錢 = 6930

# Group sizes
二分人數 = 81
三分人數 = 72
四分人數 = 63

# Shares per person
二分 = 2
三分 = 3
四分 = 4

# Multiply group sizes by their respective shares
二分總份 = 二分人數 * 二分
三分總份 = 三分人數 * 三分
四分總份 = 四分人數 * 四分

# Add all shares to get the divisor
法 = 二分總份 + 三分總份 + 四分總份

# Calculate the total money for each group
二分總錢 = Fraction(二分總份 * 錢, 法)
三分總錢 = Fraction(三分總份 * 錢, 法)
四分總錢 = Fraction(四分總份 * 錢, 法)

# Divide total money for each group by the number of people in the group
a = Fraction(二分總錢, 二分人數)  # 22
b = Fraction(三分總錢, 三分人數)  # 33
c = Fraction(四分總錢, 四分人數)  # 44
"""
"""
