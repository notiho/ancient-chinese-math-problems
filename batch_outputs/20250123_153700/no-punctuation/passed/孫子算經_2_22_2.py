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

Question: how much does each person in the three groups receive?

The procedure says:
1. Place 81 people in the top position, 72 people in the middle position, and 63 people in the bottom position.
2. Multiply the top position by 2, obtaining 162.
3. Multiply the middle position by 3, obtaining 216.
4. Multiply the bottom position by 4, obtaining 252.
5. Add these three results together, obtaining 630 as the divisor.
6. Place the 6930 qian as the total amount.
7. Multiply the top position (162) by the total amount, obtaining 1122660.
8. Multiply the middle position (216) by the total amount, obtaining 1496880.
9. Multiply the bottom position (252) by the total amount, obtaining 1746360.
10. Divide each of these results by the divisor (630), obtaining the total amount for each group:
    - Top position: 1782,
    - Middle position: 2376,
    - Bottom position: 2772.
11. Divide each group's total amount by the number of people in that group to get the amount per person.

Answer: People in the 2-part group receive *a* qian, people in the 3-part group receive *b* qian, and people in the 4-part group receive *c* qian.
"""

# Total qian and people
總錢 = 6930
總人數 = 216

# People in each group
頭位人數 = 81
中位人數 = 72
下位人數 = 63

# Multipliers for each group
頭位乘數 = 2
中位乘數 = 3
下位乘數 = 4

# Step 2-5: Calculate the divisor
頭位 = 頭位人數 * 頭位乘數
中位 = 中位人數 * 中位乘數
下位 = 下位人數 * 下位乘數
法 = 頭位 + 中位 + 下位

# Step 7-9: Calculate the total amount for each group
頭位實 = 頭位 * 總錢
中位實 = 中位 * 總錢
下位實 = 下位 * 總錢

# Step 10: Divide by the divisor to get the total amount for each group
頭位總錢 = Fraction(頭位實, 法)
中位總錢 = Fraction(中位實, 法)
下位總錢 = Fraction(下位實, 法)

# Step 11: Divide by the number of people in each group to get the amount per person
a = Fraction(頭位總錢, 頭位人數)
b = Fraction(中位總錢, 中位人數)
c = Fraction(下位總錢, 下位人數)
"""
"""
