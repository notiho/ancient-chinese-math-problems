"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
To solve this problem, we need to calculate the amount of grain (粟) each county (縣) contributes such that the transportation cost per household is equalized. Here's the Python code to compute the values of \( a \), \( b \), \( c \), \( d \), and \( e \):


"""

#----- content starts here -----

from fractions import Fraction

# Given data
households = {
    "甲": 20520,
    "乙": 12312,
    "丙": 7182,
    "丁": 13338,
    "戊": 5130
}

grain_prices = {
    "甲": Fraction(120, 100),  # 1斛20錢 = 1.2斛
    "乙": Fraction(110, 100),  # 1斛10錢 = 1.1斛
    "丙": Fraction(112, 100),  # 1斛12錢 = 1.12斛
    "丁": Fraction(117, 100),  # 1斛17錢 = 1.17斛
    "戊": Fraction(113, 100)   # 1斛13錢 = 1.13斛
}

distances = {
    "甲": 0,    # 自輸其縣, distance = 0
    "乙": 200,  # 至輸所200里
    "丙": 150,  # 至輸所150里
    "丁": 250,  # 至輸所250里
    "戊": 150   # 至輸所150里
}

# Constants
grain_per_cart = 25  # 一車載25斛
transport_cost_per_li = 1  # 僦一里一錢
total_grain = 10000  # 輸粟一萬斛

# Calculate the cost per unit grain for each county
cost_per_grain = {}
for county in households:
    transport_cost = (distances[county] * transport_cost_per_li) / grain_per_cart
    cost_per_grain[county] = grain_prices[county] + Fraction(transport_cost)

# Calculate the衰 (weight) for each county
weights = {}
for county in households:
    weights[county] = households[county] / cost_per_grain[county]

# Normalize the weights to find the proportion of grain each county contributes
total_weight = sum(weights.values())
proportions = {county: weights[county] / total_weight for county in households}

# Calculate the grain contribution for each county
a = proportions["甲"] * total_grain
b = proportions["乙"] * total_grain
c = proportions["丙"] * total_grain
d = proportions["丁"] * total_grain
e = proportions["戊"] * total_grain

# Print results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**:
   - `households`: Number of households in each county.
   - `grain_prices`: Price of 1斛 of grain in each county.
   - `distances`: Distance from each county to the delivery location.

2. **Cost Calculation**:
   - For each county, the cost per unit of grain is calculated as the sum of the grain price and the transportation cost.

3. **Weight Calculation**:
   - The weight (衰) for each county is calculated as the number of households divided by the cost per unit of grain.

4. **Proportion Calculation**:
   - The weights are normalized to determine the proportion of the total grain each county contributes.

5. **Grain Contribution**:
   - The total grain (10000斛) is distributed among the counties based on their proportions.

### Output:
The variables `a`, `b`, `c`, `d`, and `e` represent the amount of grain (in斛) contributed by counties 甲, 乙, 丙, 丁, and 戊, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 10260000/2873, Actual: 1290042735800000/161257313291
Variable 'b' has wrong value. Expected: 6840000/2873, Actual: 102069315360000/161257313291
Variable 'c' has wrong value. Expected: 3990000/2873, Actual: 76098026550000/161257313291
Variable 'd' has wrong value. Expected: 380000/221, Actual: 90083557200000/161257313291
Variable 'e' has wrong value. Expected: 2700000/2873, Actual: 54279498000000/161257313291"""
