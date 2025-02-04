"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
荅曰： a日 。各長 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a cattail (蒲) that grows 3 chi per day and starts at half its length on the first day.
There is also a rush (莞) that grows 1 chi per day and starts at double its length on the first day.
Question: after how many days will their lengths be equal?

Answer: it takes *a* days, and they will both be *b* chi long.
"""

from fractions import Fraction

# Growth rates and initial lengths
蒲_每日增長 = 3  # chi/day
莞_每日增長 = 1  # chi/day

蒲_初始長度 = Fraction(1, 2)  # half its length
莞_初始長度 = 2  # double its length

# Let the number of days be "a"
# Length of 蒲 after "a" days: 蒲_初始長度 + 蒲_每日增長 * a
# Length of 莞 after "a" days: 莞_初始長度 + 莞_每日增長 * a
# Solve for equality:
# 蒲_初始長度 + 蒲_每日增長 * a = 莞_初始長度 + 莞_每日增長 * a

a = (莞_初始長度 - 蒲_初始長度) / (蒲_每日增長 - 莞_每日增長)

# Calculate the length when they are equal
b = 蒲_初始長度 + 蒲_每日增長 * a

# Results
a = Fraction(a)
b = Fraction(b)

a, b  # Output the number of days and the length in chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 3/4
Variable 'b' has wrong value. Expected: 63/13, Actual: 11/4"""
