"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing the total amount of grain (10,000斛) among five counties such that the cost of transportation and grain is equally distributed. The solution involves calculating the "effort" (費勞) for each county and then determining the amount of grain each county should contribute.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
# Format: (number of households, grain cost per 斛, distance to transport in 里)
counties = {
    "甲": (20520, Fraction(120, 100), 0),
    "乙": (12312, Fraction(110, 100), 200),
    "丙": (7182, Fraction(112, 100), 150),
    "丁": (13338, Fraction(117, 100), 250),
    "戊": (5130, Fraction(113, 100), 150)
}

# Constants
total_grain = 10000  # Total grain to be distributed (in 斛)
grain_per_cart = 25  # A cart carries 25 斛
transport_cost_per_li = 1  # Cost of transporting 1 cart 1 里 (in 錢)

# Calculate the "effort" (衰) for each county
efforts = {}
for county, (households, grain_cost, distance) in counties.items():
    transport_cost_per_grain = Fraction(transport_cost_per_li * distance, grain_per_cart)
    total_cost_per_grain = grain_cost + transport_cost_per_grain
    efforts[county] = households / total_cost_per_grain

# Calculate the total effort
total_effort = sum(efforts.values())

# Calculate the grain contribution for each county
results = {}
for county, effort in efforts.items():
    results[county] = total_grain * Fraction(effort, total_effort)

# Assign results to variables
a = results["甲"]
b = results["乙"]
c = results["丙"]
d = results["丁"]
e = results["戊"]

# Output the results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation:
1. **Input Data**: Each county has data for the number of households, the cost of grain per 斛, and the distance to the transport location in 里.
2. **Effort Calculation**: The effort (衰) for each county is calculated as the number of households divided by the total cost per 斛 (grain cost + transport cost).
3. **Total Effort**: The sum of efforts for all counties is calculated.
4. **Grain Distribution**: The grain contribution for each county is proportional to its effort relative to the total effort.
5. **Results**: The grain contributions for each county are stored in variables `a`, `b`, `c`, `d`, and `e`.

### Output:
The variables `a`, `b`, `c`, `d`, and `e` will contain the grain contributions (in 斛) for counties 甲, 乙, 丙, 丁, and 戊, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 10260000/2873, Actual: 1290042735800000/161257313291
Variable 'b' has wrong value. Expected: 6840000/2873, Actual: 102069315360000/161257313291
Variable 'c' has wrong value. Expected: 3990000/2873, Actual: 76098026550000/161257313291
Variable 'd' has wrong value. Expected: 380000/221, Actual: 90083557200000/161257313291
Variable 'e' has wrong value. Expected: 2700000/2873, Actual: 54279498000000/161257313291"""
