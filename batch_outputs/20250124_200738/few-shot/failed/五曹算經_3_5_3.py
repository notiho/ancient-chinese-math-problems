"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
術曰：列豆八百四十九斛，以七十乘之得五萬九千四百三十斛，以九十除之即得。
答曰： a斛 奇 b升 。
"""

#----- content starts here -----
"""
Suppose there are 849 hu of beans, and for every 9 dou of beans, 7 dou of hemp can be exchanged.
Question: how much hemp is obtained?

The procedure says: Place the 849 hu of beans, multiply it by 70 (since 7 dou of hemp corresponds to 70 dou of beans), obtaining 59430 dou.
Divide it by 90 (since 9 dou of beans corresponds to 90 dou of beans), and the result is the amount of hemp.

Answer: *a* hu and *b* sheng.
"""

# 豆八百四十九斛
豆 = 849

# 每斛10斗
豆斗 = 10 * 豆

# 每九斗易麻七斗
麻率 = Fraction(7, 9)

# 列豆八百四十九斛，以七十乘之
麻斗 = 麻率 * 豆斗

# 以九十除之即得
麻斛 = 麻斗 // 10  # Convert dou to hu
麻升 = 麻斗 % 10  # Remaining dou as sheng

a = 麻斛
b = 麻升#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660
Variable 'b' has wrong value. Expected: 3, Actual: 10/3"""
