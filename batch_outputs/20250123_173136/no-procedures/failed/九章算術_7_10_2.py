"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
荅曰： a日 。各長 b尺 。
"""

"""
Suppose there is a cattail (蒲) that grows 3 chi per day and starts at half its length on the first day.
There is also a rush (莞) that grows 1 chi per day and starts at double its length on the first day.
Question: after how many days will their lengths be equal?

Answer: it takes *a* days, and each will be *b* chi long.
"""

from fractions import Fraction

# Growth rates and initial lengths
蒲_growth = 3  # chi per day
莞_growth = 1  # chi per day
蒲_initial = Fraction(1, 2)  # half its length on the first day
莞_initial = 2  # double its length on the first day

# Let the number of days be x, and solve for when their lengths are equal:
# 蒲_initial + 蒲_growth * x = 莞_initial + 莞_growth * x

# Rearrange to solve for x:
# x = (莞_initial - 蒲_initial) / (蒲_growth - 莞_growth)
a = (莞_initial - 蒲_initial) / (蒲_growth - 莞_growth)

# Calculate the length at this time:
b = 蒲_initial + 蒲_growth * a

# Results
a, b  # a is the number of days, b is the length in chi
"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 3/4
Variable 'b' has wrong value. Expected: 63/13, Actual: 11/4"""
