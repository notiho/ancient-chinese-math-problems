"""
今有貸與人絲五十七觔，限歲出息一十六觔。問：觔息幾何？
答曰： a兩 。
"""

#----- content starts here -----
"""
Suppose 57 jin of silk is loaned to someone, with an annual interest of 16 jin.
Question: how much is the interest per jin?

Answer: *a* liang.
"""

# 貸與人絲五十七觔
本金 = 57  # jin

# 歲出息一十六觔
年息 = 16  # jin

# 1 jin = 16 liang
# Calculate interest per jin in liang
a = Fraction(年息 * 16, 本金)  # Convert jin to liang and divide by total jin

a  # Output the interest per jin in liang#----- content ends here -----

"""
"""
