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

# 置金一斤，二而八之為兩
兩 = Fraction(2 * 金, 8)

# 三而八之為銖
銖 = Fraction(3 * 金, 8)

# 人數
人數 = 50

# 以人數除之
每人銖 = Fraction(銖, 人數)

# Convert 銖 to smaller units: 銖 -> 絫 -> 黍
# 1 銖 = 24 絫
每人絫 = 每人銖 * 24

# 1 絫 = 6 黍
每人黍 = 每人絫 * 6

# Extract the integer and fractional parts for 銖, 絫, and 黍
a = 每人銖.numerator // 每人銖.denominator  # 銖
remaining_銖 = 每人銖 - a

b = (remaining_銖 * 24).numerator // (remaining_銖 * 24).denominator  # 絫
remaining_絫 = (remaining_銖 * 24) - b

c = (remaining_絫 * 6).numerator // (remaining_絫 * 6).denominator  # 黍

a, b, c 
"""
Variable 'a' has wrong value. Expected: 7, Actual: 0
Variable 'b' has wrong value. Expected: 6, Actual: 0
Variable 'c' has wrong value. Expected: 8, Actual: 1"""
