"""
今有婦人河上蕩桮津吏問曰桮何以多婦人曰家有客津吏曰客幾何婦人曰二人共飯三人共羹四人共肉凡用桮六十五不知客幾何
術曰置六十五桮以十二乘之得七百八十以十三除之即得
答曰 a人 
"""

#----- content starts here -----
"""
Suppose there is a woman by the river at Dangbei ferry. The ferry officer asks: "Why do you have so many cups?"
The woman replies: "There are guests at home."
The ferry officer asks: "How many guests?"
The woman replies: "Two people share one bowl of rice, three people share one bowl of soup, and four people share one bowl of meat. Altogether, 65 cups are used."
Question: How many guests are there?

The procedure says: Place 65 cups, multiply it by 12, obtaining 780. Divide it by 13, and the result is the number of guests.

Answer: *a* people.
"""

# 置六十五桮
桮數 = 65

# 以十二乘之
實 = 12 * 桮數

# 得七百八十，以十三除之
a = Fraction(實, 13)#----- content ends here -----

"""
"""
