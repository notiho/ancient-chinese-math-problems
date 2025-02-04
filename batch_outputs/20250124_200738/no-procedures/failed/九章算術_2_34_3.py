"""
今有出錢七百二十，買縑一匹二丈一尺。欲丈率之，問︰丈幾何？
荅曰：一丈， a錢
"""

#----- content starts here -----
"""
Suppose 720 qian (coins) are spent to buy 1 bolt of silk, which is 2 zhang and 1 chi in length.
Question: What is the cost per zhang?

Answer: 1 zhang costs *a* qian.
"""

from fractions import Fraction

# 出錢七百二十
total_money = 720

# 縑一匹二丈一尺 (2 zhang and 1 chi)
total_length = 2 + Fraction(1, 10)  # 1 chi = 1/10 zhang

# Calculate cost per zhang
a = Fraction(total_money, total_length)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
