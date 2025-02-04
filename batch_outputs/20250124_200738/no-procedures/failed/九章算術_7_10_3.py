"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
荅曰： a日 。各長 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a cattail (蒲) that grows 3 chi per day, starting at half its length on the first day.
There is also a rush (莞) that grows 1 chi per day, starting at double its length on the first day.
Question: after how many days will their lengths be equal, and what will their lengths be?

Answer: after *a* days, both will be *b* chi long.
"""

from fractions import Fraction

# Growth rates and initial lengths
蒲_growth = 3  # chi per day
莞_growth = 1  # chi per day
蒲_initial = Fraction(1, 2)  # starts at half its length
莞_initial = 2  # starts at double its length

# Let the number of days be "a"
# Length of 蒲 after "a" days: 蒲_initial + 蒲_growth * a
# Length of 莞 after "a" days: 莞_initial + 莞_growth * a
# Solve for equality: 蒲_initial + 蒲_growth * a = 莞_initial + 莞_growth * a

a = (莞_initial - 蒲_initial) / (蒲_growth - 莞_growth)

# Calculate the length when they are equal
b = 蒲_initial + 蒲_growth * a

a, b  # Output the number of days and the length in chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 3/4
Variable 'b' has wrong value. Expected: 63/13, Actual: 11/4"""
