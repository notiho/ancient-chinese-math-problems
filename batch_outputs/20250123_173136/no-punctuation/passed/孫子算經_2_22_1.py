"""
今有錢六千九百三十欲令二百一十六人作九分分之八十一人人與二分七十二人人與三分六十三人人與四分問三種各得幾何
術曰先置八十一人于上七十二人次之六十三人在下頭位以二乘之得一百六十二次位以三乘之得二百一十六下位以四乘之得二百五十二副并三位得六百三十為法又置錢六千九百三十為三位頭位以一百六十二乘之得一百一十二萬二千六百六十又以二百一十六乘中位得一百四十九萬六千八百八十又以二百五十二乘下位得一百七十四萬六千三百六十各為實以法六百三十各除之頭位得一千七百八十二中位得二千三百七十六下位得二千七百七十二各以人數除之即得
答曰二分人得錢 a 三分人得錢 b 四分人得錢 c 
"""

"""
Suppose there are 6930 coins to be distributed among 216 people in three groups:
- 81 people each receive 2 parts,
- 72 people each receive 3 parts,
- 63 people each receive 4 parts.

Question: how much does each person in the three groups receive?

The procedure says:
1. Place 81 people in the top position, 72 people in the middle position, and 63 people in the bottom position.
2. Multiply the top position by 2, obtaining 162.
   Multiply the middle position by 3, obtaining 216.
   Multiply the bottom position by 4, obtaining 252.
3. Add these three results together, obtaining 630 as the divisor (法).
4. Place the total amount of money, 6930, as the dividend.
5. Multiply the total money by 162 (top position), obtaining 112,660.
   Multiply the total money by 216 (middle position), obtaining 149,880.
   Multiply the total money by 252 (bottom position), obtaining 174,360.
6. Divide each result by the divisor (630):
   - Top position: 112,660 ÷ 630 = 1782.
   - Middle position: 149,880 ÷ 630 = 2376.
   - Bottom position: 174,360 ÷ 630 = 2772.
7. Divide each result by the number of people in the respective group:
   - Top position: 1782 ÷ 81 = a.
   - Middle position: 2376 ÷ 72 = b.
   - Bottom position: 2772 ÷ 63 = c.

Answer: Each person in the 2-part group receives *a* coins, each person in the 3-part group receives *b* coins, and each person in the 4-part group receives *c* coins.
"""

# Total coins
錢 = 6930

# Number of people in each group
頭位人數 = 81
中位人數 = 72
下位人數 = 63

# Parts for each group
頭位分 = 2
中位分 = 3
下位分 = 4

# Multiply people by their respective parts
頭位 = 頭位人數 * 頭位分
中位 = 中位人數 * 中位分
下位 = 下位人數 * 下位分

# Add all parts to get the divisor (法)
法 = 頭位 + 中位 + 下位

# Calculate the total money for each group
頭位實 = 錢 * 頭位
中位實 = 錢 * 中位
下位實 = 錢 * 下位

# Divide each group's total money by the divisor
頭位錢 = Fraction(頭位實, 法)
中位錢 = Fraction(中位實, 法)
下位錢 = Fraction(下位實, 法)

# Divide each group's money by the number of people in the group
a = Fraction(頭位錢, 頭位人數)
b = Fraction(中位錢, 中位人數)
c = Fraction(下位錢, 下位人數)
"""
"""
