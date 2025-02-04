"""
今有獵圍周四百五十二里一百八十步布圍兵十步一人今欲縮令通身得地四尺問圍内縮㡬何
術曰置圍里步數一退以四因之為尺以步法除之即得縮數
答曰 a里
"""

"""
Suppose there is a hunting enclosure with a perimeter of 452 li and 180 bu. Soldiers are stationed around the enclosure, 1 person every 10 bu. 
Now it is desired to reduce the enclosure so that each soldier occupies 4 chi of land.
Question: by how much should the enclosure be reduced?

The procedure says: Place the perimeter in li and bu. Subtract 1 [li], and multiply it by 4 to convert it into chi. 
Divide it by the bu divisor, obtaining the reduction amount.

Answer: *a* li.
"""

# 圍周四百五十二里一百八十步
圍里 = 452
圍步 = 180

# 通身得地四尺
通身地 = 4

# 置圍里步數一退
圍里退 = 圍里 - 1

# 以四因之為尺
縮尺 = 圍里退 * 通身地

# 以步法除之
步法 = 180  # 1 li = 180 bu
縮數 = Fraction(縮尺, 步法)

# 答曰 a里
a = 縮數
"""
Variable 'a' has wrong value. Expected: 2263/75, Actual: 451/45"""
