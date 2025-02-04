"""
今有出錢一百六十，買瓴甓十八枚。問︰枚幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一枚， a錢
"""

"""
To solve this problem, we need to calculate the cost of one tile ("枚"). The total cost is 160 (錢), and the number of tiles is 18. Using the given formula, we divide the total cost by the number of tiles to find the cost per tile.

Here is the Python code:


"""


from fractions import Fraction

# Given data
total_cost = 160  # 錢
number_of_tiles = 18  # 枚

# Calculate the cost of one tile
a = Fraction(total_cost, number_of_tiles)

# The result
a  # 錢 per 枚


"""


The variable `a` will store the cost of one tile in 錢.
"""


"""
"""
