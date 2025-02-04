"""
今有金二斤，令九十六人分之。問：人得㡬何？
術曰：列金二斤以十六两乘之得三十二两又以二十四銖乘之得七百六十八銖，以九十六人除之即得。
答曰： a銖 。
"""

"""
To solve this problem, we need to calculate how much each person gets when 2 jin of gold is divided among 96 people. The conversion factors are:

1 jin = 16 liang  
1 liang = 24 zhu  

The solution in Python is as follows:


"""


from fractions import Fraction

# Total gold in jin
gold_in_jin = 2

# Convert jin to liang
gold_in_liang = gold_in_jin * 16

# Convert liang to zhu
gold_in_zhu = gold_in_liang * 24

# Number of people
people = 96

# Gold each person gets in zhu
a = Fraction(gold_in_zhu, people)

# The answer is stored in variable 'a'
a


"""


The value of `a` will represent the amount of gold each person gets in zhu.
"""


"""
"""
