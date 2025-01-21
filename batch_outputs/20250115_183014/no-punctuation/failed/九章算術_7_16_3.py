"""
今有善田一畝價三百惡田七畝價五百今并買一頃價錢一萬問善惡田各幾何
術曰假令善田二十畝惡田八十畝多一千七百一十四錢七分錢之二令之善田一十畝惡田九十畝不足五百七十一錢七分錢之三
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰善田 a畝 惡田 b畝 
"""

"""
Suppose there is good farmland, 1 mu of which is worth 300 qian, and poor farmland, 7 mu of which is worth 500 qian.
Now, if 1 qing of land is purchased for 10,000 qian, how many mu of good and poor farmland are there respectively?

The procedure says: Suppose there are 20 mu of good farmland and 80 mu of poor farmland.
This exceeds the price by 1714 qian and 2/7 of a qian.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland.
This falls short of the price by 571 qian and 3/7 of a qian.

The "Excess and Deficit" procedure says: Place the rates of output (good and poor farmland prices per mu) under their respective excess and deficit.
Multiply the rates of output by their respective excess and deficit, and sum them to form the dividend.
Sum the excess and deficit to form the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a fraction, resolve it.
The excess and deficit correspond to the same type of farmland.
Place the rates of output, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the farmland, and the divisor becomes the total number of mu.

Answer: *a* mu of good farmland, *b* mu of poor farmland.
"""

from fractions import Fraction

# Rates of good and poor farmland
善田價 = 300  # 1 mu of good farmland costs 300 qian
惡田價 = Fraction(500, 7)  # 1 mu of poor farmland costs 500/7 qian

# Total price of 1 qing of land
總價 = 10000

# Excess and deficit
盈 = Fraction(1714, 1) + Fraction(2, 7)  # Excess amount
不足 = Fraction(571, 1) + Fraction(3, 7)  # Deficit amount

# Rates of output for excess and deficit
善田率 = 20  # Hypothetical good farmland in the excess case
惡田率 = 80  # Hypothetical poor farmland in the excess case
善田率不足 = 10  # Hypothetical good farmland in the deficit case
惡田率不足 = 90  # Hypothetical poor farmland in the deficit case

# Calculate the dividend (實)
實 = (善田率 * 善田價 + 惡田率 * 惡田價) * 盈 + (善田率不足 * 善田價 + 惡田率不足 * 惡田價) * 不足

# Calculate the divisor (法)
法 = 盈 + 不足

# Total number of mu of good farmland
善田總數 = Fraction(實, 法)

# Calculate the number of mu of poor farmland
惡田總數 = 100 - 善田總數  # 1 qing = 100 mu

a = 善田總數
b = 惡田總數
"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 78000/7
Variable 'b' has wrong value. Expected: 175/2, Actual: -77300/7"""
