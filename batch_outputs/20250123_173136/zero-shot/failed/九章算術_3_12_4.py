"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
術曰：以一匹尺數為法，今有布尺數乘價錢為實，實如法得錢數。
荅曰： a錢 。
"""

"""
To solve the problem, let's translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
price_per_piece = 125  # Price of one piece of cloth in 錢
length_per_piece = 1  # Length of one piece of cloth in 匹 (1匹 = 10丈)
length_in_question = Fraction(2, 1) + Fraction(7, 10)  # Length of cloth in question (2丈7尺, where 1丈 = 10尺)

# Calculation
a = (length_in_question / length_per_piece) * price_per_piece  # Money in 錢


"""


The value of `a` will be the amount of money in 錢.
"""


"""
Variable 'a' has wrong value. Expected: 675/8, Actual: 675/2"""
