"""
今有兵三千八百三十七人，人給錢五百五十六文。問：計㡬何？
術曰：列兵三千八百三十七人，以五百五十六文乘之即得。
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there are 3,837 soldiers, and each soldier is given 556 wen (a unit of currency).
Question: how much total money is required?

The procedure says: Place the number of soldiers, 3,837, and multiply it by 556 wen to obtain the total amount.
Convert the result into guan (1 guan = 1,000 wen).

Answer: *a* guan.
"""

from fractions import Fraction

# 兵三千八百三十七人
兵 = 3837

# 人給錢五百五十六文
每人錢 = 556

# 以五百五十六文乘之即得
總錢文 = 兵 * 每人錢

# 1貫 = 1000文
a = Fraction(總錢文, 1000)

a#----- content ends here -----

"""
"""
