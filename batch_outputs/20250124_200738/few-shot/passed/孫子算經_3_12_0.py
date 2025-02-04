"""
今有貸與人絲五十七觔，限歲出息一十六觔。問：觔息幾何？
術曰：列限息絲一十六觔，以一十六兩乘之，得二百五十六兩，以貸絲五十七觔除之，不盡，約之，即得。
答曰： a兩 。
"""

#----- content starts here -----
"""
Suppose someone lends 57 jin of silk, with the condition that in one year, the interest is 16 jin.
Question: how many liang of interest per jin?

The procedure says: Arrange the yearly interest of 16 jin of silk.
Multiply it by 16 liang per jin, obtaining 256 liang.
Divide it by the lent silk of 57 jin.
If it does not divide evenly, simplify the fraction, and that is the result.

Answer: *a* liang.
"""

# 貸與人絲五十七觔
貸絲 = 57

# 限歲出息一十六觔
限息 = 16

# 列限息絲一十六觔，以一十六兩乘之，得二百五十六兩
總息 = 限息 * 16

# 以貸絲五十七觔除之，不盡，約之，即得
a = Fraction(總息, 貸絲)#----- content ends here -----

"""
"""
