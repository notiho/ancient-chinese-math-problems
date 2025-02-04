"""
今有丁八千九百五十八人，凡三丁出一兵。問：出兵㡬何？
術曰：列八千九百五十八人，以三除之即得。
答曰： a人 。
"""

#----- content starts here -----
"""
Suppose there are 8,958 adult males (丁). For every 3 males, 1 soldier is conscripted.
Question: how many soldiers are conscripted?

The procedure says: Place 8,958 males, divide by 3, and the result is obtained.

Answer: *a* soldiers.
"""

# 丁八千九百五十八人
丁 = 8958

# 凡三丁出一兵
兵率 = 3

# 以三除之即得
a = 丁 // 兵率  # Use integer division since the number of soldiers must be whole

a#----- content ends here -----

"""
"""
