"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
To solve this problem, we need to calculate the amount of grain (in "斛") each county contributes, such that the labor costs and grain costs are equally distributed. Below is the Python code to compute the values of the unknowns `a`, `b`, `c`, `d`, `e`, and `f`:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
total_grain = 60000  # Total grain in 斛
car_capacity = 25  # Car capacity in 斛
heavy_speed = 50  # Heavy car speed in 里 per day
empty_speed = 70  # Empty car speed in 里 per day
load_unload_time = 1  # Loading/unloading time in days
people_per_car = 6  # People per car

# County data
counties = [
    {"name": "甲", "算": 42000, "grain_price": 20, "wage": 10, "distance": 0},
    {"name": "乙", "算": 34272, "grain_price": 18, "wage": 10, "distance": 70},
    {"name": "丙", "算": 19328, "grain_price": 16, "wage": 5, "distance": 140},
    {"name": "丁", "算": 17700, "grain_price": 14, "wage": 5, "distance": 175},
    {"name": "戊", "算": 23040, "grain_price": 12, "wage": 5, "distance": 210},
    {"name": "己", "算": 19136, "grain_price": 10, "wage": 5, "distance": 280},
]

# Step 1: Calculate the cost per 斛 for each county
for county in counties:
    distance = county["distance"]
    wage = county["wage"]
    grain_price = county["grain_price"]

    # Travel time for one round trip (heavy + empty + load/unload)
    heavy_time = Fraction(distance, heavy_speed)
    empty_time = Fraction(distance, empty_speed)
    total_time = heavy_time + empty_time + load_unload_time

    # Total labor cost for one round trip
    labor_cost = total_time * people_per_car * wage

    # Cost per 斛
    county["cost_per_grain"] = labor_cost / car_capacity + grain_price

# Step 2: Normalize the "算" values to calculate the grain distribution
total_cost_per_grain = sum(county["算"] / county["cost_per_grain"] for county in counties)
scaling_factor = total_grain / total_cost_per_grain

# Step 3: Calculate the grain contribution for each county
a = Fraction(counties[0]["算"], counties[0]["cost_per_grain"]) * scaling_factor
b = Fraction(counties[1]["算"], counties[1]["cost_per_grain"]) * scaling_factor
c = Fraction(counties[2]["算"], counties[2]["cost_per_grain"]) * scaling_factor
d = Fraction(counties[3]["算"], counties[3]["cost_per_grain"]) * scaling_factor
e = Fraction(counties[4]["算"], counties[4]["cost_per_grain"]) * scaling_factor
f = Fraction(counties[5]["算"], counties[5]["cost_per_grain"]) * scaling_factor

# Results
a, b, c, d, e, f
#----- content ends here -----


"""


### Explanation:
1. **Cost per 斛 Calculation**:
   - For each county, calculate the total time for a round trip (heavy + empty + load/unload).
   - Compute the labor cost for the round trip and divide it by the car capacity to get the labor cost per 斛.
   - Add the grain price to the labor cost per 斛 to get the total cost per 斛.

2. **Normalization**:
   - Normalize the "算" values by dividing them by the cost per 斛 for each county.
   - Compute the scaling factor to ensure the total grain distributed equals 60000 斛.

3. **Grain Contribution**:
   - Multiply the normalized "算" values by the scaling factor to get the grain contribution for each county.

The variables `a`, `b`, `c`, `d`, `e`, and `f` represent the grain contributions for counties 甲, 乙, 丙, 丁, 戊, and 己, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 519735762000000/31019127247
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 363147482880000/31019127247
Variable 'c' has wrong value. Expected: 960000/133, Actual: 233343851520000/31019127247
Variable 'd' has wrong value. Expected: 900000/133, Actual: 219031499700000/31019127247
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 292422758400000/31019127247
Variable 'f' has wrong value. Expected: 960000/133, Actual: 233466280320000/31019127247"""
