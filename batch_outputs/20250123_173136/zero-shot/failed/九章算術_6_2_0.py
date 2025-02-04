"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing a total of 10,000斛 of grain among five counties such that the cost of transportation and labor is equalized. The solution involves calculating the amount of grain each county contributes.

Here is the Python code:


"""


from fractions import Fraction

# Given data
total_grain = 10000  # Total grain to be distributed (in 斛)
transport_cost_per_li = 1  # Cost per li per car (in 錢)
car_capacity = 25  # Capacity of one car (in 斛)

# County data: (households, grain cost per 斛, distance to transport location)
counties = {
    "甲": (20520, Fraction(120, 100), 0),
    "乙": (12312, Fraction(110, 100), 200),
    "丙": (7182, Fraction(112, 100), 150),
    "丁": (13338, Fraction(117, 100), 250),
    "戊": (5130, Fraction(113, 100), 150),
}

# Calculate the "衰" (weight) for each county
weights = {}
for county, (households, grain_cost, distance) in counties.items():
    transport_cost_per_斛 = (transport_cost_per_li * distance) / car_capacity
    total_cost_per_斛 = grain_cost + transport_cost_per_斛
    weights[county] = households / total_cost_per_斛

# Normalize weights to calculate the grain distribution
total_weight = sum(weights.values())
grain_distribution = {county: (weight / total_weight) * total_grain for county, weight in weights.items()}

# Assign the results to variables
a = grain_distribution["甲"]
b = grain_distribution["乙"]
c = grain_distribution["丙"]
d = grain_distribution["丁"]
e = grain_distribution["戊"]

# Print the results
a, b, c, d, e


"""


### Explanation:
1. **Input Data**:
   - Each county has a number of households, a cost per 斛 of grain, and a distance to the transport location.
   - The cost of transporting one car (25斛) for one li is given as 1錢.

2. **Calculate Total Cost per 斛**:
   - For each county, the total cost per 斛 includes the grain cost and the transportation cost. The transportation cost is calculated as `(distance * transport cost per li) / car capacity`.

3. **Calculate Weights**:
   - The weight for each county is calculated as `households / total cost per 斛`.

4. **Normalize Weights**:
   - The weights are normalized by dividing each county's weight by the total weight and then multiplying by the total grain to be distributed.

5. **Assign Results**:
   - The grain distribution for each county is stored in variables `a`, `b`, `c`, `d`, and `e`.

### Output:
The variables `a`, `b`, `c`, `d`, and `e` contain the amount of grain (in 斛) that each county should contribute.
"""


"""
Variable 'a' has wrong value. Expected: 10260000/2873, Actual: 7999.902202711441
Variable 'b' has wrong value. Expected: 6840000/2873, Actual: 632.9592951595865
Variable 'c' has wrong value. Expected: 3990000/2873, Actual: 471.9043434183715
Variable 'd' has wrong value. Expected: 380000/221, Actual: 558.6323830004408
Variable 'e' has wrong value. Expected: 2700000/2873, Actual: 336.6017757101588"""
