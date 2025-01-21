"""
今有金一斤令五十人分之問人得幾何
術曰置金一斤二而八之為兩三而八之為銖以人數除之即得
答曰人得 a銖 b 絫 c黍
"""

"""
Suppose there is 1 jin of gold, and it is to be divided among 50 people.
Question: how much does each person get?

The procedure says: Take 1 jin of gold. Multiply it by 2 and divide by 8 to convert it into liang. 
Then multiply it by 3 and divide by 8 to convert it into zhu. 
Divide by the number of people, and the result is obtained.

Answer: Each person gets *a* zhu, *b* lü, and *c* shu.
"""

# 金一斤
金 = 1

# 置金一斤，二而八之為兩
兩 = (金 * 2) / 8

# 三而八之為銖
銖 = (兩 * 3) / 8

# 人數
人數 = 50

# 以人數除之，即得每人所得銖
每人銖 = Fraction(銖, 人數)

# 將銖轉換為整數部分和餘數
a = 每人銖.numerator // 每人銖.denominator  # 整數部分為銖
剩餘銖 = 每人銖 - a

# 餘數部分轉換為絫 (1 絫 = 10 黍)
b = (剩餘銖 * 10).numerator // (剩餘銖 * 10).denominator  # 絫
剩餘絫 = (剩餘銖 * 10) - b

# 餘數部分轉換為黍
c = (剩餘絫 * 10).numerator // (剩餘絫 * 10).denominator  # 黍
"""
Code error: both arguments should be Rational instances"""
