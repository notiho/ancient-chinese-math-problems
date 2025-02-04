"""
今有丁九萬八千七百六十六，凡二十五丁出一兵。問：兵幾何？
術曰：置丁九萬八千七百六十六為實，以二十五為法。實如法，即得。
答曰： a人 奇 b 丁。
"""

#----- content starts here -----
"""
Suppose there are 98,766 adult males (丁). For every 25 adult males, one soldier (兵) is conscripted.
Question: how many soldiers are conscripted, and how many adult males are left over?

The procedure says: Place 98,766 as the dividend (實) and 25 as the divisor (法). Divide the dividend by the divisor to obtain the result.

Answer: *a* soldiers and *b* remaining adult males.
"""

# 丁九萬八千七百六十六
丁 = 98766

# 凡二十五丁出一兵
法 = 25

# 實如法，即得
a = 丁 // 法  # Number of soldiers
b = 丁 % 法   # Remaining adult males (丁)

# Output: a soldiers and b 丁 remaining
a, b#----- content ends here -----

"""
"""
