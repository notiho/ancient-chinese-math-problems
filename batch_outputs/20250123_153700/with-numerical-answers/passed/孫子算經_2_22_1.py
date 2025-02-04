"""
今有錢六千九百三十，欲令二百一十六人作九分，分之八十一人，人與二分；七十二人，人與三分；六十三人，人與四分。問：三種各得幾何？
術曰：先置八十一人于上，七十二人次之，六十三人在下，頭位以二乘之，得一百六十二，次位以三乘之，得二百一十六，下位以四乘之，得二百五十二，副并三位，得六百三十為法。又置錢六千九百三十為三位頭位，以一百六十二乘之，得一百一十二萬二千六百六十，又以二百一十六乘中位，得一百四十九萬六千八百八十，又以二百五十二乘下位，得一百七十四萬六千三百六十，各為實以法，六百三十各除之，頭位得一千七百八十二，中位得二千三百七十六，下位得二千七百七十二，各以人數除之，即得。
答曰：二分人得錢 a(=22) ，三分人得錢 b(=33) ，四分人得錢 c(=44) 。
"""

"""
Suppose there are 6930 qian, to be distributed among 216 people in 9 parts.
81 people are to receive 2 parts each, 72 people are to receive 3 parts each, and 63 people are to receive 4 parts each.
Question: how much does each group receive?

The procedure says: First, place the 81 people at the top, the 72 people next, and the 63 people at the bottom.
Multiply the top position by 2, obtaining 162.
Multiply the middle position by 3, obtaining 216.
Multiply the bottom position by 4, obtaining 252.
Add the three positions together, obtaining 630 as the divisor.
Then, place the 6930 qian as the total and multiply it by each position:
Multiply the total by 162 for the top position, obtaining 1122600.
Multiply the total by 216 for the middle position, obtaining 1496880.
Multiply the total by 252 for the bottom position, obtaining 1746360.
Divide each result by the divisor, 630, obtaining the total amount for each group.
Finally, divide each group's total by the number of people in that group to find the amount each person receives.

Answer: Each person in the 2-part group receives *a*(=22) qian, each person in the 3-part group receives *b*(=33) qian, and each person in the 4-part group receives *c*(=44) qian.
"""

# Total money and people
錢 = 6930
總人數 = 216

# Group sizes
二分人數 = 81
三分人數 = 72
四分人數 = 63

# Multiply group sizes by their respective parts
頭位 = 2 * 二分人數  # 162
中位 = 3 * 三分人數  # 216
下位 = 4 * 四分人數  # 252

# Add all positions to get the divisor
法 = 頭位 + 中位 + 下位  # 630

# Multiply total money by each position
頭位實 = 錢 * 頭位  # 1122600
中位實 = 錢 * 中位  # 1496880
下位實 = 錢 * 下位  # 1746360

# Divide each result by the divisor to get the total money for each group
頭位總錢 = Fraction(頭位實, 法)  # 1782
中位總錢 = Fraction(中位實, 法)  # 2376
下位總錢 = Fraction(下位實, 法)  # 2772

# Divide each group's total money by the number of people in that group
a = Fraction(頭位總錢, 二分人數)  # 22
b = Fraction(中位總錢, 三分人數)  # 33
c = Fraction(下位總錢, 四分人數)  # 44
"""
"""
