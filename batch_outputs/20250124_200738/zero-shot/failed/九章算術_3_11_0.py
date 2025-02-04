"""
今有縑一丈價直一百二十八。今有縑一匹九尺五寸，問︰得錢幾何？
術曰：以一丈寸數為法，以價錢數乘今有縑寸數為實，實如法得錢數。
荅曰： a錢 。
"""

"""
To solve this problem, we need to calculate the value of a piece of silk that is 9 feet 5 inches long, given that 1丈 (10 feet) of silk costs 128錢. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Known values
price_per_zhang = 128  # 1丈 = 128錢
length_of_zhang = 10  # 1丈 = 10尺
length_of_silk = 9 + Fraction(5, 10)  # 9尺5寸 = 9 + 5/10 尺

# Calculation
a = Fraction(price_per_zhang) * length_of_silk / length_of_zhang

# Result
a  # The value in 錢
#----- content ends here -----


"""


The variable `a` will contain the value of the silk in 錢.
"""


"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 608/5"""
