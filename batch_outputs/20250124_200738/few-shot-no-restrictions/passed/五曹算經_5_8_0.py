"""
今有金二斤，令九十六人分之。問：人得㡬何？
術曰：列金二斤以十六两乘之得三十二两又以二十四銖乘之得七百六十八銖，以九十六人除之即得。
答曰： a銖 。
"""

#----- content starts here -----
"""
Suppose there are 2 jin of gold, and it is to be divided among 96 people.
Question: how much does each person receive?

The procedure says: Take the 2 jin of gold and multiply it by 16 liang to get 32 liang.
Then multiply it by 24 zhu to get 768 zhu.
Divide this by 96 people to get the amount.

Answer: each person gets *a* zhu.
"""

from fractions import Fraction

# 金二斤
金 = 2

# 一斤等於十六兩
兩_per_斤 = 16

# 一兩等於二十四銖
銖_per_兩 = 24

# 九十六人
人數 = 96

# 金二斤以十六两乘之得三十二两
金_in_兩 = 金 * 兩_per_斤

# 又以二十四銖乘之得七百六十八銖
金_in_銖 = 金_in_兩 * 銖_per_兩

# 以九十六人除之即得
a = Fraction(金_in_銖, 人數)

a  # Each person gets `a` zhu.#----- content ends here -----

"""
"""
