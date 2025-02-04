"""
今有麥八斗六升、七分升之三，欲為小䵂，問︰得幾何？
術曰：以麥求小䵂，三之，十而一。
荅曰：為小䵂 a斗 。
"""

"""

"""

#----- content starts here -----

# 麥八斗六升、七分升之三
麥 = 8  # 斗
升 = 6 + Fraction(3, 7)  # 升

# Convert 麥 to 升 (1斗 = 10升)
麥_in_升 = 麥 * 10 + 升

# 以麥求小䵂，三之
小䵂 = 3 * 麥_in_升

# 十而一 (convert back to 斗, 1斗 = 10升)
a = Fraction(小䵂, 10)
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 363/140, Actual: 363/14"""
