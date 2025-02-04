"""
今有蒲生一日，長三尺。莞生一日，長一尺。蒲生日自半。莞生日自倍。問︰幾何日而長等？
術曰：假令二日，不足一尺五寸。令之三日，有餘一尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。各長 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a cattail (pu) that grows 3 chi per day and a rush (guan) that grows 1 chi per day.
The cattail starts at half its length, and the rush starts at double its length.
Question: after how many days will they be of equal length?

The procedure says: Suppose after 2 days, the difference is less than 1 chi 5 cun. 
Suppose after 3 days, the difference is more than 1 chi 7.5 cun.

The method of excess and deficiency says: Place the rates of growth, with the excess and deficiency below them. 
Multiply the rates of growth by the excess and deficiency, respectively, and add them to form the dividend. 
Add the excess and deficiency to form the divisor. 
Divide the dividend by the divisor to find the number of days. 
If there is a remainder, convert it into the same unit. 
If the excess and deficiency are related to the same object, place the rates of growth, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: *a* days. Each grows to *b* chi.
"""

from fractions import Fraction

# Rates of growth
蒲日長 = 3  # chi/day
莞日長 = 1  # chi/day

# Initial lengths
蒲初始長 = Fraction(1, 2)  # chi
莞初始長 = 2  # chi

# Excess and deficiency
# After 2 days
日1 = 2
蒲長1 = 蒲初始長 + 日1 * 蒲日長
莞長1 = 莞初始長 + 日1 * 莞日長
不足 = Fraction(3, 2)  # 1 chi 5 cun = 1.5 chi

# After 3 days
日2 = 3
蒲長2 = 蒲初始長 + 日2 * 蒓日長
莞長2 = 莞初始長 + 日2 * 莞日長#----- content ends here -----

"""
Code error: name '蒓日長' is not defined"""
