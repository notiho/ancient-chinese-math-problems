"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
荅曰： a日 。各長 b尺 。
"""

"""
Suppose there is a plant called Pu that grows 3 chi per day, starting at half its length on the first day.
Another plant called Guan grows 1 chi per day, starting at double its length on the first day.
Question: after how many days will they be of equal length, and what will that length be?

Answer: after *a* days, they will each be *b* chi long.
"""

from fractions import Fraction

# Initial lengths
蒲初始長度 = Fraction(1, 2)  # Pu starts at half its length
莞初始長度 = 2               # Guan starts at double its length

# Growth rates
蒲每日增長 = 3  # Pu grows 3 chi per day
莞每日增長 = 1  # Guan grows 1 chi per day

# Let the number of days be "a"
# The length of Pu after "a" days: 蒲初始長度 + a * 蒲每日增長
# The length of Guan after "a" days: 莞初始長度 + a * 莞每日增長
# Solve for when the lengths are equal:
# 蒲初始長度 + a * 蒲每日增長 = 莞初始長度 + a * 莞每日增長

a = (莞初始長度 - 蒲初始長度) / (蒲每日增長 - 莞每日增長)

# Calculate the length when they are equal
b = 蒲初始長度 + a * 蒲每日增長

# Results
a = Fraction(a)  # Number of days
b = Fraction(b)  # Length in chi

a, b  # Output the results
"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 3/4
Variable 'b' has wrong value. Expected: 63/13, Actual: 11/4"""
