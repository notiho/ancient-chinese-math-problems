"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
術曰：以一匹尺數為法，今有布尺數乘價錢為實，實如法得錢數。
荅曰： a錢 。
"""

"""
To solve this problem, we need to calculate the value of 2丈7尺 of cloth when 1匹 (a bolt of cloth) is worth 125錢. In ancient Chinese measurements, 1匹 of cloth typically equals 40丈. We'll use this information to compute the value.

Here's the Python code:


"""


from fractions import Fraction

# Known values
price_per_bolt = 125  # 1匹 = 125錢
length_per_bolt = 40  # 1匹 = 40丈
length_given = 2 * 10 + 7  # 2丈7尺 = 2丈 * 10尺/丈 + 7尺

# Calculation
a = Fraction(length_given, length_per_bolt) * price_per_bolt  # 得錢數

# Result
a  # a錢


"""


The variable `a` will contain the value of the cloth in 錢.
"""


"""
"""
