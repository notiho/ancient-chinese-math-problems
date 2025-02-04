"""
今有錢五千四百六十三貫四百五十文準例毎貫納五十文充墊陌問合墊幾何
術曰先置錢折半退位即得
答曰 a貫
"""

"""
Suppose there are 5463 guan and 450 wen of money. According to the rule, for every guan, 50 wen are deducted as a surcharge.
Question: how much is deducted in total?

The procedure says: First, take the amount of money, divide it by 2, and shift the decimal place (reduce the unit by one position). This gives the result.

Answer: *a* guan.
"""

# 錢五千四百六十三貫四百五十文
貫 = 5463
文 = 450

# 將文轉換為貫
文_to_貫 = Fraction(1, 1000)
總貫 = 貫 + 文 * 文_to_貫

# 先置錢折半
折半 = 總貫 / 2

# 退位即得
a = 折半  # The result is already in guan.
"""
Variable 'a' has wrong value. Expected: 109269/400, Actual: 109269/40"""
