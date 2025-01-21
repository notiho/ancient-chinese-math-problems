"""
今有貸與人絲五十七觔限歲出息一十六觔問觔息幾何
術曰列限息絲一十六觔以一十六兩乘之得二百五十六兩以貸絲五十七觔除之不盡約之即得
答曰 a兩 
"""

"""
Suppose someone lends 57 jin of silk to another person, with an annual interest of 16 jin.
Question: how many liang of interest is earned per jin of silk?

The procedure says: List the annual interest of 16 jin of silk.
Multiply it by 16 liang (since 1 jin = 16 liang), obtaining 256 liang.
Divide this by the lent silk of 57 jin.
If it does not divide evenly, reduce the fraction to its simplest form.

Answer: *a* liang.
"""

# 貸絲五十七觔
貸絲 = 57

# 限歲出息一十六觔
年息 = 16

# 以一十六兩乘之，得二百五十六兩
總息兩 = 16 * 年息

# 以貸絲五十七觔除之，不盡約之，即得
a = Fraction(總息兩, 貸絲)
"""
"""
