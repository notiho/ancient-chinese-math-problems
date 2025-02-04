"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一匹， a錢
"""

"""
To solve this problem, we need to calculate the cost of one匹 (one bolt of cloth). Here's the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Given values
total_money = 2370  # in 錢
total_cloth = 9 + Fraction(27, 10)  # 9匹 and 2丈7尺 (converted to 9.27匹)

# Calculate the cost per 匹
a = Fraction(total_money, total_cloth)

# The result is stored in variable 'a'


"""


The value of `a` will represent the cost of one匹 in 錢.
"""


"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 7900/39"""
