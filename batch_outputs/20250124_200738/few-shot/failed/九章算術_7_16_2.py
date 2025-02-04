"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：善田 a畝 ，惡田 b畝 。
"""

#----- content starts here -----
"""
Suppose there is good farmland, 1 mu, priced at 300 qian, and poor farmland, 7 mu, priced at 500 qian.
Now, a total of 1 qing (100 mu) is purchased for 10,000 qian.
Question: how many mu of good farmland and poor farmland are purchased respectively?

The procedure says: Suppose 20 mu of good farmland and 80 mu of poor farmland are chosen. This exceeds the price by 1714 qian and 2/7 qian.
Suppose 10 mu of good farmland and 90 mu of poor farmland are chosen. This falls short of the price by 571 qian and 3/7 qian.

The method of excess and deficiency says: Place the rates of the outcomes (excess and deficiency) under their respective assumptions.
Multiply the rates by the corresponding assumptions and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the result. If there are fractions, handle them accordingly.
For the farmland quantities, subtract the smaller assumption from the larger one, and simplify the divisor and dividend accordingly.
The dividend represents the price of the farmland, and the divisor represents the total number of mu.

Answer: *a* mu of good farmland, and *b* mu of poor farmland.
"""

from fractions import Fraction

# Prices and areas
善田價 = 300  # Price per mu of good farmland
惡田價 = Fraction(500, 7)  # Price per mu of poor farmland (500 qian for 7 mu)
總價 = 10000  # Total price in qian
總畝 = 100  # Total area in mu

# Assumptions
假設1_善田 = 20  # Assumption 1: 20 mu of good farmland
假設1_惡田 = 80  # Assumption 1: 80 mu of poor farmland
假設1_盈 = Fraction(1714, 7) + Fraction(2, 7)  # Excess amount for assumption 1

假設2_善田 = 10  # Assumption 2: 10 mu of good farmland
假設2_惡田 = 90  # Assumption 2: 90 mu of poor farmland
假設2_不足 = Fraction(571, 7) + Fraction(3, 7)  # Deficiency amount for assumption 2

# 盈不足術 calculations
# Place the rates (excess and deficiency) under their respective assumptions
盈率 = 假設1_盈
不足率 = 假設2_不足

# Multiply the rates by the corresponding assumptions and sum them to form the dividend
實 = (假設1_善田 * 不足率) + (假設2_善田 * 盈率)

# Sum the excess and deficiency to form the divisor
法 = 盈率 + 不足率

# Divide the dividend by the divisor to find the result for good farmland
善田 = Fraction(實, 法)

# Calculate the remaining area for poor farmland
惡田 = 總畝 - 善田

# Assign results
a = 善田
b = 惡田#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 2864/229
Variable 'b' has wrong value. Expected: 175/2, Actual: 20036/229"""
