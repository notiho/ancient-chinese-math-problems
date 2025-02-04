"""
今有均賦粟甲縣四萬二千算粟一斛二十自輸其縣乙縣三萬四千二百七十二算粟一斛一十八傭價一日一十錢到輸所七十里丙縣一萬九千三百二十八算粟一斛一十六傭價一日五錢到輸所一百四十里丁縣一萬七千七百算粟一斛一十四傭價一日五錢到輸所一百七十五里戊縣二萬三千四十算粟一斛一十二傭價一日五錢到輸所二百一十里己縣一萬九千一百三十六算粟一斛一十傭價一日五錢到輸所二百八十里凡六縣賦粟六萬斛皆輸甲縣六人共車車載二十五斛重車日行五十里空車日行七十里載輸之間各一日粟有貴賤傭各別價以算出錢令費勞等問縣各粟幾何
術曰以車程行空重相乘為法并空重以乘道里各自為實實如法得一日加載輸各一日而以六人乘之又以傭價乘之以二十五斛除之加一斛粟價即致一斛之費各以約其算數為衰副并為法以所賦粟乘未并者各自為實實如法得一斛
荅曰甲縣 a斛 乙縣 b斛 丙縣 c斛 丁縣 d斛 戊縣 e斛 己縣 f斛 
"""

"""
This problem is quite complex and involves multiple steps to calculate the distribution of grain among the six counties while considering transportation costs, labor costs, and grain prices. Below is the Python implementation of the procedure described in the problem:


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
counties = [
    {"name": "甲", "粟算": 42000, "粟價": 20, "傭價": 10, "道里": 70},
    {"name": "乙", "粟算": 34272, "粟價": 18, "傭價": 10, "道里": 70},
    {"name": "丙", "粟算": 19328, "粟價": 16, "傭價": 5, "道里": 140},
    {"name": "丁", "粟算": 17700, "粟價": 14, "傭價": 5, "道里": 175},
    {"name": "戊", "粟算": 23040, "粟價": 12, "傭價": 5, "道里": 210},
    {"name": "己", "粟算": 19136, "粟價": 10, "傭價": 5, "道里": 280},
]

# Constants
車載 = 25  # 車載 25 斛
重車日行 = 50  # 重車日行 50 里
空車日行 = 70  # 空車日行 70 里
載輸日 = 1  # 載輸之間各 1 日
六人 = 6  # 六人共車

# Step 1: Calculate the cost per dou (斛) for each county
for county in counties:
    道里 = county["道里"]
    粟價 = county["粟價"]
    傭價 = county["傭價"]

    # 車程行空重相乘為法
    法 = 重車日行 * 空車日行

    # 并空重以乘道里各自為實
    實 = (重車日行 + 空車日行) * 道里

    # 實如法得一日
    一日 = Fraction(實, 法)

    # 加載輸各一日而以六人乘之
    總日 = (一日 + 載輸日) * 六人

    # 又以傭價乘之
    傭費 = 總日 * 傭價

    # 以 25 斛除之
    每斛傭費 = Fraction(傭費, 車載)

    # 加 1 斛粟價即致 1 斛之費
    每斛總費 = 每斛傭費 + 粟價

    # Store the cost per dou in the county data
    county["每斛總費"] = 每斛總費

# Step 2: Normalize the 粟算 values based on the cost per dou
# 各以約其算數為衰副并為法
法 = sum(Fraction(county["粟算"], county["每斛總費"]) for county in counties)

# 以所賦粟乘未并者各自為實
for county in counties:
    county["實"] = Fraction(county["粟算"], county["每斛總費"]) * 法

# 實如法得一斛
total_grain = 60000  # 總賦粟 60000 斛
for county in counties:
    county["分配粟"] = Fraction(county["實"], 法) * total_grain

# Output the results
results = {county["name"]: county["分配粟"] for county in counties}
a, b, c, d, e, f = results["甲"], results["乙"], results["丙"], results["丁"], results["戊"], results["己"]

# Final Answer
print(f"甲縣 {a} 斛, 乙縣 {b} 斛, 丙縣 {c} 斛, 丁縣 {d} 斛, 戊縣 {e} 斛, 己縣 {f} 斛")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Step 1: Calculate the cost per dou (斛) for each county**:
   - The cost per dou includes both the transportation cost and the grain price.
   - The transportation cost is calculated based on the distance, the speed of loaded and empty carts, and the labor cost.

2. **Step 2: Normalize the 粟算 values**:
   - The 粟算 values are adjusted based on the cost per dou to ensure fairness in distribution.

3. **Step 3: Calculate the grain distribution**:
   - The total grain (60000 斛) is distributed among the counties based on the normalized 粟算 values.

4. **Output the results**:
   - The final distribution of grain for each county is printed.

This implementation follows the procedure described in the problem and ensures that the distribution is fair based on the costs and distances.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 984375000/11
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 8568000000/109
Variable 'c' has wrong value. Expected: 960000/133, Actual: 14496000000/287
Variable 'd' has wrong value. Expected: 900000/133, Actual: 331875000/7
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 5760000000/91
Variable 'f' has wrong value. Expected: 960000/133, Actual: 3588000000/71"""
