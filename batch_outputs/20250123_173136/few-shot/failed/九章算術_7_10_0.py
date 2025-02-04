"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。各長 b尺 。
"""

"""
Suppose there is a cattail (pu) that grows 3 chi in one day, and a rush (guan) that grows 1 chi in one day.
The cattail starts growing from half its length, and the rush starts growing from double its length.
Question: after how many days will their lengths be equal?

The procedure says: Suppose 2 days, the difference is less than 1 chi 5 cun. Suppose 3 days, the difference exceeds 1 chi 7.5 cun.
The method of excess and deficiency says: Place the growth rates, with the excess and deficiency below each.
Multiply the growth rates by their respective excess or deficiency, and add them to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the number of days. If there is a remainder, convert it to the same unit.
If the excess and deficiency relate to the same object, place the growth rates, subtract the smaller from the larger, and simplify the dividend and divisor.
The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: *a* days. Each grows to *b* chi.
"""

from fractions import Fraction

# Growth rates
蒲率 = 3  # Cattail grows 3 chi per day
莞率 = 1  # Rush grows 1 chi per day

# Initial lengths
蒲初長 = Fraction(1, 2)  # Cattail starts at half its length
莞初長 = 2  # Rush starts at double its length

# Excess and deficiency
盈 = Fraction(1, 2) + Fraction(7, 10)  # 1 chi 7.5 cun = 1.75 chi
不足 = Fraction(1, 2) + Fraction(5, 10)  # 1 chi 5 cun = 1.5 chi

# Multiply growth rates by excess and deficiency
實 = (蒲率 * 盈) + (莞率 *不足)


"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
