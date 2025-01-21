"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
術曰：以價直為法，以一匹一丈尺數乘今有錢數為實。實如法得素數。
荅曰：得素 a匹 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
price_per_unit = 625  # Price for 1匹1丈
money_available = 500  # Available money

# Calculation
a = Fraction(money_available, price_per_unit)  # Amount of 素 in 匹

# Result
a  # This represents the amount of 素 in 匹


"""


The variable `a` will hold the result, which is the amount of 素 (in 匹) that can be obtained with the given money.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 4/5"""
