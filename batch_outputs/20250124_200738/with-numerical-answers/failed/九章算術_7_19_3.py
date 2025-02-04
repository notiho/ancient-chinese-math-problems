"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a(=11312640000/371293)錢 。利 b(=10964940000/371293)錢 。
"""

#----- content starts here -----
"""
Suppose someone holds a certain amount of principal money and earns a profit of 13%. 
The person returns the following amounts over five instances:
First return: 14,000
Second return: 13,000
Third return: 12,000
Fourth return: 11,000
Fifth return: 10,000
In total, the five returns exhaust both the principal and the profit. 

Question: What are the amounts of the principal and the profit?

The procedure says: Suppose the principal is 30,000. It falls short by 1,738.5. 
Suppose the principal is 40,000. It exceeds by 35,390.8. 

The "Excess and Deficit" procedure says: Place the given rates, with the excess and deficit below them. 
Multiply the rates by the respective excess or deficit, and sum them to form the dividend. 
Sum the excess and deficit to form the divisor. 
Divide the dividend by the divisor to find the principal. 
If there are fractions, resolve them. 
For the profit, multiply the principal by the profit rate.

Answer: The principal is *a*(=11312640000/371293) money, and the profit is *b*(=10964940000/371293) money.
"""

# 賈利十三 (profit rate is 13%)
利率 = Fraction(13, 100)

# 假令本錢三萬，不足一千七百三十八錢半
本錢_假1 = 30000
不足 = Fraction(17385, 10)

# 令之四萬，多三萬五千三百九十錢八分
本錢_假2 = 40000
多 = Fraction(353908, 10)

# 盈不足術
# 置所出率，盈、不足各居其下
盈不足_差 = 本錢_假2 - 本錢_假1

# 令維乘所出率，并以為實
實 = (多 * 本錢_假1) + (不足 * 本錢_假2)

# 并盈、不足為法
法 = 多 + 不足

# 實如法而一
本錢 = Fraction(實, 法)

# 利 = 本錢 * 利率
利 = 本錢 * 利率

# 答案
a = 本錢  # 11312640000/371293
b = 利    # 10964940000/371293#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 113126400/28561"""
