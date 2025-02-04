"""
今有縑一丈價直一百二十八。今有縑一匹九尺五寸，問︰得錢幾何？
術曰：以一丈寸數為法，以價錢數乘今有縑寸數為實，實如法得錢數。
荅曰： a錢 。
"""

"""
To solve this problem, we will calculate the value of a piece of silk based on its length and the price per unit length. Here's the Python code:


"""


from fractions import Fraction

# Given data
price_per_zhang = 128  # Price of one zhang in qian
length_of_zhang = 10  # One zhang is 10 chi
length_of_piece = 9 + Fraction(5, 10)  # 9 chi 5 cun (1 chi = 10 cun)

# Calculation
price_per_chi = Fraction(price_per_zhang, length_of_zhang)  # Price per chi
a = price_per_chi * length_of_piece  # Total price of the given piece in qian

# Result
a  # The answer in qian


"""


This code calculates the value of the silk piece in qian (`a`). The result is stored in the variable `a`.
"""


"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 608/5"""
