"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
荅曰：一匹， a錢
"""

#----- content starts here -----
"""
Suppose there is 2370 qian (money) used to buy 9 bolts of cloth, each bolt being 2 zhang and 7 chi in length.
Question: what is the cost per bolt of cloth?

Answer: one bolt costs *a* qian.
"""

from fractions import Fraction

# 出錢二千三百七十
total_money = 2370

# 買布九匹
bolts_of_cloth = 9

# Calculate the cost per bolt
a = Fraction(total_money, bolts_of_cloth)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/3"""
