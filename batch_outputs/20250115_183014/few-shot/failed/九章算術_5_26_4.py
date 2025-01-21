"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

### Part 1: Calculating the volume of the pond (積幾何)

"""
Suppose there is a pond. The top width is 6 zhang, the top length is 8 zhang, the bottom width is 4 zhang, the bottom length is 6 zhang, and the depth is 2 zhang.
Question: what is the volume?

Answer: 76,066.5 chi³ (七萬六百六十六尺、太半尺).
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

# Calculate the average area of the top and bottom
上面積 = 上廣 * 上袤
下面積 = 下廣 * 下袤
平均面積 = Fraction(上面積 + 下面積, 2)

# Calculate the volume
積 = 平均面積 * 深

# Convert to chi³
積尺 = 積
a = 積尺  # Volume in chi³

### Part 2: Calculating human labor (人到、用徒)

"""
Suppose the soil is transported over a distance of 70 bu, with 20 bu for the up-and-down slope (棚除). 
The棚除 is equivalent to 2 units of flat ground being equal to 5 units of棚除. 
The hesitation (踟躕) adds 1 for every 10, and the loading/unloading (載輸) adds 30 bu. 
One round trip is thus 140 bu. 
Each soil basket holds 1 chi 6 cun of soil. 
The autumn work rate is 59.5 li per person. 
Question: how much soil does one person transport, and how many workers are needed?

Procedure: Multiply the soil basket volume by the total distance traveled. 
For棚除, 2棚除 is equivalent to 5 flat ground. 
Set the total round-trip distance, add hesitation (10 adds 1), and add the loading/unloading distance. 
Divide by this to get the soil transported by one person. 
Divide the total soil volume by this to get the number of workers needed.

Answer: one person transports *a* chi³ of soil, and *b* workers are needed.
"""

# 負土往來七十步
往來步數 = 70

# 其二十步上下棚除
棚除步數 = 20

# 棚除二當平道五
棚除當平道 = Fraction(5, 2)

# 棚除換算為平道步數
棚除平道步數 = 棚除步數 * 棚除當平道

# 十加一
踟躕加成 = Fraction(1, 10)

# 載輸之間三十步
載輸步數 = 30

# 定一返一百四十步
定往返步數 = 往來步數 + 棚除平道步數 + 載輸步數 + (往來步數 * 踟躕加成)

# 土籠積一尺六寸
土籠積尺 = 1 + Fraction(6, 10)

# 秋程人功行五十九里半
秋程行里 = 59 + Fraction(1, 2)

# 一里 = 180步
秋程行步數 = 秋程行里 * 180

# 以一籠積尺乘程行步數為實
實 = 土籠積尺 * 秋程行步數

# 以定往返步數為法
法 = 定往返步數

# 所得即一人所到尺
人到尺 = Fraction(實, 法)

# 以所到約積尺，即用徒人數
用徒人數 = Fraction(積尺, 人到尺)

# Final results
a = 人到尺  # Soil transported by one person in chi³
b = 用徒人數  # Number of workers needed
"""
Variable 'a' has wrong value. Expected: 204, Actual: 17136/157
Variable 'b' has wrong value. Expected: 53000/153, Actual: 78500/119"""
