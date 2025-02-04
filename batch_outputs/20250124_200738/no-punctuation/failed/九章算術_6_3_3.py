"""
今有均賦粟甲縣四萬二千算粟一斛二十自輸其縣乙縣三萬四千二百七十二算粟一斛一十八傭價一日一十錢到輸所七十里丙縣一萬九千三百二十八算粟一斛一十六傭價一日五錢到輸所一百四十里丁縣一萬七千七百算粟一斛一十四傭價一日五錢到輸所一百七十五里戊縣二萬三千四十算粟一斛一十二傭價一日五錢到輸所二百一十里己縣一萬九千一百三十六算粟一斛一十傭價一日五錢到輸所二百八十里凡六縣賦粟六萬斛皆輸甲縣六人共車車載二十五斛重車日行五十里空車日行七十里載輸之間各一日粟有貴賤傭各別價以算出錢令費勞等問縣各粟幾何
術曰以車程行空重相乘為法并空重以乘道里各自為實實如法得一日加載輸各一日而以六人乘之又以傭價乘之以二十五斛除之加一斛粟價即致一斛之費各以約其算數為衰副并為法以所賦粟乘未并者各自為實實如法得一斛
荅曰甲縣 a斛 乙縣 b斛 丙縣 c斛 丁縣 d斛 戊縣 e斛 己縣 f斛 
"""

"""
This problem is quite complex and involves multiple steps to calculate the distribution of grain among six counties while considering transportation costs, labor costs, and grain prices. Below is the Python implementation of the procedure described in the problem:


"""

#----- content starts here -----

from fractions import Fraction

# 賦粟總數
總粟 = 60000

# 縣數據: [賦粟數, 粟價(每斛), 傭價(每日), 到輸所里程]
縣數據 = [
    [42000, 20, 10, 70],   # 甲縣
    [34272, 18, 10, 70],   # 乙縣
    [19328, 16, 5, 140],   # 丙縣
    [17700, 14, 5, 175],   # 丁縣
    [23040, 12, 5, 210],   # 戊縣
    [19136, 10, 5, 280],   # 己縣
]

# 車數據
車載量 = 25  # 每車載粟量
重車日行 = 50  # 重車每日行里
空車日行 = 70  # 空車每日行里
載輸時間 = 1  # 載輸之間各一日
車人數 = 6  # 六人共車

# 計算每縣一斛粟的費用
一斛費用 = []
for 賦粟數, 粟價, 傭價, 里程 in 縣數據:
    # 以車程行空重相乘為法
    法 = 重車日行 * 空車日行

    # 并空重以乘道里各自為實
    實 = (重車日行 + 空車日行) * 里程

    # 實如法得一日
    一日 = Fraction(實, 法)

    # 加載輸各一日
    總日數 = 一日 + 載輸時間

    # 而以六人乘之
    總工日 = 總日數 * 車人數

    # 又以傭價乘之
    總傭價 = 總工日 * 傭價

    # 以二十五斛除之
    每斛運費 = Fraction(總傭價, 車載量)

    # 加一斛粟價
    每斛總費用 = 每斛運費 + 粟價

    # 記錄每縣一斛粟的費用
    一斛費用.append(每斛總費用)

# 各以約其算數為衰副并為法
法 = sum(Fraction(賦粟數, 費用) for 賦粟數, 費用 in zip([x[0] for x in 縣數據], 一斛費用))

# 以所賦粟乘未并者各自為實
實 = [Fraction(賦粟數, 費用) * 總粟 for 賦粟數, 費用 in zip([x[0] for x in 縣數據], 一斛費用)]

# 實如法得一斛
結果 = [Fraction(項, 法) for 項 in 實]

# 輸出結果
a, b, c, d, e, f = 結果
print(f"甲縣 {a} 斛, 乙縣 {b} 斛, 丙縣 {c} 斛, 丁縣 {d} 斛, 戊縣 {e} 斛, 己縣 {f} 斛")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: The data for each county includes the total grain assigned, the price of grain per hu, the daily labor cost, and the distance to the delivery location.
2. **Transportation Costs**: For each county, the cost of transporting one hu of grain is calculated based on the distance, the speed of loaded and empty carts, the number of people involved, and the labor cost.
3. **Total Cost per Hu**: The transportation cost is added to the grain price to get the total cost per hu for each county.
4. **Weighted Distribution**: The grain is distributed proportionally based on the inverse of the total cost per hu for each county.
5. **Final Results**: The amount of grain assigned to each county is calculated and displayed.

This implementation follows the procedure described in the problem and calculates the grain distribution accordingly.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 2273843958750000/160860154321
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 1997311155840000/160860154321
Variable 'c' has wrong value. Expected: 960000/133, Actual: 1283391183360000/160860154321
Variable 'd' has wrong value. Expected: 900000/133, Actual: 1204673248350000/160860154321
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 1608325171200000/160860154321
Variable 'f' has wrong value. Expected: 960000/133, Actual: 1284064541760000/160860154321"""
