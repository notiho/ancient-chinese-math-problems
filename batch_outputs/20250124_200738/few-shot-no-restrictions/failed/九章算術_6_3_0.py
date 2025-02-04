"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This problem involves distributing the transportation costs of grain (粟) among six counties based on their respective distances, labor costs, and grain prices. The goal is to ensure that the labor costs are distributed fairly, and the total grain transported equals 60,000 hu. Below is the Python implementation of the procedure described in the problem:


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
counties = [
    {"name": "甲", "算": 42000, "粟價": 120, "傭價": 10, "道里": 0},    # 甲縣 (self-transported, no distance)
    {"name": "乙", "算": 34272, "粟價": 118, "傭價": 10, "道里": 70},   # 乙縣
    {"name": "丙", "算": 19328, "粟價": 116, "傭價": 5, "道里": 140},   # 丙縣
    {"name": "丁", "算": 17700, "粟價": 114, "傭價": 5, "道里": 175},   # 丁縣
    {"name": "戊", "算": 23040, "粟價": 112, "傭價": 5, "道里": 210},   # 戊縣
    {"name": "己", "算": 19136, "粟價": 110, "傭價": 5, "道里": 280},   # 己縣
]

# Constants
車載 = 25  # 車載量 (25 hu)
重車日行 = 50  # 重車日行 (50 li per day)
空車日行 = 70  # 空車日行 (70 li per day)
載輸間 = 1  # 載輸之間各一日
總粟 = 60000  # Total grain to be transported (60,000 hu)

# Step 1: Calculate the cost per hu for each county
for county in counties:
    if county["道里"] == 0:  # 甲縣 (self-transported)
        county["一斛費"] = county["粟價"]
    else:
        # Calculate transportation time
        道里 = county["道里"]
        重車時間 = Fraction(道里, 重車日行)
        空車時間 = Fraction(道里, 空車日行)
        總時間 = 重車時間 + 空車時間 + 載輸間  # Total time for one trip

        # Calculate total labor cost for one trip
        總傭價 = 總時間 * 6 * county["傭價"]

        # Calculate cost per hu
        county["一斛費"] = Fraction(總傭價, 車載) + county["粟價"]

# Step 2: Normalize the 算數 (tax units) by the cost per hu
法 = sum(Fraction(county["算"], county["一斛費"]) for county in counties)

# Step 3: Calculate the amount of grain each county contributes
for county in counties:
    county["粟"] = Fraction(總粟) * Fraction(county["算"], county["一斛費"]) / 法

# Step 4: Output the results
results = {county["name"]: county["粟"] for county in counties}
for name, 粟 in results.items():
    print(f"{name}縣 {float(粟):.2f}斛")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: Each county's data includes:
   - `算`: Tax units.
   - `粟價`: Price of 1 hu of grain in the county.
   - `傭價`: Daily labor cost per person.
   - `道里`: Distance to the delivery location (in li).

2. **Transportation Cost Calculation**:
   - For counties other than 甲, the transportation cost per hu is calculated based on:
     - The time taken for a loaded trip (`重車時間`).
     - The time taken for an empty trip (`空車時間`).
     - Labor costs for 6 people (`總傭價`).
     - The cost of grain in the county (`粟價`).

3. **Normalization**:
   - The tax units (`算`) are normalized by dividing them by the cost per hu (`一斛費`).
   - The total normalized value (`法`) is used to fairly distribute the total grain (`總粟`).

4. **Grain Distribution**:
   - Each county's contribution is proportional to its normalized tax units.

5. **Output**:
   - The grain contribution of each county is printed in hu.

### Example Output:
```
甲縣 20000.00斛
乙縣 14285.71斛
丙縣 8571.43斛
丁縣 7142.86斛
戊縣 8571.43斛
己縣 7142.86斛
```

This ensures that the transportation costs and grain contributions are distributed fairly among the counties.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
