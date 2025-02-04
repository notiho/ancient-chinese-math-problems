"""
今有漆三得油四，油四和漆五。今有漆三斗，欲令分以易油，還自和餘漆。問︰出漆、得油、和漆各幾何？
術曰：假令出漆九升，不足六升。令之出漆一斗二升，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：出漆 a斗 ，得油 b斗 ，和漆 c斗 ， d升 。
"""

"""
To solve this problem, we will carefully follow the procedure described in the text. Here's the Python implementation:


"""


from fractions import Fraction

# 漆三得油四
漆出率 = 3
油得率 = 4

# 油四和漆五
油和率 = 4
漆和率 = 5

# 今有漆三斗
漆總量 = 3

# 假令出漆九升，不足六升
假出漆 = Fraction(9, 10)  # 9升 = 9/10斗
不足 = Fraction(6, 10)    # 6升 = 6/10斗

# 盈不足術曰：置所出率，盈、不足各居其下
盈 = 漆出率
不足 = 漆出率 - 不足

# 令維乘所出率，并以為實
實 = 假出漆 * 漆出率

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
出漆 = Fraction(實, 法)

# 有分者，通之
出漆 = 出漆.limit_denominator()

# 得油
得油 = (出漆 / 漆出率) * 油得率

# 和漆
和漆 = (得油 / 油和率) * 漆和率

# 剩餘漆
剩餘漆 = 漆總量 - 出漆 - 和漆

# 將剩餘漆轉換為斗和升
剩餘漆斗 = int(剩餘漆)
剩餘漆升 = (剩餘漆 - 剩餘漆斗) * 10

# 結果
a = 出漆
b = 得油
c = 和漆
d = 剩餘漆升

# Output
a, b, c, d


"""


### Explanation of Variables:
- `a`: 出漆 (amount of lacquer extracted in 斗)
- `b`: 得油 (amount of oil obtained in 斗)
- `c`: 和漆 (amount of lacquer mixed back in 斗)
- `d`: Remaining 漆 in 升

This code follows the procedure described in the problem and calculates the required values step by step.
"""


"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 1/2
Variable 'b' has wrong value. Expected: 3/2, Actual: 2/3
Variable 'c' has wrong value. Expected: 9/5, Actual: 5/6
Variable 'd' has wrong value. Expected: 3/4, Actual: 20/3"""
