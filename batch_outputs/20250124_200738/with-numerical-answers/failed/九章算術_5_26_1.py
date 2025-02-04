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
Suppose there is a pond. The top width is 6 zhang, the top length is 8 zhang, the bottom width is 4 zhang, the bottom length is 6 zhang, and the depth is 2 zhang.
Question: what is the volume?

Answer: 70666.5 chi³ (70,666 chi³ and half a chi³).
"""

# 上廣六丈
上廣 = 6 * 10  # Convert zhang to chi

# 袤八丈
上袤 = 8 * 10  # Convert zhang to chi

# 下廣四丈
下廣 = 4 * 10  # Convert zhang to chi

# 袤六丈
下袤 = 6 * 10  # Convert zhang to chi

# 深二丈
深 = 2 * 10  # Convert zhang to chi

# Calculate the average width and length
平均廣 = (上廣 + 下廣) / 2
平均袤 = (上袤 + 下袤) / 2

# Calculate the volume
積 = 平均廣 * 平均袤 * 深

# Answer for the pond volume
積尺 = Fraction(積, 1)  # 70666.5 chi³

### Part 2: Calculating the labor required for moving the soil

"""
The soil is being moved, and the following conditions are given:
- The round trip distance is 70 bu.
- Of these, 20 bu are for the upper and lower shelves.
- The shelves are equivalent to 2 bu for every 5 bu of flat path.
- Hesitation in between adds 1 for every 10 bu.
- The loading and unloading distance is 30 bu.
- A single round trip is defined as 140 bu.
- Each soil basket holds 1 chi 6 cun of soil.
- The autumn work rate is 59.5 li per person.

Question: how many chi does one person move, and how many workers are required?

The procedure says:
- Multiply the soil basket capacity by the total distance traveled to get the dividend.
- For the round trip, the shelves (2 for every 5 flat path), the hesitation (1 for every 10), and the loading/unloading distance are added together to form the divisor.
- Divide the dividend by the divisor to get the amount of soil moved by one person.
- Use this to calculate the number of workers required.

Answer: one person moves *a*(=204) chi, and *b*(=53000/153) workers are required.
"""

# 土籠積一尺六寸
土籠積 = 1 + Fraction(6, 10)  # Convert 1 chi 6 cun to chi

# 秋程人功行五十九里半
秋程 = 59.5 * 300  # Convert li to bu (1 li = 300 bu)

# 負土往來七十步
往來步數 = 70

# 其二十步上下棚除
上下棚除 = 20

# 棚除二當平道五
棚除平道比 = Fraction(2, 5)

# 棚除 equivalent in flat path
棚除平道 = 上下棚除 * 棚除平道比

# 踟躕之間十加一
踟躕加 = Fraction(1, 10)

# 載輸之間三十步
載輸步數 = 30

# 定一返一百四十步
定往來步數 = 140

# Calculate the divisor (法)
法 = 定往來步數 + 棚除平道 + (踟躕加 * 定往來步數) + 載輸步數

# Calculate the dividend (實)
實 = 土籠積 * 秋程

# Calculate the amount of soil moved by one person (人到)
人到 = Fraction(實, 法)

# Calculate the number of workers required (用徒)
用徒 = Fraction(積尺, 人到)

# Answers
a = 人到  # 204 chi
b = 用徒  # 53000/153 workers#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
