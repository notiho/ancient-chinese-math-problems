"""
今有田三百七十九畞畞出稅穀三升納官毎斛加二升耗問輸正及耗各幾何
術曰置田畞數以三升因之得一十一斛三斗七升為正又二因之得二斗二升七合四勺為耗
答曰正 a斛 耗 b斗
"""

"""
Suppose there is a field of 379 mu. Each mu yields 3 sheng of tax grain.
When delivering to the officials, for every hu, an additional 2 sheng is added as wastage.
Question: how much is the actual tax grain delivered (zheng) and how much is the wastage (hao)?

The procedure says: Place the number of mu of the field.
Multiply it by 3 sheng, obtaining 11 hu, 3 dou, and 7 sheng as the actual tax grain (zheng).
Then multiply it by 2, obtaining 2 dou, 2 sheng, 7 ge, and 4 jue as the wastage (hao).

Answer: the actual tax grain delivered is *a* hu, and the wastage is *b* dou.
"""

# 置田畞數
田畞數 = 379

# 每畞出稅穀三升
稅穀每畞 = 3

# 納官每斛加二升耗
耗每斛 = 2

# 以三升因之，得正
正升 = 稅穀每畞 * 田畞數

# 升轉換為斛、斗、升
正斛 = 正升 // 100
正升 %= 100
正斗 = 正升 // 10
正升 %= 10

# 又二因之，得耗
耗升 = 耗每斛 * 田畞數

# 升轉換為斗、升、合、勺
耗斗 = 耗升 // 10
耗升 %= 10
耗合 = 耗升 // 1
耗升 %= 1
耗勺 = 耗升 * 10  # Convert remaining fractional升 into勺

# 答案
a = Fraction(正斛)  # 正斛
b = Fraction(耗斗)  # 耗斗
"""
Variable 'a' has wrong value. Expected: 1137/100, Actual: 11
Variable 'b' has wrong value. Expected: 1137/500, Actual: 75"""
