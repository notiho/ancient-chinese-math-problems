"""
今有出錢七百二十，買縑一匹二丈一尺。欲丈率之，問︰丈幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一丈， a錢
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. The problem involves determining the cost per丈 (unit of length) when given the total cost, the total length, and the relationship between them.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_cost = 720  # in 錢
total_length = Fraction(2, 1) + Fraction(1, 10)  # 2丈1尺 = 2丈 + 1/10丈

# Calculation
a = total_cost / total_length  # cost per 丈 in 錢

# Output the result
a  # This is the cost per 丈 in 錢
#----- content ends here -----


"""


The variable `a` will contain the cost per 丈 in 錢.
"""


"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
