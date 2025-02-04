"""
今有金二斤，令九十六人分之。問：人得㡬何？
術曰：列金二斤以十六两乘之得三十二两又以二十四銖乘之得七百六十八銖，以九十六人除之即得。
答曰： a(=8)銖 。
"""

#----- content starts here -----
"""
Suppose there are 2 jin of gold, and it is to be divided among 96 people.
Question: how much does each person receive?

The procedure says: Place the 2 jin of gold, multiply it by 16 liang, obtaining 32 liang.
Then multiply it by 24 zhu, obtaining 768 zhu.
Divide it by 96 people, and the result is obtained.

Answer: *a*(=8) zhu.
"""

# 金二斤
金 = 2

# 以十六两乘之得三十二两
兩 = 16 * 金

# 又以二十四銖乘之得七百六十八銖
銖 = 24 * 兩

# 以九十六人除之即得
a = Fraction(銖, 96) # 8#----- content ends here -----

"""
"""
