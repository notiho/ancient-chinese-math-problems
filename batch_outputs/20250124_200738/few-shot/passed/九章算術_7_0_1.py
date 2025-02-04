"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，物價 b 。
"""

#----- content starts here -----
"""
Suppose there is a group of people buying an item together. 
If each person contributes 8, there is an excess of 3. 
If each person contributes 7, there is a shortage of 4. 
Question: What are the number of people and the price of the item?

The procedure for the surplus and deficit says: Place the contribution rates, with the surplus and deficit below each. 
Multiply the contribution rates by their respective surplus or deficit, and add them together to form the dividend. 
Add the surplus and deficit to form the divisor. 
Divide the dividend by the divisor to find the result. 
If there is a fraction, simplify it. 
For those sharing the purchase of the item, place the contribution rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* people, and the price of the item is *b*.
"""

# 人出八，盈三
出率1 = 8
盈 = 3

# 人出七，不足四
出率2 = 7
不足 = 4

# 令維乘所出率，并以為實
實 = (出率1 * 不足) + (出率2 * 盈)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
人數 = Fraction(實, 法)

# 置所出率，以少減多，餘
餘 = 出率1 - 出率2

# 以約法、實
約法 = 法 // 餘
約實 = 實 // 餘

# 實為物價，法為人數
a = 約法  # 人數
b = 約實  # 物價#----- content ends here -----

"""
"""
