"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a ，三分人得錢 b ，四分人得錢 c 。
"""

"""
Suppose there are 6930 qian to be distributed among 216 people in 9 parts.
81 people are to receive 2 parts each, 72 people are to receive 3 parts each, and 63 people are to receive 4 parts each.
Question: how much does each group receive?

The procedure says:
First, place 81 people at the top, 72 people in the middle, and 63 people at the bottom.
Multiply the top position by 2, obtaining 162.
Multiply the middle position by 3, obtaining 216.
Multiply the bottom position by 4, obtaining 252.
Add the three positions together, obtaining 630 as the divisor.
Next, place the 6930 qian as the total amount.
Multiply it by 162 for the top position, obtaining 1122660.
Multiply it by 216 for the middle position, obtaining 1496880.
Multiply it by 252 for the bottom position, obtaining 1746360.
Each of these is the dividend.
Divide each by the divisor, 630.
The results are the total amounts for each group.
Finally, divide each total amount by the number of people in the group to obtain the amount per person.

Answer: the 2-part people receive *a* qian, the 3-part people receive *b* qian, and the 4-part people receive *c* qian.
"""

# Total money
錢 = 6930

# Number of people in each group
二分人數 = 81
三分人數 = 72
四分人數 = 63

# Multipliers for each group
二分乘數 = 2
三分乘數 = 3
四分乘數 = 4

# 頭位以二乘之，次位以三乘之，下位以四乘之
頭位 = 二分人數 * 二分乘數
次位 = 三分人數 * 三分乘數
下位 = 四分人數 * 四分乘數

# 副并三位，得六百三十為法
法 = 頭位 + 次位 + 下位

# Multiply total money by each group's multiplier
頭位實 = 錢 * 頭位
次位實 = 錢 * 次位
下位實 = 錢 * 下位

# Divide each by the divisor
頭位總錢 = Fraction(頭位實, 法)
次位總錢 = Fraction(次位實, 法)
下位總錢 = Fraction(下位實, 法)

# Divide each group's total money by the number of people in the group
a = Fraction(頭位總錢, 二分人數)
b = Fraction(次位總錢, 三分人數)
c = Fraction(下位總錢, 四分人數)
"""
"""
