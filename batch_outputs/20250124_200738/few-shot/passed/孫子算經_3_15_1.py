"""
今有婦人河上蕩桮，津吏問曰：「桮何以多？」婦人曰：「家有客。」津吏曰：「客幾何？」婦人曰：「二人共飯，三人共羹，四人共肉，凡用桮六十五，不知客幾何？」
術曰：置六十五桮，以十二乘之，得七百八十；以十三除之，即得。
答曰：「 a人 。」
"""

#----- content starts here -----
"""
A woman is washing cups by the river. The ferry officer asks: "Why are there so many cups?" 
The woman replies: "There are guests at home." 
The ferry officer asks: "How many guests?" 
The woman replies: "Two people share one bowl of rice, three people share one bowl of soup, and four people share one plate of meat. 
Altogether, 65 cups are used. How many guests are there?"

The procedure says: Place the 65 cups, multiply it by 12, obtaining 780. 
Divide it by 13, and the result is the number of guests.

Answer: *a* people.
"""

# 置六十五桮
桮 = 65

# 以十二乘之，得七百八十
實 = 12 * 桮

# 以十三除之，即得
a = Fraction(實, 13)#----- content ends here -----

"""
"""
