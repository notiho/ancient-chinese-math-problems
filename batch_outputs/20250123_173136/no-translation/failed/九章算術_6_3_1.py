"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This problem is quite complex and involves multiple steps of calculation. Let's break it down and encode the procedure step by step in Python.


"""


from fractions import Fraction

# Data for each county
counties = [
    {"name": "甲", "算": 42000, "粟價": 20, "傭價": 0, "道里": 0},  # 甲縣 (self-delivery, no transport cost)
    {"name": "乙", "算": 34272, "粟價": 18, "傭價": 10, "道里": 70},
    {"name": "丙", "算": 19328, "粟價": 16, "傭價": 5, "道里": 140},
    {"name": "丁", "算": 17700, "粟價": 14, "傭價": 5, "道里": 175},
    {"name": "戊", "算": 23040, "粟價": 12, "傭價": 5, "道里": 210},
    {"name": "己", "算": 19136, "粟價": 10, "傭價": 5, "道里": 280},
]

# Constants
車載 = 25  # 車載二十五斛
重車日行 = 50  # 重車日行五十里
空車日行 = 70  # 空車日行七十里
載輸各一日 = 1  # 載輸之間各一日
總粟 = 60000  # 六縣賦粟六萬斛

# Step 1: Calculate the cost of transporting 1 斛 for each county
for county in counties:
    if county["name"] == "甲":  # 甲縣 has no transport cost
        county["一斛費"] = county["粟價"]
        continue

    # 以車程行空、重相乘為法
    法 = 重車日行 * 空車日行

    # 并空、重以乘道里，各自為實
    重實 = 空車日行 * county["道里"]
    空實 = 重車日行 * county["道里"]

    # 實如法得一日
    一日 = Fraction(重實 + 空實, 法)

    # 加載輸各一日
    總日 = 一日 + 載輸各一日

    # 而以六人乘之
    總日 *= 6

    # 又以傭價乘之
    總費用 = 總日 * county["傭價"]

    # 以二十五斛除之
    每斛運費 = Fraction(總費用, 車載)

    # 加一斛粟價，即致一斛之費
    county["一斛費"] = 每斛運費 + county["粟價"]

# Step 2: Normalize the 算數 (算數為衰) and calculate the 粟 allocation
# 副并為法
法 = sum(Fraction(county["算"], county["一斛費"]) for county in counties)

# Calculate 粟 allocation for each county
for county in counties:
    # 以所賦粟乘未并者，各自為實
    實 = Fraction(county["算"], county["一斛費"]) * 總粟

    # 實如法得一斛
    county["粟分配"] = Fraction(實, 法)

# Output results
results = {county["name"]: county["粟分配"] for county in counties}
a, b, c, d, e, f = results["甲"], results["乙"], results["丙"], results["丁"], results["戊"], results["己"]

# Final answers
print(f"甲縣 {a}斛")
print(f"乙縣 {b}斛")
print(f"丙縣 {c}斛")
print(f"丁縣 {d}斛")
print(f"戊縣 {e}斛")
print(f"己縣 {f}斛")


"""


### Explanation of the Code:
1. **Step 1: Transport Cost Calculation**
   - For each county, calculate the transport cost for 1 斛 of 粟 based on the distance, transport rates, and labor costs.
   - Counties with no transport cost (like 甲縣) directly use their 粟價.

2. **Step 2: Normalize 算數 and Allocate 粟**
   - Normalize the 算數 by dividing it by the transport-adjusted cost of 1 斛 for each county.
   - Use the normalized values to proportionally allocate the total 粟 (60000 斛) among the counties.

3. **Output Results**
   - The results are stored in the `results` dictionary and printed for each county.

This code follows the procedure described in the problem and ensures that the labor and transport costs are evenly distributed among the counties.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 582104053440000/32058598771
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 363147482880000/32058598771
Variable 'c' has wrong value. Expected: 960000/133, Actual: 233343851520000/32058598771
Variable 'd' has wrong value. Expected: 900000/133, Actual: 219031499700000/32058598771
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 292422758400000/32058598771
Variable 'f' has wrong value. Expected: 960000/133, Actual: 233466280320000/32058598771"""
