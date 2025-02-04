"""
今有漆三得油四油四和漆五今有漆三斗欲令分以易油還自和餘漆問出漆得油和漆各幾何
術曰假令出漆九升不足六升令之出漆一斗二升有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰出漆 a斗 得油 b斗 和漆 c斗  d升 
"""

#----- content starts here -----
"""
Suppose there are 3 dou of lacquer that yield 4 dou of oil. 
If 4 dou of oil are mixed with 5 dou of lacquer, and now there are 3 dou of lacquer, it is desired to exchange lacquer for oil and then mix the remaining lacquer with the oil.
Question: how much lacquer is exchanged, how much oil is obtained, and how much lacquer and oil are mixed together?

The procedure says: Suppose 9 sheng of lacquer are exchanged, but it is insufficient by 6 sheng. 
Then suppose 1 dou and 2 sheng of lacquer are exchanged, with 2 sheng remaining.

The procedure for surplus and deficiency says: Place the exchange rate, surplus, and deficiency below each other. 
Multiply the exchange rate by the surplus and deficiency, and sum them to obtain the dividend. 
Sum the surplus and deficiency to obtain the divisor. 
Divide the dividend by the divisor. If there is a remainder, adjust it. 
If the surplus and deficiency are equal, the exchange rate is used directly. 
If the surplus and deficiency differ, reduce the larger by the smaller, and simplify the divisor and dividend. 
The dividend is the price of the goods, and the divisor is the number of people.

Answer: *a* dou of lacquer are exchanged, *b* dou of oil are obtained, and *c* dou and *d* sheng of lacquer and oil are mixed together.
"""

# 漆三得油四
漆率 = 3
油率 = 4

# 油四和漆五
油和率 = 4
漆和率 = 5

# 今有漆三斗
漆總量 = 3

# 假令出漆九升不足六升
假出漆1 = Fraction(9, 10)  # 9升 = 9/10斗
不足1 = Fraction(-6, 10)  # -6升 = -6/10斗

# 令之出漆一斗二升有餘二升
假出漆2 = Fraction(12, 10)  # 1斗2升 = 12/10斗
有餘2 = Fraction(2, 10)  # 2升 = 2/10斗

# 盈不足術
# 置所出率盈不足各居其下
盈不足 = [不足1, 有餘2]
所出率 = [假出漆1, 假出漆2]

# 維乘所出率并以為實
實 = sum([盈不足[i] * 所出率[i] for i in range(2)])

# 并盈不足為法
法 = sum([abs(x) for x in 盈不足])

# 實如法而一
出漆 = Fraction(實, 法)

# 出漆得油
得油 = (油率 / 漆率) * 出漆

# 和漆餘量
和漆 = 漆總量 - 出漆

# 漆和油混合
混合 = 和漆 + 得油

# 分解混合為斗和升
c = int(混合)  # 斗
d = int((混合 - c) * 10)  # 升

# 最終答案
a = 出漆
b = 得油#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9/8, Actual: -3/8
Variable 'b' has wrong value. Expected: 3/2, Actual: -0.5
Variable 'c' has wrong value. Expected: 9/5, Actual: 2
Variable 'd' has wrong value. Expected: 3/4, Actual: 8"""
