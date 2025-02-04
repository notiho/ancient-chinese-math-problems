"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
術曰：先置三人所語為位，以三乘之，各為積，甲得二百七十，乙得二百一十，丙得八十四，又置甲九十，乙七十，丙五十六，各半之，以甲乙減丙，以甲丙減乙，以乙丙減甲，即各得元數。
答曰：甲 a ，乙 b ，丙 c 。
"""

#----- content starts here -----
"""
Suppose there are three people, Jia, Yi, and Bing, each holding some amount of money.
Jia says to Yi and Bing: "Each of you give me half of the money you hold, and my total will become 90."
Yi says to Jia and Bing: "Each of you give me half of the money you hold, and my total will become 70."
Bing says to Jia and Yi: "Each of you give me half of the money you hold, and my total will become 56."
Question: How much money did each person originally hold?

The procedure says: First, place the amounts spoken by the three people as positions, and multiply each by 3, obtaining the totals: Jia gets 270, Yi gets 210, and Bing gets 84.
Then, place Jia's 90, Yi's 70, and Bing's 56, and take half of each.
Subtract Bing's from Jia's and Yi's, subtract Yi's from Jia's and Bing's, and subtract Jia's from Yi's and Bing's, obtaining the original amounts for each.

Answer: Jia has *a*, Yi has *b*, and Bing has *c*.
"""

from fractions import Fraction

# Jia, Yi, and Bing's final amounts after receiving half from the others
甲最終 = 90
乙最終 = 70
丙最終 = 56

# Multiply each final amount by 3 to calculate the total sums
甲積 = 3 * 甲最終  # 270
乙積 = 3 * 乙最終  # 210
丙積 = 3 * 丙最終  # 84

# Take half of each final amount
甲半 = Fraction(甲最終, 2)  # 45
乙半 = Fraction(乙最終, 2)  # 35
丙半 = Fraction(丙最終, 2)  # 28

# Subtract to calculate the original amounts
a = 甲積 - 乙半 - 丙半  # Jia's original amount
b = 乙積 - 甲半 - 丙半  # Yi's original amount
c = 丙積 - 甲半 - 乙半  # Bing's original amount

a, b, c  # Jia, Yi, and Bing's original amounts#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 72, Actual: 207
Variable 'b' has wrong value. Expected: 32, Actual: 137
Variable 'c' has wrong value. Expected: 4, Actual: 88"""
