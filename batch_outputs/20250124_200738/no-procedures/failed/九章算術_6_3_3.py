"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This is a complex ancient Chinese math problem involving the distribution of grain (粟) among six counties, considering transportation costs, labor costs, and the value of grain. The goal is to allocate the total grain (60,000斛) among the six counties such that the total cost (including labor and transportation) is equalized.

To solve this problem programmatically, we need to calculate the grain allocation for each county while balancing the costs. Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
total_grain = 60000  # Total grain to be distributed (斛)
car_capacity = 25  # Car capacity in hu (斛)
loaded_speed = 50  # Loaded car speed in li per day
empty_speed = 70  # Empty car speed in li per day
loading_unloading_time = 1  # Time for loading/unloading in days

# County data: [number of households (算), grain price per hu (錢), labor cost per day (錢), distance to transport location (里)]
counties = [
    [42000, 120, 0, 0],    # 甲縣
    [34272, 118, 10, 70],  # 乙縣
    [19328, 116, 5, 140],  # 丙縣
    [17700, 114, 5, 175],  # 丁縣
    [23040, 112, 5, 210],  # 戊縣
    [19136, 110, 5, 280],  # 己縣
]

# Function to calculate transportation cost for a given distance
def transport_cost(distance, labor_cost):
    # Total round trip time (days)
    round_trip_time = Fraction(distance, loaded_speed) + Fraction(distance, empty_speed) + 2 * loading_unloading_time
    # Total cost per hu for transportation
    return round_trip_time * labor_cost / car_capacity

# Calculate the total cost per hu for each county
total_costs = []
for households, grain_price, labor_cost, distance in counties:
    transport = transport_cost(distance, labor_cost)
    total_cost = grain_price + transport
    total_costs.append(total_cost)

# Inverse the total costs to calculate the proportion of grain each county should receive
inverse_costs = [1 / cost for cost in total_costs]
total_inverse_costs = sum(inverse_costs)

# Calculate the grain allocation for each county
allocations = [Fraction(inverse_cost, total_inverse_costs) * total_grain for inverse_cost in inverse_costs]

# Output the results
a, b, c, d, e, f = allocations
print(f"甲縣: {a} 斛")
print(f"乙縣: {b} 斛")
print(f"丙縣: {c} 斛")
print(f"丁縣: {d} 斛")
print(f"戊縣: {e} 斛")
print(f"己縣: {f} 斛")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: The data for each county includes the number of households, the price of grain per hu, the labor cost per day, and the distance to the transport location.
2. **Transportation Cost**: The transportation cost is calculated based on the round trip time and labor cost, divided by the car's capacity.
3. **Total Cost**: The total cost per hu for each county is the sum of the grain price and the transportation cost.
4. **Inverse Costs**: To balance the costs, the grain is allocated inversely proportional to the total costs.
5. **Grain Allocation**: The grain is distributed among the counties based on the calculated proportions.

### Output:
The program will output the amount of grain (in hu) allocated to each county:
```
甲縣: a 斛
乙縣: b 斛
丙縣: c 斛
丁縣: d 斛
戊縣: e 斛
己縣: f 斛
```

This approach ensures that the costs are balanced across all counties.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 117408086308890000/12102911372719
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 117643373055000000/12102911372719
Variable 'c' has wrong value. Expected: 960000/133, Actual: 120049168005000000/12102911372719
Variable 'd' has wrong value. Expected: 900000/133, Actual: 121876906203000000/12102911372719
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 123761159145000000/12102911372719
Variable 'f' has wrong value. Expected: 960000/133, Actual: 125435989646250000/12102911372719"""
