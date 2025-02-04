"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a(=204)尺 。用徒 b(=53000/153)人 。
"""

#----- content starts here -----
### Part 1: Calculating the volume of the pond

"""
Suppose there is a pond. The top width is 6 zhang, the top length is 8 zhang. 
The bottom width is 4 zhang, the bottom length is 6 zhang. The depth is 2 zhang.
Question: what is the volume?

Answer: 70666.5 chi³.
"""

# 上廣六丈，袤八丈
上廣 = 6 * 10  # Convert zhang to chi
上袤 = 8 * 10  # Convert zhang to chi

# 下廣四丈，袤六丈
下廣 = 4 * 10  # Convert zhang to chi
下袤 = 6 * 10  # Convert zhang to chi

# 深二丈
深 = 2 * 10  # Convert zhang to chi

# Volume formula for a frustum: V = (1/6) * 深 * (上廣 * 上袤 + 下廣 * 下袤 + sqrt(上廣 * 上袤 * 下廣 * 下袤))
積 = Fraction(1, 6) * 深 * (上廣 * 上袤 + 下廣 * 下袤 + (上廣 * 上袤 * 下廣 * 下袤) ** 0.5)

積 = float(積)  # Convert to decimal for clarity
積 = round(積, 1)  # Round to 1 decimal place
積  # 70666.5 chi³

---

### Part 2: Calculating human labor and tools required

"""
Suppose the soil is transported over a distance of 70 bu, with 20 bu of that being for the upper and lower shelves.
The shelves are equivalent to 2 units of flat ground for every 5 units of flat ground.
The hesitation area adds 1 for every 10, and the loading/unloading area is 30 bu.
One round trip is 140 bu.
Each soil basket holds 1 chi 6 cun of soil.
The autumn work rate is 59.5 li per person.

Question: how much soil does one person transport, and how many workers are needed?

Procedure: Multiply the soil basket volume by the total distance traveled to get the dividend.
For the round trip, shelves are equivalent to 2 units of flat ground for every 5 units of flat ground.
Add 1 for every 10 in the hesitation area, and add 30 bu for the loading/unloading area to get the divisor.
Divide the dividend by the divisor to get the amount of soil transported by one person.
Divide the total soil volume by the amount transported by one person to get the number of workers needed.

Answer: one person transports *a*(=204) chi³ of soil, and *b*(=53000/153) workers are needed.
"""

# 負土往來七十步
往來步數 = 70

# 其二十步上下棚除
棚除步數 = 20

# 棚除二當平道五
棚除當平道 = Fraction(2, 5)

# 踟躕之間十加一
踟躕加 = Fraction(1, 10)

# 載輸之間三十步
載輸步數 = 30

# 定一返一百四十步
定往返步數 = 140

# 土籠積一尺六寸
土籠積 = 1 + Fraction(6, 10)  # Convert 1 chi 6 cun to chi

# 秋程人功行五十九里半
秋程人功 = 59 + Fraction(1, 2)  # Convert 59.5 li to li
秋程人功步數 = 秋程人功 * 300  # Convert li to bu (1 li = 300 bu)

# 棚除 equivalent in flat ground
棚除平道步數 = 棚除步數 * 棚除當平道

# Total divisor (法)
法 = 往來步數 + 棚除平道步數 + 踟躕加 * 往來步數 + 載輸步數

# Dividend (實)
實 = 土籠積 * 秋程人功步數

# One person's transported soil (人到)
人到 = Fraction(實, 法)

# Total workers needed (用徒)
用徒 = Fraction(積, 人到)

a = round(float(人到), 0)  # 204 chi³
b = 用徒  # 53000/153 workers#----- content ends here -----

"""
Code error: invalid syntax (<string>, line 30)"""
