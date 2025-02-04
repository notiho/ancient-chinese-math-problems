"""
今有出錢五千七百八十五，買漆一斛六斗七升、太半升。欲斗率之，問︰斗幾何。
荅曰：一斗， a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 5785 qian to buy 1 hu, 6 dou, 7 sheng, and half a sheng of lacquer.
Question: how much does 1 dou cost?

Answer: 1 dou costs *a* qian.
"""

# 出錢
total_money = 5785

# 漆的總量 (1斛 = 10斗, 1斗 = 10升)
漆_total_dou = 1 * 10 + 6 + Fraction(7, 10) + Fraction(1, 20)

# 每斗的價格
a = Fraction(total_money, 漆_total_dou)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 173550/503, Actual: 23140/67"""
