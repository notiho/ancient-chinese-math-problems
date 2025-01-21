"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This problem is quite complex and involves multiple steps to calculate the distribution of costs and the amount of grain each county should contribute. Below is the Python code that follows the procedure described in the problem:


"""


from fractions import Fraction

# Data for each county
counties = [
    {"算": 42000, "粟價": 20, "傭價": 10, "道里": 0},    # 甲縣
    {"算": 34272, "粟價": 18, "傭價": 10, "道里": 70},   # 乙縣
    {"算": 19328, "粟價": 16, "傭價": 5, "道里": 140},   # 丙縣
    {"算": 17700, "粟價": 14, "傭價": 5, "道里": 175},   # 丁縣
    {"算": 23040, "粟價": 12, "傭價": 5, "道里": 210},   # 戊縣
    {"算": 19136, "粟價": 10, "傭價": 5, "道里": 280},   # 己縣
]

# Constants
車載 = 25  # 車載二十五斛
重車日行 = 50  # 重車日行五十里
空車日行 = 70  # 空車日行七十里
載輸日 = 1  # 載輸之間各一日
總粟 = 60000  # 六縣賦粟六萬斛

# Step 1: Calculate the cost of transporting one 斛 of grain for each county
for county in counties:
    道里 = county["道里"]
    if 道里 == 0:
        county["一斛費"] = county["粟價"]  # 甲縣直接輸送，無運輸費
    else:
        # 以車程行空、重相乘為法
        法 = 重車日行 * 空車日行

        # 并空、重以乘道里，各自為實
        重車實 = 空車日行 * 道里
        空車實 = 重車日行 * 道里

        # 實如法得一日
        一日 = Fraction(重車實 + 空車實, 法)

        # 加載輸各一日
        總日 = 一日 + 載輸日

        # 而以六人乘之
        總日 *= 6

        # 又以傭價乘之
        總費 = 總日 * county["傭價"]

        # 以二十五斛除之
        每斛運費 = Fraction(總費, 車載)

        # 加一斛粟價，即致一斛之費
        county["一斛費"] = 每斛運費 + county["粟價"]

# Step 2: Normalize the costs to distribute the grain proportionally
# 各以約其算數為衰
for county in counties:
    county["衰"] = Fraction(county["算"], county["一斛費"])

# 副并為法
法 = sum(county["衰"] for county in counties)

# 以所賦粟乘未并者，各自為實
for county in counties:
    county["實"] = Fraction(總粟 * county["衰"], 法)

# 實如法得一斛
results = [county["實"] for county in counties]

# Output results
a, b, c, d, e, f = results


"""


### Explanation of the Code:
1. **Step 1: Calculate the cost of transporting one 斛 of grain for each county.**
   - For counties other than 甲縣, the transportation cost is calculated based on the distance (`道里`), the speed of the loaded and empty cart, the number of people involved, and the wage per person per day.
   - The total cost per 斛 includes the transportation cost and the base price of the grain.

2. **Step 2: Normalize the costs to distribute the grain proportionally.**
   - The contribution of each county is weighted by the ratio of its "算" to the cost of one 斛 of grain.
   - The total grain (`總粟`) is then distributed proportionally based on these weights.

3. **Output:**
   - The results (`a`, `b`, `c`, `d`, `e`, `f`) represent the amount of grain each county should contribute.

### Results:
- `a`: Amount of grain contributed by 甲縣.
- `b`: Amount of grain contributed by 乙縣.
- `c`: Amount of grain contributed by 丙縣.
- `d`: Amount of grain contributed by 丁縣.
- `e`: Amount of grain contributed by 戊縣.
- `f`: Amount of grain contributed by 己縣.
"""


"""
Variable 'a' has wrong value. Expected: 360000/19, Actual: 582104053440000/32058598771
Variable 'b' has wrong value. Expected: 1440000/133, Actual: 363147482880000/32058598771
Variable 'c' has wrong value. Expected: 960000/133, Actual: 233343851520000/32058598771
Variable 'd' has wrong value. Expected: 900000/133, Actual: 219031499700000/32058598771
Variable 'e' has wrong value. Expected: 1200000/133, Actual: 292422758400000/32058598771
Variable 'f' has wrong value. Expected: 960000/133, Actual: 233466280320000/32058598771"""
