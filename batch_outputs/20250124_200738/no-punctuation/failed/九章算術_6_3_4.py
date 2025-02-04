"""
今有均賦粟甲縣四萬二千算粟一斛二十自輸其縣乙縣三萬四千二百七十二算粟一斛一十八傭價一日一十錢到輸所七十里丙縣一萬九千三百二十八算粟一斛一十六傭價一日五錢到輸所一百四十里丁縣一萬七千七百算粟一斛一十四傭價一日五錢到輸所一百七十五里戊縣二萬三千四十算粟一斛一十二傭價一日五錢到輸所二百一十里己縣一萬九千一百三十六算粟一斛一十傭價一日五錢到輸所二百八十里凡六縣賦粟六萬斛皆輸甲縣六人共車車載二十五斛重車日行五十里空車日行七十里載輸之間各一日粟有貴賤傭各別價以算出錢令費勞等問縣各粟幾何
術曰以車程行空重相乘為法并空重以乘道里各自為實實如法得一日加載輸各一日而以六人乘之又以傭價乘之以二十五斛除之加一斛粟價即致一斛之費各以約其算數為衰副并為法以所賦粟乘未并者各自為實實如法得一斛
荅曰甲縣 a斛 乙縣 b斛 丙縣 c斛 丁縣 d斛 戊縣 e斛 己縣 f斛 
"""

"""
This problem is quite complex and involves multiple steps to calculate the distribution of grain (粟) among six counties while considering transportation costs, labor costs, and grain prices. Below is the Python implementation of the procedure described in the problem.


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
counties = [
    {"name": "甲", "粟": 42000, "粟價": 20, "傭價": 10, "道里": 70},
    {"name": "乙", "粟": 34272, "粟價": 18, "傭價": 10, "道里": 70},
    {"name": "丙", "粟": 19328, "粟價": 16, "傭價": 5, "道里": 140},
    {"name": "丁", "粟": 17700, "粟價": 14, "傭價": 5, "道里": 175},
    {"name": "戊", "粟": 23040, "粟價": 12, "傭價": 5, "道里": 210},
    {"name": "己", "粟": 19136, "粟價": 10, "傭價": 5, "道里": 280},
]

# Constants
車載 = 25  # 車載量 (25斛)
重車日行 = 50  # 重車日行里數
空車日行 = 70  # 空車日行里數
載輸日 = 1  # 載輸之間各一日
六人 = 6  # 六人共車

# Step 1: Calculate the cost per unit of grain for each county
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
    總日 = 一日 + 載輸日
    總日 *= 六人

    # 又以傭價乘之
    傭費 = 總日 * 傭價

    # 以二十五斛除之
    每斛傭費 = Fraction(傭費, 車載)

    # 加一斛粟價即致一斛之費
    每斛總費 = 每斛傭費 + 粟價

    # Store the cost per unit of grain
    county["每斛費"] = 每斛總費

# Step 2: Normalize the grain distribution based on cost
# 各以約其算數為衰副并為法
法 = sum(Fraction(1, county["每斛費"]) for county in counties)

# 以所賦粟乘未并者各自為實
for county in counties:
    county["實"] = county["粟"] * Fraction(1, county["每斛費"])

# 實如法得一斛
total_grain = sum(county["實"] for county in counties)
for county in counties:
    county["分配粟"] = county["實"] / total_grain * 60000  # Total grain is 60000斛

# Output the results
results = {county["name"]: county["分配粟"] for county in counties}
a, b, c, d, e, f = results["甲"], results["乙"], results["丙"], results["丁"], results["戊"], results["己"]

# Final answer
print(f"甲縣 {a} 斛, 乙縣 {b} 斛, 丙縣 {c} 斛, 丁縣 {d} 斛, 戊縣 {e} 斛, 己縣 {f} 斛")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Step 1: Calculate the cost per unit of grain for each county**:
   - The transportation cost is calculated based on the distance (道里), the speed of loaded and empty carts, and the labor cost (傭價).
   - The total cost per unit of grain includes the transportation cost and the price of the grain (粟價).

2. **Step 2: Normalize the grain distribution**:
   - The grain is distributed proportionally based on the inverse of the cost per unit of grain for each county.
   - The total grain (60000斛) is divided among the counties according to this proportionality.

3. **Output**:
   - The final distribution of grain for each county is printed.

This code follows the procedure described in the problem and calculates the grain distribution accordingly.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 2273843958750000/160860154321
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 1997311155840000/160860154321
Variable 'c' has wrong value. Expected: 960000/133, Actual: 1283391183360000/160860154321
Variable 'd' has wrong value. Expected: 900000/133, Actual: 1204673248350000/160860154321
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 1608325171200000/160860154321
Variable 'f' has wrong value. Expected: 960000/133, Actual: 1284064541760000/160860154321"""
