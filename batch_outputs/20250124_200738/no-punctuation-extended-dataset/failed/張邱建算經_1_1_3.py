"""
今有獵圍周四百五十二里一百八十步布圍兵十步一人今欲縮令通身得地四尺問圍内縮㡬何
術曰置圍里步數一退以四因之為尺以步法除之即得縮數
答曰 a里
"""

#----- content starts here -----
"""
Suppose there is a hunting enclosure with a perimeter of 452 li and 180 bu. Soldiers are stationed around the enclosure, with one soldier every 10 bu. 
Now, it is desired to shrink the enclosure so that each soldier occupies 4 chi of land.
Question: by how much should the enclosure be reduced?

The procedure says: Place the total perimeter in li and bu. Convert it to chi by multiplying by 4. 
Divide by the step divisor (10 bu per soldier), and the result is the amount of reduction.

Answer: *a* li.
"""

# 圍周四百五十二里一百八十步
圍里 = 452
圍步 = 180

# 每步為 6 尺 (1 步 = 6 尺)
步為尺 = 6

# 每里為 300 步 (1 里 = 300 步)
里為步 = 300

# 每兵占地 4 尺
占地尺 = 4

# 置圍里步數，轉換為尺
圍尺 = (圍里 * 里為步 + 圍步) * 步為尺

# 以四因之，得縮減總尺數
縮減尺數 = 圍尺 - (圍尺 // (10 * 步為尺)) * 占地尺

# 將縮減尺數轉換回里
縮減里 = Fraction(縮減尺數, 里為步 * 步為尺)

a = 縮減里#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2263/75, Actual: 31682/75"""
