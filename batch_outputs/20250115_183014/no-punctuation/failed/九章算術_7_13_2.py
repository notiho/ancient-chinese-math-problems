"""
今有大器五小器一容三斛大器一小器五容二斛問大小器各容幾何
術曰假令大器五斗小器亦五斗盈一十斗令之大器五斗五升小器二斗五升不足二斗
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰大器容 a斛 小器容 b斛 
"""

"""
Suppose there is a large vessel and a small vessel. Five large vessels and one small vessel together hold 3 hu. 
One large vessel and five small vessels together hold 2 hu.
Question: how much does each large vessel and each small vessel hold?

The procedure says: Suppose the large vessel holds 5 dou, and the small vessel also holds 5 dou, making a total of 10 dou.
Adjust this by letting the large vessel hold 5 dou and 5 sheng, and the small vessel hold 2 dou and 5 sheng, leaving a deficit of 2 dou.

The procedure for surplus and deficit says: Place the rates of the given conditions, surplus and deficit, each below their respective conditions.
Let them be multiplied by the rates of the given conditions and summed to form the dividend.
Sum the surplus and deficit to form the divisor.
Divide the dividend by the divisor to find the value of one unit. If there is a remainder, adjust it proportionally.
The surplus and deficit are then used to calculate the values of the items.

Answer: The large vessel holds *a* hu, and the small vessel holds *b* hu.
"""

# 大器五小器一容三斛
大器率1 = 5
小器率1 = 1
總容1 = 3

# 大器一小器五容二斛
大器率2 = 1
小器率2 = 5
總容2 = 2

# 盈不足術
# 盈 = 大器率1 * 小器率2 = 5 * 5 = 25
盈 = 大器率1 * 小器率2

# 不足 = 大器率2 * 小器率1 = 1 * 1 = 1
不足 = 大器率2 * 小器率1

# 法 = 盈 + 不足 = 25 + 1 = 26
法 = 盈 + 不足

# 實 = 總容1 * 小器率2 + 總容2 * 小器率1 = 3 * 5 + 2 * 1 = 15 + 2 = 17
實 = 總容1 * 小器率2 + 總容2 * 小器率1

# 每單位值 = 實 / 法
單位值 = Fraction(實, 法)

# 大器容 = 單位值 * 大器率1 = 單位值 * 5
a = 單位值 * 大器率1

# 小器容 = 單位值 * 小器率1 = 單位值 * 1
b = 單位值 * 小器率1
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 85/26
Variable 'b' has wrong value. Expected: 7/24, Actual: 17/26"""
