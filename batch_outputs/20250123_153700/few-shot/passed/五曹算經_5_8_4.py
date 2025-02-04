"""
今有金二斤，令九十六人分之。問：人得㡬何？
術曰：列金二斤以十六两乘之得三十二两又以二十四銖乘之得七百六十八銖，以九十六人除之即得。
答曰： a銖 。
"""

"""
Suppose there are 2 jin of gold, to be divided among 96 people.
Question: how much does each person receive?

The procedure says: Take 2 jin of gold and multiply it by 16 liang, obtaining 32 liang.
Then multiply it by 24 zhu, obtaining 768 zhu.
Divide this by 96 people to obtain the result.

Answer: each person receives *a* zhu.
"""

# 金二斤
金 = 2

# 一斤等於十六兩
兩每斤 = 16

# 列金二斤以十六两乘之得三十二两
金兩 = 金 * 兩每斤

# 一兩等於二十四銖
銖每兩 = 24

# 又以二十四銖乘之得七百六十八銖
金銖 = 金兩 * 銖每兩

# 九十六人
人數 = 96

# 以九十六人除之即得
a = Fraction(金銖, 人數)
"""
"""
