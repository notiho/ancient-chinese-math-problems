"""
今有均賦粟甲縣四萬二千算粟一斛二十自輸其縣乙縣三萬四千二百七十二算粟一斛一十八傭價一日一十錢到輸所七十里丙縣一萬九千三百二十八算粟一斛一十六傭價一日五錢到輸所一百四十里丁縣一萬七千七百算粟一斛一十四傭價一日五錢到輸所一百七十五里戊縣二萬三千四十算粟一斛一十二傭價一日五錢到輸所二百一十里己縣一萬九千一百三十六算粟一斛一十傭價一日五錢到輸所二百八十里凡六縣賦粟六萬斛皆輸甲縣六人共車車載二十五斛重車日行五十里空車日行七十里載輸之間各一日粟有貴賤傭各別價以算出錢令費勞等問縣各粟幾何
術曰以車程行空重相乘為法并空重以乘道里各自為實實如法得一日加載輸各一日而以六人乘之又以傭價乘之以二十五斛除之加一斛粟價即致一斛之費各以約其算數為衰副并為法以所賦粟乘未并者各自為實實如法得一斛
荅曰甲縣 a斛 乙縣 b斛 丙縣 c斛 丁縣 d斛 戊縣 e斛 己縣 f斛 
"""

"""
This problem is quite complex and involves multiple steps to calculate the distribution of grain among six counties while considering transportation costs, labor costs, and grain prices. Let's break it down step by step and encode the procedure into Python.


"""


from fractions import Fraction

# Data for each county
# Each entry is in the format: (total grain assigned, grain price per hu, labor cost per day, distance to the destination)
counties = {
    "甲": (42000, 20, 10, 70),
    "乙": (34272, 18, 10, 70),
    "丙": (19328, 16, 5, 140),
    "丁": (17700, 14, 5, 175),
    "戊": (23040, 12, 5, 210),
    "己": (19136, 10, 5, 280),
}

# Constants
car_capacity = 25  # A cart can carry 25 hu of grain
heavy_speed = 50    # Distance traveled per day with a loaded cart
empty_speed = 70    # Distance traveled per day with an empty cart
loading_unloading_days = 1  # Days required for loading and unloading
workers_per_cart = 6  # Number of workers per cart

# Step 1: Calculate the cost to transport 1 hu of grain for each county
transport_costs = {}
for county, (total_grain, grain_price, labor_cost, distance) in counties.items():
    # Calculate the total days required for a round trip
    heavy_days = Fraction(distance, heavy_speed)
    empty_days = Fraction(distance, empty_speed)
    total_days = heavy_days + empty_days + 2 * loading_unloading_days

    # Calculate the labor cost for transporting 1 hu of grain
    labor_cost_per_hu = (total_days * workers_per_cart * labor_cost) / car_capacity

    # Add the grain price to the labor cost to get the total cost per hu
    total_cost_per_hu = labor_cost_per_hu + grain_price

    # Store the transport cost for this county
    transport_costs[county] = total_cost_per_hu

# Step 2: Normalize the transport costs to distribute the grain proportionally
# Calculate the inverse of the transport costs (衰副) and sum them up (法)
inverse_costs = {county: Fraction(1, cost) for county, cost in transport_costs.items()}
法 = sum(inverse_costs.values())

# Step 3: Calculate the grain distribution for each county
grain_distribution = {}
for county, (total_grain, _, _, _) in counties.items():
    # Calculate the proportion of grain for this county
    proportion = inverse_costs[county] / 法

    # Multiply the proportion by the total grain to get the grain assigned to this county
    grain_distribution[county] = proportion * total_grain

# Step 4: Output the results
a = grain_distribution["甲"]
b = grain_distribution["乙"]
c = grain_distribution["丙"]
d = grain_distribution["丁"]
e = grain_distribution["戊"]
f = grain_distribution["己"]

print(f"甲縣 {a}斛")
print(f"乙縣 {b}斛")
print(f"丙縣 {c}斛")
print(f"丁縣 {d}斛")
print(f"戊縣 {e}斛")
print(f"己縣 {f}斛")


"""


### Explanation of the Code:
1. **County Data**: Each county has its assigned grain, grain price, labor cost, and distance to the destination.
2. **Transport Cost Calculation**: For each county, the total cost to transport 1 hu of grain is calculated based on the round-trip distance, labor costs, and grain price.
3. **Normalization**: The inverse of the transport costs is used to normalize the distribution of grain among the counties.
4. **Grain Distribution**: The total grain assigned to each county is calculated proportionally based on the normalized transport costs.
5. **Output**: The grain distribution for each county is printed.

This code follows the procedure described in the problem and ensures that the grain is distributed fairly based on the costs.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 9585811740960000/1651001966723
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 8369783051535360/1651001966723
Variable 'c' has wrong value. Expected: 960000/133, Actual: 5579855367690240/1651001966723
Variable 'd' has wrong value. Expected: 900000/133, Actual: 5231114407209600/1651001966723
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 6974819209612800/1651001966723
Variable 'f' has wrong value. Expected: 960000/133, Actual: 5579855367690240/1651001966723"""
