"""
今有丁八千九百五十八人，凡三丁出一兵。問：出兵㡬何？
術曰：列八千九百五十八人，以三除之即得。
答曰： a(=2986)人 。
"""

"""
Suppose there are 8958 adult males (丁). For every 3 males, 1 soldier is recruited.
Question: how many soldiers are recruited?

The procedure says: Place the 8958 males, divide it by 3, and the result is obtained.

Answer: *a*(=2986) soldiers.
"""

# 丁八千九百五十八人
丁 = 8958

# 凡三丁出一兵
每兵所需丁 = 3

# 以三除之即得
a = 丁 // 每兵所需丁 # 2986
"""
"""
