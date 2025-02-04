"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
術曰：列三百二十斛，每上十之得三萬二千升，以五人乘之得一十六萬升，以二升除之即得。
答曰： a人 。
"""

"""
Suppose there are 2 sheng of sauce to feed 5 people. There are 320 hu of sauce.
Question: how many people can it feed?

The procedure says: Write down 320 hu. For each hu, multiply it by 10, obtaining 32,000 sheng. 
Multiply this by 5 people, obtaining 160,000 sheng. 
Divide this by 2 sheng, and the result is the number of people.

Answer: *a* people.
"""

# 醬二升
每人醬 = 2

# 飼五人
每五人醬 = 5 * 每人醬

# 醬三百二十斛
醬斛 = 320

# 每斛十升
每斛升 = 10

# 列三百二十斛，每上十之得三萬二千升
總升 = 醬斛 * 每斛升

# 以五人乘之得一十六萬升
總需求 = 總升 * 5

# 以二升除之即得
a = Fraction(總需求, 每人醬)
"""
Variable 'a' has wrong value. Expected: 80000, Actual: 8000"""
