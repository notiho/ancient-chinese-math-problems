"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the amount of grain (in "斛") assigned to each county such that the labor costs are equalized. The solution involves using fractions to ensure accuracy.

Here is the Python code:


"""


from fractions import Fraction

# Constants
total_grain = 60000  # Total grain to be distributed (in 斛)
car_capacity = 25  # Car capacity (in 斛)
loaded_speed = 50  # Loaded car speed (in 里/day)
empty_speed = 70  # Empty car speed (in 里/day)
loading_unloading_time = 1  # Time for loading/unloading (in days)
people_per_car = 6  # Number of people per car

# County data
counties = [
    {"name": "甲", "算": 42000, "grain_price": 20, "wage": 10, "distance": 0},
    {"name": "乙", "算": 34272, "grain_price": 18, "wage": 10, "distance": 70},
    {"name": "丙", "算": 19328, "grain_price": 16, "wage": 5, "distance": 140},
    {"name": "丁", "算": 17700, "grain_price": 14, "wage": 5, "distance": 175},
    {"name": "戊", "算": 23040, "grain_price": 12, "wage": 5, "distance": 210},
    {"name": "己", "算": 19136, "grain_price": 10, "wage": 5, "distance": 280},
]

# Calculate the cost per 斛 for each county
for county in counties:
    distance = county["distance"]
    wage = county["wage"]
    grain_price = county["grain_price"]

    # Time for a round trip (loaded + empty) in days
    round_trip_time = Fraction(distance, loaded_speed) + Fraction(distance, empty_speed)

    # Total time per trip (including loading/unloading)
    total_trip_time = round_trip_time + 2 * loading_unloading_time

    # Total labor cost per trip
    labor_cost_per_trip = total_trip_time * people_per_car * wage

    # Cost per 斛 (including grain price)
    cost_per_grain = labor_cost_per_trip / car_capacity + grain_price

    # Store the cost per 斛 in the county data
    county["cost_per_grain"] = cost_per_grain

# Normalize the "算" values by the cost per 斛
total_normalized = sum(Fraction(county["算"], county["cost_per_grain"]) for county in counties)

# Calculate the grain allocation for each county
for county in counties:
    county["grain_allocation"] = Fraction(county["算"], county["cost_per_grain"]) / total_normalized * total_grain

# Assign the results to variables
a = counties[0]["grain_allocation"]
b = counties[1]["grain_allocation"]
c = counties[2]["grain_allocation"]
d = counties[3]["grain_allocation"]
e = counties[4]["grain_allocation"]
f = counties[5]["grain_allocation"]

# Print the results
print(f"甲縣 a = {a} 斛")
print(f"乙縣 b = {b} 斛")
print(f"丙縣 c = {c} 斛")
print(f"丁縣 d = {d} 斛")
print(f"戊縣 e = {e} 斛")
print(f"己縣 f = {f} 斛")


"""


### Explanation:
1. **Input Data**: The problem provides data for six counties, including their "算" values, grain prices, wage rates, and distances to the delivery location.
2. **Cost Calculation**: For each county, the cost per 斛 is calculated based on the round-trip time, labor costs, and grain price.
3. **Normalization**: The "算" values are normalized by dividing them by the cost per 斛. This ensures that the labor costs are equalized across counties.
4. **Grain Allocation**: The grain allocation for each county is calculated proportionally based on the normalized "算" values.
5. **Output**: The results are stored in variables `a`, `b`, `c`, `d`, `e`, and `f` and printed.

This code ensures that the labor costs are equalized while distributing the total grain among the counties.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 9000000/553
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 44640000/3871
Variable 'c' has wrong value. Expected: 960000/133, Actual: 29760000/3871
Variable 'd' has wrong value. Expected: 900000/133, Actual: 27900000/3871
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 37200000/3871
Variable 'f' has wrong value. Expected: 960000/133, Actual: 29760000/3871"""
