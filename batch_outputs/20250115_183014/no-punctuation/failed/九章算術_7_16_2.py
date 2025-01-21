"""
今有善田一畝價三百惡田七畝價五百今并買一頃價錢一萬問善惡田各幾何
術曰假令善田二十畝惡田八十畝多一千七百一十四錢七分錢之二令之善田一十畝惡田九十畝不足五百七十一錢七分錢之三
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰善田 a畝 惡田 b畝 
"""

"""
Suppose there is good farmland, 1 mu of which is worth 300 qian, and poor farmland, 7 mu of which is worth 500 qian.
Now, if 1 qing of land is purchased for 10,000 qian, how much of it is good farmland and how much is poor farmland?

The procedure says: Suppose there are 20 mu of good farmland and 80 mu of poor farmland. 
This exceeds the price by 1714 qian and 2/7 of a qian.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland. 
This falls short of the price by 571 qian and 3/7 of a qian.

The excess and deficiency procedure says: Place the rates of output (good and poor farmland prices per mu) under their respective excess or deficiency.
Multiply the rates of output by their respective quantities and combine them to form the dividend.
Combine the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the adjustment factor.
If there is a fraction, adjust it accordingly.
The excess and deficiency are then used to adjust the quantities of the purchased land.
Finally, calculate the amount of good and poor farmland.

Answer: *a* mu of good farmland, *b* mu of poor farmland.
"""

from fractions import Fraction

# Prices and areas
善田價 = 300  # 1 mu of good farmland costs 300 qian
惡田價 = Fraction(500, 7)  # 1 mu of poor farmland costs 500/7 qian
總價 = 10000  # Total price for 1 qing (100 mu)

# Assumed areas
假善田1 = 20  # Assume 20 mu of good farmland
假惡田1 = 80  # Assume 80 mu of poor farmland
假善田2 = 10  # Assume 10 mu of good farmland
假惡田2 = 90  # Assume 90 mu of poor farmland

# Calculate total prices for assumed areas
假總價1 = 假善田1 * 善田價 + 假惡田1 * 惡田價
假總價2 = 假善田2 * 善田價 + 假惡田2 * 惡田價

# Calculate excess and deficiency
盈 = 假總價1 - 總價  # Excess: 1714 2/7 qian
不足 = 總價 - 假總價2  # Deficiency: 571 3/7 qian

# Combine excess and deficiency to form the divisor
法 = 盈 + 不足

# Multiply rates of output by their respective quantities and combine to form the dividend
實 = 假善田1 * 不足 + 假善田2 * 盈

# Divide the dividend by the divisor to find the adjustment factor
調整量 = Fraction(實, 法)

# Calculate the actual areas of good and poor farmland
a = 假善田1 - 調整量  # Good farmland
b = 假惡田1 + 調整量  # Poor farmland
"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 15/2
Variable 'b' has wrong value. Expected: 175/2, Actual: 185/2"""
