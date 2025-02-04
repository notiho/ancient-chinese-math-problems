"""
今有金二斤，令九十六人分之。問：人得㡬何？
術曰：列金二斤以十六两乘之得三十二两又以二十四銖乘之得七百六十八銖，以九十六人除之即得。
答曰： a銖 。
"""

#----- content starts here -----
"""
Suppose there are 2 jin of gold, and it is to be divided among 96 people.
Question: how much does each person get?

The procedure says: Place the 2 jin of gold, multiply it by 16 liang to convert it into liang, obtaining 32 liang.
Then multiply it by 24 zhu to convert it into zhu, obtaining 768 zhu.
Divide this by 96 people to obtain the amount each person gets.

Answer: each person gets *a* zhu.
"""

from fractions import Fraction

# 金二斤
金 = 2  # in jin

# 一斤 = 16兩
兩_per_斤 = 16
金_in_兩 = 金 * 兩_per_斤

# 一兩 = 24銖
銖_per_兩 = 24
金_in_銖 = 金_in_兩 * 銖_per_兩

# 九十六人
人數 = 96

# 每人所得
a = Fraction(金_in_銖, 人數)

a  # Answer in zhu#----- content ends here -----

"""
"""
