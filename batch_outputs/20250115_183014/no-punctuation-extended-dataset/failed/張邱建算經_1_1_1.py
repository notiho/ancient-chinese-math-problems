"""
今有獵圍周四百五十二里一百八十步布圍兵十步一人今欲縮令通身得地四尺問圍内縮㡬何
術曰置圍里步數一退以四因之為尺以步法除之即得縮數
答曰 a里
"""

"""
Suppose there is a hunting enclosure with a circumference of 452 li and 180 bu. Soldiers are stationed around the enclosure, one soldier every 10 bu.
Now, it is desired to reduce the enclosure so that each soldier occupies 4 chi of ground.
Question: by how much should the circumference be reduced?

The procedure says: Place the circumference in li and bu. Convert it into chi by multiplying by 4.
Divide it by the bu divisor, obtaining the reduction amount.

Answer: the reduction is *a* li.
"""

# 圍周四百五十二里一百八十步
圍里 = 452
圍步 = 180

# 每步為 6 尺 (1 步 = 6 尺)
步為尺 = 6

# 每里為 300 步 (1 里 = 300 步)
里為步 = 300

# 置圍里步數，轉換為尺
圍尺 = (圍里 * 里為步 + 圍步) * 步為尺

# 退以四，因之為尺
縮尺 = 4

# 以步法除之 (每兵占 10 步，轉換為尺)
步法 = 10 * 步為尺
縮數 = Fraction(圍尺, 步法)

# 將縮數轉換回里 (1 里 = 300 步 = 1800 尺)
縮里 = Fraction(縮數, 里為步 * 步為尺)

a = 縮里
"""
Variable 'a' has wrong value. Expected: 2263/75, Actual: 2263/300"""
