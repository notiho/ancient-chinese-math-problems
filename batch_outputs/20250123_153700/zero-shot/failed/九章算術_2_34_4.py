"""
今有出錢七百二十，買縑一匹二丈一尺。欲丈率之，問︰丈幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一丈， a錢
"""

"""
To solve this problem, we need to calculate the cost per丈 (unit length) of the fabric. The given information is:

- Total cost: 720錢
- Total length: 2丈1尺

Since 1丈 = 10尺, the total length in terms of 尺 is \( 2丈1尺 = 2 \times 10 + 1 = 21尺 \).

The cost per 丈 can be calculated as follows:

1. Convert the total length to 丈: \( 21尺 = \frac{21}{10}丈 \).
2. Divide the total cost by the total length in 丈 to get the cost per 丈.

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given values
total_cost = 720  # in 錢
total_length_in_zhang = Fraction(21, 10)  # 21尺 = 21/10丈

# Calculate the cost per 丈
a = total_cost / total_length_in_zhang

# Result
a  # Cost per 丈 in 錢


"""


The variable `a` will contain the cost per 丈 in 錢.
"""


"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
