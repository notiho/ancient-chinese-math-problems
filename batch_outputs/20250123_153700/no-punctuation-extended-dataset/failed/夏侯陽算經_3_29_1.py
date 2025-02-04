"""
今有錢五千四百六十三貫四百五十文準例毎貫納五十文充墊陌問合墊幾何
術曰先置錢折半退位即得
答曰 a貫
"""

"""
Suppose there is 5463 guan and 450 wen of money. According to the rule, for every guan, 50 wen are deducted as a surcharge.
Question: how much is deducted in total?

The procedure says: First, take the amount of money, divide it in half, and shift the decimal place (reduce the unit by one position). The result is obtained.

Answer: *a* guan.
"""

# 錢五千四百六十三貫四百五十文
錢貫 = 5463
錢文 = 450

# Convert all to wen (1 貫 = 1000 文)
總錢文 = (錢貫 * 1000) + 錢文

# 每貫納五十文充墊陌
# 先置錢折半 (divide by 2)
墊文 = 總錢文 / 2

# 退位即得 (convert back to 貫 by dividing by 1000)
a = Fraction(墊文, 1000)
"""
Code error: both arguments should be Rational instances"""
