"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
術曰：以一匹尺數為法，今有布尺數乘價錢為實，實如法得錢數。
荅曰： a錢 。
"""

"""
To solve this problem, we will calculate the value of 2丈7尺 of cloth based on the price of 1匹 of cloth. First, we need to convert the given lengths into the same unit (尺), then compute the price proportionally.

1匹 of cloth is equivalent to 10丈 (since 1匹 = 10丈 = 100尺). The price of 1匹 is 125錢. The given length is 2丈7尺, which is equivalent to \( 2 \times 10 + 7 = 27 \) 尺.

We calculate the price proportionally as follows:


"""


from fractions import Fraction

# Known values
price_per匹 = 125  # 錢
length_per匹 = 10 * 10  # 尺 (1匹 = 10丈 = 100尺)
length_given = 2 * 10 + 7  # 尺 (2丈7尺)

# Calculate the price for the given length
a = Fraction(length_given, length_per匹) * price_per匹

# Output the result
a  # 錢


"""


The variable `a` will contain the price in 錢 for 2丈7尺 of cloth.
"""


"""
Variable 'a' has wrong value. Expected: 675/8, Actual: 135/4"""
