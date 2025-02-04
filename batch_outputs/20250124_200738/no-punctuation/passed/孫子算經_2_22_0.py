"""
今有錢六千九百三十欲令二百一十六人作九分分之八十一人人與二分七十二人人與三分六十三人人與四分問三種各得幾何
術曰先置八十一人于上七十二人次之六十三人在下頭位以二乘之得一百六十二次位以三乘之得二百一十六下位以四乘之得二百五十二副并三位得六百三十為法又置錢六千九百三十為三位頭位以一百六十二乘之得一百一十二萬二千六百六十又以二百一十六乘中位得一百四十九萬六千八百八十又以二百五十二乘下位得一百七十四萬六千三百六十各為實以法六百三十各除之頭位得一千七百八十二中位得二千三百七十六下位得二千七百七十二各以人數除之即得
答曰二分人得錢 a 三分人得錢 b 四分人得錢 c 
"""

#----- content starts here -----
"""
Suppose there are 6930 coins to be distributed among 216 people in three groups:
- 81 people should each receive 2 parts,
- 72 people should each receive 3 parts,
- 63 people should each receive 4 parts.

Question: how much does each person in the three groups receive?

The procedure says:
1. Place 81 people in the top position, 72 people in the middle position, and 63 people in the bottom position.
2. Multiply the top position by 2, obtaining 162.
3. Multiply the middle position by 3, obtaining 216.
4. Multiply the bottom position by 4, obtaining 252.
5. Add these three values together, obtaining 630 as the divisor (法).
6. Place the total amount of coins, 6930, as the dividend.
7. Multiply the top position (162) by the total coins, obtaining 112,660.
8. Multiply the middle position (216) by the total coins, obtaining 149,880.
9. Multiply the bottom position (252) by the total coins, obtaining 174,360.
10. Divide each of these results by the divisor (630), obtaining the total coins for each group:
    - Top position: 1782 coins,
    - Middle position: 2376 coins,
    - Bottom position: 2772 coins.
11. Divide these totals by the number of people in each group to find the coins per person:
    - Top position: 1782 ÷ 81,
    - Middle position: 2376 ÷ 72,
    - Bottom position: 2772 ÷ 63.

Answer: People receiving 2 parts get *a* coins each, people receiving 3 parts get *b* coins each, and people receiving 4 parts get *c* coins each.
"""

# Total coins
錢 = 6930

# Group sizes
頭位人數 = 81
中位人數 = 72
下位人數 = 63

# Multipliers for each group
頭位乘數 = 2
中位乘數 = 3
下位乘數 = 4

# Calculate the weighted values for each group
頭位值 = 頭位人數 * 頭位乘數
中位值 = 中位人數 * 中位乘數
下位值 = 下位人數 * 下位乘數

# Add these values to get the divisor (法)
法 = 頭位值 + 中位值 + 下位值

# Calculate the total coins for each group
頭位總錢 = Fraction(頭位值 * 錢, 法)
中位總錢 = Fraction(中位值 * 錢, 法)
下位總錢 = Fraction(下位值 * 錢, 法)

# Divide the total coins for each group by the number of people in that group
a = Fraction(頭位總錢, 頭位人數)  # Coins per person in the top group
b = Fraction(中位總錢, 中位人數)  # Coins per person in the middle group
c = Fraction(下位總錢, 下位人數)  # Coins per person in the bottom group#----- content ends here -----

"""
"""
