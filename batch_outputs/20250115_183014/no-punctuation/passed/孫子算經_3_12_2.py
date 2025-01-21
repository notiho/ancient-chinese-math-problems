"""
今有貸與人絲五十七觔限歲出息一十六觔問觔息幾何
術曰列限息絲一十六觔以一十六兩乘之得二百五十六兩以貸絲五十七觔除之不盡約之即得
答曰 a兩 
"""

"""
Suppose someone lends 57 jin of silk, with an annual interest of 16 jin.
Question: how much is the interest per jin?

The procedure says: List the annual interest of 16 jin of silk.
Multiply it by 16 liang, obtaining 256 liang.
Divide it by the lent silk of 57 jin.
If it does not divide evenly, reduce it to its simplest form, and the result is obtained.

Answer: *a* liang.
"""

# 貸絲五十七觔
貸絲 = 57

# 限歲出息一十六觔
歲息 = 16

# 以一十六兩乘之，得二百五十六兩
總息 = 歲息 * 16

# 以貸絲五十七觔除之
a = Fraction(總息, 貸絲)
"""
"""
