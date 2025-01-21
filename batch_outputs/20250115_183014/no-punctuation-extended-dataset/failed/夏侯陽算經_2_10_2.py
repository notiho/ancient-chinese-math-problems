"""
今有馬七千六百八十匹匹日給料五升問一日幾何
術曰置馬匹數以五因之得三萬八千四百升再退為石數
答曰 a日 b石
"""

"""
Suppose there are 7680 horses, and each horse is given 5 sheng of feed per day.
Question: how much feed is required in one day?

The procedure says: Place the number of horses, multiply it by 5, obtaining 38400 sheng.
Then convert it into shi by dividing by 10 (since 1 shi = 10 sheng).

Answer: *a* sheng and *b* shi.
"""

# 馬匹數
馬匹數 = 7680

# 每匹日給料五升
日給料 = 5

# 置馬匹數，以五因之，得三萬八千四百升
總升數 = 馬匹數 * 日給料

# 再退為石數 (1石 = 10升)
總石數 = 總升數 // 10
剩餘升數 = 總升數 % 10

a = 剩餘升數  # 升
b = 總石數  # 石
"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'b' has wrong value. Expected: 384, Actual: 3840"""
