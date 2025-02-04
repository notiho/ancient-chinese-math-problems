"""
今有貸與人絲五十七觔，限歲出息一十六觔。問：觔息幾何？
術曰：列限息絲一十六觔，以一十六兩乘之，得二百五十六兩，以貸絲五十七觔除之，不盡，約之，即得。
答曰： a兩 。
"""

"""
Suppose someone lends 57 jin of silk, with an agreement to receive 16 jin of interest in one year.
Question: how many liang of interest per jin?

The procedure says: Arrange the agreed interest of 16 jin.
Multiply it by 16 liang, obtaining 256 liang.
Divide it by the lent silk of 57 jin.
If it does not divide evenly, reduce it to its simplest form, and the result is obtained.

Answer: *a* liang.
"""

# 貸絲五十七觔
貸絲 = 57

# 限歲出息一十六觔
限息 = 16

# 以一十六兩乘之，得二百五十六兩
總息兩 = 16 * 限息

# 以貸絲五十七觔除之，不盡，約之，即得
a = Fraction(總息兩, 貸絲)
"""
"""
