"""
今有凡錢五文買雉三隻，有錢一萬七千五百二十五文。問：得雉㡬何？
答曰： a隻 。
"""

"""
Suppose 5 wen (coins) can buy 3 pheasants. If you have 17,525 wen, how many pheasants can you buy?

Answer: *a* pheasants.
"""

# 錢五文買雉三隻
錢_per_雉 = Fraction(5, 3)

# 總錢數
總錢 = 17525

# 計算雉的數量
a = Fraction(總錢, 錢_per_雉)
"""
"""
