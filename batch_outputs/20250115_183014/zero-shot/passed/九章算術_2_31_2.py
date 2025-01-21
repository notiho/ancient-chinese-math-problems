"""
今有出錢一百六十，買瓴甓十八枚。問︰枚幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一枚， a錢
"""

"""
To solve this problem, we need to determine the cost of one tile (瓴甓) in terms of money (錢). The problem states that 160 units of money are spent to buy 18 tiles. Using the given formula, the cost of one tile is calculated as follows:


"""


from fractions import Fraction

# Given data
total_money = 160  # total money spent
total_tiles = 18   # total tiles bought

# Calculate the cost of one tile
a = Fraction(total_money, total_tiles)  # cost of one tile in terms of money

# The result
a  # This is the cost of one tile in 錢


"""


The value of `a` will represent the cost of one tile in 錢.
"""


"""
"""
