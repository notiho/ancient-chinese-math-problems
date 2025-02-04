"""
今有田三百七十九畞畞出稅穀三升納官毎斛加二升耗問輸正及耗各幾何
術曰置田畞數以三升因之得一十一斛三斗七升為正又二因之得二斗二升七合四勺為耗
答曰正 a斛 耗 b斗
"""

"""
Suppose there is a field of 379 mu. Each mu yields 3 sheng of tax grain. When delivering to the officials, for every hu, 2 sheng are added as wastage.
Question: how much is the actual tax grain delivered (正, "correct amount") and how much is the wastage (耗, "wastage amount")?

The procedure says: Place the number of mu of the field.
Multiply it by 3 sheng, obtaining 11 hu, 3 dou, and 7 sheng as the correct amount.
Then multiply by 2, obtaining 2 dou, 2 sheng, 7 ge, and 4 jue as the wastage.

Answer: the correct amount is *a* hu, and the wastage is *b* dou.
"""

# 田三百七十九畞
田畞數 = 379

# 每畞出稅穀三升
稅穀每畞 = 3  # 升

# 納官每斛加二升耗
每斛耗 = 2  # 升

# 置田畞數，以三升因之，得正
正稅穀升 = 田畞數 * 稅穀每畞

# 升轉換為斛、斗、升
正稅穀斛 = 正稅穀升 // 100
正稅穀升 %= 100
正稅穀斗 = 正稅穀升 // 10
正稅穀升 %= 10

# 正稅穀結果
a = Fraction(正稅穀斛) + Fraction(正稅穀斗, 10) + Fraction(正稅穀升, 100)

# 又二因之，得耗
耗升 = 田畞數 * 每斛耗

# 升轉換為斗、升、合、勺
耗斗 = 耗升 // 10
耗升 %= 10
耗合 = 耗升 * 10 // 100
耗勺 = (耗升 * 10 % 100) * 10 // 100

# 耗結果
b = Fraction(耗斗) + Fraction(耗升, 10) + Fraction(耗合, 100) + Fraction(耗勺, 1000)
"""
Variable 'b' has wrong value. Expected: 1137/500, Actual: 9476/125"""
