"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a(=11312640000/371293)錢 。利 b(=10964940000/371293)錢 。
"""

"""
Suppose someone holds money in Shu (a region) and earns a profit of 13%. 
The first return is 14,000, the second return is 13,000, the third return is 12,000, the fourth return is 11,000, and the final return is 10,000. 
In total, there are five returns, and the principal and profit are fully exhausted.
Question: how much was the principal and how much was the profit?

The procedure says: Suppose the principal is 30,000; it falls short by 1,738.5. 
Suppose it is 40,000; it exceeds by 35,390.8. 
The "excess and deficiency" procedure says: Place the given rates, with the excess and deficiency below them. 
Multiply the rates by their respective excess or deficiency, and add them to form the dividend. 
Add the excess and deficiency to form the divisor. 
Divide the dividend by the divisor to find the principal. 
If there are fractions, simplify them. 
The excess and deficiency correspond to the same object being purchased. 
Place the rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: The principal is *a*(=11312640000/371293) qian, and the profit is *b*(=10964940000/371293) qian.
"""

from fractions import Fraction

# 賈利十三 (profit rate is 13%)
利率 = Fraction(13, 100)

# 假令本錢三萬，不足一千七百三十八錢半
本錢1 = 30000
不足 = Fraction(17385, 10)

# 令之四萬，多三萬五千三百九十錢八分
本錢2 = 40000
多 = Fraction(353908, 10)

# 盈不足術曰：置所出率，盈、不足各居其下
# Multiply rates by their respective excess or deficiency
實 = (本錢1 * 多) + (本錢2 * 不足)

# Add the excess and deficiency to form the divisor
法 = 多 + 不足

# Divide the dividend by the divisor to find the principal
本錢 = Fraction(實, 法)

# 利 = 本錢 * 利率
利 = 本錢 * 利率

# Final results
a = 本錢  # Principal
b = 利     # Profit
"""
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 113126400/28561"""
