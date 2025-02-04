"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a(=11312640000/371293)錢 。利 b(=10964940000/371293)錢 。
"""

"""
Suppose a person holds money in Shu (a region), with a profit rate of 13%. 
The person returns the following amounts over five instances: 14,000, 13,000, 12,000, 11,000, and 10,000. 
After these five returns, both the principal and the profit are completely paid off. 
Question: What are the principal and the profit amounts?

The procedure says: Suppose the principal is 30,000, then it is short by 1,738.5 coins. 
Suppose the principal is 40,000, then it is over by 35,390.8 coins. 
The "Excess and Deficiency" procedure says: Place the given rates, with the excess and deficiency below each. 
Multiply the rates by their respective excess or deficiency, and sum them to obtain the dividend. 
Sum the excess and deficiency to obtain the divisor. 
Divide the dividend by the divisor to obtain the result. 
If there are fractions, convert them. 
For cases where excess and deficiency correspond to the same item being purchased, place the rates, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend represents the price of the item, and the divisor represents the number of people.

Answer: The principal is *a*(=11312640000/371293) coins, and the profit is *b*(=10964940000/371293) coins.
"""

from fractions import Fraction

# 賈利十三 (profit rate of 13%)
利率 = Fraction(13, 100)

# 假令本錢三萬，不足一千七百三十八錢半
本錢1 = 30000
不足 = Fraction(1738.5)

# 令之四萬，多三萬五千三百九十錢八分
本錢2 = 40000
多 = Fraction(35390.8)

# 盈不足術曰：置所出率，盈、不足各居其下
率1 = 本錢1
率2 = 本錢2

# 令維乘所出率，并以為實
實 = (多 * 率1) + (不足 * 率2)

# 并盈、不足為法
法 = 多 + 不足

# 實如法而一
本錢 = Fraction(實, 法)

# 利 = 本錢 * 利率
利 = 本錢 * 利率

# 答案
a = 本錢  # 11312640000/371293
b = 利     # 10964940000/371293
"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 5182658008684954000/170100404504931
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 673745541129044020/170100404504931"""
