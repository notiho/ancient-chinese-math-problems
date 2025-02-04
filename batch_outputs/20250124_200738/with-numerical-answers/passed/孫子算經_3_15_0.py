"""
今有婦人河上蕩桮，津吏問曰：「桮何以多？」婦人曰：「家有客。」津吏曰：「客幾何？」婦人曰：「二人共飯，三人共羹，四人共肉，凡用桮六十五，不知客幾何？」
術曰：置六十五桮，以十二乘之，得七百八十；以十三除之，即得。
答曰：「 a(=60)人 。」
"""

#----- content starts here -----
"""
A woman is washing cups by the river. The ferryman asks, "Why are there so many cups?"
The woman replies, "There are guests at home."
The ferryman asks, "How many guests?"
The woman replies, "Two people share one rice cup, three people share one soup cup, and four people share one meat cup. Altogether, 65 cups were used. How many guests are there?"

The procedure says: Place the 65 cups, multiply it by 12, obtaining 780. Divide it by 13, and the result is the number of guests.

Answer: *a*(=60) people.
"""

# 置六十五桮
桮數 = 65

# 以十二乘之，得七百八十
實 = 12 * 桮數

# 以十三除之，即得
a = Fraction(實, 13) # 60#----- content ends here -----

"""
"""
