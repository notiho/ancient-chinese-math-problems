"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""

"""


from fractions import Fraction

# 縣戶數與粟價及至輸所里數
縣戶數 = [20520, 12312, 7182, 13338, 5130]
粟價 = [120, 110, 112, 117, 113]  # 每斛粟價（錢）
里數 = [0, 200, 150, 250, 150]  # 至輸所里數

# 一車載粟量與僦價
車載量 = 25  # 每車載粟量（斛）
僦價每里 = 1  # 每里僦價（錢）

# 計算致一斛之費
致一斛費 = []
for i in range(len(縣戶數)):
    運費 = Fraction(里數[i] * 僦價每里, 車載量)  # 運費
    致一斛費.append(運費 + 粟價[i])  # 致一斛費 = 運費 + 粟價

# 計算各縣的衰
衰 = []
for i in range(len(縣戶數)):
    衰.append(Fraction(縣戶數[i], 致一斛費[i]))

# 副并為法
法 = sum(衰)

# 所賦粟
所賦粟 = 10000  # 總輸粟量（斛）

# 所賦粟乘未并者，各自為實
實 = [Fraction(所賦粟 * s, 法) for s in 衰]

# 實如法得一
a, b, c, d, e = 實

# 結果
a, b, c, d, e


"""
 

This Python code calculates the distribution of 粟 (grain) among the five counties such that the transportation cost and labor are balanced. The results `a`, `b`, `c`, `d`, and `e` represent the amount of 粟 (in 斛) assigned to counties 甲, 乙, 丙, 丁, and 戊, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 10260000/2873, Actual: 557291875/157846
Variable 'b' has wrong value. Expected: 6840000/2873, Actual: 170021250/78923
Variable 'c' has wrong value. Expected: 3990000/2873, Actual: 198358125/157846
Variable 'd' has wrong value. Expected: 380000/221, Actual: 13164375/6071
Variable 'e' has wrong value. Expected: 2700000/2873, Actual: 70246875/78923"""
