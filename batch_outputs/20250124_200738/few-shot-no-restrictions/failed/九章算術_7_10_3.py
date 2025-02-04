"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。各長 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a cattail (蒲) that grows 3 chi per day and a rush (莞) that grows 1 chi per day.
The cattail starts at half its length, and the rush starts at double its length.
Question: after how many days will their lengths be equal?

The procedure says: Suppose 2 days, the difference is less than 1 chi 5 cun.
Suppose 3 days, the difference exceeds 1 chi 7 cun and a half.

The method of "excess and deficiency" says: Place the growth rates, with the excess and deficiency below each.
Multiply the assumed days by their respective growth rates, and combine them as the dividend.
Combine the excess and deficiency as the divisor.
Divide the dividend by the divisor to find the number of days.
If there is a remainder, simplify it.
For the excess and deficiency to match the same unit, adjust the growth rates accordingly.
Subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: *a* days. Each grows to *b* chi.
"""

from fractions import Fraction

# Growth rates per day
蒲生率 = 3  # chi/day
莞生率 = 1  # chi/day

# Initial lengths
蒲初始 = Fraction(1, 2)  # chi
莞初始 = 2  # chi

# Assumptions
假令_2日 = 2
假令_3日 = 3

# Lengths after 2 days
蒲長_2日 = 蒲初始 + 假令_2日 * 蒲生率
莞長_2日 = 莞初始 + 假令_2日 * 莞生率
不足 = (莞長_2日 - 蒲長_2日)  # Difference after 2 days

# Lengths after 3 days
蒲長_3日 = 蒲初始 + 假令_3日 * 蒲生率
莞長_3日 = 莞初始 + 假令_3日 * 莞生率
有餘 = (蒲長_3日 - 莞長_3日)  # Difference after 3 days

# 盈不足術
# Combine the rates and differences
實 = (假令_2日 * 有餘) + (假令_3日 * 不足)
法 = 有餘 + 不足

# Calculate the number of days
a = Fraction(實, 法)

# Calculate the length after `a` days
蒲長 = 蒲初始 + a * 蒲生率
莞長 = 莞初始 + a * 莞生率
b = 蒲長  # or 莞長, since they are equal at this point

# Output results
a日 = a
b尺 = b

a日, b尺#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 3/4
Variable 'b' has wrong value. Expected: 63/13, Actual: 11/4"""
