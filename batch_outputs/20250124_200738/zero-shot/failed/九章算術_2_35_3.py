"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一匹， a錢
"""

"""
To solve this problem, we need to calculate the cost of one匹 (one bolt of cloth). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_money = 2370  # in 錢
total_cloth = 9 * 2 + Fraction(7, 10)  # 9 bolts, 2丈7尺 (1丈 = 10尺)

# Calculate the cost per bolt (匹)
a = Fraction(total_money, total_cloth)

# Result
a  # in 錢
#----- content ends here -----


"""


The variable `a` will contain the cost of one匹 in 錢.
"""


"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 23700/187"""
