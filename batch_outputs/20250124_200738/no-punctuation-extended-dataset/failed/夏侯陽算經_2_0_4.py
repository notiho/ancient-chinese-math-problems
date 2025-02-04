"""
今有田三百七十九畞畞出稅穀三升納官毎斛加二升耗問輸正及耗各幾何
術曰置田畞數以三升因之得一十一斛三斗七升為正又二因之得二斗二升七合四勺為耗
答曰正 a斛 耗 b斗
"""

#----- content starts here -----
"""
Suppose there is a field of 379 mu. Each mu produces 3 sheng of tax grain. When delivering to the officials, for every 1 hu, an additional 2 sheng is consumed as wastage.
Question: how much is the actual tax grain delivered (zheng), and how much is the wastage (hao)?

The procedure says: Place the number of mu of the field. Multiply it by 3 sheng, obtaining 11 hu, 3 dou, and 7 sheng as the actual tax grain (zheng). 
Then multiply it by 2, obtaining 2 dou, 2 sheng, 7 ge, and 4 jue as the wastage (hao).

Answer: the actual tax grain delivered is *a* hu, and the wastage is *b* dou.
"""

from fractions import Fraction

# 置田畞數
田畞數 = 379

# 每畞出稅穀三升
稅穀每畞 = 3  # 升

# 納官每斛加二升耗
耗每斛 = 2  # 升

# 以三升因之，得正稅穀
正稅穀升 = 田畞數 * 稅穀每畞  # 總稅穀數，單位：升

# 升轉換為斛、斗、升
正稅穀斛 = 正稅穀升 // 100  # 1 斛 = 100 升
正稅穀升 %= 100

正稅穀斗 = 正稅穀升 // 10  # 1 斗 = 10 升
正稅穀升 %= 10

正稅穀升 = 正稅穀升  # 剩餘升數

# 正稅穀結果
a = 正稅穀斛 + Fraction(正稅穀斗, 10) + Fraction(正稅穀升, 100)

# 以二升因之，得耗
耗升 = 田畞數 * 耗每斛  # 總耗損數，單位：升

# 升轉換為斗、升、合、勺
耗斗 = 耗升 // 10  # 1 斗 = 10 升
耗升 %= 10

耗升 = 耗升  # 剩餘升數

耗合 = 耗升 * 10 // 100  # 1 升 = 10 合
耗升 %= 1

耗勺 = 耗升 * 100 // 1000  # 1 合 = 10 勺

# 耗結果
b = 耗斗 + Fraction(耗升, 10) + Fraction(耗合, 100) + Fraction(耗勺, 1000)#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 1137/500, Actual: 75"""
