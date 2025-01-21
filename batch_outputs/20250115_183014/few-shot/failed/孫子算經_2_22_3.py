"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

"""
Suppose there are 6930 coins to be distributed among 216 people in three groups:
- 81 people, each receiving 2 parts,
- 72 people, each receiving 3 parts,
- 63 people, each receiving 4 parts.

Question: how much does each group receive in total?

The procedure says:
First, place 81 people at the top, 72 people in the middle, and 63 people at the bottom.
Multiply the top position by 2, obtaining 162.
Multiply the middle position by 3, obtaining 216.
Multiply the bottom position by 4, obtaining 252.
Add these three results together, obtaining 630 as the divisor.

Next, place the 6930 coins as the total.
Multiply the total by 162 for the top position, obtaining 1122660.
Multiply the total by 216 for the middle position, obtaining 1496880.
Multiply the total by 252 for the bottom position, obtaining 1746360.
Each of these results is divided by the divisor, 630, to obtain the total coins for each group.
Finally, divide the total coins for each group by the number of people in that group to find the coins per person.

Answer: The group receiving 2 parts gets *a* coins, the group receiving 3 parts gets *b* coins, and the group receiving 4 parts gets *c* coins.
"""

# Total coins
總錢 = 6930

# Group sizes
二分人數 = 81
三分人數 = 72
四分人數 = 63

# Multipliers for each group
二分乘數 = 2
三分乘數 = 3
四分乘數 = 4

# Multiply group sizes by their respective multipliers
二分總分 = 二分人數 * 二分乘數
三分總分 = 三分人數 * 三分乘數
四分總分 = 四分人數 * 四分乘數

# Add all the results to get the divisor
法 = 二分總分 + 三分總分 + 四分總分

# Calculate the total coins for each group
二分總錢 = Fraction(總錢 * 二分總分, 法)
三分總錢 = Fraction(總錢 * 三分總分, 法)
四分總錢 = Fraction(總錢 * 四分總分, 法)

# Assign results
a = 二分總錢
b = 三分總錢
c = 四分總錢
"""
Variable 'a' has wrong value. Expected: 22, Actual: 1782
Variable 'b' has wrong value. Expected: 33, Actual: 2376
Variable 'c' has wrong value. Expected: 44, Actual: 2772"""
