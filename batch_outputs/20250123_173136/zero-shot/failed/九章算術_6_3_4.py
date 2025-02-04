"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the amount of grain (in "斛") assigned to each county (甲, 乙, 丙, 丁, 戊, 己) such that the transportation costs are equalized. Here's the Python code:


"""


from fractions import Fraction

# Given data
# County data: (算, 粟價 (per 斛), 傭價 (per day), 到輸所 (里))
counties = {
    "甲": (42000, 20, 0, 0),  # 甲縣 has no transportation cost
    "乙": (34272, 18, 10, 70),
    "丙": (19328, 16, 5, 140),
    "丁": (17700, 14, 5, 175),
    "戊": (23040, 12, 5, 210),
    "己": (19136, 10, 5, 280),
}

# Constants
car_capacity = 25  # 車載二十五斛
heavy_speed = 50    # 重車日行五十里
empty_speed = 70    # 空車日行七十里
loading_unloading_days = 1  # 載輸之間各一日
total_grain = 60000  # 六縣賦粟六萬斛

# Calculate the cost per 斛 for each county
cost_per_hu = {}
for county, (算, 粟價, 傭價, distance) in counties.items():
    if distance == 0:  # No transportation cost for 甲縣
        transport_cost = 0
    else:
        # Calculate transportation time
        heavy_time = Fraction(distance, heavy_speed)
        empty_time = Fraction(distance, empty_speed)
        total_time = heavy_time + empty_time + loading_unloading_days
        # Total cost for transportation
        transport_cost = total_time * 傭價 * 6 / car_capacity
    # Total cost per 斛
    cost_per_hu[county] = 粟價 + transport_cost

# Normalize the 算數 (weights) for each county
normalized_weights = {county: Fraction(算, cost) for county, (算, _, _, _) in counties.items() for cost in [cost_per_hu[county]]}

# Calculate the total weight
total_weight = sum(normalized_weights.values())

# Calculate the grain assigned to each county
a = normalized_weights["甲"] * total_grain / total_weight
b = normalized_weights["乙"] * total_grain / total_weight
c = normalized_weights["丙"] * total_grain / total_weight
d = normalized_weights["丁"] * total_grain / total_weight
e = normalized_weights["戊"] * total_grain / total_weight
f = normalized_weights["己"] * total_grain / total_weight

# Results
a, b, c, d, e, f


"""


### Explanation of the Code:
1. **Input Data**: The data for each county includes the number of 算 (算數), the price of grain per 斛 (粟價), the daily wage for labor (傭價), and the distance to the delivery location (到輸所).

2. **Transportation Cost Calculation**:
   - For counties with transportation costs, the time required for a round trip (heavy and empty) is calculated.
   - The total transportation cost per 斛 is then computed based on the time, labor cost, and car capacity.

3. **Cost per 斛**:
   - The total cost per 斛 for each county is the sum of the grain price and the transportation cost.

4. **Normalized Weights**:
   - The 算數 for each county is divided by its cost per 斛 to normalize the weights.

5. **Grain Allocation**:
   - The total grain (60000 斛) is distributed among the counties in proportion to their normalized weights.

6. **Output**:
   - The variables `a`, `b`, `c`, `d`, `e`, and `f` represent the grain assigned to counties 甲, 乙, 丙, 丁, 戊, and 己, respectively.

This code ensures that the transportation costs are equalized across all counties while distributing the grain.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 582104053440000/32058598771
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 363147482880000/32058598771
Variable 'c' has wrong value. Expected: 960000/133, Actual: 233343851520000/32058598771
Variable 'd' has wrong value. Expected: 900000/133, Actual: 219031499700000/32058598771
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 292422758400000/32058598771
Variable 'f' has wrong value. Expected: 960000/133, Actual: 233466280320000/32058598771"""
