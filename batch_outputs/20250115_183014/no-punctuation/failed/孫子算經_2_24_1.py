"""
今有甲乙丙三人持錢甲語乙丙各將公等所持錢半以益我錢成九十乙復語甲丙各將公等所持錢半以益我錢成七十丙復語甲乙各將公等所持錢半以益我錢成五十六問三人元持錢各若干
術曰先置三人所語為位以三乘之各為積甲得二百七十乙得二百一十丙得八十四又置甲九十乙七十丙五十六各半之以甲乙減丙以甲丙減乙以乙丙減甲即各得元數
答曰甲 a 乙 b 丙 c 
"""

"""
Suppose there are three people, Jia, Yi, and Bing, each holding some amount of money.
Jia says to Yi and Bing: "Each of you take half of what you are holding and give it to me, and I will have 90."
Yi then says to Jia and Bing: "Each of you take half of what you are holding and give it to me, and I will have 70."
Bing then says to Jia and Yi: "Each of you take half of what you are holding and give it to me, and I will have 56."
Question: How much money did each of the three originally hold?

The procedure says: First, place the amounts spoken by the three as positions and multiply each by 3, obtaining the totals:
Jia gets 270, Yi gets 210, and Bing gets 84.
Then, place Jia's 90, Yi's 70, and Bing's 56, and halve each of them.
Subtract Bing from Jia and Yi to get Jia's amount.
Subtract Yi from Jia and Bing to get Yi's amount.
Subtract Jia from Yi and Bing to get Bing's amount.
This gives the original amounts.

Answer: Jia has *a*, Yi has *b*, and Bing has *c*.
"""

# Jia, Yi, and Bing's final amounts after receiving contributions
甲最終 = 90
乙最終 = 70
丙最終 = 56

# Multiply each by 3 to calculate the totals
甲積 = 3 * 甲最終
乙積 = 3 * 乙最終
丙積 = 3 * 丙最終

# Halve each of Jia, Yi, and Bing's final amounts
甲半 = Fraction(甲最終, 2)
乙半 = Fraction(乙最終, 2)
丙半 = Fraction(丙最終, 2)

# Calculate the original amounts
a = 甲半 + 乙半 - 丙半  # Jia's original amount
b = 甲半 + 丙半 - 乙半  # Yi's original amount
c = 乙半 + 丙半 - 甲半  # Bing's original amount

# Results
a, b, c
"""
Variable 'a' has wrong value. Expected: 72, Actual: 52
Variable 'b' has wrong value. Expected: 32, Actual: 38
Variable 'c' has wrong value. Expected: 4, Actual: 18"""
