"""
今有錢三千四百六十三貫五百文欲毎貫墊四十二文問墊幾何
術曰先置錢數以六七因之退位即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there are 3463 guan and 500 wen of money, and it is desired to calculate how much is needed to add 42 wen for every guan.
Question: how much is the total addition?

The procedure says: First, place the total amount of money. Multiply it by 6 and 7, then shift the decimal place back (divide by 10). This gives the result.

Answer: *a* guan.
"""

from fractions import Fraction

# 錢三千四百六十三貫五百文
錢貫 = 3463
錢文 = 500

# 每貫墊四十二文
每貫墊文 = 42

# 將錢數轉換為文 (1 貫 = 1000 文)
總文數 = 錢貫 * 1000 + 錢文

# 以六七因之 (乘以 6 再乘以 7)
墊文數 = 總文數 * 6 * 7

# 退位 (除以 10)
墊文數 = Fraction(墊文數, 10)

# 將墊文數轉換為貫 (1 貫 = 1000 文)
a = Fraction(墊文數, 1000)  # 答案以貫表示#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 145467/1000, Actual: 145467/10"""
