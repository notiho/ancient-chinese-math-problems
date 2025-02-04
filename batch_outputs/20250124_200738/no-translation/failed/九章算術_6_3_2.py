"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This is a complex problem involving proportional distribution of costs and labor across multiple counties. Below is the Python code that follows the procedure ("術") step by step:


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
counties = [
    {"name": "甲", "算": 42000, "粟價": 20, "傭價": 10, "道里": 0},    # 甲縣 (self-transport, no distance)
    {"name": "乙", "算": 34272, "粟價": 18, "傭價": 10, "道里": 70},   # 乙縣
    {"name": "丙", "算": 19328, "粟價": 16, "傭價": 5, "道里": 140},   # 丙縣
    {"name": "丁", "算": 17700, "粟價": 14, "傭價": 5, "道里": 175},   # 丁縣
    {"name": "戊", "算": 23040, "粟價": 12, "傭價": 5, "道里": 210},   # 戊縣
    {"name": "己", "算": 19136, "粟價": 10, "傭價": 5, "道里": 280},   # 己縣
]

# Constants
車載 = 25  # 車載二十五斛
重車日行 = 50  # 重車日行五十里
空車日行 = 70  # 空車日行七十里
載輸日 = 1  # 載輸之間各一日
總粟 = 60000  # 六縣賦粟六萬斛

# Step 1: Calculate the cost of transporting one 斛 of 粟 for each county
for county in counties:
    if county["道里"] == 0:
        # 甲縣 has no transportation cost
        county["一斛費"] = county["粟價"]
    else:
        # Calculate transportation cost
        道里 = county["道里"]
        法 = (重車日行 * 空車日行)  # 空、重相乘為法
        實 = (重車日行 + 空車日行) * 道里  # 并空、重以乘道里
        日數 = Fraction(實, 法) + 載輸日  # 實如法得一日，加載輸各一日
        總日數 = 日數 * 6  # 六人共車
        傭費 = 總日數 * county["傭價"]  # 傭價乘之
        運費 = Fraction(傭費, 車載)  # 以二十五斛除之
        county["一斛費"] = 運費 + county["粟價"]  # 加一斛粟價，即致一斛之費

# Step 2: Normalize the costs to distribute 粟 proportionally
法 = sum(Fraction(county["算"], county["一斛費"]) for county in counties)  # 副并為法
for county in counties:
    實 = Fraction(county["算"], county["一斛費"]) * 總粟  # 所賦粟乘未并者
    county["粟"] = Fraction(實, 法)  # 實如法得一斛

# Step 3: Output the results
results = {county["name"]: county["粟"] for county in counties}
a, b, c, d, e, f = results["甲"], results["乙"], results["丙"], results["丁"], results["戊"], results["己"]

# Final results
print(f"甲縣 {a}斛 。乙縣 {b}斛 。丙縣 {c}斛 。丁縣 {d}斛 。戊縣 {e}斛 。己縣 {f}斛 。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Step 1: Calculate Transportation Costs**  
   For each county, the cost of transporting one 斛 of 粟 is calculated based on the distance (`道里`), the speed of loaded and empty carts, and the labor costs. For counties with no transportation (e.g., 甲縣), the cost is simply the price of 粟.

2. **Step 2: Normalize Costs**  
   The normalized cost (`法`) is calculated by summing the ratios of `算` to `一斛費` for all counties. Each county's 粟 allocation is then proportional to this normalized cost.

3. **Step 3: Output Results**  
   The 粟 allocation for each county is calculated and displayed.

This code adheres to the procedure described in the problem and uses the `Fraction` class to ensure precise calculations.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 582104053440000/32058598771
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 363147482880000/32058598771
Variable 'c' has wrong value. Expected: 960000/133, Actual: 233343851520000/32058598771
Variable 'd' has wrong value. Expected: 900000/133, Actual: 219031499700000/32058598771
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 292422758400000/32058598771
Variable 'f' has wrong value. Expected: 960000/133, Actual: 233466280320000/32058598771"""
