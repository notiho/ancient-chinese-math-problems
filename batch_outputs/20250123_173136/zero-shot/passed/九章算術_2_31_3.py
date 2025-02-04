"""
今有出錢一百六十，買瓴甓十八枚。問︰枚幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一枚， a錢
"""

"""
To solve this problem, we need to calculate the cost per tile (枚). The total cost is 160 (錢), and the total number of tiles is 18 (枚). Using the given formula, the cost per tile is calculated as:


"""


from fractions import Fraction

# Total money spent
total_money = 160

# Total number of tiles
total_tiles = 18

# Cost per tile
a = Fraction(total_money, total_tiles)

# Result
a  # This represents the cost per tile in 錢


"""


The value of `a` will be the cost of one tile in 錢.
"""


"""
"""
