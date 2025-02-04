"""
今有貸與人絲五十七觔，限歲出息一十六觔。問：觔息幾何？
術曰：列限息絲一十六觔，以一十六兩乘之，得二百五十六兩，以貸絲五十七觔除之，不盡，約之，即得。
答曰： a兩 。
"""

#----- content starts here -----
"""
Suppose 57 jin of silk is lent to a person, with an annual interest of 16 jin.
Question: what is the interest rate in liang per jin?

The procedure says: Take the annual interest of 16 jin of silk.
Multiply it by 16 liang (since 1 jin = 16 liang), obtaining 256 liang.
Divide this by the lent silk of 57 jin.
If there is a remainder, reduce it to its simplest form.

Answer: *a* liang.
"""

from fractions import Fraction

# 貸與人絲五十七觔
貸絲 = 57  # jin

# 限歲出息一十六觔
限息 = 16  # jin

# 以一十六兩乘之
限息兩 = 限息 * 16  # Convert jin to liang

# 得二百五十六兩
總息兩 = 限息兩  # Total interest in liang

# 以貸絲五十七觔除之
a = Fraction(總息兩, 貸絲)  # Interest rate in liang per jin

a  # Output the result#----- content ends here -----

"""
"""
