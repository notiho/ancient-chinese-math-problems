"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

"""
Suppose there are 6930 qian to be distributed among 216 people, divided into three groups:
- 81 people, each receiving 2 shares,
- 72 people, each receiving 3 shares,
- 63 people, each receiving 4 shares.

Question: how much does each group receive?

The procedure says:
1. Place 81 people at the top, 72 people next, and 63 people at the bottom.
2. Multiply the top position by 2, obtaining 162.
   Multiply the middle position by 3, obtaining 216.
   Multiply the bottom position by 4, obtaining 252.
3. Add these three results together, obtaining 630 as the divisor.
4. Place the total amount of money, 6930 qian, as the dividend.
5. Multiply the dividend by 162 for the top position, obtaining 1122660.
   Multiply the dividend by 216 for the middle position, obtaining 1496880.
   Multiply the dividend by 252 for the bottom position, obtaining 1746360.
6. Divide each of these results by 630 to get the total amount for each group.
7. Divide the total amount for each group by the number of people in that group to get the amount per person.

Answer: The 2-share group receives *a* qian, the 3-share group receives *b* qian, and the 4-share group receives *c* qian.
"""

# Total money and people
總錢 = 6930
總人數 = 216

# Group sizes
二分人數 = 81
三分人數 = 72
四分人數 = 63

# Shares per person
二分份數 = 2
三分份數 = 3
四分份數 = 4

# Step 2: Multiply group sizes by their respective shares
頭位 = 二分人數 * 二分份數  # 81 * 2
次位 = 三分人數 * 三分份數  # 72 * 3
下位 = 四分人數 * 四分份數  # 63 * 4

# Step 3: Add the results to get the divisor
法 = 頭位 + 次位 + 下位  # 162 + 216 + 252

# Step 5: Multiply total money by each group's weighted share
頭位實 = 總錢 * 頭位  # 6930 * 162
次位實 = 總錢 * 次位  # 6930 * 216
下位實 = 總錢 * 下位  # 6930 * 252

# Step 6: Divide each result by the divisor to get the total money for each group
二分總錢 = Fraction(頭位實, 法)
三分總錢 = Fraction(次位實, 法)
四分總錢 = Fraction(下位實, 法)

# Step 7: Divide the total money for each group by the number of people in that group
a = Fraction(二分總錢, 二分人數)  # Money per person in the 2-share group
b = Fraction(三分總錢, 三分人數)  # Money per person in the 3-share group
c = Fraction(四分總錢, 四分人數)  # Money per person in the 4-share group
"""
"""
