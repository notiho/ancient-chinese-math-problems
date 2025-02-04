"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，璡價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a jade (璡). 
If each person contributes half of the price, there is an excess of 4. 
If each person contributes less than half of the price, there is a shortfall of 3. 
Question: what are the number of people and the price of the jade?

The procedure for surplus and deficit says: 
Place the contribution rates, with the surplus and deficit below them respectively. 
Multiply the contribution rates by their respective surplus or deficit, and add them to form the dividend. 
Add the surplus and deficit to form the divisor. 
Divide the dividend by the divisor to obtain 1 unit. 
If there is a fraction, simplify it. 
For cases where the surplus and deficit are related to the same purchased item, 
place the contribution rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* people, jade price *b*.
"""

# 盈、不足各居其下
盈 = 4
不足 = 3

# 所出率
多出率 = Fraction(1, 2)  # 人出半
少出率 = Fraction(1, 2) - Fraction(1, 2)  # 人出少半

# 令維乘所出率，并以為實
實 = (多出率 * 不足) + (少出率 * 盈)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
一 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實
餘 = 多出率 - 少出率
法 = 法 // 餘
實 = 實 // 餘

# 實為物價，法為人數
b = 實
a = 法#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 42, Actual: 14
Variable 'b' has wrong value. Expected: 17, Actual: 3"""
