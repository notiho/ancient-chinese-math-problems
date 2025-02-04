"""
今有出錢一百六十，買瓴甓十八枚。問︰枚幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一枚， a錢
"""

"""
The problem describes a situation where 160 units of money are spent to buy 18 tiles. We are tasked with finding the cost of one tile (denoted as "a"). Here's the Python code to compute the value of "a":


"""


from fractions import Fraction

# Given data
total_money = 160  # total money spent
total_tiles = 18   # total number of tiles

# Calculate the cost of one tile
a = Fraction(total_money, total_tiles)

# The result is stored in the variable "a"


"""


The value of `a` represents the cost of one tile in units of money.
"""


"""
"""
