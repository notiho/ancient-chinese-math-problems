"""
今有甲乙丙三人持錢甲語乙丙各將公等所持錢半以益我錢成九十乙復語甲丙各將公等所持錢半以益我錢成七十丙復語甲乙各將公等所持錢半以益我錢成五十六問三人元持錢各若干
術曰先置三人所語為位以三乘之各為積甲得二百七十乙得二百一十丙得八十四又置甲九十乙七十丙五十六各半之以甲乙減丙以甲丙減乙以乙丙減甲即各得元數
答曰甲 a 乙 b 丙 c 
"""

#----- content starts here -----
"""
Suppose there are three people, Jia, Yi, and Bing, each holding some amount of money.
Jia says to Yi and Bing: "Each of you give me half of the money you hold equally, and my total will become 90."
Yi then says to Jia and Bing: "Each of you give me half of the money you hold equally, and my total will become 70."
Finally, Bing says to Jia and Yi: "Each of you give me half of the money you hold equally, and my total will become 56."
Question: How much money did each person originally hold?

The procedure says:
First, place the amounts spoken by the three people as positions and multiply each by 3, obtaining the sums:
Jia gets 270, Yi gets 210, and Bing gets 84.
Then, place Jia's 90, Yi's 70, and Bing's 56, and halve each of them.
Subtract Bing from Jia and Yi to get Jia's amount.
Subtract Yi from Jia and Bing to get Yi's amount.
Subtract Jia from Yi and Bing to get Bing's amount.
This gives the original amounts held by each person.

Answer: Jia holds *a*, Yi holds *b*, and Bing holds *c*.
"""

# Jia, Yi, and Bing's final amounts after receiving half of the others' money
甲語 = 90
乙語 = 70
丙語 = 56

# Multiply each by 3 to calculate the total sums
甲積 = 3 * 甲語
乙積 = 3 * 乙語
丙積 = 3 * 丙語

# Halve the amounts spoken by Jia, Yi, and Bing
甲半 = Fraction(甲語, 2)
乙半 = Fraction(乙語, 2)
丙半 = Fraction(丙語, 2)

# Calculate the original amounts
a = 甲半 + 乙半 - 丙半  # Jia's original amount
b = 甲半 + 丙半 - 乙半  # Yi's original amount
c = 乙半 + 丙半 - 甲半  # Bing's original amount

# Results
a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 72, Actual: 52
Variable 'b' has wrong value. Expected: 32, Actual: 38
Variable 'c' has wrong value. Expected: 4, Actual: 18"""
