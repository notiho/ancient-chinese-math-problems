"""
今有出錢一百六十，買瓴甓十八枚。問︰枚幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一枚， a錢
"""

"""
This problem involves calculating the cost of one item when the total cost and the number of items are given. Here's the Python code to solve it:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_money = 160  # total money spent in 錢
total_items = 18  # total items bought

# Calculate the cost of one item
a = Fraction(total_money, total_items)

# Output the result
a  # cost of one item in 錢
#----- content ends here -----


"""


The variable `a` will hold the value of the cost of one item in 錢.
"""


"""
"""
