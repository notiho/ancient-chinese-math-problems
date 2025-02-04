"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
術曰：以一匹尺數為法，今有布尺數乘價錢為實，實如法得錢數。
荅曰： a錢 。
"""

"""
To solve this problem, we will calculate the value of 2丈7尺 of cloth when 1匹 of cloth is worth 125錢. In ancient Chinese measurements, 1匹 of cloth is typically 40丈. We will use this information to compute the value.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
匹價值 = 125  # 1匹 is worth 125錢
匹尺數 = 40  # 1匹 is 40丈
布尺數 = 2 * 10 + 7  # 2丈7尺 converted to 尺 (1丈 = 10尺)

# Calculation
a = Fraction(布尺數, 匹尺數) * 匹價值  # (布尺數 / 匹尺數) * 匹價值

# Result
a  # The value in 錢
#----- content ends here -----


"""


The variable `a` will contain the value of the cloth in 錢 as a fraction.
"""


"""
"""
