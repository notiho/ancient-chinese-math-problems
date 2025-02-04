"""
今有金二斤，令九十六人分之。問：人得㡬何？
術曰：列金二斤以十六两乘之得三十二两又以二十四銖乘之得七百六十八銖，以九十六人除之即得。
答曰： a銖 。
"""

"""
To solve this problem, we need to calculate how much each person gets when 2 jin of gold is divided among 96 people. The units are converted from jin to liang (1 jin = 16 liang) and then from liang to zhu (1 liang = 24 zhu). Finally, the total amount in zhu is divided by the number of people.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total gold in jin
gold_in_jin = 2

# Convert jin to liang (1 jin = 16 liang)
gold_in_liang = gold_in_jin * 16

# Convert liang to zhu (1 liang = 24 zhu)
gold_in_zhu = gold_in_liang * 24

# Number of people
people = 96

# Gold each person gets in zhu
a = Fraction(gold_in_zhu, people)

# Result
a
#----- content ends here -----


"""


The variable `a` will contain the amount of gold each person gets in zhu.
"""


"""
"""
