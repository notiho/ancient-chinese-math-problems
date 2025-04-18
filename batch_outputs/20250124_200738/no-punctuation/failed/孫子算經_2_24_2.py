"""
今有甲乙丙三人持錢甲語乙丙各將公等所持錢半以益我錢成九十乙復語甲丙各將公等所持錢半以益我錢成七十丙復語甲乙各將公等所持錢半以益我錢成五十六問三人元持錢各若干
術曰先置三人所語為位以三乘之各為積甲得二百七十乙得二百一十丙得八十四又置甲九十乙七十丙五十六各半之以甲乙減丙以甲丙減乙以乙丙減甲即各得元數
答曰甲 a 乙 b 丙 c 
"""

#----- content starts here -----
"""
Suppose there are three people, A (Jia), B (Yi), and C (Bing), each holding some amount of money.
A says to B and C: "Each of you give me half of the money you hold equally, and I will have 90."
B then says to A and C: "Each of you give me half of the money you hold equally, and I will have 70."
C then says to A and B: "Each of you give me half of the money you hold equally, and I will have 56."
Question: How much money did each person originally hold?

The procedure says: First, place the amounts spoken by the three people as positions, and multiply each by 3, obtaining their respective sums:
A gets 270, B gets 210, and C gets 84.
Then, place A's 90, B's 70, and C's 56, and halve each.
Subtract C from A and B, subtract B from A and C, and subtract A from B and C, obtaining the original amounts for each.

Answer: A has *a*, B has *b*, and C has *c*.
"""

# 先置三人所語為位
甲語 = 90
乙語 = 70
丙語 = 56

# 以三乘之，各為積
甲積 = 3 * 甲語
乙積 = 3 * 乙語
丙積 = 3 * 丙語

# 甲得二百七十，乙得二百一十，丙得八十四
甲積 = 270
乙積 = 210
丙積 = 84

# 又置甲九十，乙七十，丙五十六，各半之
甲半 = Fraction(甲語, 2)
乙半 = Fraction(乙語, 2)
丙半 = Fraction(丙語, 2)

# 以甲乙減丙
甲乙減丙 = 甲半 + 乙半 - 丙半

# 以甲丙減乙
甲丙減乙 = 甲半 + 丙半 - 乙半

# 以乙丙減甲
乙丙減甲 = 乙半 + 丙半 - 甲半

# 即各得元數
a = 甲乙減丙
b = 甲丙減乙
c = 乙丙減甲#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 72, Actual: 52
Variable 'b' has wrong value. Expected: 32, Actual: 38
Variable 'c' has wrong value. Expected: 4, Actual: 18"""
