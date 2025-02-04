"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
荅曰： a日 。各長 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a cattail (蒲) that grows 3 chi per day, starting at half its length on the first day.
There is also a rush (莞) that grows 1 chi per day, starting at double its length on the first day.
Question: after how many days will their lengths be equal?

Answer: it takes *a* days, and they will each be *b* chi long.
"""

from fractions import Fraction

# Growth rates and initial lengths
蒲每日增長 = 3  # chi per day
莞每日增長 = 1  # chi per day

蒲初始長度 = Fraction(1, 2)  # half its length
莞初始長度 = 2  # double its length

# Let the number of days be x
# Length of 蒲 after x days: 蒲初始長度 + 蒲每日增長 * x
# Length of 莞 after x days: 莞初始長度 + 莞每日增長 * x
# Solve for when their lengths are equal:
# 蒲初始長度 + 蒲每日增長 * x = 莞初始長度 + 莞每日增長 * x

# Rearrange to solve for x:
# x = (莞初始長度 - 蒲初始長度) / (蒲每日增長 - 莞每日增長)
a = (莞初始長度 - 蒲初始長度) / (蒲每日增長 - 莞每日增長)

# Calculate the length when they are equal
b = 蒲初始長度 + 蒲每日增長 * a

# Results
a = Fraction(a)  # Number of days
b = Fraction(b)  # Length in chi

a, b  # Output the results#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 3/4
Variable 'b' has wrong value. Expected: 63/13, Actual: 11/4"""
