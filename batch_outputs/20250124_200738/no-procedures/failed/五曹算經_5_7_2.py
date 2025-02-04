"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade (錦) worth 8 guan (貫) of money. 
Question: how much is one zhang (丈), one chi (尺), and one cun (寸) worth respectively?

Answer: one zhang is worth *a* guan, one chi is worth *b* wen, and one cun is worth *c* wen.
"""

from fractions import Fraction

# Total value of one bolt of brocade
total_value = 8  # in guan

# One bolt of brocade is 1 bolt = 1 zhang = 10 chi = 100 cun
total_length_in_cun = 100  # 1 zhang = 10 chi = 100 cun

# Value per cun
value_per_cun = Fraction(total_value * 1000, total_length_in_cun)  # Convert guan to wen (1 guan = 1000 wen)

# Value of one zhang (10 chi = 100 cun)
a = Fraction(value_per_cun * 100, 1000)  # Convert back to guan

# Value of one chi (10 cun)
b = value_per_cun * 10  # in wen

# Value of one cun
c = value_per_cun  # in wen

a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2, Actual: 8
Variable 'b' has wrong value. Expected: 200, Actual: 800
Variable 'c' has wrong value. Expected: 20, Actual: 80"""
