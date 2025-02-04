"""
今有金二斤，令九十六人分之。問：人得㡬何？
術曰：列金二斤以十六两乘之得三十二两又以二十四銖乘之得七百六十八銖，以九十六人除之即得。
答曰： a銖 。
"""

#----- content starts here -----
"""
Suppose there are 2 jin of gold, and it is to be divided among 96 people.
Question: how much does each person receive?

The procedure says: Take the 2 jin of gold, multiply it by 16 liang to convert it into 32 liang.
Then multiply it by 24 zhu to convert it into 768 zhu.
Divide this by 96 people, and the result is the amount each person receives.

Answer: each person receives *a* zhu.
"""

from fractions import Fraction

# 金二斤
金 = 2  # in jin

# 1斤 = 16两
金_兩 = 金 * 16  # convert jin to liang

# 1两 = 24銖
金_銖 = 金_兩 * 24  # convert liang to zhu

# 分給九十六人
人數 = 96

# 每人所得
a = Fraction(金_銖, 人數)

a  # Output the amount each person receives in zhu#----- content ends here -----

"""
"""
