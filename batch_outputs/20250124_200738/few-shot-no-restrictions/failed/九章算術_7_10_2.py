"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。各長 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a cattail (蒲) that grows 3 chi per day, and a rush (莞) that grows 1 chi per day.
The cattail starts at half its length, while the rush starts at double its length.
Question: after how many days will their lengths be equal?

The procedure says: Suppose 2 days, the difference is less than 1 chi 5 cun.
Suppose 3 days, the difference is more than 1 chi 7.5 cun.

The "excess and deficiency" method says: Place the growth rates, with the excess and deficiency below each.
Multiply the growth rates by the respective excess and deficiency, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the number of days.
If there is a remainder, simplify it.
If the excess and deficiency are related to the same object, place the growth rates, subtract the smaller from the larger, and simplify the dividend and divisor.
The dividend is the price of the object, and the divisor is the number of people.

Answer: *a* days. Each grows to *b* chi.
"""

from fractions import Fraction

# Growth rates
蒲日長 = 3  # chi/day
莞日長 = 1  # chi/day

# Initial lengths
蒲初長 = Fraction(1, 2)  # chi
莞初長 = 2  # chi

# Excess and deficiency
# After 2 days
蒲長_2日 = 蒲初長 + 2 * 蒲日長
莞長_2日 = 莞初長 + 2 * 莞日長
不足 = (莞長_2日 - 蒲長_2日)  # Difference is less than 1 chi 5 cun
不足 = Fraction(15, 10)  # Convert 1 chi 5 cun to chi

# After 3 days
蒲長_3日 = 蒲初長 + 3 * 蒲日長
莞長_3日 = 莞初長 + 3 * 莞日長
盈 = (蒲長_3日 - 莞長_3日)  # Difference is more than 1 chi 7.5 cun
盈 = Fraction(17.5, 10)  # Convert 1 chi 7.5 cun to chi

# "Excess and deficiency" method
# Place growth rates
所出率_蒲 = 蒲日長
所出率_莞 = 莞日長

# Multiply rates by excess and deficiency
實 = (所出率_蒲 * 盈) + (所出率_莞 * 不足)

# Sum excess and deficiency
法 = 盈 + 不足

# Divide to find days
a = 實 / 法

# Each grows to the same length
b = 蒲初長 + a * 蒲日長

# Final answer
a_days = a
b_chi = b

a_days, b_chi#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
