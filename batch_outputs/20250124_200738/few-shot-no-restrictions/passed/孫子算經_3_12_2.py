"""
今有貸與人絲五十七觔，限歲出息一十六觔。問：觔息幾何？
術曰：列限息絲一十六觔，以一十六兩乘之，得二百五十六兩，以貸絲五十七觔除之，不盡，約之，即得。
答曰： a兩 。
"""

#----- content starts here -----
"""
Suppose there is a loan of 57 jin of silk given to someone, with an annual interest of 16 jin.
Question: what is the interest rate in liang per jin?

The procedure says: Take the annual interest of 16 jin of silk, multiply it by 16 liang per jin, obtaining 256 liang.
Divide this by the loan of 57 jin of silk. If it does not divide evenly, reduce it to its simplest form.

Answer: *a* liang.
"""

from fractions import Fraction

# 貸與人絲五十七觔
貸絲 = 57  # jin

# 限歲出息一十六觔
限息 = 16  # jin

# 以一十六兩乘之
總息兩 = 限息 * 16  # liang

# 以貸絲五十七觔除之
a = Fraction(總息兩, 貸絲)

# 答案
a#----- content ends here -----

"""
"""
