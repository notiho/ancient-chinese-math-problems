"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing a total of 10,000斛 of grain among five counties such that the cost of transportation and labor is equalized. The solution involves calculating the proportional "衰" (weights) for each county and then distributing the grain accordingly.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_grain = 10000  # Total grain to be distributed (in 斛)
transport_cost_per_li = 1  # Cost per li for transporting one car
car_capacity = 25  # Capacity of one car (in 斛)

# County data: (households, grain price per 斛, distance to transport location)
counties = {
    "甲": (20520, Fraction(120, 100), 0),
    "乙": (12312, Fraction(110, 100), 200),
    "丙": (7182, Fraction(112, 100), 150),
    "丁": (13338, Fraction(117, 100), 250),
    "戊": (5130, Fraction(113, 100), 150),
}

# Calculate weights (衰) for each county
weights = {}
for county, (households, grain_price, distance) in counties.items():
    cost_per_斛 = grain_price + Fraction(transport_cost_per_li * distance, car_capacity)
    weights[county] = households / cost_per_斛

# Normalize weights and calculate grain distribution
total_weight = sum(weights.values())
grain_distribution = {county: total_grain * weight / total_weight for county, weight in weights.items()}

# Assign results to variables
a = grain_distribution["甲"]
b = grain_distribution["乙"]
c = grain_distribution["丙"]
d = grain_distribution["丁"]
e = grain_distribution["戊"]

# Results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation:
1. **Input Data**:
   - Each county has a number of households, a grain price per 斛, and a distance to the transport location.
   - The cost per 斛 includes the grain price and the transportation cost (calculated as `distance * transport_cost_per_li / car_capacity`).

2. **Weights (衰)**:
   - The weight for each county is calculated as `households / cost_per_斛`.

3. **Normalization**:
   - The weights are normalized by dividing each weight by the total weight.

4. **Grain Distribution**:
   - The total grain (10,000斛) is distributed proportionally to the normalized weights.

5. **Output**:
   - The grain distribution for each county is stored in variables `a`, `b`, `c`, `d`, and `e`.

This code calculates the grain distribution while ensuring that the transportation and labor costs are equalized across counties.
"""


"""
Variable 'a' has wrong value. Expected: 10260000/2873, Actual: 1290042735800000/161257313291
Variable 'b' has wrong value. Expected: 6840000/2873, Actual: 102069315360000/161257313291
Variable 'c' has wrong value. Expected: 3990000/2873, Actual: 76098026550000/161257313291
Variable 'd' has wrong value. Expected: 380000/221, Actual: 90083557200000/161257313291
Variable 'e' has wrong value. Expected: 2700000/2873, Actual: 54279498000000/161257313291"""
