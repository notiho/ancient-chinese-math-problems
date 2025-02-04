"""
今有醤二升給五兵見有三百二十斛問給幾何
術曰置醤數再上十之為升以五因之得一十六萬以二升為法除之即得
答曰給兵 a人
"""

#----- content starts here -----
"""
Suppose there are 2 sheng of sauce allocated to 5 soldiers. 
It is observed that there are 320 hu of sauce available.
Question: how many soldiers can be allocated?

The procedure says: Place the amount of sauce, multiply it by 10 to convert to sheng.
Multiply it by 5, obtaining 160,000.
Take 2 sheng as the divisor and divide it, obtaining the number of soldiers.

Answer: it can allocate *a* soldiers.
"""

# 醤二升
醤 = 2

# 給五兵
兵 = 5

# 見有三百二十斛
醤總量 = 320

# 置醤數再上十之為升
醤總量升 = 醤總量 * 10 * 10  # 1斛 = 10斗, 1斗 = 10升

# 以五因之
總兵醤 = 醤總量升 * 兵

# 得一十六萬 (確認計算)
assert 總兵醤 == 160000

# 以二升為法除之
a = Fraction(總兵醤, 醤)  # 給兵數

a#----- content ends here -----

"""
"""
