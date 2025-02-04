"""
今有獵圍周四百五十二里一百八十步布圍兵十步一人今欲縮令通身得地四尺問圍内縮㡬何
術曰置圍里步數一退以四因之為尺以步法除之即得縮數
答曰 a里
"""

"""
Suppose there is a hunting enclosure with a perimeter of 452 li and 180 bu.
Soldiers are stationed around the enclosure, with one soldier every 10 bu.
Now, it is desired to reduce the enclosure such that each soldier occupies 4 chi of ground.
Question: by how much should the enclosure be reduced?

The procedure says: Place the total perimeter in li and bu.
Convert it into chi by multiplying by 4.
Divide by the bu divisor (10 bu per soldier), obtaining the reduction amount.

Answer: *a* li.
"""

# 圍周四百五十二里一百八十步
圍里 = 452
圍步 = 180

# 退以四因之為尺 (convert li and bu to chi)
# 1 li = 300 bu, 1 bu = 6 chi
圍尺 = (圍里 * 300 + 圍步) * 6

# 步法 (10 bu per soldier, converted to chi)
步法 = 10 * 6

# 以步法除之，即得縮數
縮尺 = Fraction(圍尺, 步法)

# Convert the reduction back to li (1 li = 300 bu, 1 bu = 6 chi)
縮里 = Fraction(縮尺, 300 * 6)

a = 縮里

"""
Variable 'a' has wrong value. Expected: 2263/75, Actual: 2263/300"""
