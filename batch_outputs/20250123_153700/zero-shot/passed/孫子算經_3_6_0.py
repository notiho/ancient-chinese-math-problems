"""
今有丁九萬八千七百六十六，凡二十五丁出一兵。問：兵幾何？
術曰：置丁九萬八千七百六十六為實，以二十五為法。實如法，即得。
答曰： a人 奇 b 丁。
"""

"""
To solve this problem, we need to calculate how many soldiers ("兵") can be formed from the total number of people ("丁") given that 25 丁 are required to form 1 兵. The remainder 丁 that cannot form a full 兵 will also be calculated.

Here is the Python code to solve the problem:


"""


from fractions import Fraction

# Given data
total_ding = 98766  # Total 丁
ding_per_bing = 25  # 丁 required for 1 兵

# Calculate the number of 兵 and the remainder 丁
a = total_ding // ding_per_bing  # Number of 兵
b = total_ding % ding_per_bing   # Remaining 丁

# Results
# a represents the number of 兵
# b represents the remaining 丁


"""


After running this code:
- `a` will contain the number of 兵 (soldiers).
- `b` will contain the remaining 丁 (people).
"""


"""
"""
