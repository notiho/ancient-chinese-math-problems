"""
今有圍兵二萬三千四百人以布圍周各相去五步今圍内縮除一十九里一百五十步而止問兵相去㡬何
術曰置人數以五乗之又以十九里一百五十步減之餘以人數除之不盡平約之
答曰 a步
"""

"""
Suppose there are 23,400 soldiers forming a circular formation, with each soldier initially spaced 5 bu apart.
Now, the circle is reduced in size, shortening the circumference by 19 li and 150 bu.
Question: what is the new spacing between soldiers?

The procedure says: Place the number of soldiers, multiply it by 5, then subtract 19 li and 150 bu.
Take the remainder and divide it by the number of soldiers.
If it does not divide evenly, simplify it to the lowest terms.

Answer: *a* bu.
"""

# 置人數
人數 = 23400

# 以五乗之
初始周長 = 5 * 人數

# 以十九里一百五十步減之
縮減量 = (19 * 300) + 150  # 1 里 = 300 步
縮減後周長 = 初始周長 - 縮減量

# 餘以人數除之
a = Fraction(縮減後周長, 人數)  # 平約之 to lowest terms
"""
"""
