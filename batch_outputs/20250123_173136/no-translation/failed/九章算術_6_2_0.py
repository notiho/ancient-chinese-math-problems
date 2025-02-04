"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""

"""


from fractions import Fraction

# 各縣戶數與粟價及至輸所里數
縣戶數 = [20520, 12312, 7182, 13338, 5130]
粟價 = [120, 110, 112, 117, 113]
輸所里數 = [0, 200, 150, 250, 150]

# 一車載二十五斛，與僦一里一錢
車載量 = 25
僦價每里 = 1

# 計算致一斛之費
致一斛費 = []
for i in range(len(縣戶數)):
    運費 = Fraction(輸所里數[i] * 僦價每里, 車載量)
    致一斛費.append(運費 + 粟價[i])

# 各縣衰數
衰數 = [Fraction(縣戶數[i], 致一斛費[i]) for i in range(len(縣戶數))]

# 副并為法
法 = sum(衰數)

# 所賦粟
總賦粟 = 10000

# 所賦粟乘未并者，各自為實
實 = [總賦粟 * 衰數[i] for i in range(len(衰數))]

# 實如法得一
分配粟 = [Fraction(實[i], 法) for i in range(len(實))]

# 各縣所分配粟
a, b, c, d, e = 分配粟


"""
 

### Explanation:
1. **Input Data**: The data for each county includes the number of households, the price of one "斛" of grain, and the distance to the delivery location.
2. **Calculation of Cost per Unit Grain**: For each county, the cost of delivering one unit of grain is calculated by adding the transportation cost (distance × cost per mile ÷ grain capacity per cart) to the price of one unit of grain.
3. **Calculation of "衰數"**: The "衰數" for each county is calculated as the number of households divided by the cost per unit of grain.
4. **Total "法"**: The sum of all "衰數" is calculated as the "法".
5. **Grain Distribution**: The total grain to be distributed is multiplied by each county's "衰數" and divided by the "法" to determine the grain allocated to each county.

### Output:
- `a`: Grain allocated to 甲縣
- `b`: Grain allocated to 乙縣
- `c`: Grain allocated to 丙縣
- `d`: Grain allocated to 丁縣
- `e`: Grain allocated to 戊縣
"""


"""
Variable 'a' has wrong value. Expected: 10260000/2873, Actual: 557291875/157846
Variable 'b' has wrong value. Expected: 6840000/2873, Actual: 170021250/78923
Variable 'c' has wrong value. Expected: 3990000/2873, Actual: 198358125/157846
Variable 'd' has wrong value. Expected: 380000/221, Actual: 13164375/6071
Variable 'e' has wrong value. Expected: 2700000/2873, Actual: 70246875/78923"""
