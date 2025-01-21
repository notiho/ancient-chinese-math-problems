"""
今有金一斤令五十人分之問人得幾何
術曰置金一斤二而八之為兩三而八之為銖以人數除之即得
答曰人得 a銖 b 絫 c黍
"""

"""
Suppose there is 1 jin of gold, and it is to be divided among 50 people.
Question: how much does each person get?

The procedure says: Place 1 jin of gold. Multiply it by 2 and divide by 8 to convert it into liang. 
Then multiply it by 3 and divide by 8 to convert it into zhu. 
Divide by the number of people, and the result is obtained.

Answer: each person gets *a* zhu, *b* lü, and *c* shu.
"""

# 金一斤
金 = 1

# 一斤二而八之為兩
兩 = Fraction(2 * 金, 8)

# 三而八之為銖
銖 = Fraction(3 * 金, 8)

# 人數
人數 = 50

# 以人數除之
每人銖 = Fraction(銖, 人數)

# 將銖轉換為整數部分和餘數
a = 每人銖.numerator // 每人銖.denominator  # 整數部分為銖
剩餘 = 每人銖 - a  # 餘數部分

# 餘數部分轉換為絫（1銖 = 24絫）
絫 = 剩餘 * 24
b = 絫.numerator // 絫.denominator  # 整數部分為絫
剩餘 = 絫 - b  # 餘數部分

# 餘數部分轉換為黍（1絫 = 6黍）
黍 = 剩餘 * 6
c = 黍.numerator // 黍.denominator  # 整數部分為黍

# 答案為 a銖 b絫 c黍
"""
Variable 'a' has wrong value. Expected: 7, Actual: 0
Variable 'b' has wrong value. Expected: 6, Actual: 0
Variable 'c' has wrong value. Expected: 8, Actual: 1"""
