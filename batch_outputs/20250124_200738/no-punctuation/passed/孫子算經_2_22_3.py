"""
今有錢六千九百三十欲令二百一十六人作九分分之八十一人人與二分七十二人人與三分六十三人人與四分問三種各得幾何
術曰先置八十一人于上七十二人次之六十三人在下頭位以二乘之得一百六十二次位以三乘之得二百一十六下位以四乘之得二百五十二副并三位得六百三十為法又置錢六千九百三十為三位頭位以一百六十二乘之得一百一十二萬二千六百六十又以二百一十六乘中位得一百四十九萬六千八百八十又以二百五十二乘下位得一百七十四萬六千三百六十各為實以法六百三十各除之頭位得一千七百八十二中位得二千三百七十六下位得二千七百七十二各以人數除之即得
答曰二分人得錢 a 三分人得錢 b 四分人得錢 c 
"""

#----- content starts here -----
"""
Suppose there are 6930 coins to be distributed among 216 people in three groups:
- 81 people each receive 2 parts,
- 72 people each receive 3 parts,
- 63 people each receive 4 parts.

Question: how much does each person in each group receive?

The procedure says:
1. Place the 81 people in the top position, 72 people in the middle position, and 63 people in the bottom position.
2. Multiply the top position by 2, obtaining 162.
3. Multiply the middle position by 3, obtaining 216.
4. Multiply the bottom position by 4, obtaining 252.
5. Add these three results together, obtaining 630 as the divisor.
6. Place the 6930 coins as the dividend.
7. Multiply the dividend by 162 for the top position, obtaining 112260.
8. Multiply the dividend by 216 for the middle position, obtaining 149880.
9. Multiply the dividend by 252 for the bottom position, obtaining 174360.
10. Divide each result by the divisor (630).
11. Divide the result for each position by the number of people in that position to find the amount each person receives.

Answer: Each person in the 2-part group receives *a* coins, each person in the 3-part group receives *b* coins, and each person in the 4-part group receives *c* coins.
"""

# 人數
頭位人數 = 81  # 二分人
中位人數 = 72  # 三分人
下位人數 = 63  # 四分人

# 分數
頭位分數 = 2
中位分數 = 3
下位分數 = 4

# 先置八十一人于上，七十二人次之，六十三人在下
# 頭位以二乘之得一百六十二
頭位積 = 頭位人數 * 頭位分數

# 次位以三乘之得二百一十六
中位積 = 中位人數 * 中位分數

# 下位以四乘之得二百五十二
下位積 = 下位人數 * 下位分數

# 副并三位得六百三十為法
法 = 頭位積 + 中位積 + 下位積

# 置錢六千九百三十
錢 = 6930

# 頭位以一百六十二乘之
頭位實 = 頭位積 * 錢

# 中位以二百一十六乘之
中位實 = 中位積 * 錢

# 下位以二百五十二乘之
下位實 = 下位積 * 錢

# 各以法六百三十除之
頭位總錢 = Fraction(頭位實, 法)
中位總錢 = Fraction(中位實, 法)
下位總錢 = Fraction(下位實, 法)

# 各以人數除之，即得
a = Fraction(頭位總錢, 頭位人數)  # 二分人得錢
b = Fraction(中位總錢, 中位人數)  # 三分人得錢
c = Fraction(下位總錢, 下位人數)  # 四分人得錢#----- content ends here -----

"""
"""
