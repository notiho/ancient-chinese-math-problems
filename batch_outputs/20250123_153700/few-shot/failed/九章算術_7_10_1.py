"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。各長 b尺 。
"""

"""
Suppose there is a cattail (pu) that grows 3 chi in one day, and a rush (guan) that grows 1 chi in one day.
The cattail starts growing at half its length, and the rush starts growing at double its length.
Question: after how many days will their lengths be equal?

The procedure says: Suppose for 2 days, the difference is less than 1 chi 5 cun.
Suppose for 3 days, the difference exceeds 1 chi 7.5 cun.

The "Excess and Deficiency" procedure says: Place the rates of growth, with the excess and deficiency below each.
Multiply the rates of growth by the respective excess and deficiency, and add them to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the result.
If there is a remainder, simplify it.
If the excess and deficiency are related to the same object, place the rates of growth, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: *a* days. Each grows to *b* chi.
"""

from fractions import Fraction

# Rates of growth per day
蒲生率 = 3  # Cattail grows 3 chi per day
莞生率 = 1  # Rush grows 1 chi per day

# Initial conditions
蒲初始 = Fraction(1, 2)  # Cattail starts at half its length
莞初始 = 2  # Rush starts at double its length

# Differences after 2 days and 3 days
不足 = Fraction(3 * 2 - 1 * 2 - (1.5), 1)  # Difference after 2 days (不足: less by 1 chi 5 cun = 1.5 chi)
盈 = Fraction(1 * 3 - 3 * 3 - (1.75), 1)
"""
Code error: both arguments should be Rational instances"""
