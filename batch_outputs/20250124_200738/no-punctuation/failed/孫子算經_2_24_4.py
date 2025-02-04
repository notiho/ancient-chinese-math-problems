"""
今有甲乙丙三人持錢甲語乙丙各將公等所持錢半以益我錢成九十乙復語甲丙各將公等所持錢半以益我錢成七十丙復語甲乙各將公等所持錢半以益我錢成五十六問三人元持錢各若干
術曰先置三人所語為位以三乘之各為積甲得二百七十乙得二百一十丙得八十四又置甲九十乙七十丙五十六各半之以甲乙減丙以甲丙減乙以乙丙減甲即各得元數
答曰甲 a 乙 b 丙 c 
"""

#----- content starts here -----
"""
Suppose there are three people, A (Jia), B (Yi), and C (Bing), each holding some amount of money.
A says to B and C: "Each of you take half of the money you hold equally and give it to me, so that my total becomes 90."
B says to A and C: "Each of you take half of the money you hold equally and give it to me, so that my total becomes 70."
C says to A and B: "Each of you take half of the money you hold equally and give it to me, so that my total becomes 56."
Question: How much money did each person originally hold?

The procedure says: First, place the amounts spoken by the three people as positions, and multiply each by 3, obtaining their respective totals:
A gets 270, B gets 210, and C gets 84.
Then, place A's 90, B's 70, and C's 56, and take half of each.
Subtract C from A and B, subtract B from A and C, and subtract A from B and C, obtaining the original amounts for each.

Answer: A originally held *a*, B originally held *b*, and C originally held *c*.
"""

from fractions import Fraction

# A, B, and C's final totals after receiving contributions
甲語 = 90
乙語 = 70
丙語 = 56

# Multiply each by 3 to calculate their respective totals
甲積 = 3 * 甲語
乙積 = 3 * 乙語
丙積 = 3 * 丙語

# Take half of each person's spoken amount
甲半 = Fraction(甲語, 2)
乙半 = Fraction(乙語, 2)
丙半 = Fraction(丙語, 2)

# Subtract to find the original amounts
a = 甲半 + 乙半 - 丙語  # A's original amount
b = 甲半 + 丙半 - 乙語  # B's original amount
c = 乙半 + 丙半 - 甲語  # C's original amount

# Results
a = float(a)
b = float(b)
c = float(c)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 72, Actual: 24.0
Variable 'b' has wrong value. Expected: 32, Actual: 3.0
Variable 'c' has wrong value. Expected: 4, Actual: -27.0"""
