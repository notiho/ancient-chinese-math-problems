"""
今有金一斤令五十人分之問人得幾何
術曰置金一斤二而八之為兩三而八之為銖以人數除之即得
答曰人得 a銖 b 絫 c黍
"""

"""
Suppose there is 1 jin of gold, and it is to be divided among 50 people.
Question: how much does each person get?

The procedure says: Take 1 jin of gold, multiply it by 2 and divide by 8 to convert it into liang.
Then multiply it by 3 and divide by 8 to convert it into zhu.
Divide by the number of people, and you will obtain the result.

Answer: each person gets *a* zhu, *b* lü, and *c* shu.
"""

# 金一斤
金 = 1

# 置金一斤，二而八之，為兩
兩 = Fraction(2 * 金, 8)

# 三而八之，為銖
銖 = Fraction(3 * 金, 8)

# 1 斤 = 16 兩
兩 = 16 * 金

# 1 兩 = 24 銖
銖 = 24 * 兩

# 1 銖 = 1000 黍
黍 = 1000 * 銖

# 以人數除之，即得
人數 = 50
每人得黍 = Fraction(黍, 人數)

# 將結果轉換為銖、絫、黍
a = 每人得黍 // 1000  # 銖
剩餘黍 = 每人得黍 % 1000

b = 剩餘黍 // 100  # 絫
c = 剩餘黍 % 100  # 黍
"""
Variable 'c' has wrong value. Expected: 8, Actual: 80"""
