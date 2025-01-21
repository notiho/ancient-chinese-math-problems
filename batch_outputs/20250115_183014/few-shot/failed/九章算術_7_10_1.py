"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a日 。各長 b尺 。
"""

"""
Suppose a cattail grows 3 chi in one day, and a rush grows 1 chi in one day.
The cattail starts at half its length, and the rush starts at double its length.
Question: after how many days will their lengths be equal?

The procedure says: Suppose 2 days, the difference is less than 1 chi 5 cun. 
Suppose 3 days, the difference exceeds 1 chi 7.5 cun.

The method of excess and deficiency says: Place the rates of growth, with the excess and deficiency below each. 
Multiply the rates of growth by the respective excess and deficiency, and sum them to obtain the dividend. 
Sum the excess and deficiency to obtain the divisor. 
Divide the dividend by the divisor to find the number of days. 
If there is a remainder, simplify it. 
For problems involving the same goods, place the rates of growth, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend is the price of the goods, and the divisor is the number of people.

Answer: *a* days. Each grows to *b* chi.
"""

from fractions import Fraction

# Rates of growth per day
蒲日長 = 3  # Cattail grows 3 chi per day
莞日長 = 1  # Rush grows 1 chi per day

# Initial lengths
蒲初長 = Fraction(1, 2)  # Cattail starts at half its length
莞初長 = 2  # Rush starts at double its length

# 盈不足 setup
盈 = Fraction(1, 2) + 3 * 3 - (2 + 1 * 3) #盈
"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
