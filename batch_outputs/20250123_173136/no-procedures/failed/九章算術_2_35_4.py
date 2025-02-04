"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
荅曰：一匹， a錢
"""

"""
Suppose there is a total of 2370 qian spent to buy 9 bolts of cloth, each bolt being 2 zhang and 7 chi in length.
Question: what is the cost per bolt of cloth?

Answer: one bolt costs *a* qian.
"""

# 出錢二千三百七十
總錢 = 2370

# 買布九匹
布匹數 = 9

# Calculate the cost per bolt
a = Fraction(總錢, 布匹數)
"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/3"""
