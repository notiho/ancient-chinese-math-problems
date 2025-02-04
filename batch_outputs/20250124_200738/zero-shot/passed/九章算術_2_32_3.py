"""
今有出錢一萬三千五百，買竹二千三百五十箇。問︰箇幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一箇， a錢
"""

"""
To solve this problem, we need to calculate the cost of one bamboo (箇) in terms of money (錢). The problem states that 13,500 (錢) is spent to buy 2,350 bamboo (箇). Using the given formula, we divide the total money by the total number of bamboo to find the cost per bamboo.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_money = 13500  # in 錢
total_bamboo = 2350  # in 箇

# Calculate the cost of one bamboo
a = Fraction(total_money, total_bamboo)

# The result
a  # in 錢
#----- content ends here -----


"""


The variable `a` represents the cost of one bamboo in 錢.
"""


"""
"""
