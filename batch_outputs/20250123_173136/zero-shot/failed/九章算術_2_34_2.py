"""
今有出錢七百二十，買縑一匹二丈一尺。欲丈率之，問︰丈幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一丈， a錢
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
total_money = 720  # in 錢
length_per_piece = Fraction(2, 1) + Fraction(1, 10)  # 2丈1尺 = 2丈 + 1/10丈

# Calculation
a = total_money / length_per_piece  # a is the cost per 丈 in 錢

# Result
a  # This is the cost per 丈 in 錢


"""


The variable `a` will contain the value of the cost per 丈 in 錢.
"""


"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
