"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This is a complex ancient Chinese problem involving proportional distribution of resources (grain) based on transportation costs and labor. Below is the Python implementation of the procedure described in the problem.


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
counties = [
    {"name": "甲", "算": 42000, "粟價": 20, "傭價": 10, "道里": 0},   # 甲縣
    {"name": "乙", "算": 34272, "粟價": 18, "傭價": 10, "道里": 70},  # 乙縣
    {"name": "丙", "算": 19328, "粟價": 16, "傭價": 5, "道里": 140},  # 丙縣
    {"name": "丁", "算": 17700, "粟價": 14, "傭價": 5, "道里": 175}, # 丁縣
    {"name": "戊", "算": 23040, "粟價": 12, "傭價": 5, "道里": 210}, # 戊縣
    {"name": "己", "算": 19136, "粟價": 10, "傭價": 5, "道里": 280}, # 己縣
]

# Constants
車載 = 25  # 車載二十五斛
重車日行 = 50  # 重車日行五十里
空車日行 = 70  # 空車日行七十里
載輸日 = 1  # 載輸之間各一日
總粟 = 60000  # 六縣賦粟六萬斛

# Step 1: Calculate the cost of transporting 1 斛 of grain for each county
for county in counties:
    道里 = county["道里"]
    傭價 = county["傭價"]
    粟價 = county["粟價"]

    # 車程行空、重相乘為法
    法 = 重車日行 * 空車日行

    # 并空、重以乘道里，各自為實
    重車實 = 空車日行 * 道里
    空車實 = 重車日行 * 道里

    # 實如法得一日
    日數 = Fraction(重車實 + 空車實, 法)

    # 加載輸各一日
    日數 += 載輸日

    # 以六人乘之
    日數 *= 6

    # 又以傭價乘之
    費用 = 日數 * 傭價

    # 以二十五斛除之
    費用 /= 車載

    # 加一斛粟價，即致一斛之費
    一斛費 = 費用 + 粟價

    # Store the cost of 1 斛 for this county
    county["一斛費"] = 一斛費

# Step 2: Normalize the 算數 (tax units) by the cost of 1 斛
for county in counties:
    county["衰"] = Fraction(county["算"], county["一斛費"])

# Step 3: Calculate the divisor (法) by summing the normalized 算數
法 = sum(county["衰"] for county in counties)

# Step 4: Calculate the actual grain allocation for each county
for county in counties:
    county["粟"] = Fraction(總粟 * county["衰"], 法)

# Step 5: Extract results
results = {county["name"]: county["粟"] for county in counties}

# Final Answer
a = results["甲"]
b = results["乙"]
c = results["丙"]
d = results["丁"]
e = results["戊"]
f = results["己"]

# Output the results
print(f"甲縣 {a} 斛")
print(f"乙縣 {b} 斛")
print(f"丙縣 {c} 斛")
print(f"丁縣 {d} 斛")
print(f"戊縣 {e} 斛")
print(f"己縣 {f} 斛")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Step 1**: Calculate the cost of transporting 1 斛 of grain for each county using the formula provided in the problem. This includes the transportation distance, labor costs, and grain price.
2. **Step 2**: Normalize the tax units (`算數`) by dividing them by the cost of transporting 1 斛 of grain.
3. **Step 3**: Calculate the divisor (`法`) by summing the normalized tax units.
4. **Step 4**: Allocate the total grain (`總粟`) proportionally to each county based on their normalized tax units.
5. **Step 5**: Extract and display the results for each county.

### Final Answer:
The grain allocation for each county is given as fractions of 斛 (`a`, `b`, `c`, `d`, `e`, `f`).
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 519735762000000/31019127247
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 363147482880000/31019127247
Variable 'c' has wrong value. Expected: 960000/133, Actual: 233343851520000/31019127247
Variable 'd' has wrong value. Expected: 900000/133, Actual: 219031499700000/31019127247
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 292422758400000/31019127247
Variable 'f' has wrong value. Expected: 960000/133, Actual: 233466280320000/31019127247"""
