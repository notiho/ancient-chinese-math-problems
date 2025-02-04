"""
今有甲乙丙三人持錢，甲語乙丙：各將公等所持錢半以益我錢成九十。乙復語甲丙：各將公等所持錢，半以益我，錢成七十。丙復語甲乙：各將公等所持錢，半以益我，錢成五十六。問：三人元持錢各若干？
術曰：先置三人所語為位，以三乘之，各為積，甲得二百七十，乙得二百一十，丙得八十四，又置甲九十，乙七十，丙五十六，各半之，以甲乙減丙，以甲丙減乙，以乙丙減甲，即各得元數。
答曰：甲 a ，乙 b ，丙 c 。
"""

#----- content starts here -----
"""
Suppose there are three people, Jia, Yi, and Bing, each holding some amount of money.
Jia says to Yi and Bing: "Each of you give me half of what you have, and my money will become 90."
Yi then says to Jia and Bing: "Each of you give me half of what you have, and my money will become 70."
Bing then says to Jia and Yi: "Each of you give me half of what you have, and my money will become 56."
Question: How much money did each person originally hold?

The procedure says: First, place the statements of the three people as positions, and multiply each by 3, obtaining their respective totals:
Jia gets 270, Yi gets 210, and Bing gets 84.
Then, place Jia's 90, Yi's 70, and Bing's 56, and take half of each.
Subtract Bing's half from Jia's and Yi's halves, subtract Yi's half from Jia's and Bing's halves, and subtract Jia's half from Yi's and Bing's halves.
This gives the original amounts for each person.

Answer: Jia has *a*, Yi has *b*, Bing has *c*.
"""

# Jia's statement: "Each of you give me half of what you have, and my money will become 90."
甲語 = 90

# Yi's statement: "Each of you give me half of what you have, and my money will become 70."
乙語 = 70

# Bing's statement: "Each of you give me half of what you have, and my money will become 56."
丙語 = 56

# Multiply each statement by 3 to get their respective totals
甲積 = 3 * 甲語
乙積 = 3 * 乙語
丙積 = 3 * 丙語

# Take half of each statement
甲半 = Fraction(甲語, 2)
乙半 = Fraction(乙語, 2)
丙半 = Fraction(丙語, 2)

# Subtract Bing's half from Jia's and Yi's halves
甲乙減丙 = 甲半 + 乙半 - 丙半

# Subtract Yi's half from Jia's and Bing's halves
甲丙減乙 = 甲半 + 丙半 - 乙半

# Subtract Jia's half from Yi's and Bing's halves
乙丙減甲 = 乙半 + 丙半 - 甲半

# The original amounts for each person
a = 甲乙減丙
b = 甲丙減乙
c = 乙丙減甲#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 72, Actual: 52
Variable 'b' has wrong value. Expected: 32, Actual: 38
Variable 'c' has wrong value. Expected: 4, Actual: 18"""
