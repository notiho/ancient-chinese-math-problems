"""
今有馬七千六百八十匹匹日給料五升問一日幾何
術曰置馬匹數以五因之得三萬八千四百升再退為石數
答曰一日 a石
"""

#----- content starts here -----
"""
Suppose there are 7680 horses, and each horse is given 5 sheng of feed per day.
Question: how much feed is needed in total for one day?

The procedure says: Place the number of horses and multiply it by 5, obtaining 38400 sheng.
Then convert it into shi by dividing.

Answer: one day requires *a* shi.
"""

# 馬七千六百八十匹
馬匹數 = 7680

# 匹日給料五升
日給料 = 5

# 置馬匹數，以五因之，得三萬八千四百升
總升數 = 馬匹數 * 日給料

# 再退為石數 (1石 = 10斗, 1斗 = 10升, so 1石 = 100升)
升每石 = 100
a = Fraction(總升數, 升每石)#----- content ends here -----

"""
"""
