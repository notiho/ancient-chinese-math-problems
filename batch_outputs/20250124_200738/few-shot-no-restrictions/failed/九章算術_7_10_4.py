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

The procedure says: Suppose 2 days, it is short by 1 chi 5 cun. Suppose 3 days, it exceeds by 1 chi 7 cun and a half.

The "Excess and Deficiency" procedure says: Place the growth rates under the respective excess and deficiency. Multiply the rates by the respective excess or deficiency, and sum them to obtain the dividend. Sum the excess and deficiency to obtain the divisor. Divide the dividend by the divisor to find the solution. If there is a remainder, simplify it. If the excess and deficiency relate to the same object, place the rates, subtract the smaller from the larger, and simplify the dividend and divisor. The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: *a* days. Each grows to *b* chi.
"""

from fractions import Fraction

# Growth rates
蒲每日增長 = 3  # chi/day
莞每日增長 = 1  # chi/day

# Initial lengths
蒲初始長度 = Fraction(1, 2)  # chi
莞初始長度 = 2  # chi

# Excess and deficiency
假設_2日_不足 = Fraction(1, 2) + 1  # 1 chi 5 cun = 1.5 chi
假設_3日_有餘 = 1 + Fraction(7, 10)  # 1 chi 7.5 cun = 1.75 chi

# 盈不足術
# Rates for excess and deficiency
盈率 = 3  # chi/day (蒲)
不足率 = 1  # chi/day (莞)

# Dividend (實)
實 = (盈率 * 假設_3日_有餘) + (不足率 * 假設_2日_不足)

# Divisor (法)
法 = 假設_3日_有餘 + 假設_2日_不足

# Days until lengths are equal
a = 實 / 法

# Lengths after a days
b = (蒲每日增長 * a) + 蒲初始長度

# Answer
a_days = a
b_chi = b

a_days, b_chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 32/13, Actual: 33/16
Variable 'b' has wrong value. Expected: 63/13, Actual: 107/16"""
