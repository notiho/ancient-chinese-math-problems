"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
術曰：列三百二十斛，每上十之得三萬二千升，以五人乘之得一十六萬升，以二升除之即得。
答曰： a(=80000)人 。
"""

"""
Suppose there are 2 sheng of sauce to feed 5 people. There are 320 hu of sauce.
Question: how many people can it feed?

The procedure says: Place the 320 hu, and for each hu, multiply by 10 to get 32,000 sheng.
Multiply this by 5 people to get 160,000 sheng.
Divide this by 2 sheng, and the result is the number of people.

Answer: *a*(=80,000) people.
"""

# 醬二升飼五人
醬每人 = 2
每組人數 = 5

# 醬三百二十斛
醬斛 = 320

# 每上十之得三萬二千升
醬升 = 10 * 醬斛

# 以五人乘之得一十六萬升
總醬升 = 每組人數 * 醬升

# 以二升除之即得
a = 總醬升 // 醬每人 # 80000
"""
Variable 'a' has wrong value. Expected: 80000, Actual: 8000"""
