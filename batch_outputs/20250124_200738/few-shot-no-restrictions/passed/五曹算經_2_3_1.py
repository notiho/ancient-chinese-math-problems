"""
今有兵三千八百三十七人，人給錢五百五十六文。問：計㡬何？
術曰：列兵三千八百三十七人，以五百五十六文乘之即得。
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there are 3837 soldiers, and each soldier is given 556 wen.  
Question: how much money is needed in total?

The procedure says: Place the 3837 soldiers, multiply by 556 wen, and the result is obtained.

Answer: *a* guan.
"""

from fractions import Fraction

# 兵三千八百三十七人
兵 = 3837

# 人給錢五百五十六文
每人錢 = 556  # 文

# 以五百五十六文乘之即得
總錢文 = 兵 * 每人錢

# 1貫 = 1000文
總錢貫 = Fraction(總錢文, 1000)

a = 總錢貫

# Output the result
a#----- content ends here -----

"""
"""
