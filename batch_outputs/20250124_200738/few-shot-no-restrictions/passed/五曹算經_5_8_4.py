"""
今有金二斤，令九十六人分之。問：人得㡬何？
術曰：列金二斤以十六两乘之得三十二两又以二十四銖乘之得七百六十八銖，以九十六人除之即得。
答曰： a銖 。
"""

#----- content starts here -----
"""
Suppose there are 2 jin of gold, and it is to be divided among 96 people.
Question: how much does each person receive?

The procedure says: Represent the 2 jin of gold in terms of liang by multiplying it by 16, obtaining 32 liang.
Then convert liang to zhu by multiplying it by 24, obtaining 768 zhu.
Divide this by 96 people to get the amount each person receives.

Answer: each person gets *a* zhu.
"""

from fractions import Fraction

# 金二斤
金 = 2

# 一斤等於十六兩
兩每斤 = 16
金_兩 = 金 * 兩每斤

# 一兩等於二十四銖
銖每兩 = 24
金_銖 = 金_兩 * 銖每兩

# 九十六人
人數 = 96

# 每人所得
a = Fraction(金_銖, 人數)

a  # Output the amount each person receives in zhu.#----- content ends here -----

"""
"""
