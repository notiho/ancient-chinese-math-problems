"""
今有貸與人絲五十七觔，限歲出息一十六觔。問：觔息幾何？
答曰： a兩 。
"""

#----- content starts here -----
"""
Suppose 57 jin of silk is lent to someone, with an annual interest of 16 jin.
Question: how much is the interest per jin?

Answer: *a* liang.
"""

# 貸與人絲五十七觔
貸絲 = 57

# 限歲出息一十六觔
歲息 = 16

# 1 jin = 16 liang, so convert the interest to liang
歲息_兩 = 歲息 * 16

# Calculate the interest per jin
a = Fraction(歲息_兩, 貸絲)  # Interest per jin in liang

a  # Output the result#----- content ends here -----

"""
"""
