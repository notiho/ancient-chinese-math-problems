"""
今有錢五千四百六十三貫四百五十文準例毎貫納五十文充墊陌問合墊幾何
術曰先置錢折半退位即得
答曰 a貫
"""

"""
Suppose there are 5463 guan and 450 wen. According to the rule, for every guan, 50 wen are deducted as a fee.
Question: how much is deducted in total?

The procedure says: First, place the total amount of money. Halve it, and shift the decimal place (divide by 10). The result is obtained.

Answer: *a* guan.
"""

# 錢五千四百六十三貫四百五十文
錢貫 = 5463
錢文 = 450

# Convert all to wen (1 貫 = 1000 文)
總錢文 = 錢貫 * 1000 + 錢文

# 每貫納五十文充墊陌
# 先置錢，折半
折半 = 總錢文 / 2

# 退位 (divide by 10)
a = Fraction(折半, 1000)  # Convert back to 貫
"""
Code error: both arguments should be Rational instances"""
