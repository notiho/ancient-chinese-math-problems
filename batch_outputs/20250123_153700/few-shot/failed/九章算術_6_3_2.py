"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This problem is quite complex and involves multiple steps. Let's break it down and translate the procedure into Python code step by step.

### Problem Description:
There are six counties (甲, 乙, 丙, 丁, 戊, 己) that need to deliver a total of 60,000 hu of grain to county 甲. Each county has different conditions for grain price, labor costs, and distances to the delivery location. The goal is to distribute the grain among the counties such that the total cost (including labor and transportation) is equalized.

### Procedure:
The procedure involves calculating the cost per hu of grain for each county, considering transportation and labor costs, and then distributing the grain proportionally to equalize the costs.

---


"""


from fractions import Fraction

# Data for each county
counties = [
    {"name": "甲", "算": 42000, "粟價": 20, "傭價": 0, "道里": 0},  # 甲縣
    {"name": "乙", "算": 34272, "粟價": 18, "傭價": 10, "道里": 70},  # 乙縣
    {"name": "丙", "算": 19328, "粟價": 16, "傭價": 5, "道里": 140},  # 丙縣
    {"name": "丁", "算": 17700, "粟價": 14, "傭價": 5, "道里": 175},  # 丁縣
    {"name": "戊", "算": 23040, "粟價": 12, "傭價": 5, "道里": 210},  # 戊縣
    {"name": "己", "算": 19136, "粟價": 10, "傭價": 5, "道里": 280},  # 己縣
]

# Constants
車載 = 25  # 車載二十五斛
重車日行 = 50  # 重車日行五十里
空車日行 = 70  # 空車日行七十里
載輸日 = 1  # 載輸之間各一日
總賦粟 = 60000  # 六縣賦粟六萬斛

# Step 1: Calculate the cost per hu for each county
for county in counties:
    if county["name"] == "甲":
        # 甲縣 does not have transportation costs
        county["一斛費"] = county["粟價"]
    else:
        # Calculate transportation time
        道里 = county["道里"]
        重車時間 = Fraction(道里, 重車日行)
        空車時間 = Fraction(道里, 空車日行)
        總時間 = 重車時間 + 空車時間 + 載輸日

        # Multiply by 6 people and daily labor cost
        總傭費 = 總時間 * 6 * county["傭價"]

        # Divide by 25 hu (carrying capacity) and add grain price
        county["一斛費"] = Fraction(總傭費, 車載) + county["粟價"]

# Step 2: Normalize the 算數 (tax units) by the cost per hu
法 = sum(Fraction(county["算"], county["一斛費"]) for county in counties)

# Step 3: Calculate the grain allocation for each county
for county in counties:
    county["分配粟"] = Fraction(總賦粟) * Fraction(county["算"], county["一斛費"]) / 法

# Output the results
results = {county["name"]: county["分配粟"] for county in counties}
a, b, c, d, e, f = results["甲"], results["乙"], results["丙"], results["丁"], results["戊"], results["己"]

# Final answer
print(f"甲縣 {a}斛。乙縣 {b}斛。丙縣 {c}斛。丁縣 {d}斛。戊縣 {e}斛。己縣 {f}斛。")


"""


---

### Explanation of the Code:
1. **Input Data**: Each county's tax units (`算`), grain price (`粟價`), labor cost (`傭價`), and distance to the delivery location (`道里`) are provided.
2. **Cost Calculation**: For each county, the cost per hu of grain is calculated, including transportation and labor costs.
3. **Normalization**: The tax units are normalized by dividing by the cost per hu to ensure proportional distribution.
4. **Grain Allocation**: The total grain (60,000 hu) is distributed among the counties based on the normalized tax units.
5. **Output**: The grain allocation for each county is printed.

This code adheres to the procedure described in the problem and uses the `Fraction` class to ensure precise calculations.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 582104053440000/32058598771
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 363147482880000/32058598771
Variable 'c' has wrong value. Expected: 960000/133, Actual: 233343851520000/32058598771
Variable 'd' has wrong value. Expected: 900000/133, Actual: 219031499700000/32058598771
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 292422758400000/32058598771
Variable 'f' has wrong value. Expected: 960000/133, Actual: 233466280320000/32058598771"""
