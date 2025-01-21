"""
今有丁九萬八千七百六十六，凡二十五丁出一兵。問：兵幾何？
術曰：置丁九萬八千七百六十六為實，以二十五為法。實如法，即得。
答曰： a人 奇 b 丁。
"""

"""
Suppose there are 98,766 adult males (丁). For every 25 males, one soldier (兵) is conscripted.
Question: how many soldiers are conscripted, and how many males are left over?

The procedure says: Place 98,766 as the dividend (實), and 25 as the divisor (法).
Divide the dividend by the divisor, obtaining the quotient as the number of soldiers and the remainder as the leftover males.

Answer: *a* soldiers and *b* males.
"""

# 置丁九萬八千七百六十六為實
實 = 98766

# 以二十五為法
法 = 25

# 實如法，即得
a = 實 // 法  # Quotient: number of soldiers
b = 實 % 法   # Remainder: leftover males
"""
"""
