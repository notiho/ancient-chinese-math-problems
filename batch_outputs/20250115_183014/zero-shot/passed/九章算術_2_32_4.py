"""
今有出錢一萬三千五百，買竹二千三百五十箇。問︰箇幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一箇， a錢
"""

"""
To solve this problem, we need to calculate the cost of one bamboo (箇) in terms of "錢" (money). Here's the Python code:


"""


from fractions import Fraction

# Given data
total_money = 13500  # total money in 錢
total_bamboo = 2350  # total bamboo in 箇

# Calculate the cost of one bamboo
a = Fraction(total_money, total_bamboo)

# The result
a  # cost of one bamboo in 錢


"""


The variable `a` will hold the value of the cost of one bamboo in 錢.
"""


"""
"""
