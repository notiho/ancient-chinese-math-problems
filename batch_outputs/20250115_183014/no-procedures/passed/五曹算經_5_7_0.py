"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

"""
Suppose there is a bolt of brocade (錦) that is worth 8 guan (貫) of coins. 
Question: How much is 1 zhang (丈), 1 chi (尺), and 1 cun (寸) worth?

Answer: 1 zhang is worth *a* guan, 1 chi is worth *b* wen (文), and 1 cun is worth *c* wen (文).
"""

# Total length of one bolt of brocade
# 1 bolt = 1 pi (疋) = 40 chi (尺)
total_length_in_chi = 40

# Total value of the bolt
total_value_in_wen = 8 * 1000  # 1 guan = 1000 wen

# Value per chi
value_per_chi = Fraction(total_value_in_wen, total_length_in_chi)

# Convert to zhang, chi, and cun
# 1 zhang = 10 chi, 1 chi = 10 cun
a = Fraction(value_per_chi * 10, 1000)  # Value of 1 zhang in guan
b = value_per_chi  # Value of 1 chi in wen
c = Fraction(value_per_chi, 10)  # Value of 1 cun in wen

a, b, c  # Outputs the values of a, b, and c
"""
"""
