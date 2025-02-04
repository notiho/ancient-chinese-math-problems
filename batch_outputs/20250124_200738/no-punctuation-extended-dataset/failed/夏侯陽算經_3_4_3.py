"""
今有金一斤令五十人分之問人得幾何
術曰置金一斤二而八之為兩三而八之為銖以人數除之即得
答曰人得 a銖
"""

#----- content starts here -----
"""
Suppose there is 1 jin of gold, and it is to be divided among 50 people.
Question: how much does each person get?

The procedure says: Place 1 jin of gold. Multiply it by 2 and divide by 8 to convert it to liang. 
Then multiply it by 3 and divide by 8 to convert it to zhu.
Divide by the number of people, and the result is obtained.

Answer: each person gets *a* zhu.
"""

# 金一斤
金 = 1

# 二而八之為兩 (convert jin to liang)
兩 = Fraction(2 * 金, 8)

# 三而八之為銖 (convert liang to zhu)
銖 = Fraction(3 * 兩, 8)

# 人數
人數 = 50

# 以人數除之，即得
a = Fraction(銖, 人數)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 192/25, Actual: 3/1600"""
