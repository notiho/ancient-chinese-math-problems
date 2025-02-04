"""
今有馬七千六百八十匹匹日給料五升問一日幾何
術曰置馬匹數以五因之得三萬八千四百升再退為石數
答曰一日 a石
"""

"""
Suppose there are 7680 horses, and each horse is given 5 sheng of feed per day.
Question: how much feed is required in one day?

The procedure says: Place the number of horses, and multiply it by 5, obtaining the total in sheng.
Then convert it into shi by dividing by 10 (since 10 sheng = 1 dou, and 10 dou = 1 shi).

Answer: In one day, *a* shi.
"""

# 馬匹數
馬匹數 = 7680

# 每匹日給料五升
日給料 = 5

# 置馬匹數以五因之，得總升數
總升數 = 馬匹數 * 日給料

# 再退為石數 (10升 = 1斗, 10斗 = 1石, so 1石 = 100升)
a = Fraction(總升數, 100)  # Convert sheng to shi
"""
"""
