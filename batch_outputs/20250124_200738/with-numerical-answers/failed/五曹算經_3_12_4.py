"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
術曰：列三百二十斛，每上十之得三萬二千升，以五人乘之得一十六萬升，以二升除之即得。
答曰： a(=80000)人 。
"""

#----- content starts here -----
"""
Suppose there are 2 sheng of sauce to feed 5 people. There are 320 hu of sauce.
Question: how many people can it feed?

The procedure says: Place the 320 hu, and for each hu, multiply it by 10 to obtain 32000 sheng.
Multiply this by 5 people to obtain 160000 sheng.
Divide this by 2 sheng, and the result is the number of people.

Answer: *a*(=80000) people.
"""

# 醬二升
醬每人 = 2

# 飼五人
每五人醬 = 5 * 醬每人

# 醬三百二十斛
醬總量斛 = 320

# 每上十之得三萬二千升
醬總量升 = 10 * 醬總量斛

# 以五人乘之得一十六萬升
總需求升 = 5 * 醬總量升

# 以二升除之即得
a = 總需求升 // 醬每人  # 80000#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 80000, Actual: 8000"""
