"""
今有方窖從一丈三尺廣六尺深一丈問受粟㡬何
術曰列從一丈三尺以廣六尺乘之得七十八尺以深一丈乘之得七百八十尺以斛法除之即得
答曰 a斛 奇 b寸 
"""

#----- content starts here -----
"""
Suppose there is a rectangular pit with a length of 1 zhang and 3 chi, a width of 6 chi, and a depth of 1 zhang.
Question: how much millet can it hold?

The procedure says: Place the length of 1 zhang and 3 chi.
Multiply it by the width of 6 chi, obtaining 78 chi².
Multiply it by the depth of 1 zhang, obtaining 780 chi³.
Divide it by the hu-divisor, obtaining the result.

Answer: *a* hu and *b* cun.
"""

from fractions import Fraction

# 長一丈三尺
長 = 1 * 10 + 3  # Convert zhang to chi (1 zhang = 10 chi)

# 廣六尺
廣 = 6

# 深一丈
深 = 1 * 10  # Convert zhang to chi

# 列從一丈三尺，以廣六尺乘之，得七十八尺
面積 = 長 * 廣

# 以深一丈乘之，得七百八十尺
體積 = 面積 * 深

# 斛法 (1斛 = 10立方尺)
斛法 = 10

# 以斛法除之，即得
總斛 = Fraction(體積, 斛法)

# 取整數部分為斛數
a = 總斛.numerator // 總斛.denominator

# 餘數部分轉換為寸 (1斛 = 10寸)
剩餘 = 總斛 - a
b = 剩餘 * 10

a = int(a)
b = int(b)

# Answer: a斛 奇 b寸#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 78
Variable 'b' has wrong value. Expected: 39/5, Actual: 0"""
