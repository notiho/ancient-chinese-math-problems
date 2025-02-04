"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This is a complex ancient Chinese problem involving proportional distribution of resources (粟) based on transportation costs and labor, ensuring equalized labor costs across multiple counties. Below is the Python code that follows the procedure ("術") step by step:


"""

#----- content starts here -----

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
載輸各一日 = 1  # 載輸之間各一日
總粟 = 60000  # 六縣賦粟六萬斛

# Step 1: Calculate the cost to transport one 斛 of 粟 for each county
for county in counties:
    道里 = county["道里"]
    傭價 = county["傭價"]
    粟價 = county["粟價"]

    # 空車日數 = 道里 / 空車日行
    空車日數 = Fraction(道里, 空車日行)

    # 重車日數 = 道里 / 重車日行
    重車日數 = Fraction(道里, 重車日行)

    # 車程行空、重相乘為法
    法 = 空車日數 * 重車日數

    # 并空、重以乘道里，各自為實
    實 = (空車日數 + 重車日數) * 道里

    # 實如法得一日
    一日 = Fraction(實, 法)

    # 加載輸各一日
    總日數 = 一日 + 載輸各一日

    # 以六人乘之
    總日數 *= 6

    # 又以傭價乘之
    總費用 = 總日數 * 傭價

    # 以二十五斛除之
    每斛費用 = Fraction(總費用, 車載)

    # 加一斛粟價，即致一斛之費
    每斛總費用 = 每斛費用 + 粟價

    # Store the cost per 斛 in the county data
    county["每斛費用"] = 每斛總費用

# Step 2: Normalize the costs to distribute 粟 proportionally
# 各以約其算數為衰
for county in counties:
    county["衰"] = Fraction(county["算"], county["每斛費用"])

# 副并為法
法 = sum(county["衰"] for county in counties)

# 以所賦粟乘未并者，各自為實
for county in counties:
    county["實"] = 總粟 * county["衰"]

# 實如法得一斛
for county in counties:
    county["粟"] = Fraction(county["實"], 法)

# Results
a = counties[0]["粟"]  # 甲縣
b = counties[1]["粟"]  # 乙縣
c = counties[2]["粟"]  # 丙縣
d = counties[3]["粟"]  # 丁縣
e = counties[4]["粟"]  # 戊縣
f = counties[5]["粟"]  # 己縣

# Output the results
a, b, c, d, e, f
#----- content ends here -----


"""


### Explanation of the Code:
1. **Step 1**: Calculate the cost to transport one 斛 of 粟 for each county based on the distance, labor cost, and other parameters. This involves calculating the total days required for transportation (including empty and loaded trips) and converting it into a cost per 斛.
2. **Step 2**: Normalize the costs using the "算" (tax units) for each county to determine the proportional distribution of 粟.
3. **Final Step**: Use the normalized values to distribute the total 粟 (60000 斛) among the counties.

### Output:
The variables `a`, `b`, `c`, `d`, `e`, and `f` represent the amount of 粟 allocated to 甲縣, 乙縣, 丙縣, 丁縣, 戊縣, and 己縣, respectively. These are expressed as fractions for precise representation.
"""


"""
Code error: Fraction(0, 0)"""
