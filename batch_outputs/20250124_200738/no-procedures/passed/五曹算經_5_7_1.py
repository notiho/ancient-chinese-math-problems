"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

#----- content starts here -----
"""
Suppose there is a bolt of brocade (1 pi) worth 8 guan (8000 wen).
Question: how much is 1 zhang, 1 chi, and 1 cun worth respectively?

Answer: 1 zhang is worth *a* guan, 1 chi is worth *b* wen, and 1 cun is worth *c* wen.
"""

# Total value of 1 pi
total_value = 8 * 1000  # 8 guan = 8000 wen

# Length of 1 pi in chi (1 pi = 40 chi)
total_length_in_chi = 40

# Value per chi
value_per_chi = Fraction(total_value, total_length_in_chi)

# 1 zhang = 10 chi
a = Fraction(10 * value_per_chi, 1000)  # Convert to guan

# 1 chi
b = value_per_chi  # In wen

# 1 cun = 1/10 chi
c = Fraction(value_per_chi, 10)  # In wen

a, b, c  # Outputs the values for 1 zhang, 1 chi, and 1 cun respectively.#----- content ends here -----

"""
"""
