"""
今有城周四十八里，欲令禦賊，每三步置一兵。問：用兵㡬何？
術曰：列城周四十八里，以三百步乘之，得一萬四千四百步，以三步除之即得。
答曰： a(=4800)人 。
"""

#----- content starts here -----
"""
Suppose there is a city with a circumference of 48 li. It is desired to defend against invaders by placing one soldier every 3 bu.
Question: how many soldiers are needed?

The procedure says: Place the city's circumference of 48 li, and multiply it by 300 bu (since 1 li = 300 bu), obtaining 14400 bu.
Divide this by 3 bu to obtain the number of soldiers.

Answer: *a*(=4800) soldiers.
"""

# 城周四十八里
城周 = 48

# 一里三百步
一里步數 = 300

# 以三百步乘之，得一萬四千四百步
總步數 = 城周 * 一里步數

# 每三步置一兵
每兵步數 = 3

# 以三步除之即得
a = 總步數 // 每兵步數 # 4800#----- content ends here -----

"""
"""
