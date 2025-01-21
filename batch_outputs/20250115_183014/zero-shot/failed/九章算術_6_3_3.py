"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the amount of grain (in "斛") each county contributes to ensure the labor costs are evenly distributed. We'll use the `Fraction` class from Python's `fractions` module to handle fractional calculations.

Here is the Python code:


"""


from fractions import Fraction

# Given data
total_grain = 60000  # Total grain in 斛
counties = [
    {"name": "甲", "算": 42000, "粟價": 20, "傭價": 0, "道里": 0},  # 甲縣
    {"name": "乙", "算": 34272, "粟價": 18, "傭價": 10, "道里": 70},  # 乙縣
    {"name": "丙", "算": 19328, "粟價": 16, "傭價": 5, "道里": 140},  # 丙縣
    {"name": "丁", "算": 17700, "粟價": 14, "傭價": 5, "道里": 175},  # 丁縣
    {"name": "戊", "算": 23040, "粟價": 12, "傭價": 5, "道里": 210},  # 戊縣
    {"name": "己", "算": 19136, "粟價": 10, "傭價": 5, "道里": 280},  # 己縣
]

# Constants
car_capacity = 25  # 車載量 in 斛
heavy_speed = 50  # 重車日行 in 里
empty_speed = 70  # 空車日行 in 里
load_unload_days = 1  # 載輸之間各一日
people_per_car = 6  # 六人共車

# Step 1: Calculate the cost to transport 1 斛 of grain for each county
for county in counties:
    if county["name"] == "甲":  # 甲縣 does not transport grain
        county["費"] = Fraction(county["粟價"])
    else:
        # Calculate the total time for a round trip
        distance = county["道里"]
        round_trip_days = (
            Fraction(distance, heavy_speed) + Fraction(distance, empty_speed) + load_unload_days
        )
        # Multiply by the number of people and daily wage, then divide by car capacity
        transport_cost = Fraction(round_trip_days * people_per_car * county["傭價"], car_capacity)
        # Add the cost of 1 斛 of grain
        county["費"] = transport_cost + Fraction(county["粟價"])

# Step 2: Normalize the "算" values by the cost per 1 斛 of grain
total算 = sum(Fraction(county["算"], county["費"]) for county in counties)

# Step 3: Calculate the amount of grain each county contributes
for county in counties:
    county["粟"] = Fraction(county["算"], county["費"]) / total算 * total_grain

# Assign results to variables
a = counties[0]["粟"]
b = counties[1]["粟"]
c = counties[2]["粟"]
d = counties[3]["粟"]
e = counties[4]["粟"]
f = counties[5]["粟"]

# Print results
print(f"甲縣 a = {a} 斛")
print(f"乙縣 b = {b} 斛")
print(f"丙縣 c = {c} 斛")
print(f"丁縣 d = {d} 斛")
print(f"戊縣 e = {e} 斛")
print(f"己縣 f = {f} 斛")


"""


### Explanation:
1. **Input Data**: The problem provides data for six counties, including their "算" (tax units), grain price per 斛, labor cost per day, and distance to the destination.
2. **Transportation Cost**: For counties other than 甲, the transportation cost per 1 斛 of grain is calculated based on the round trip time, labor cost, and car capacity.
3. **Normalize "算"**: The "算" values are divided by the cost per 1 斛 of grain to normalize them.
4. **Proportional Distribution**: The normalized "算" values are used to proportionally distribute the total grain (60000 斛) among the counties.
5. **Output**: The results are stored in variables `a`, `b`, `c`, `d`, `e`, and `f`, corresponding to the grain contributions of counties 甲, 乙, 丙, 丁, 戊, and 己, respectively.

This code ensures that the labor costs are evenly distributed while meeting the total grain requirement.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 582104053440000/32058598771
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 363147482880000/32058598771
Variable 'c' has wrong value. Expected: 960000/133, Actual: 233343851520000/32058598771
Variable 'd' has wrong value. Expected: 900000/133, Actual: 219031499700000/32058598771
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 292422758400000/32058598771
Variable 'f' has wrong value. Expected: 960000/133, Actual: 233466280320000/32058598771"""
