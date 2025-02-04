"""
今有出錢七百二十，買縑一匹二丈一尺。欲丈率之，問︰丈幾何？
荅曰：一丈， a錢
"""

#----- content starts here -----
"""
Suppose 720 qian is spent to buy a bolt of silk that is 2 zhang and 1 chi in length.
Question: what is the cost per zhang?

Answer: 1 zhang costs *a* qian.
"""

# 出錢七百二十
錢 = 720

# 縑一匹二丈一尺 (convert to chi: 1 zhang = 10 chi)
總長度 = 2 * 10 + 1  # 2 zhang and 1 chi = 21 chi

# 每丈的費用 (1 zhang = 10 chi)
a = Fraction(錢, 總長度) * 10  # Cost per zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
