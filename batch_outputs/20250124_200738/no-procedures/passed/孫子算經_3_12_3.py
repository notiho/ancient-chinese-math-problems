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
本金 = 57  # jin

# 歲出息一十六觔
年息 = 16  # jin

# 1 jin = 16 liang, so convert the annual interest to liang
年息_兩 = 年息 * 16

# Divide the annual interest in liang by the principal in jin to get the interest per jin
a = Fraction(年息_兩, 本金)

# Output the result
a#----- content ends here -----

"""
"""
