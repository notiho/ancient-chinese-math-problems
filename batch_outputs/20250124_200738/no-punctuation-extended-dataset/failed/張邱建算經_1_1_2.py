"""
今有獵圍周四百五十二里一百八十步布圍兵十步一人今欲縮令通身得地四尺問圍内縮㡬何
術曰置圍里步數一退以四因之為尺以步法除之即得縮數
答曰 a里
"""

#----- content starts here -----
"""
Suppose there is a hunting enclosure with a perimeter of 452 li and 180 bu. Soldiers are stationed every 10 bu along the perimeter.
Now, it is desired to reduce the enclosure such that each soldier occupies 4 chi of ground.
Question: by how much should the enclosure be reduced?

The procedure says: Place the perimeter in li and bu. Subtract 1 from it, and multiply it by 4 to convert to chi.
Divide it by the bu divisor, obtaining the amount of reduction.

Answer: *a* li.
"""

from fractions import Fraction

# 圍周四百五十二里一百八十步
圍里 = 452
圍步 = 180

# 通身得地四尺
得地尺 = 4

# 步法
步法 = 10

# 置圍里步數一退，以四因之為尺
總尺 = (圍里 * 300 + 圍步) * 得地尺

# 以步法除之，即得縮數
縮數步 = Fraction(總尺, 步法)

# 將縮數轉換為里
a = Fraction(縮數步, 300)  # 1 里 = 300 步#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2263/75, Actual: 4526/25"""
