"""
今有金二斤，令九十六人分之。問：人得㡬何？
術曰：列金二斤以十六两乘之得三十二两又以二十四銖乘之得七百六十八銖，以九十六人除之即得。
答曰： a銖 。
"""

"""
To solve this problem, we need to calculate how much each person gets when 2 jin of gold is divided among 96 people. The problem specifies that 1 jin = 16 liang and 1 liang = 24 zhu. We'll compute the amount each person gets in zhu.

Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total gold in jin
gold_in_jin = 2

# Conversion factors
jin_to_liang = 16  # 1 jin = 16 liang
liang_to_zhu = 24  # 1 liang = 24 zhu

# Total gold in zhu
gold_in_zhu = gold_in_jin * jin_to_liang * liang_to_zhu

# Number of people
people = 96

# Gold each person gets in zhu
a = Fraction(gold_in_zhu, people)

# The answer is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` contains the amount of gold each person gets in zhu as a fraction.
"""


"""
"""
