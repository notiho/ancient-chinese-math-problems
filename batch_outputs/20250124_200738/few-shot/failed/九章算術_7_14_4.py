"""
今有漆三得油四，油四和漆五。今有漆三斗，欲令分以易油，還自和餘漆。問︰出漆、得油、和漆各幾何？
術曰：假令出漆九升，不足六升。令之出漆一斗二升，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：出漆 a斗 ，得油 b斗 ，和漆 c斗 ， d升 。
"""

#----- content starts here -----
"""
Suppose 3 dou of lacquer yields 4 dou of oil, and 4 dou of oil mixes with 5 dou of lacquer.
Now, there are 3 dou of lacquer, and it is desired to exchange lacquer for oil, and then mix the remaining lacquer with the obtained oil.
Question: how much lacquer is exchanged, how much oil is obtained, and how much lacquer remains mixed with the oil?

The procedure says: Suppose 9 sheng of lacquer is exchanged, but it is insufficient by 6 sheng. 
Let it be 1 dou and 2 sheng of lacquer exchanged, with 2 sheng remaining.
The procedure for surplus and deficiency says: Place the exchange rate, with surplus and deficiency below it.
Multiply the exchange rate by the surplus and deficiency, and add them to form the dividend.
Add the surplus and deficiency to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
For surplus and deficiency cases involving the same traded item, place the exchange rate, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* dou of lacquer is exchanged, *b* dou of oil is obtained, and *c* dou and *d* sheng of lacquer remain mixed with the oil.
"""

from fractions import Fraction

# 漆三得油四
漆得油率 = Fraction(4, 3)

# 油四和漆五
油和漆率 = Fraction(5, 4)

# 今有漆三斗
漆總量 = 3

# 假令出漆九升，不足六升
假出漆 = Fraction(9, 10)  # 9升 = 9/10斗
不足 = Fraction(6, 10)    # 6升 = 6/10斗

# 令之出漆一斗二升，有餘二升
出漆 = Fraction(1, 1) + Fraction(2, 10)  # 1斗2升 = 1 + 2/10斗
餘漆 = 漆總量 - 出漆  # 剩餘漆量

# 得油
得油 = 出漆 * 漆得油率

# 和漆
和漆 = 餘漆 + 得油

# 將結果轉換為斗和升
a = 出漆  # 出漆量
b = 得油  # 得油量
c = 和漆.numerator // 和漆.denominator  # 和漆的斗數
d = (和漆 - c).numerator * 10 // 和漆.denominator  # 和漆的升數

a斗 = a
b斗 = b
c斗 = c
d升 = d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 6/5
Variable 'b' has wrong value. Expected: 3/2, Actual: 8/5
Variable 'c' has wrong value. Expected: 9/5, Actual: 3
Variable 'd' has wrong value. Expected: 3/4, Actual: 4"""
