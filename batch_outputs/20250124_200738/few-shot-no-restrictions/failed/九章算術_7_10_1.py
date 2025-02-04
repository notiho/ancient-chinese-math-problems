"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。各長 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a reed (pu) that grows 3 chi in one day and starts at half its length on the first day.
There is also a rush (guan) that grows 1 chi in one day and starts at double its length on the first day.
Question: after how many days will their lengths be equal?

The procedure says: Suppose 2 days, the difference is less than 1 chi 5 cun.
Suppose 3 days, the difference exceeds 1 chi 7.5 cun.

The "Excess and Deficiency" method says: Place the growth rates of each plant, with the excess and deficiency below them.
Multiply the rates by the excess and deficiency, respectively, and add them together to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the number of days. If there is a remainder, simplify it.
For the lengths, substitute the number of days back into the growth formula.

Answer: *a* days. Each grows to *b* chi.
"""

from fractions import Fraction

# Growth rates
蒲日長 = 3  # Pu grows 3 chi per day
莞日長 = 1  # Guan grows 1 chi per day

# Initial conditions
蒲初始 = Fraction(1, 2)  # Pu starts at half its length
莞初始 = 2  # Guan starts at double its length

# Excess and deficiency
不足 = Fraction(1, 2) + 1  # Difference when assuming 2 days (1 chi 5 cun = 1.5 chi)
有餘 = 1 + Fraction(7, 10) + Fraction(1, 20)  # Difference when assuming 3 days (1 chi 7.5 cun = 1.75 chi)

# Rates of growth
所出率蒲 = 3  # Pu's growth rate
所出率莞 = 1  # Guan's growth rate

# Multiply rates by excess and deficiency, then sum
實 = (所出率蒲 * 有餘) + (所出率莞 * 不足)

# Add excess and deficiency
法 = 有餘 + 不足

# Number of days
a = Fraction(實, 法)

# Calculate the length after `a` days
蒲長 = 蒲初始 + a * 蒲日長
莞長 = 莞初始 + a * 莞日長

# Since their lengths are equal:
b = 蒲長  # or 莞長

# Final answer
a_days = a
b_chi = b

a_days, b_chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 27/13
Variable 'b' has wrong value. Expected: 63/13, Actual: 175/26"""
