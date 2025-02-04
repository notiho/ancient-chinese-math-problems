"""
今有絲一斤，價直二百四十。今有錢一千三百二十八，問︰得絲幾何？
術曰：以一斤價數為法，以一斤乘今有錢數為實，實如法得絲數。
荅曰： a斤 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
price_per_jin = 240  # price of one jin of silk
total_money = 1328  # total money available

# Calculation
a = Fraction(total_money, price_per_jin)  # silk obtained in jin

# Result
a  # a is the amount of silk in jin


"""


The variable `a` will hold the value of the silk obtained in jin.
"""


"""
"""
