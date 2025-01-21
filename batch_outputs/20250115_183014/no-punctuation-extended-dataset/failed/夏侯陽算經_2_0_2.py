"""
今有田三百七十九畞畞出稅穀三升納官毎斛加二升耗問輸正及耗各幾何
術曰置田畞數以三升因之得一十一斛三斗七升為正又二因之得二斗二升七合四勺為耗
答曰正 a斛 耗 b斗
"""

"""
Suppose there is a field of 379 mu. Each mu yields 3 sheng of tax grain. 
When delivering to the government, for every hu, an additional 2 sheng is added as wastage.
Question: how much is the actual tax grain delivered (zheng), and how much is the wastage (hao)?

The procedure says: Place the number of mu of the field.
Multiply it by 3 sheng, obtaining 11 hu, 3 dou, and 7 sheng as the actual tax grain (zheng).
Then multiply it by 2, obtaining 2 dou, 2 sheng, 7 ge, and 4 jue as the wastage (hao).

Answer: the actual tax grain delivered is *a* hu, and the wastage is *b* dou.
"""

# 置田畞數
田畞數 = 379

# 每畞出稅穀三升
稅穀每畞 = 3  # 升

# 納官每斛加二升耗
耗每斛 = 2  # 升

# 正：以三升因之
正稅穀升 = 稅穀每畞 * 田畞數  # 總稅穀量（升）

# 升轉換為斛、斗、升
正稅穀斛 = 正稅穀升 // 100
正稅穀升 %= 100
正稅穀斗 = 正稅穀升 // 10
正稅穀升 %= 10

# 耗：以二因之
耗升 = 耗每斛 * 田畞數  # 總耗量（升）

# 升轉換為斗、升、合、勺
耗斗 = 耗升 // 10
耗升 %= 10
耗合 = 耗升 // 1
耗升 %= 1
耗勺 = 耗升 * 10  # 升的小數部分轉換為勺

# 答案
a = f"{正稅穀斛}斛 {正稅穀斗}斗 {正稅穀升}升"
b = f"{耗斗}斗 {耗合}升 {耗勺:.0f}勺"
"""
Variable 'a' has wrong value. Expected: 1137/100, Actual: 11斛 3斗 7升
Variable 'b' has wrong value. Expected: 1137/500, Actual: 75斗 8升 0勺"""
