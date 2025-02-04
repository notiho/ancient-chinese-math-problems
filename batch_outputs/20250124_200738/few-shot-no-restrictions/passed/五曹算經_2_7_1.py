"""
今有城周四十八里，欲令禦賊，每三步置一兵。問：用兵㡬何？
術曰：列城周四十八里，以三百步乘之，得一萬四千四百步，以三步除之即得。
答曰： a人 。
"""

#----- content starts here -----
"""
Suppose there is a city with a circumference of 48 li. It is desired to defend against invaders by placing one soldier every 3 bu.
Question: how many soldiers are needed?

The procedure says: Take the city's circumference of 48 li, multiply it by 300 bu (since 1 li = 300 bu), obtaining 14,400 bu. Divide this by 3 bu to get the number of soldiers.

Answer: *a* soldiers.
"""

from fractions import Fraction

# 城周四十八里
城周 = 48  # in li

# 1里 = 300步
步每里 = 300

# 每三步置一兵
步每兵 = 3

# 以三百步乘之，得一萬四千四百步
總步數 = 城周 * 步每里

# 以三步除之即得
a = Fraction(總步數, 步每兵)

# Output the result
a#----- content ends here -----

"""
"""
