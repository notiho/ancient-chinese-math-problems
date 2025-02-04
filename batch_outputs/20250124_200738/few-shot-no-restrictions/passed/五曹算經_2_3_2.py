"""
今有兵三千八百三十七人，人給錢五百五十六文。問：計㡬何？
術曰：列兵三千八百三十七人，以五百五十六文乘之即得。
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there are 3837 soldiers, and each soldier is given 556 wen.
Question: how much money is required in total?

The procedure says: Place the 3837 soldiers, and multiply it by 556 wen to obtain the total.
Convert the result into guan (1 guan = 1000 wen).

Answer: *a* guan.
"""

from fractions import Fraction

# 兵三千八百三十七人
兵 = 3837

# 每人給錢五百五十六文
每人錢 = 556

# 總文數
總文數 = 兵 * 每人錢

# 1貫 = 1000文
文轉貫 = 1000

# 計算總貫數
a = Fraction(總文數, 文轉貫)

a#----- content ends here -----

"""
"""
