"""
今有圍兵二萬三千四百人以布圍周各相去五步今圍内縮除一十九里一百五十步而止問兵相去㡬何
術曰置人數以五乗之又以十九里一百五十步減之餘以人數除之不盡平約之
答曰 a步
"""

"""
Suppose there are 23,400 soldiers arranged in a circular formation, with each soldier initially spaced 5 bu apart. 
Now, the circle is reduced inward by 19 li and 150 bu. 
Question: what is the new spacing between the soldiers?

The procedure says: Place the number of soldiers and multiply it by 5. 
Then subtract 19 li and 150 bu from the result. 
Take the remainder and divide it by the number of soldiers. 
If there is a remainder, simplify it.

Answer: *a* bu.
"""

# 置人數
人數 = 23400

# 各相去五步
初始間距 = 5

# 以五乗之
初始周長 = 人數 * 初始間距

# 以十九里一百五十步減之
# 1 里 = 300 步
縮減量 = 19 * 300 + 150
縮減後周長 = 初始周長 - 縮減量

# 餘以人數除之
新間距 = Fraction(縮減後周長, 人數)

# 答曰
a = 新間距
"""
"""
