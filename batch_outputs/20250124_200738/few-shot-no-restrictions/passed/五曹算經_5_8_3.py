"""
今有金二斤，令九十六人分之。問：人得㡬何？
術曰：列金二斤以十六两乘之得三十二两又以二十四銖乘之得七百六十八銖，以九十六人除之即得。
答曰： a銖 。
"""

#----- content starts here -----
"""
Suppose there are 2 jin of gold, and it is to be divided among 96 people.
Question: how much does each person receive?

The procedure says: Place the 2 jin of gold, multiply it by 16 liang to convert it into 32 liang.
Then multiply it by 24 zhu to convert it into 768 zhu.
Divide it by 96 people to obtain the result.

Answer: each person receives *a* zhu.
"""

from fractions import Fraction

# 金二斤
金 = 2  # in jin

# 一斤 = 16兩
兩_per_斤 = 16

# 一兩 = 24銖
銖_per_兩 = 24

# 九十六人
人數 = 96

# 以十六兩乘之，得金的總兩數
金_兩 = 金 * 兩_per_斤

# 以二十四銖乘之，得金的總銖數
金_銖 = 金_兩 * 銖_per_兩

# 以九十六人除之，即每人所得銖數
a = Fraction(金_銖, 人數)

a  # Output the result in zhu (銖) per person#----- content ends here -----

"""
"""
