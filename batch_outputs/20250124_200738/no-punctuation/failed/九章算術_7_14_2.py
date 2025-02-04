"""
今有漆三得油四油四和漆五今有漆三斗欲令分以易油還自和餘漆問出漆得油和漆各幾何
術曰假令出漆九升不足六升令之出漆一斗二升有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰出漆 a斗 得油 b斗 和漆 c斗  d升 
"""

#----- content starts here -----
"""
Suppose there are 3 dou of lacquer that yield 4 dou of oil. 
If 4 dou of oil are mixed with 5 dou of lacquer, then the resulting mixture is balanced. 
Now, given 3 dou of lacquer, it is desired to exchange it for oil and then mix the remaining lacquer with the oil. 
Question: how much lacquer is exchanged, how much oil is obtained, and how much lacquer remains mixed with the oil?

The procedure says: Suppose 9 sheng of lacquer are exchanged, but it is insufficient by 6 sheng. 
Adjust it to exchange 1 dou and 2 sheng, leaving 2 sheng remaining.

The procedure for surplus and deficiency says: Place the exchange rate and the surplus/deficiency values below them. 
Multiply the exchange rate by the surplus/deficiency, summing them to form the dividend. 
Sum the surplus and deficiency to form the divisor. 
Divide the dividend by the divisor to find the result. 
If there are fractions, simplify them. 
For surplus and deficiency, adjust them to match the exchanged item. 
Place the exchange rate, subtract the smaller value from the larger, and reduce the divisor and dividend accordingly. 
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* dou of lacquer is exchanged, *b* dou of oil is obtained, and *c* dou *d* sheng of lacquer remain mixed with the oil.
"""

from fractions import Fraction

# 漆三得油四
漆率 = 3
油率 = 4

# 漆三斗
漆總量 = 3

# 假令出漆九升不足六升
盈 = 9
不足 = 6

# 盈不足術
# 置所出率
所出率 = Fraction(油率, 漆率)

# 盈不足各居其下
盈不足和 = 盈 + 不足

# 令維乘所出率并以為實
實 = 盈 * 所出率 + 不足 * 所出率

# 并盈不足為法
法 = 盈不足和

# 實如法而一
出漆 = Fraction(實, 法)

# 有分者通之
出漆 = 出漆.limit_denominator()

# 出漆得油
得油 = 出漆 * 所出率

# 餘漆
餘漆 = 漆總量 - 出漆

# 餘漆分為斗和升
c = int(餘漆)
d = (餘漆 - c) * 10  # 1斗 = 10升

a = 出漆
b = 得油#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 4/3
Variable 'b' has wrong value. Expected: 3/2, Actual: 16/9
Variable 'c' has wrong value. Expected: 9/5, Actual: 1
Variable 'd' has wrong value. Expected: 3/4, Actual: 20/3"""
