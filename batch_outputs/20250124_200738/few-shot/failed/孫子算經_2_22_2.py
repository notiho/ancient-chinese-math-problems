"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

#----- content starts here -----
"""
Suppose there are 6930 coins to be distributed among 216 people, divided into three groups:
- 81 people, each receiving 2 parts,
- 72 people, each receiving 3 parts,
- 63 people, each receiving 4 parts.

Question: how much does each group receive in total?

The procedure says:
First, place 81 people at the top, 72 people in the middle, and 63 people at the bottom.
Multiply the first position (81 people) by 2, obtaining 162.
Multiply the second position (72 people) by 3, obtaining 216.
Multiply the third position (63 people) by 4, obtaining 252.
Add these three results together, obtaining 630 as the divisor.

Next, place the total coins (6930) as the three positions:
- Multiply 6930 by 162 for the first position, obtaining 1122600.
- Multiply 6930 by 216 for the second position, obtaining 1496880.
- Multiply 6930 by 252 for the third position, obtaining 1746360.

Each result is divided by the divisor (630):
- The first position gives 1782 coins,
- The second position gives 2376 coins,
- The third position gives 2772 coins.

Finally, divide each result by the number of people in each group to find the amount per person.

Answer: The group receiving 2 parts gets *a* coins, the group receiving 3 parts gets *b* coins, and the group receiving 4 parts gets *c* coins.
"""

# 人數與分數
二分人數 = 81
三分人數 = 72
四分人數 = 63

# 分數
二分 = 2
三分 = 3
四分 = 4

# 頭位以二乘之，次位以三乘之，下位以四乘之
頭位 = 二分人數 * 二分
次位 = 三分人數 * 三分
下位 = 四分人數 * 四分

# 副并三位，得法
法 = 頭位 + 次位 + 下位

# 總錢數
總錢 = 6930

# 各位乘總錢數
頭位實 = 總錢 * 頭位
次位實 = 總錢 * 次位
下位實 = 總錢 * 下位

# 各為實以法除之
頭位得 = Fraction(頭位實, 法)
次位得 = Fraction(次位實, 法)
下位得 = Fraction(下位實, 法)

# 答案
a = 頭位得
b = 次位得
c = 下位得#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 22, Actual: 1782
Variable 'b' has wrong value. Expected: 33, Actual: 2376
Variable 'c' has wrong value. Expected: 44, Actual: 2772"""
