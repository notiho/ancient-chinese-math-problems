"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a(=22) ，三分人得錢 b(=33) ，四分人得錢 c(=44) 。
"""

#----- content starts here -----
"""
Suppose there are 6930 qian to be distributed among 216 people, divided into three groups:
- 81 people, each receiving 2 parts;
- 72 people, each receiving 3 parts;
- 63 people, each receiving 4 parts.

Question: how much does each person in the three groups receive?

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
Each of these is the dividend, and divide each by 630.

Finally, divide each result by the number of people in the respective group to obtain the amount each person receives.

Answer: Each person in the 2-part group receives *a*(=22) qian, in the 3-part group receives *b*(=33) qian, and in the 4-part group receives *c*(=44) qian.
"""

# Total qian and group sizes
總錢 = 6930
二分人數 = 81
三分人數 = 72
四分人數 = 63

# Multipliers for each group
二分乘數 = 2
三分乘數 = 3
四分乘數 = 4

# Calculate the weighted contributions
二分權重 = 二分人數 * 二分乘數
三分權重 = 三分人數 * 三分乘數
四分權重 = 四分人數 * 四分乘數

# Total weight (法)
總權重 = 二分權重 + 三分權重 + 四分權重

# Calculate the total qian distributed to each group
二分總錢 = Fraction(總錢 * 二分權重, 総權重)
三分總錢 = Fraction(總錢 * 三分權重, 総權重)
四分總錢 = Fraction(總錢 * 四分權重, 総權重)

# Calculate the amount each person receives in each group
a = 二分總錢 / 二分人數  # 22
b = 三分總錢 / 三分人數  # 33
c = 四分總錢 / 四分人數  # 44#----- content ends here -----

"""
Code error: name '総權重' is not defined"""
