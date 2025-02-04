"""
今有錢六千九百三十欲令二百一十六人作九分分之八十一人人與二分七十二人人與三分六十三人人與四分問三種各得幾何
術曰先置八十一人于上七十二人次之六十三人在下頭位以二乘之得一百六十二次位以三乘之得二百一十六下位以四乘之得二百五十二副并三位得六百三十為法又置錢六千九百三十為三位頭位以一百六十二乘之得一百一十二萬二千六百六十又以二百一十六乘中位得一百四十九萬六千八百八十又以二百五十二乘下位得一百七十四萬六千三百六十各為實以法六百三十各除之頭位得一千七百八十二中位得二千三百七十六下位得二千七百七十二各以人數除之即得
答曰二分人得錢 a 三分人得錢 b 四分人得錢 c 
"""

"""
Suppose there are 6930 qian to be distributed among 216 people in three groups:
- 81 people each receive 2 parts,
- 72 people each receive 3 parts,
- 63 people each receive 4 parts.

Question: How much does each person in the three groups receive?

The procedure says:
1. Place 81 people in the top position, 72 people in the middle position, and 63 people in the bottom position.
2. Multiply the top position by 2, obtaining 162.
3. Multiply the middle position by 3, obtaining 216.
4. Multiply the bottom position by 4, obtaining 252.
5. Add these three results together, obtaining 630 as the divisor.
6. Place the 6930 qian as the total.
7. Multiply the total by 162 for the top position, obtaining 112260.
8. Multiply the total by 216 for the middle position, obtaining 149880.
9. Multiply the total by 252 for the bottom position, obtaining 174630.
10. Divide each result by the divisor (630), obtaining the total qian for each group:
    - Top position: 1782 qian,
    - Middle position: 2376 qian,
    - Bottom position: 2772 qian.
11. Divide each group's total qian by the number of people in that group to find the qian per person.

Answer: Each person in the 2-part group gets *a* qian, each person in the 3-part group gets *b* qian, and each person in the 4-part group gets *c* qian.
"""

# Total qian
錢 = 6930

# People in each group
頭位人數 = 81
中位人數 = 72
下位人數 = 63

# Multipliers for each group
頭位乘數 = 2
中位乘數 = 3
下位乘數 = 4

# Calculate the weighted contributions
頭位 = 頭位人數 * 頭位乘數
中位 = 中位人數 * 中位乘數
下位 = 下位人數 * 下位乘數

# Calculate the divisor (法)
法 = 頭位 + 中位 + 下位

# Calculate the total qian for each group
頭位總錢 = Fraction(錢 * 頭位, 法)
中位總錢 = Fraction(錢 * 中位, 法)
下位總錢 = Fraction(錢 * 下位, 法)

# Calculate the qian per person in each group
a = Fraction(頭位總錢, 頭位人數)
b = Fraction(中位總錢, 中位人數)
c = Fraction(下位總錢, 下位人數)
"""
"""
