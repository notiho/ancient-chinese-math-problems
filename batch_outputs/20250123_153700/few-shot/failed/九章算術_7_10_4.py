"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。各長 b尺 。
"""

"""
Suppose a cattail grows 3 chi in one day, and a rush grows 1 chi in one day.
The cattail starts growing from half its length, and the rush starts growing from double its length.
Question: after how many days will their lengths be equal?

The procedure says: Suppose 2 days, the difference is less than 1 chi 5 cun.
Suppose 3 days, the difference is more than 1 chi 7.5 cun.

The procedure for excess and deficiency says: Place the rates of growth under their respective excess and deficiency.
Multiply the rates of growth by the respective excess and deficiency, and sum them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain the number of days.
If there is a fraction, simplify it.
If the excess and deficiency relate to the same object, place the rates of growth, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend is the price of the object, and the divisor is the number of people.

Answer: *a* days. Each grows to *b* chi.
"""

from fractions import Fraction

# Rates of growth
蒲生率 = 3  # Cattail grows 3 chi per day
莞生率 = 1  # Rush grows 1 chi per day

# Initial lengths
蒲初始 = Fraction(1, 2)  # Cattail starts at half its length
莞初始 = 2  # Rush starts at double its length

# Hypothetical scenarios
假令二日 = 2
假令三日 = 3

# Growth after 2 days
蒲二日 = 蒲初始 + 假令二日 * 蒲生率
莞二日 = 莞初始 + 假令二日 * 莞生率
不足 = 蒲二日 - 莞二日  # Difference after 2 days
不足 = abs(不足)  # Absolute value (1 chi 5 cun = 1.5 chi)
不足 = Fraction(3, 2)

# Growth after 3 days
蒲三日 = 蒲初始 + 假令三日 * 蒲生率
莞三日 = 莞初始 + 假令三日 * 莞生率
盈 = 蒲三日 - 莞三日  # Difference after 3 days
盈 = abs(盈)  # Absolute value (1 chi 7.5 cun = 1.75 chi)
盈 = Fraction(7, 4)

# 盈不足術
# Place the rates of growth under their respective excess and deficiency
盈實 = 盈 * 莞生率
不足實 = 不足 * 蒲生率

# Sum the results to obtain the dividend
實 = 盈實 + 不足實

# Sum the excess and deficiency to obtain the divisor
法 = 盈 + 不足

# Divide the dividend by the divisor to obtain the number of days
a = Fraction(實, 法)

# Each grows to the same length after `a` days
b = 蒲初始 + a * 蒲生率  # Length of either plant after `a` days

a日 = a
b尺 = b
"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 25/13
Variable 'b' has wrong value. Expected: 63/13, Actual: 163/26"""
