"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
術曰：列錢二百三十八貫五百七十三文足以九十二除之即得。
答曰： a貫 奇足錢 b分 。
"""

#----- content starts here -----
"""
Suppose there is 238 guan and 573 wen of money in total, and it is desired to divide it into 92 *mo* (units).
Question: how much does each *mo* receive?

The procedure says: Place the total money, 238 guan and 573 wen, and divide it by 92. The result is the amount for each *mo*.

Answer: *a* guan and *b* wen.
"""

from fractions import Fraction

# 錢二百三十八貫五百七十三文足
總錢 = 238 * 1000 + 573  # Convert guan to wen (1 guan = 1000 wen)

# 欲為九十二陌
陌 = 92

# 以九十二除之即得
每陌錢 = Fraction(總錢, 陌)

# Convert result back to 貫 and 文
a = 每陌錢 // 1000  # 貫
b = 每陌錢 % 1000  # 文

a, b  # Output the result as (a貫, b文)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 54573/92"""
