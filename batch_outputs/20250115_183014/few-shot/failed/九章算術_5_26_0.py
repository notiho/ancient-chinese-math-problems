"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

### Part 1: Calculating the volume of the irregular pond (盤池)

"""
Suppose there is a pond. The top width is 6 zhang, the top length is 8 zhang. 
The bottom width is 4 zhang, the bottom length is 6 zhang. The depth is 2 zhang.
Question: what is the volume?

Answer: 76066 chi² and a little more than half a chi².
"""

# 上廣六丈，袤八丈
上廣 = 6 * 10  # Convert zhang to chi
上袤 = 8 * 10  # Convert zhang to chi

# 下廣四丈，袤六丈
下廣 = 4 * 10  # Convert zhang to chi
下袤 = 6 * 10  # Convert zhang to chi

# 深二丈
深 = 2 * 10  # Convert zhang to chi

# Calculate the average area of the top and bottom
上積 = 上廣 * 上袤
下積 = 下廣 * 下袤
平均積 = Fraction(上積 + 下積, 2)

# Multiply by the depth to get the volume
積 = 平均積 * 深

# Convert to the final answer
a = 積  # Volume in chi³

### Part 2: Calculating the work required for moving the soil

"""
The soil is moved over a distance of 70 bu, with 20 bu for the up-and-down slope.
The slope requires 2 units of effort for every 5 units of flat ground.
The hesitation in movement adds 1 unit of effort for every 10 bu, and the loading/unloading adds 30 bu.
A single round trip is 140 bu.
Each basket holds 1 chi 6 cun of soil.
The autumn work rate is 59.5 li per person.

Question: how much soil does one person move, and how many workers are required?

The procedure says: Multiply the volume of one basket by the total distance traveled.
For the up-and-down slope, 2 units of effort are equivalent to 5 units of flat ground.
Add the hesitation effort and the loading/unloading effort to the total round trip distance.
Divide the total effort by the adjusted distance to find how much soil one person moves.
Divide the total soil by the amount moved by one person to find the number of workers required.

Answer: one person moves *a* chi³ of soil, and *b* workers are required.
"""

# 負土往來七十步
往來步數 = 70

# 其二十步上下棚除
上下步數 = 20

# 棚除二當平道五
上下當平道 = Fraction(2, 5)

# 踟躕之間十加一
踟躕加 = Fraction(1, 10)

# 載輸之間三十步
載輸步數 = 30

# 定一返一百四十步
定往來步數 = 140

# 土籠積一尺六寸
土籠積 = Fraction(1, 6 / 10)  # Convert 1 chi 6 cun to chi³

# 秋程人功行五十九里半
秋程 = 59.5 * 300  # Convert li to bu (1 li = 300 bu)

# Adjust the total effort for the slope and additional factors
上下調整 = 上下步數 * 上下當平道
總步數 = 定往來步數 + 載輸步數 + 踟躕加 * 定往來步數 + 上下調整

# Calculate how much soil one person moves
人到 = 土籠積 * 秋程 / 總步數

# Calculate the number of workers required
用徒 = Fraction(積, 人到)

# Final answers
a = 人到  # Soil moved by one person in chi³
b = 用徒  # Number of workers required
"""
Code error: both arguments should be Rational instances"""
