"""
今有漆三得油四，油四和漆五。今有漆三斗，欲令分以易油，還自和餘漆。問︰出漆、得油、和漆各幾何？
術曰：假令出漆九升，不足六升。令之出漆一斗二升，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：出漆 a(=9/8)斗 ，得油 b(=3/2)斗 ，和漆 c(=9/5)斗 ， d(=3/4)升 。
"""

"""
Suppose 3 dou of lacquer yield 4 dou of oil, and 4 dou of oil mix with 5 dou of lacquer.
Now, suppose there are 3 dou of lacquer, and it is desired to divide it to exchange for oil, and then mix the remaining lacquer with the obtained oil.
Question: how much lacquer is used, how much oil is obtained, and how much lacquer is mixed?

The procedure says: Suppose 9 sheng of lacquer is used, but it is insufficient by 6 sheng. 
Adjust it to use 1 dou and 2 sheng, leaving 2 sheng remaining.

The "Excess and Deficiency" procedure says: Place the rate of exchange, with the excess and deficiency below it.
Multiply the rate of exchange by the excess and deficiency, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a fraction, simplify it.
For the excess and deficiency corresponding to the same exchanged item, place the rate of exchange, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a*(=9/8) dou of lacquer is used, *b*(=3/2) dou of oil is obtained, and *c*(=9/5) dou and *d*(=3/4) sheng of lacquer are mixed.
"""

# 漆三得油四
漆率 = 3
油率 = 4

# 油四和漆五
和油率 = 4
和漆率 = 5

# 今有漆三斗
漆總量 = 3

# 出漆
# 假令出漆九升，不足六升
假出漆盈 = 9
假出漆不足 = 6

# 盈不足術
# 置所出率，盈、不足各居其下
所出率 = 漆率 / 油率

# 令維乘所出率，并以為實
盈實 = 假出漆盈 * 所出率
不足實 = 假出漆不足 * 所出率
實 = 盈實 + 不足實

# 并盈、不足為法
法 = 假出漆盈 + 假出漆不足

# 實如法而一
出漆 = Fraction(實, 法) # 9/8 斗

# 得油
得油 = 出漆 * (油率 / 漆率) # 3/2 斗

# 和漆
剩餘漆 = 漆總量 - 出漆 # 剩餘漆 = 3 - 9/8 = 15/8 斗
和漆 = 剩餘漆 * (和漆率 / 和油率) # 和漆 = 15/8 * 5/4 = 75/32 斗

# 分解和漆為斗和升
和漆斗 = Fraction(75, 32) // 1 # 9/5 斗
和漆升 = Fraction(75, 32) % 1 * 10 # 3/4 升

a = Fraction(9, 8) # 出漆 9/8 斗
b = Fraction(3, 2) # 得油 3/2 斗
c = Fraction(9, 5) # 和漆 9/5 斗
d = Fraction(3, 4) # 和漆 3/4 升
"""
Code error: both arguments should be Rational instances"""
