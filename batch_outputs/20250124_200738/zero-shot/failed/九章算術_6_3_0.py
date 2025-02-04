"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
To solve this problem, we need to calculate the amount of grain (in "斛") assigned to each county such that the labor costs and transportation costs are distributed equally. Below is the Python code that computes the values of the unknowns `a`, `b`, `c`, `d`, `e`, and `f` using the given method.


"""

#----- content starts here -----

from fractions import Fraction

# Inputs
# County data: (算, 粟價 (per 斛), 傭價 (per day), 到輸所里程)
counties = [
    (42000, Fraction(1, 20), 10, 70),   # 甲縣
    (34272, Fraction(1, 18), 10, 70),  # 乙縣
    (19328, Fraction(1, 16), 5, 140),  # 丙縣
    (17700, Fraction(1, 14), 5, 175),  # 丁縣
    (23040, Fraction(1, 12), 5, 210),  # 戊縣
    (19136, Fraction(1, 10), 5, 280)   # 己縣
]

# Constants
car_capacity = 25  # 車載量 (斛)
loaded_speed = 50   # 重車日行 (里)
empty_speed = 70    # 空車日行 (里)
extra_days = 1      # 載輸之間各一日
total_grain = 60000  # 總賦粟 (斛)

# Step 1: Calculate the cost per 斛 for each county
cost_per_hu = []
for 算, 粟價, 傭價, 里程 in counties:
    # Calculate the time for a round trip (重車 + 空車) and add extra days
    round_trip_days = Fraction(里程, loaded_speed) + Fraction(里程, empty_speed) + extra_days
    # Multiply by 6 people and daily wage, then divide by car capacity
    labor_cost_per_hu = (round_trip_days * 6 * 傭價) / car_capacity
    # Add the grain price per 斛
    total_cost_per_hu = labor_cost_per_hu + 粟價
    cost_per_hu.append(total_cost_per_hu)

# Step 2: Normalize the 算數 for each county
normalized_weights = []
for (算, _, _, _), cost in zip(counties, cost_per_hu):
    normalized_weight = 算 / cost
    normalized_weights.append(normalized_weight)

# Step 3: Calculate the total normalized weight
total_normalized_weight = sum(normalized_weights)

# Step 4: Calculate the grain assigned to each county
a = normalized_weights[0] * total_grain / total_normalized_weight
b = normalized_weights[1] * total_grain / total_normalized_weight
c = normalized_weights[2] * total_grain / total_normalized_weight
d = normalized_weights[3] * total_grain / total_normalized_weight
e = normalized_weights[4] * total_grain / total_normalized_weight
f = normalized_weights[5] * total_grain / total_normalized_weight

# Results
a, b, c, d, e, f
#----- content ends here -----


"""


### Explanation of the Code:
1. **Inputs**: The data for each county includes the number of 算, the price of grain per 斛, the daily wage for labor, and the distance to the delivery location.
2. **Cost Calculation**: For each county, the cost per 斛 is calculated by considering the transportation cost (round trip time, labor cost) and the grain price.
3. **Normalization**: The 算數 for each county is divided by the cost per 斛 to normalize the weights.
4. **Grain Distribution**: The total grain (60000 斛) is distributed among the counties based on their normalized weights.

### Output:
The variables `a`, `b`, `c`, `d`, `e`, and `f` represent the amount of grain (in 斛) assigned to counties 甲, 乙, 丙, 丁, 戊, and 己, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 14806870988669011980000000/865589332151712575767
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 12074236313765846482080000/865589332151712575767
Variable 'c' has wrong value. Expected: 960000/133, Actual: 7966220591196481336320000/865589332151712575767
Variable 'd' has wrong value. Expected: 900000/133, Actual: 6047470689883122017700000/865589332151712575767
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 6720197766742762214400000/865589332151712575767
Variable 'f' has wrong value. Expected: 960000/133, Actual: 4320363578845530515520000/865589332151712575767"""
