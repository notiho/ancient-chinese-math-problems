"""
今有貸與人絲五十七觔，限歲出息一十六觔。問：觔息幾何？
術曰：列限息絲一十六觔，以一十六兩乘之，得二百五十六兩，以貸絲五十七觔除之，不盡，約之，即得。
答曰： a兩 。
"""

#----- content starts here -----
"""
Suppose 57 jin of silk is lent to a person, with an annual interest of 16 jin.
Question: how many liang of interest per jin?

The procedure says: Place the annual interest of 16 jin, and multiply it by 16 liang (since 1 jin = 16 liang), obtaining 256 liang.
Divide this by the lent silk of 57 jin. If it does not divide evenly, reduce it to its simplest fraction.

Answer: *a* liang.
"""

from fractions import Fraction

# 貸與人絲五十七觔
貸絲 = 57

# 限歲出息一十六觔
限息 = 16

# 以一十六兩乘之，得二百五十六兩
總息兩 = 限息 * 16

# 以貸絲五十七觔除之
a = Fraction(總息兩, 貸絲)

# 答案
a#----- content ends here -----

"""
"""
