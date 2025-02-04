"""
今有醤二升給五兵見有三百二十斛問給幾何
術曰置醤數再上十之為升以五因之得一十六萬以二升為法除之即得
答曰給兵 a人
"""

#----- content starts here -----
"""
Suppose there are 2 sheng of sauce to be distributed to 5 soldiers. 
It is observed that there are 320 hu of sauce.
Question: how many soldiers can be supplied?

The procedure says: Place the amount of sauce, multiply it by 10 to convert it to sheng.
Multiply it by 5, obtaining 160,000.
Take 2 sheng as the divisor and divide it, obtaining the result.

Answer: it supplies *a* soldiers.
"""

# 醤二升
醤 = 2

# 給五兵
兵 = 5

# 見有三百二十斛
斛 = 320

# 置醤數再上十之為升
升 = 斛 * 10

# 以五因之
總量 = 升 * 兵

# 得一十六萬 (確認)
assert 總量 == 160000

# 以二升為法除之
a = Fraction(總量, 醤)#----- content ends here -----

"""
Code error: """
