"""
今有金二斤，令九十六人分之。問：人得㡬何？
術曰：列金二斤以十六两乘之得三十二两又以二十四銖乘之得七百六十八銖，以九十六人除之即得。
答曰： a銖 。
"""

"""
To solve this problem, we need to calculate how much each person gets when 2 jin of gold is divided among 96 people. The conversion factors are:

1 jin = 16 liang  
1 liang = 24 zhu  

Thus, 2 jin = 2 × 16 liang = 32 liang.  
32 liang = 32 × 24 zhu = 768 zhu.  

Now, divide 768 zhu by 96 people to find how much each person gets.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total gold in zhu
total_gold_zhu = 2 * 16 * 24  # 2 jin to zhu

# Number of people
people = 96

# Gold per person in zhu
a = Fraction(total_gold_zhu, people)

# The result is stored in variable 'a'
#----- content ends here -----


"""


The value of `a` will represent the amount of gold each person gets in zhu.
"""


"""
"""
