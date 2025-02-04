"""
今有金一斤直錢一百貫問一兩幾何
術曰置錢數以十六兩除之即得
答曰一兩 a貫
"""

#----- content starts here -----
"""
Suppose there is 1 jin of gold worth 100 guan of money.
Question: how much is 1 liang worth?

The procedure says: Place the amount of money and divide it by 16 liang, then you obtain the value.

Answer: 1 liang is worth *a* guan.
"""

# 金一斤直錢一百貫
錢數 = 100  # 貫

# 一斤等於十六兩
兩數 = 16

# 置錢數以十六兩除之即得
a = Fraction(錢數, 兩數)  # 貫 per 1 兩#----- content ends here -----

"""
"""
