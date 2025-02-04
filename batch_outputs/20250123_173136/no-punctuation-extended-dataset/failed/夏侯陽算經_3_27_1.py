"""
今有錢三千四百六十三貫五百文欲毎貫墊四十二文問墊幾何
術曰先置錢數以六七因之退位即得
答曰 a貫
"""

"""
Suppose there is 3463 guan and 500 wen of money. It is desired to calculate how much is needed to add 42 wen per guan.
Question: how much additional money is required?

The procedure says: First place the total amount of money. Multiply it by 6/7, and shift the decimal place (adjust the units), then the result is obtained.

Answer: *a* guan.
"""

from fractions import Fraction

# 錢三千四百六十三貫五百文
錢貫 = 3463
錢文 = 500

# Convert to total wen (1 貫 = 1000 文)
總錢文 = 錢貫 * 1000 + 錢文

# 每貫墊四十二文
墊文每貫 = 42

# 以六七因之 (multiply by 6/7)
墊總文 = Fraction(6, 7) * 總錢文

# Convert back to 貫 (1 貫 = 1000 文)
a = 墊總文 / 1000
"""
Variable 'a' has wrong value. Expected: 145467/1000, Actual: 20781/7"""
