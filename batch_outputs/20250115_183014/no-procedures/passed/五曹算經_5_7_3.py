"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

"""
Suppose there is a bolt of brocade (錦) that is worth 8 guan (貫) of coins. 
Question: how much is 1 zhang (丈), 1 chi (尺), and 1 cun (寸) worth respectively?

Answer: 1 zhang is worth *a* guan, 1 chi is worth *b* wen, and 1 cun is worth *c* wen.
"""

# Total length of one bolt of brocade (1 疋) is 40 chi (4 丈).
total_length_in_chi = 40

# Total value of the brocade is 8 guan.
total_value_in_wen = 8 * 1000  # 1 guan = 1000 wen

# Value per chi
value_per_chi = Fraction(total_value_in_wen, total_length_in_chi)

# Value of 1 zhang (10 chi)
a = Fraction(value_per_chi * 10, 1000)  # Convert to guan

# Value of 1 chi
b = value_per_chi  # In wen

# Value of 1 cun (1/10 of a chi)
c = Fraction(value_per_chi, 10)  # In wen

a, b, c  # Output the results
"""
"""
