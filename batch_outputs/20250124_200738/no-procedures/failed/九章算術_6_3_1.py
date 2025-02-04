"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This is a classic ancient Chinese math problem involving proportional distribution of labor and resources to ensure fairness. The problem is complex and involves multiple variables, including distances, transportation costs, and the value of grain in different counties. Below is the Python code to solve this problem step by step.


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
counties = {
    "甲": {"算": 42000, "粟": 20, "距離": 0, "傭價": 0},  # 自輸 (no transportation cost)
    "乙": {"算": 34272, "粟": 18, "距離": 70, "傭價": 10},
    "丙": {"算": 19328, "粟": 16, "距離": 140, "傭價": 5},
    "丁": {"算": 17700, "粟": 14, "距離": 175, "傭價": 5},
    "戊": {"算": 23040, "粟": 12, "距離": 210, "傭價": 5},
    "己": {"算": 19136, "粟": 10, "距離": 280, "傭價": 5},
}

# Constants
total_grain = 60000  # Total grain to be distributed (斛)
car_capacity = 25  # Capacity of the cart (斛)
loaded_speed = 50  # Speed of the cart when loaded (里/日)
empty_speed = 70  # Speed of the cart when empty (里/日)
loading_unloading_time = 1  # Time for loading/unloading (日)

# Calculate the transportation cost for each county
for county, data in counties.items():
    if data["距離"] == 0:  # 自輸 (self-transport, no cost)
        data["運費"] = 0
    else:
        # Calculate round trip time
        round_trip_time = Fraction(data["距離"], loaded_speed) + Fraction(data["距離"], empty_speed) + loading_unloading_time
        # Calculate transportation cost per cart
        transport_cost_per_cart = round_trip_time * data["傭價"]
        # Calculate transportation cost per unit of grain
        data["運費"] = transport_cost_per_cart / car_capacity

# Calculate the total cost per unit of grain for each county
for county, data in counties.items():
    data["總成本"] = data["粟"] + data["運費"]

# Calculate the weighted "算" for each county
total_weighted_suan = sum(data["算"] / data["總成本"] for data in counties.values())

# Calculate the grain allocation for each county
results = {}
for county, data in counties.items():
    results[county] = Fraction(data["算"] / data["總成本"], total_weighted_suan) * total_grain

# Output the results
for county, grain in results.items():
    print(f"{county}縣得 {grain} 斛。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: Each county's data includes the number of "算" (a measure of contribution), the base cost of grain (粟), the distance to the delivery point (距離), and the daily wage for labor (傭價).
2. **Transportation Cost**: For counties that require transportation, the round trip time is calculated based on the loaded and empty speeds of the cart. The transportation cost per unit of grain is then derived.
3. **Total Cost**: The total cost per unit of grain for each county is the sum of the base grain cost and the transportation cost.
4. **Weighted Contribution**: The "算" for each county is divided by its total cost to determine its weighted contribution. The total weighted contribution across all counties is used to proportionally allocate the grain.
5. **Grain Allocation**: The grain is distributed proportionally based on the weighted contributions.

### Output:
The program will output the amount of grain (in 斛) allocated to each county, ensuring fairness based on the given parameters. For example:
```
甲縣得 a 斛。
乙縣得 b 斛。
丙縣得 c 斛。
丁縣得 d 斛。
戊縣得 e 斛。
己縣得 f 斛。
```

This approach ensures that the labor and transportation costs are fairly distributed among the counties.
"""


"""
Code error: both arguments should be Rational instances"""
