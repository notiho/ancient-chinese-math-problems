"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This is a complex ancient Chinese math problem involving proportional distribution of grain (粟) among six counties based on labor costs, transportation distances, and other factors. The goal is to distribute the total grain (60,000斛) among the six counties such that the labor costs are equalized.

To solve this, we need to calculate the total cost for each county based on the given parameters (grain price, transportation distance, labor cost, etc.) and then distribute the grain proportionally to equalize the costs.

Here is the Python code to solve this problem:


"""

#----- content starts here -----

from fractions import Fraction

# Given data for each county
counties = [
    {"name": "甲", "算": 42000, "粟價": 20, "傭價": 0, "距離": 0},   # 甲縣 (self-delivery, no labor cost)
    {"name": "乙", "算": 34272, "粟價": 18, "傭價": 10, "距離": 70},  # 乙縣
    {"name": "丙", "算": 19328, "粟價": 16, "傭價": 5, "距離": 140},  # 丙縣
    {"name": "丁", "算": 17700, "粟價": 14, "傭價": 5, "距離": 175},  # 丁縣
    {"name": "戊", "算": 23040, "粟價": 12, "傭價": 5, "距離": 210},  # 戊縣
    {"name": "己", "算": 19136, "粟價": 10, "傭價": 5, "距離": 280},  # 己縣
]

# Constants
total_grain = 60000  # Total grain to be distributed (in 斛)
車載量 = 25          # Capacity of one cart (in 斛)
重車日行 = 50        # Distance a loaded cart can travel in one day (in 里)
空車日行 = 70        # Distance an empty cart can travel in one day (in 里)
載輸時間 = 1          # Additional day for loading/unloading

# Calculate total cost for each county
for county in counties:
    if county["距離"] == 0:
        # No transportation cost for 甲縣
        county["總費"] = county["粟價"]
    else:
        # Transportation cost
        往返距離 = 2 * county["距離"]
        重車時間 = Fraction(往返距離, 重車日行)
        空車時間 = Fraction(往返距離, 空車日行)
        總時間 = 重車時間 + 空車時間 + 2 * 載輸時間
        運費 = 總時間 * county["傭價"]
        county["總費"] = county["粟價"] + 運費

# Calculate the total "算費" (weighted cost) for all counties
total_cost = sum(county["算"] * county["總費"] for county in counties)

# Distribute the total grain proportionally to equalize costs
for county in counties:
    county["分配粟"] = Fraction(county["算"] * county["總費"], total_cost) * total_grain

# Output the results
results = {county["name"]: county["分配粟"] for county in counties}
a, b, c, d, e, f = results["甲"], results["乙"], results["丙"], results["丁"], results["戊"], results["己"]

print(f"甲縣得 {a} 斛")
print(f"乙縣得 {b} 斛")
print(f"丙縣得 {c} 斛")
print(f"丁縣得 {d} 斛")
print(f"戊縣得 {e} 斛")
print(f"己縣得 {f} 斛")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: Each county's data includes the number of "算" (a unit of labor), the price of grain (粟價), the labor cost per day (傭價), and the distance to the delivery location (距離).
2. **Transportation Cost**: For counties other than 甲, the transportation cost is calculated based on the round-trip distance, cart capacity, and labor costs.
3. **Total Cost**: The total cost for each county is the sum of the grain price and transportation cost.
4. **Proportional Distribution**: The grain is distributed proportionally based on the total cost for each county to equalize the labor burden.
5. **Output**: The final distribution of grain (in 斛) for each county is printed.

This code uses the `Fraction` class to ensure precise calculations without floating-point errors.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 5040000/1109
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 17684352/1109
Variable 'c' has wrong value. Expected: 960000/133, Actual: 8581632/1109
Variable 'd' has wrong value. Expected: 900000/133, Actual: 8920800/1109
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 12994560/1109
Variable 'f' has wrong value. Expected: 960000/133, Actual: 13318656/1109"""
