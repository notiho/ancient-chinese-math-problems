"""
今有錢五千四百六十三貫四百五十文準例毎貫納五十文充墊陌問合墊幾何
術曰先置錢折半退位即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there is 5463 guan and 450 wen. According to the rule, for every guan, 50 wen are deducted as a surcharge.
Question: how much is the total surcharge?

The procedure says: First, take the total amount of money, divide it in half, and shift the decimal place (i.e., divide by 10). The result is obtained.

Answer: *a* guan.
"""

# 錢五千四百六十三貫四百五十文
貫 = 5463
文 = 450

# Convert everything to wen (1 貫 = 1000 文)
總文 = 貫 * 1000 + 文

# 術曰：先置錢折半
折半 = 總文 / 2

# 術曰：退位 (divide by 10)
墊陌 = 折半 / 10

# Convert back to 貫
a = Fraction(墊陌, 1000)  # Convert wen to guan#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
